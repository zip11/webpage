import os
import sys
 
#获取脚本所在目录
print( os.path.split( os.path.realpath( sys.argv[0] ) )[0])
#获取脚本运行目录
print( os.getcwd())
os.system("pause")