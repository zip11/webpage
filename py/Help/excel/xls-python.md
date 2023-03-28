## "Python3 操作excel库总结" ##
[https://www.w3cschool.cn/python3/python3-excel.html](https://www.w3cschool.cn/python3/python3-excel.html "Python3 操作excel库总结")

## xlwt 写xls 设置-详细格式 ##

[https://www.w3cschool.cn/python3/python-xlwt.html](https://www.w3cschool.cn/python3/python-xlwt.html)

## Python读写Excel文件  3种方式  ##
[https://zhuanlan.zhihu.com/p/82200512](https://zhuanlan.zhihu.com/p/82200512)

## xlwt库 ##

xlwt库是一个python用于操作excel的第三方库。它的主要功能是用来写入excel。通常会与xlrd 、 xlutils组合进行使用。 

xlwt库直接操作的是excel打开的xls文件！注意！xlrd库只能创建和修改excel，不能打开excel！


Successfully installed xlrd-2.0.1

Successfully installed xlwt-1.3.0

一 、xlwt的安装

可以使用pip进行安装

​pip install xlrd

# 二、创建表格并写入 #

    import xlwt
     
    # 创建一个workbook并设置编码
    workbook = xlwt.Workbook(encoding = 'utf-8')

    # 添加sheet
    worksheet = workbook.add_sheet('微课列表')

    # 写入excel, 参数对应 行, 列, 值
    worksheet.write(1,0, label = 'MySQL零基础入门课程')

    # 保存
    workbook.save('W3Cschool课程内容.xls')


# xlrd 读取 excel #

    import xlrd
    
    data = xlrd.open_workbook('test.xls') # 打开xls文件
    
    table = data.sheets()[0] # 打开第一张表
    
    nrows = table.nrows # 获取表的行数
    
    # 循环逐行输出
    
    for i in range(nrows): 
    
       if i == 0: # 跳过第一行
    
           continue
    
       print (table.row_values(i)[:13]) 
       # 取前十三列数据

#  xlutils  修改原有xls #​

[https://www.cnblogs.com/machangwei-8/p/10739115.html](https://www.cnblogs.com/machangwei-8/p/10739115.html)

安装
pip install xlutils

copy:       将xlrd.Book转为xlwt.Workbook
styles:     读取xlrd.Workbook的每一个单元格的style
display:    简单而安全地呈现xlrd读取的数据
filter:     拆分与整合多个xls文件
margins:    查看表格稀疏程度
save:       序列化xlrd.Book，转存为binary xls或stream