#!/bin/bash

# 脚本用途：将原始文件夹中的 .opus 文件移动到同名的目的地文件夹中的子文件夹

# 原始文件夹路径
source_folder="原始文件夹"
# 目的地文件夹路径
destination_folder="目的地文件夹"

echo "Starting file transfer from $source_folder to $destination_folder..."

# 遍历原始文件夹下的子文件夹
for subdir in "$source_folder"/*; do

    # 检查子文件夹是否存在
    if [ -d "$subdir" ]; then

        # 获取子文件夹名称
        subdir_name=$(basename "$subdir")

        echo "Processing subdirectory: $subdir_name"
        # 创建目的地文件夹中的同名子文件夹（如果不存在）
        mkdir -p "$destination_folder/$subdir_name"

        # 检查目的地文件夹中的子文件夹是否成功创建
        if [ $? -eq 0 ]; then
            echo "Destination subdirectory created: $destination_folder/$subdir_name"
        else
            echo "Failed to create destination subdirectory: $destination_folder/$subdir_name"
            exit 1
        fi

        echo "Moving files from $subdir_name..."
        # 复制原始文件夹下的 opus 文件到目的地文件夹的同名子文件夹中
        cp "$subdir"/*.opus "$destination_folder/$subdir_name/"

        # 检查文件是否成功移动
        if [ $? -eq 0 ]; then
            echo "Files moved successfully to $destination_folder/$subdir_name"
        else
            echo "Failed to move files to $destination_folder/$subdir_name"
            exit 1
        fi

    fi
done

echo "File transfer completed successfully!"
