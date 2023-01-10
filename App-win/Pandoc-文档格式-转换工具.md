最近发现了一款免费的文档格式转换工具：Pandoc

## Pandoc 简介 ##

Pandoc 是一个由 John MacFarlane 开发的通用文档转换工具，可以支持大量标记语言之间的格式转换，例如 Markdown 、Microsoft Word、PowerPoint、 Jupyter Notebook、HTML、PDF、LaTeX、Wiki、EPUB 格式之间的相互转换。

[https://pandoc.org/](https://pandoc.org/)


## 下载安装 ##

Pandoc 提供了一个 Haskell 代码库和命令行程序，支持 Windows、macOS、Linux、Chrome OS、BSD、Docker、GitHub Actions 以及源码编译等方式。最简单的安装方式就是点击下载编译好的安装文件。

[https://github.com/jgm/pandoc/releases/tag/2.19.2](https://github.com/jgm/pandoc/releases/tag/2.19.2)

## Windows ##

Pandoc 为 Windows 系统提供了编译后的 msi 安装包，可以直接运行安装；或者直接下载免安装的 zip 文件解压即可。



----------


## 转换命令 ##

然后在命令行输入以下命令：

    pandoc.exe test.md -f markdown -t html -s -o test.html

文件名 test.md 是要转换的源文件；-f 设置输入文件的格式；-t 设置输出文件的格式；-s 表示创建一个“独立”文件，将会生成文件
页眉和页脚。默认的转换格式为 markdown 到 HTML，所以上面的命令也可以省略这两个选项。


----------


Pandoc 可以根据文件名扩展猜测出输入和输出文件的格式，例如以下命令可以将文件转换为 Word 文档格式：

    pandoc.exe test.md -s -o test.docx



----------


如果已经安装了 LaTeX，可以使用以下命令转换为 PDF 文件：

    pandoc.exe test.md -f markdown -s -o test.pdf


----------

输入 pandoc --help 命令可以查看工具的选项帮助，详细的使用介绍可以查看用户手册。

