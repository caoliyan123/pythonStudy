import cx_Oracle
import pandas as pd

#连接数据库
cx_user = "fe_app5"
cx_password = "feadmin"
cx_url = "192.168.0.221:1521/orcljw"
cx_conn = cx_Oracle.connect(cx_user,cx_password,cx_url)
cx_curosr = cx_conn.cursor()

def person_info():
    #人员列表
    sql_perlist='''select  a.IDCARD , a.name
                    from fe_app5.T_TOP_PARTY_PROFILE a
                where ISHISTORY=0 and CONDITION in (1,2,3) and OBJECT_TYPE in (1,2) and substr(unitnum,0,15) ='360101000002015' '''
    perlist=cx_curosr.execute(sql_perlist).fetchall()
    for per in perlist:
        print(per[0])
        #个人详情-基本情况
        sql_perinfo='''select a.name as 姓名,'身份证' as 证件类型 ,a.IDCARD as 证件号码,BIRTHPLACE as 出生地,JOINPARTYDATE as 入党时间,WORKDATE as 参加工作时间,b.CHRONIC+'-'+b.HEARTDISEASE+'-'+b.OPERATION+'-'+PREVALENCE as 健康状况,
        null as 中共党代表,null as 人大代表	,null as 政协委员,null as "全日制学历（学历学位）",
        null as "全日制教育（学习院校及专业）",null as "在职教育（学历学位）"	,null as "在职教育（学习院校及专业）"
        ,AREA as 常住地址,TEL as 移动电话
        from fe_app5.T_TOP_PARTY_PROFILE a
        left join fe_app5.T_TOP_PARTY_HEALTH b on a.id=b.PROFILEID
        left join fe_app5.T_TOP_SYS_UNIT c on a.UNITNUM=c.UNIT_CODE         
        where a.ISHISTORY=0 and a.idcard='{0}'  '''.format(per[0])
        perinfo=pd.read_sql_query(sql_perinfo,cx_conn)
        writer1 = pd.ExcelWriter('C:\\Users\\Yan\\Desktop\\纪委\\富山乡\\{0}_{1}.xlsx'.format(per[0],per[1]))
        perinfo.to_excel(writer1,sheet_name='基本情况',index=None)
        #出国证件
        sql_passport='''select a.name as 证件名称,a.code 证件号码,null as 发证机关,b.AREA as 地区或国家,null as 审批时间,null as 发证时间,
                round((months_between(to_date(ENDDATE),to_date(STARTDATE)))/12,0) as 有效期,CUSTODIAN as	保管机关
                from T_TOP_PASSPORT a
                full join
                (select PROFILEID,  AREA from T_TOP_PARTY_INOUTCOUNTRY union
                select PROFILEID,GOBACK as area from T_TOP_PARTY_LZ_OUT_ACTIVE) b
                on a.PROFILEID=b.PROFILEID
                left join fe_app5.T_TOP_PARTY_PROFILE c on a.PROFILEID=c.id
                where a.code<>'无' and substr(c.unitnum,0,15) ='360101000002015' and c.ishistory=0
                and c.IDCARD='{0}'  '''.format(per[0])
        passport=pd.read_sql_query(sql_passport,cx_conn)
        passport.to_excel(writer1, sheet_name='出国证件', index=None)
        #个人简历
        sql_workexp='''select GZKSSJ as 起始时间,GZJSSJ as 截止时间,GZDWCODE as 单位, GZZW as 职务,null as 职级,null as 备注
                    from T_TOP_PARTY_PROFILE_WORKEXP a
                    left join fe_app5.T_TOP_PARTY_PROFILE c on a.PROFILEID=c.id  
                    where c.idcard='{0}' and c.ISHISTORY=0 '''.format(per[0])
        workexp=pd.read_sql_query(sql_workexp,cx_conn)
        workexp.to_excel(writer1, sheet_name='个人简历', index=None)
        #家庭成员
        sql_family='''select b.si02 as 与本人关系,a.name as 姓名, '身份证' as 证件类型 , a.IDCARD as 证件号码,
                        c.si02 as 政治面貌,a.unit as 工作单位,a.job as 职务,
                        case  when f.si02= '1' then '省部级以上'   when  f.si02 in ('2','3') then '厅局级'
			            when f.si02 in ('4','5') then '县处级' when f.si02 in ('6','7') then '乡科级' else '一般干部' end 	as 职级
                        ,null as 学历,null as 是否中国国籍	,null as 是否境外居住
                        from T_TOP_PARTY_PROFILE_FAMILY a
                        left join FE_BASE5.SORT_INFOR b on a.title=b.si01
                        left join FE_BASE5.SORT_INFOR c on a.POLITICS=c.si01
                        left join (select * from fe_base5.SORT_INFOR where SI06='icdi职级' and si04=1) f on a.rank=to_number(f.SI01)
                        left join fe_app5.T_TOP_PARTY_PROFILE d on a.PROFILEID=d.id
                        where b.si06='icdi称谓' and c.si06='icdi政治面貌' and f.si06='icdi职级'  and d.ISHISTORY=0 and d.idcard='{0}'
        '''.format(per[0])
        family=pd.read_sql_query(sql_family,cx_conn)
        family.to_excel(writer1, sheet_name='家庭成员', index=None)
        writer1.save()

    cx_curosr.close()
    cx_conn.close()

person_info()