UTF-8 不需要 BOM，尽管 Unicode 标准允许在 UTF-8 中使用 BOM。
所以不含 BOM 的 UTF-8 才是标准形式，在 UTF-8 文件中放置 BOM 主要是微软的习惯（顺便提一下：把带有 BOM 的小端序 UTF-16 称作「Unicode」而又不详细说明，这也是微软的习惯）。

## 什么是BOM ##
BOM（byte-order mark），即字节顺序标记，它是插入到以UTF-8、UTF16或UTF-32编码Unicode文件开头的特殊标记，用来识别Unicode文件的编码类型。

对于UTF-8来说，BOM并不是必须的，因为BOM用来标记多字节编码文件的编码类型和字节顺序（big-endian或little-endian）。

在绝大多数编辑器中都看不到BOM字符，因为它们能理解Unicode，去掉了读取器看不到的题头信息。若要查看某个Unicode文件是否以BOM开头，可以使用十六进制编辑器。下表列出了不同编码所对应的BOM。

BOM Encoding
EF BB BF UTF-8
FE FF UTF-16 (big-endian)
FF FE UTF-16 (little-endian)
00 00 FE FF UTF-32 (big-endian)
FF FE 00 00 UTF-32 (little-endian)

UTF-8以字节为编码单元因此不需要 BOM 来表明字节顺序，但可以用 BOM 来表明编码方式。字符 “Zero Width No-Break Space” 的 UTF-8 编码是 EF BB BF。所以如果接收者收到以 EF BB BF 开头的字节流，就知道这是 UTF-8编码了。
因此UTF-8编码的字符串开头处的三个bytes 0xef,0xbb,0xbf就称为UTF-8 BOM头。

## BOM的来历 ##
为了识别 Unicode 文件，Microsoft 建议所有的 Unicode 文件应该以 ZERO WIDTH NOBREAK SPACE（U+FEFF）字符开头。这作为一个“特征符”或“字节顺序标记（byte-order mark，BOM）”来识别文件中使用的编码和字节顺序。

Linux/UNIX 并没有使用 BOM，因为它会破坏现有的 ASCII 文件的语法约定。

带BOM和不带BOM的区别
「UTF-8」和「带 BOM 的 UTF-8」的区别就是有没有 BOM。即文件开头有没有 U+FEFF，也就是说有没有这个标记。


bom是为utf-16和utf-32准备的，用于标记字节顺序。微软在utf-8中使用bom是因为这样可以把UTF-8和ASCII等编码区分开来，但这样的文件在windows之外的操作系统里会带来问题。

带还是不带？
如果你的编程平台需要跨平台编译，比如，会在linux平台上编译，而不是只在windows上运行，建议不带BOM，unicode标准就是不带，带BOM毕竟那是微软的那一套，带了会出现很大的问题。反之，如果你的程序只在windows平台上编译出windows程序，这个可有可无。
注意：这里所说的带还是不带，指的是：源码字符集(the source character set)-源码文件是使用何种编码保存的；
