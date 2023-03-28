###python-分割文件名和后缀

路径的文件名{只是名称} 和 后缀名分开

os.path.splitext(path)

os.path.splitext(path)：将路径的文件名和后缀名分割。其中文件名只是名称。
path指一个文件的路径（相对路径或者绝对路径）作为参数：

1.1 如果给出的是一个目录和文件名，则输出路径的文件名称和后缀；

1.2 如果给出的是一个目录名，则输出路径和空后缀；
    
    import os
    
    file_path = "D:/test/data_expand/192.168.1.70_01_20210901163745710_250_150_4...jpg"
    
    filename,extension = os.path.splitext(file_path)
    
    print("filename:",filename)   # D:/test/data_expand/192.168.1.70_01_20210901163745710_250_150_4..
    
    print("extension:",extension) # .jpg
    
    file_path ="D:/test/data_expand/"
    
    filename,extension = os.path.splitext(file_path)
    
    print("filename:",filename) # D:/test/data_expand/
    print("extension:",extension)   # 空文件后缀
    