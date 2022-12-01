# 判断字符串 是否 存在 子字符串 #

    def check(string, sub_str): 
    	if (string.find(sub_str) == -1): 
    		print("不存在！") 
    	else: 
    		print("存在！") 


----------

删除字符串中字符的四种方法

[https://blog.csdn.net/qdPython/article/details/120510123](https://blog.csdn.net/qdPython/article/details/120510123)
 
# 删除字符串中 任意位置的 一种或多种字符 #

    str =  "avc"
    str.replace(被替换的字符, ‘’)；

# re.sub 正则 替换 字符 #

re.sub(’[多种需要被替换的字符]’, ‘’ ,字符串对象, count, Flags)

count = 0时，替换全部；count = n，替换前n个；count默认为0‘

flags = 1时：从字符串左端开始；flags = 0时，从右端开始；默认为1；

    import re
    s = 'a\tb\tc\rd\re'
    s1 = re.sub('[\t\r]', '', s)
    print(s1)
    #输出：abcde
