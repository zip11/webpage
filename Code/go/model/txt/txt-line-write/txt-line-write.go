package main

import (
	"log"
	"os"
	"strconv"
)

func main() {

	WriteTxt()
}

func WriteTxt() {

	// 打开文件路径 "D:/helloworld.txt"
	// 只写方式打开 os.O_WRONLY
	// os.FileMode(0600) 文件权限：windows系统权限失效。

	file, err := os.OpenFile("helloworld.txt", os.O_WRONLY, 0)

	if err != nil {
		log.Fatal(err)
	}

	// 关闭文件
	defer file.Close()

	for i := 0; i < 10; i++ {

		for j := 0; j < 10; j++ {
			// 写入一行
			_, err := file.WriteString(strconv.Itoa(j) + " ")

			if err != nil {
				log.Fatal(err)
			}
		}
		file.WriteString("\r\n")
	}
}
