#!/bin/bash

echo "ts-down-pt-file_create a new folder and set its permissions."

echo "500g-tosh-2.5inch"

# 获取脚本所在的当前目录
CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# 读取键盘输入的路径
read -p "Enter the folder path: " folder_path

dir_full="${CURRENT_DIR}/ts/${folder_path}"

echo "${dir_full}"

# 创建文件夹
sudo mkdir -p "${dir_full}"

# 将文件夹的所有权分配给 debian-transmission 用户
sudo chown debian-transmission:debian-transmission "${dir_full}"

# 使用 chmod -R 757 更改文件夹及其所有子文件和子文件夹的权限
sudo chmod -R 757 "${dir_full}"

# 显示新文件夹的权限
ls -ld "${dir_full}"
