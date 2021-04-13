import cx_Oracle

#连接数据库
cx_user = "fe_app5"
cx_password = "feadmin"
cx_url = "192.168.0.221:1521/orcljw"
cx_conn = cx_Oracle.connect(cx_user,cx_password,cx_url)
cx_curosr = cx_conn.cursor()

def filelist_count(menuid):
    catalog_menu_id=cx_curosr.execute("select menuid  from T_TOP_PARTY_FILECATALOG m start with menuid='%s' connect by m.PARENTID=prior m.menuid"%(menuid) ).fetchall()
    for i in catalog_menu_id:
        #print (i)
        filelist=cx_curosr.execute("select  sum(count) from v_filelistcount m   start with m.MENUID='%s' connect by m.PARENTID=prior m.MENUID"%(i)).fetchone()[0]
        print(i[0],filelist)
    cx_curosr.close()
    cx_conn.close()
#入口函数
if __name__ == '__main__':
    filelist_count('1010102_29')