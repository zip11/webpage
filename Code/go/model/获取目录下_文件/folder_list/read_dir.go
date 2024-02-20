package main

import (
	"fmt"
	"os"
)

func main() {
	names, _ := ListDir("./")
	fmt.Printf("names:%v\n", names)
}

func ListDir(dirname string) ([]string, error) {
	infos, err := os.ReadDir(dirname)
	if err != nil {
		return nil, err
	}
	names := make([]string, len(infos))
	for i, info := range infos {
		names[i] = info.Name()
	}
	return names, nil
}
