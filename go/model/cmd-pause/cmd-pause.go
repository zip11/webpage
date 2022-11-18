package main

import (
	"fmt"
	"io/ioutil"
)

func main() {
	// 将保存的字符串转换为字节流
	str := []byte(`要保存入文件的字符串`)

	// 保存到文件
	ioutil.WriteFile(`保存文件的文件名.txt`, str, 0666)

	pause()
}

func pause() {

	fmt.Println("--------------------------------------")

	var s string

	fmt.Println("输入exit退出:")

	fmt.Scan(&s)

	if s == "exit" {

	} else {

		pause()

	}
}
