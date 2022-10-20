package main

import (
	"fmt"
	"os"
	"os/signal"
	"path/filepath"
	"regexp"
	"strings"
	"syscall"
)

func main() {

	// folder path
	var pwd string

	println("delete folder name space")

	println("input folder path:")

	// input folder path text
	fmt.Scanln(&pwd)

	// replace \ to \\
	pwd = strings.Replace(pwd, "\\", "\\\\", -1)

	// 当前 目录
	//pwd, _ := os.Getwd()

	//pwd := "J:\\pic\\aa"

	//获取当前目录下的所有文件或目录信息

	filepath.Walk(pwd, func(path string, info os.FileInfo, err error) error {

		// folder yes
		if IsDir(path) {

			// no pwd path
			if path != pwd {

				// 打印path信息
				fmt.Println("folder path:" + path)

				cmm(path)

				// 打印文件或目录名
				// mz1 := info.Name()

				// delete space
				// mz1 = compressStr(mz1)
				// fmt.Println(mz1)

			}

		}

		return nil

		// pause

	})
	fmt.Println("system(pause)")

	quit := make(chan os.Signal)

	signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)

	sig := <-quit

	for {
		if sig.String() == "interrupt" {
			break
		}
	}

}

// test path is folder  or file

// 判断所给路径是否为文件夹

func IsDir(path string) bool {

	s, err := os.Stat(path)

	if err != nil {

		return false

	}

	return s.IsDir()

}

// delete string space

func compressStr(str string) string {

	if str == "" {
		return ""
	}

	//匹配一个或多个空白符的正则表达式
	reg := regexp.MustCompile("\\s+")
	return reg.ReplaceAllString(str, "")

}

// folder rename, delete space

func cmm(str string) string {

	folder := str
	nfoler := str

	nfoler = compressStr(nfoler)

	err2 := os.Rename(folder, nfoler)

	if err2 != nil {
		panic(err2)

	} else {
		println(`文件夹重命名成功:` + nfoler)
		return "ok"
	}
}
