新增硬盘后，在linux系统下输入 fdisk -l 命令查看当前磁盘信息

进入 fdisk 命令，输入 h 可以看到该命令的帮助，输入 n 进行分区




- 这里输入 e 即分为逻辑分区，按 p 即分为主分区，我们要将这块盘分为主分区即输入 p



到这里需要你选择该主分区为第几个主分区，由于是新盘我们输入1来分第一个主分区


First Cylinder是选择该分区的起始磁盘数，这里可自定义也可不做选择，默认是1，如无特殊需求强烈建议选择默认，也就是1来分区（直接按回车）




- 接下来是定义该分区的大小，如果按默认（按回车）即是使用全部可用存储额，也可以是用M或m单位结尾的数字(大写M是大B的意思，如果输入1M实际上是X8也就是8m的空间)，这里我们先分一个1G的空间，所以输入+1024m


之后输入w写入分区，等待结束皆可


再输入fdisk -l 可以看到我们刚才分的一个分区，之后用 mkfs -t ext3 -c /dev/sdb1 进行格式化，如有多个分区可把sdb1改成sdb2 sdb3...以此类推，具体可用 fdisk -l 看到每个分区的名字


---

现在分区好了我们用mount 挂载一下该分区即可使用了，这里我把它挂载到mnt目录下，也可以自建一个目录挂载




- 来看一下分区大小是否和预定的一样，使用 df -TH 命令看一下当前挂载的分区和大小，

- 看到我们刚分的分区了吧如果想每次系统重启都能自动挂载该分区可修改/etc/fstab文件，在最后加一段 /dev/sdb1 /www ext3 defaults 1 2 

- (格式说明：/dev/sdb1 代表哪个分区 ext3是该分区的格式 defaults 是挂载时所要设定的参数(只读，读写，启用quota等)，输入defaults包括的参数有(rw、dev、exec、auto、nouser、async) ，1是使用dump是否要记录，0是不要。 2是开机时检查的顺序，是boot系统文件就为1，其他文件系统都为2，如不要检查就为0)
