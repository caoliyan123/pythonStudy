#coding:utf-8
import  psycopg2
import psycopg2.extras
#import psycopg2-binary

def gp_connect():
    try:
        db = psycopg2.connect(dbname="vsps_v5",
                              user="gpadmin",
                              password="gpadmin",
                              host="192.168.0.204",
                              port="5432")
        return db
    except psycopg2.DatabaseError as e:
        print("could not curect to Greenplum server",e)

tablename=input('请输入表名：')

conn=gp_connect()
cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)


try:
    table_name = tablename.lower().split('.')[1]
    talbe_schema = tablename.lower().split('.')[0]

except (IndexError):
    print('Please in put "tableschema.table_name"')

get_table_oid = "select oid,reloptions,relkind from pg_class where relname=\'%s\' " %(table_name)


try:
    cur.execute(get_table_oid)
    rv_oid = cur.fetchone()
    if not rv_oid:
        print('Did not find any relation named"' + tablename + '".')
except (IndexError):
    print( 'Did not find any relation named"' + tablename + '".')
table_oid = rv_oid['oid']
rv_reloptions = rv_oid['reloptions']
rv_relkind = rv_oid['relkind']


create_sql = "";
table_kind = 'table';
if rv_relkind != 'r' and rv_relkind != 'v':
    cur.error('%s is not table or view' % (tablename));
elif rv_relkind == 'v':
    get_view_def = "select pg_get_viewdef(%s,'t') as viewdef;" % (table_oid)
    rv_viewdef = cur.execute(get_view_def);
    create_sql = 'create view %s as \n' % (tablename)
    create_sql += rv_viewdef[0]['viewdef'] + '\n';
    table_kind = 'view'
else:
    get_columns = "select a.attname,pg_catalog.format_type(a.atttypid,a.atttypmod),\
       (select substring(pg_catalog.pg_get_expr(d.adbin,d.adrelid) for 128) \
        from pg_catalog.pg_attrdef d where d.adrelid=a.attrelid and d.adnum=a.attnum and a.atthasdef) \
        as default,a.attnotnull as isnull from pg_catalog.pg_attribute \
        a where a.attrelid= %s and a.attnum >0 and not a.attisdropped order by a.attnum;" % (table_oid);
    cur.execute(get_columns)
    rv_columns = cur.fetchall()

    get_table_distribution1 = "select distkey from pg_catalog.gp_distribution_policy t where localoid =%d; " % (
        table_oid);
    cur.execute(get_table_distribution1, 500)
    rv_distribution1 = cur.fetchone()
    rv_distribution11=rv_distribution1['distkey']
    rv_distribution111=rv_distribution11.replace(' ',',')
    rv_distribution2 = ''
if rv_distribution1 :
    get_table_distribution2 = "select attname from pg_attribute where attrelid=%d and attnum in (%s) " %(table_oid,rv_distribution111);
    cur.execute(get_table_distribution2, 500)
    rv_distribution2 = cur.fetchall()


    create_sql = 'create table %s (\n' % (tablename)
    get_index = "select pg_get_indexdef(indexrelid) as indexdef from pg_index where indrelid=%s" % (table_oid);
    cur.execute(get_index)
    rv_index = cur.fetchall()

    get_parinfo1 = "select attname as columnname from pg_attribute where attnum =(select paratts[0] from pg_partition where parrelid=%s) and attrelid=%s;" % (
    table_oid, table_oid);
    get_parinfo2 = """ select pp.parrelid,prl.parchildrelid,case when pp.parkind='h'::"char" then 'hash'::text when pp.parkind='r'::"char" then 'range'::text when pp.parkind='l'::"char" then 'list'::text else null::text end as partitiontype,pg_get_partition_rule_def(prl.oid,true) as partitionboundary from pg_partition pp,pg_partition_rule prl where pp.paristemplate=false and pp.parrelid = %s and prl.paroid = pp.oid order by prl.parname; """ % (
        table_oid)
    cur.execute(get_parinfo1)
    v_par_parent = cur.fetchall()
    cur.execute(get_parinfo2)
    v_par_info = cur.fetchall()
    max_column_len = 10
    max_type_len = 4
    max_modifiers_len = 4
    max_default_len = 4
    for i in rv_columns:
        if i['attname']:
            if max_column_len < i['attname'].__len__():
                max_column_len = i['attname'].__len__()
        if i['format_type']:
            if max_type_len < i['format_type'].__len__():
                max_type_len = i['format_type'].__len__()
        if i['default']:
            if max_type_len < i['default'].__len__():
                max_default_len = i['default'].__len__()
    first = True
    for i in rv_columns:
        if first == True:
            split_char = ' ';
            first = False
        else:
            split_char = ',';
        if i['attname']:
            create_sql += " " + split_char + i['attname'].ljust(max_column_len + 6) + ''
        else:
            create_sql += "" + split_char + ' '.ljust(max_column_len + 6)
        if i['format_type']:
            create_sql += ' ' + i['format_type'].ljust(max_type_len + 2)
        else:
            create_sql += ' ' + ' '.ljust(max_type_len + 2)
        if i['isnull'] and i['isnull']:
            create_sql += ' ' + ' not null '.ljust(8)
        if i['default']:
            create_sql += ' default ' + i['default'].ljust(max_default_len + 6)
        create_sql += "\n"
    create_sql += ")"

    if rv_reloptions:
        create_sql += " with (" + str(rv_reloptions).strip('{').strip('}').strip('[').strip(']') + ")\n"
        create_sql = create_sql.replace("'", '')
    if rv_distribution2:
        create_sql += 'Distributed by ('
        for i in rv_distribution2:
            create_sql += i['attname'] + ','
        create_sql = create_sql.strip(',') + ')'
    elif rv_distribution1:
        create_sql += 'Distributed randomly\n'
    if v_par_parent:
        partitiontype = v_par_info[0]['partitiontype'];
        create_sql += '\nPARTITION BY ' + partitiontype + "(" + v_par_parent[0]['columnname'] + ")\n(\n";
        for i in v_par_info:
            create_sql += " " + i['partitionboundary'] + ',\n';
        create_sql = create_sql.strip(',\n');
        create_sql += "\n)"
    create_sql += ";\n\n"
    for i in rv_index:
        create_sql += i['indexdef'] + ';\n'

    get_table_comment = "select 'comment on %s %s is '''|| COALESCE (description,'')|| '''' as comment from pg_description where objoid=%s and objsubid=0;" % (
    table_kind, tablename, table_oid)
    get_column_comment = "select 'comment on column %s.'||b.attname ||' is ''' || COALESCE(a.description,'')|| ''' ' as comment from pg_catalog.pg_description a,pg_catalog.pg_attribute b where objoid=%s and a.objoid=b.attrelid and a.objsubid=b.attnum;" % (
    tablename, table_oid)
    cur.execute(get_table_comment)
    rv_table_comment = cur.fetchall()
    cur.execute(get_column_comment)
    rv_column_comment = cur.fetchall()


    for i in rv_table_comment:
        create_sql += i['comment'] + ';\n'
    for i in rv_column_comment:
        create_sql += i['comment'] + ';\n'
    print(create_sql)