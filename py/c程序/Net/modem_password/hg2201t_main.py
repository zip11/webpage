import re


# 正则 分割 加密的 英语 和 数字 字符串
def string_spilt(encrypted_string):

    # 使用正则表达式分割字符串

    # 匹配非两位数后面跟着'&'的模式，例如 "120&", "105&", "112&" 等
    # 匹配两位数的部分，例如 "48&49&50", "48&49&50&48&49&" 等

    # 正则表达式中的捕获组将，非两位数部分作为第1部分,两位数部分作为第2部分

    parts = re.split(r'(\d{2,3})&|(\d{2}&)', encrypted_string)

    # 分别处理两部分

    # 两位数的
    two_digit_parts = []
    # 非两位数的
    non_two_digit_parts = []

    # 遍历 
    for part in parts:

        if part:  
        # 确保part不是空字符串或None

            if len(part) == 2 and part.isdigit():
            # 检查是否为两位数
                
                two_digit_parts.append(part+"&")
            else:
                non_two_digit_parts.append(part+"&")

    print("两位数部分:", two_digit_parts)
    print("非两位数部分:", non_two_digit_parts)

    # two_digit_parts 转 字符串
    two_digit_parts_str = ''.join(two_digit_parts)
    # non_two_digit_parts 转 字符串
    non_two_digit_parts_str = ''.join(non_two_digit_parts)

    return non_two_digit_parts_str , two_digit_parts_str


# 解密 12位 英文部分，120&，三位数部分
def decrypt_string_eng(encrypted_string):

    # 解密字符串
    decrypted_string = ""

    for i in encrypted_string.split('&'):  
        # 分割字符串，以'&'为分隔符

        if i:  
            # 确保i不是空字符串
            
            # 将字符串转换为整数
            num = int(i)
            # 减去4得到ASCII码
            ascii_code = num - 4

            # 将ASCII码转换为字符
            char = chr(ascii_code)
            # 将字符添加到解密后的字符串
            decrypted_string += char



    return decrypted_string





# 解密8位数字 ，48&
def decrypt_string_number(encrypted_string):

    # 解密字符串
    decrypted_string = ""
    for i in range(0, len(encrypted_string), 3):
        # 提取ASCII码的十进制表示（两个数字）
        ascii_code = encrypted_string[i:i+2]
        # 将字符串转换为对应的十进制数值
        num = int(ascii_code)
        # 获取对应的ASCII字符
        char = chr(num)
        # 将字符添加到解密后的字符串
        decrypted_string += char


    return decrypted_string


# 开始程序 ~~~~~~~~~~~~
print("光猫超级用户密码解密，例如120&105&112&105&103&115&113&101&104&113&109&114&48&49&50&48&49&50&48&49&")


# 键盘输入 加密字符串
encrypted_string = input("请输入加密后的字符串：")

# 加密的字符串
# encrypted_string = "120&105&112&105&103&115&113&101&104&113&109&114&48&49&50&48&49&50&48&49&"

# 分割 加密字符串，120& 部分 ，12位英语，48&部分，8位数字
eng_str , num_str = string_spilt(encrypted_string)

# 解密 英语部分
decrypt_string_eng_2 = decrypt_string_eng(eng_str)
print("解密后的英文部分：", decrypt_string_eng_2)

# 解密数字部分
decrypt_string_num_2  = decrypt_string_number(num_str)
print("解密后的数字部分：", decrypt_string_num_2)

print("解密后的结果：", decrypt_string_eng_2 + decrypt_string_num_2 )


