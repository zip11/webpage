
# 解密英文部分，三位数部分
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


encrypted_string2 = "120&105&112&105&103&115&113&101&104&113&109&114&"
# 解密英文部分，12位
decrypted_string = decrypt_string_eng(encrypted_string2)
print("解密英文-字符串",decrypted_string)

# 加密的  数字 字符串，8位数
encrypted_string = "48&49&50&48&49&50&48&49&"
decrypted_string2 = decrypt_string_number(encrypted_string)

print("解密数字-字符串",decrypted_string2)

total_string = decrypted_string + decrypted_string2
print("解密后的总字符串",total_string)