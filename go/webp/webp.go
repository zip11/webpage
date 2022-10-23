package main

import (
	"bufio"
	"bytes"
	"fmt"
	"log"
	"os"
	"os/exec"
	"os/signal"
	"path"
	"path/filepath"
	"strings"
	"syscall"
	"unsafe"
)

func main() {

	// ~~~ jpg List ~~~

	fmt.Println(" jpg , png to webp ,ffmpeg,分辨率/2,压缩质量 95，golang win")

	var files []string

	// ~~~ 遍历 jpg png 图片 ~~~ start

	// input jpg folder path
	root := inputjpglj()

	err := filepath.Walk(root, func(path string, info os.FileInfo, err error) error {
		files = append(files, path)
		return nil
	})

	if err != nil {
		panic(err)
	}

	// ~~~ end ~~~~~

	// ~~~ trans  jpg  start ~~~

	jpgfileall(files)

	ShowMessage2("webp ffmpeg", "task end !")

	// pause cmd
	pauserun()

}

// input jpg folder path 路径文件名 可以有空格
func inputjpglj() string {
	// jpg root path

	println("input jpg folder path :")

	var jpglj string

	var msg string
	reader := bufio.NewReader(os.Stdin) // 标准输入输出
	msg, _ = reader.ReadString('\n')    // 回车结束
	msg = strings.TrimSpace(msg)        // 去除最后一个空格

	jpglj = msg

	//jpglj = "D:\\go\\src\\3"

	//jpglj = `D:\go\src\Okita Rinka-2021.11Patreon-Tier1~7\`

	// replace \ to \\
	jpglj = strings.Replace(jpglj, "\\", "\\\\", 1)

	fmt.Println("jpglj: ", jpglj)

	return jpglj
}

// all jpg to webp
func jpgfileall(files []string) {

	// jpg file list
	var wj []string

	for _, file := range files {

		//fmt.Println(file)

		//只 添加 文件
		if IsFile(file) {

			// pic .jpg

			//获取 小写 扩展名
			kzm := strings.ToLower(filepath.Ext(file))

			// 只 需要 图片 文件
			if kzm == ".jpg" || kzm == ".png" {

				wj = append(wj, file)

				//fmt.Println(file)

			}

		}
	}

	// jpg to webp
	for _, value := range wj {

		fmt.Println("\n jpg wj[]:", value, '\n')

		otp := value

		// old-jpg name  to  new-webp name
		ntp := tontp(otp)

		// ffmpeg jpg to webp 1-pic
		towebp(otp, ntp)

		// delete jpg file 1-pic
		delfile(otp)

	}
}

// ~~~ jpg delete ~~~

func delfile(file string) {

	err := os.Remove(file)
	//删除文件test.txt

	if err != nil {

		//如果删除失败则输出 file remove Error!

		fmt.Println("file remove Error!")

		//输出错误详细信息

		fmt.Printf("%s", err)

	} else {

		//如果删除成功则输出 file remove OK!

		fmt.Print("file remove OK:  ", file)

	}
}

// check file  true
func IsFile(f string) bool {

	fi, e := os.Stat(f)
	if e != nil {
		return false
	}
	return !fi.IsDir()
}

// make new webp name
func tontp(otp string) string {

	// \ to / linux

	otp = filepath.ToSlash(otp)

	// replace \ to \\
	//otp = strings.Replace(otp, "\\", "\\\\", -1)

	// jpg file name

	//path to 1.jpg
	wjm := path.Base(otp)

	// path to dir name
	ml := path.Dir(otp)

	//fmt.Println("jpg name: " + wjm + "\n folder name:" + ml)

	//  path to .jpg
	kzm := filepath.Ext(otp)

	// new webp path
	ntp := strings.Replace(wjm, kzm, ".webp", 1)
	ntp = path.Join(ml, ntp)

	// liunx / to \
	ntp = filepath.FromSlash(ntp)

	fmt.Println("new webp:" + ntp)

	//otp = filepath.FromSlash(otp)
	return ntp
}

// jpg to webp ffmpeg cmd

func towebp(otp string, ntp string) {

	//~~~~ cmd start ~~~~~~~~~~

	//"ffmpeg -i " + oldtp1 + "  -vf scale=-1:ih/" + tpgd + " -preset   picture -quality 95  " + ntp1

	cmdArguments := []string{"-i", otp, "-vf", "scale=-1:ih/2", "-preset", "picture", "-quality", "95", ntp}

	cmd := exec.Command("ffmpeg", cmdArguments...)

	var out bytes.Buffer
	cmd.Stdout = &out

	err := cmd.Run()

	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf("command output: %q", out.String())
}

// pause cmd

func pauserun() {

	//pause , ctrl+c exit

	fmt.Println("system(pause)")

	quit := make(chan os.Signal)

	signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)

	sig := <-quit

	for {
		if sig.String() == "interrupt" {
			break
		}
	}

	//~~~ pause end ~~~
}

// ------ msgbox start------

func IntPtr(n int) uintptr {

	//uintptr是golang的内置类型，是能存储指针的整型
	return uintptr(n)

}

func StrPtr(s string) uintptr {

	//unsafe.Pointer是特别定义的一种指针类型（译注：类似C语言中的void类型的指针），
	//它可以包含任意类型变量的地址。当然，我们不可以直接通过*p来获取unsafe.Pointer指针指向的真实变量的值，
	//因为我们并不知道变量的具体类型

	return uintptr(unsafe.Pointer(syscall.StringToUTF16Ptr(s)))

}

func ShowMessage2(tittle, text string) {

	//立即加载DLL
	user32dll, _ := syscall.LoadLibrary("user32.dll")

	//懒加载方式加载DLL
	user32 := syscall.NewLazyDLL("user32.dll")

	MessageBoxW := user32.NewProc("MessageBoxW")

	MessageBoxW.Call(IntPtr(0), StrPtr(text), StrPtr(tittle), IntPtr(0))

	//不再需要使用DLL里的函数之后可以卸载DLL
	defer syscall.FreeLibrary(user32dll)

}

// --- msgbox end ------
