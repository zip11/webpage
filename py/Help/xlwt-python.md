## 设置单元格宽度 ##
    import xlwt
     
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('微课列表')
     
    worksheet.write(1, 1,'MySQL')
     
    # 设置单元格宽度
    worksheet.col(0).width = 3000
     
    workbook.save('W3Cschool课程内容.xls')

## 设置单元格内容对其方式 ##

    import xlwt
     
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('微课列表')
     
    # 创建对其格式的对象 Create Alignment
    alignment = xlwt.Alignment()
     
    #水平居中 May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
    alignment.horz = xlwt.Alignment.HORZ_CENTER
     
    #我上下对齐 May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
    alignment.vert = xlwt.Alignment.VERT_CENTER 
     
    #创建样式对象 Create Style
    style = xlwt.XFStyle()
     
    # 将格式Alignment对象加入到样式对象Add Alignment to Style
    style.alignment = alignment
     
    #写入的时候调用样式style
    worksheet.write(0, 0, '单元居中', style)
     
    workbook.save('W3Cschool课程内容.xls')
