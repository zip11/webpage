package main

import (
	"bytes"
	"fmt"
	"log"
	"os/exec"
)

func main() {

	cmdArguments := []string{"-i", "divx.avi", "-c:v", "libx264",
		"-crf", "20", "-c:a", "aac", "-strict", "-2", "video1-fix.ts"}

	cmd := exec.Command("ffmpeg", cmdArguments...)

	var out bytes.Buffer
	cmd.Stdout = &out
	err := cmd.Run()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("command output: %q", out.String())
}
