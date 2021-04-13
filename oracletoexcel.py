import cx_Oracle
import openpyxl
import xlwt

#连接数据库
cx_user = "fe_app5"
cx_password = "feadmin"
cx_url = "192.168.0.221:1521/orcljw"
cx_conn = cx_Oracle.connect(cx_user,cx_password,cx_url)
cx_curosr = cx_conn.cursor()

def person_list():
    #获取所有的乡镇
    xz_list=cx_curosr.execute("select name,unit_code from fe_app5.T_TOP_SYS_UNIT where PARENT_UNIT_CODE=  '360101000002'").fetchall()
    for xz in xz_list:
        #创建excel文件
        w=xlwt.Workbook()
        sheet = w.add_sheet('人员列表')
        titles=('姓名','证件类型','证件号码','性别','出生年月','民族','籍贯','政治面貌','工作单位','部门','职务','干部管理权限','职级','监察类型','纪检监察干部')
        title_style = xlwt.XFStyle()
        font = xlwt.Font()  # 字体基本设置
        font.name = u'微软雅黑'
        font.color = 'red'
        font.height = 220
        title_style.font = font
        aligment = xlwt.Alignment()
        aligment.horz = xlwt.Alignment.HORZ_CENTER
        aligment.vert = xlwt.Alignment.VERT_CENTER
        title_style.alignment = aligment
        # 添加表头内容到表中
        for col_index, title in enumerate(titles):
            # 这里第四个参数title_style是样式设置，可以不加
            sheet.write(0, col_index, title, title_style)
        sql_1='''select a.name as 姓名,'身份证' as 证件类型 ,a.IDCARD as 证件号码 ,b.si02 as 性别   ,a.BIRTHDAY as 出生年月,c.si02 as 民族,a.NATIVEPLACE as 籍贯,d.si02 as 政治面貌,a.unit as 工作单位,e.name as 部门,a.job as 职务,'均不是' as 干部管理权限,
            case  when f.si02= '1' then '省部级以上'  when  f.si02 in ('2','3') then '厅局级' when f.si02 in ('4','5') then '县处级'
            when f.si02 in ('6','7') then '乡科级' else '一般干部' end as 职级,case when OBJECT_TYPE=1 then '公务员及参公管理人员'  when OBJECT_TYPE=2 then  '公务员及参公管理人员'when OBJECT_TYPE=3 then '非监察对象' end 监察类型,null as 纪检监察干部 from fe_app5.T_TOP_PARTY_PROFILE a 
            left join fe_base5.SORT_INFOR b on a.SEX=b.SI01
            left join fe_base5.SORT_INFOR c on a.nation=c.SI01
            left join fe_base5.SORT_INFOR d on a.POLITICS=d.SI01
            left join fe_app5.T_TOP_SYS_UNIT e on a.UNITNUM=e.UNIT_CODE
            left join (select * from fe_base5.SORT_INFOR where SI06='icdi职级' and si04=1) f on a.rank=to_number(f.SI01)
            where substr(unitnum,0,15) ='{0}' and b.SI06='icdi性别' and c.SI06='icdi民族'  and d.SI06='icdi政治面貌' and f.SI06='icdi职级' '''.format(xz[1])
        person_info=cx_curosr.execute(sql_1).fetchall()
        for row_index,row in enumerate(person_info):
            for col_index,value in enumerate(row):
                sheet.write(row_index + 1, col_index, value)
        w.save(r'C:\Users\Yan\Desktop\纪委\03人员列表_{}.xls'.format(xz[0]))
    cx_curosr.close()
    cx_conn.close()

person_list()