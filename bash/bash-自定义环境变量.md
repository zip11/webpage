## export 命令用于设置或显示环境变量。 ##

export 可新增，修改或删除环境变量，供后续执行的程序使用。export 的效力仅限于该次登陆操作。


export VARIABLE=value

请注意，变量，等号（“ =”）和值之间没有空格 。 如果该值包含空格，则该值应放在引号中。

env 显示环境变量

## 每次bash 生效 ##

要使每个bash shell的变量设置生效，请将exporting 命令放入~/.bashrc （每个单独的交互式shell启动文件）中。