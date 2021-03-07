import hashlib
import pyperclip

print("字符串转sha512")

while(1):
 a = input("input string :")
 hash = hashlib.sha512( str( a ).encode("utf-8") ).hexdigest()

 print(hash,"\n已经复制到剪贴板")
 pyperclip.copy(hash)