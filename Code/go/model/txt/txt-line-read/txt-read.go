package main

import (
	"bufio"
	"log"
	"os"
)

func main() {

	ReadTxt()
}

func ReadTxt() {

	file, err := os.Open("hw.txt")

	if err != nil {

		log.Fatal(err)
		return
	}

	defer file.Close()
	// close file

	scanner := bufio.NewScanner(file)
	// 该变量从程序的 输入中读取内容。

	for scanner.Scan() {

		// 每次调用 Scan()，即 读入下一行 ，并移除行末的换行符。
		// scan函数在读到一行时返回true，不再有输入时返回false。

		line := scanner.Text()
		// 读取的内容可以调用 Text() 得到

		// line text
		println(line)
	}
}

// strArr := strings.Split(line, " ")
// // 函数用于将指定的分隔符切割字符串，并返回切割后的字符串切片。

// for str := range strArr {

// 	// range的使用非常简单，对于遍历array，*array，string它返回两个值分别是数据的索引和值，
// 	// 遍历map时返回的两个值分别是key和value，遍历channel时，则只有一个返回数据。
// 	//各种类型

// 	print(str, " ")
// }
