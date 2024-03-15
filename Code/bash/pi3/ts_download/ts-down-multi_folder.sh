#!/bin/bash

echo "ts-down-pt-file_create a new folder and set its permissions."

echo "500g-tosh-2.5inch"

# 读取键盘输入的路径
# read -p "Enter the parent folder path: " parent_folder_path

# 获取脚本所在的当前目录
CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

#  添加 ts主目录
CURRENT_DIR="${CURRENT_DIR}/ts"

echo "ts-folder: ${CURRENT_DIR}"

# 子文件夹名称列表
subfolders=("mt" "ptt" "nc")

# 遍历子文件夹列表并创建子文件夹
for subfolder in "${subfolders[@]}"; do

  folder_path="$parent_folder_path/$subfolder"
  
  mkdir -p "$folder_path"
  
  sudo chown debian-transmission:debian-transmission "$folder_path"
  sudo chmod -R 757 "$folder_path"
  
  ls -ld "$folder_path"

done