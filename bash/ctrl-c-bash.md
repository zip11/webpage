## shell脚本中如何ctrl-z,ctrl-c,ctrl-d (^z,^c,^d) ##

Ctrl + C To terminate（终止进程）
Ctrl + D signals EOF（文件结束符）
Ctrl + Z suppends a program（暂停一个进程）

echo -e '\003'


CTRL-A \001   十进制1
CTRL-B \002   十进制2
....
CTRL-Z \032   十进制26