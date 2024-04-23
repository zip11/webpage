#!/bin/bash

# 脚本用途：删除文件夹下子文件夹内的 .opus 文件，并显示删除进度

# 文件夹路径
folder="/home"

# 获取文件夹下的所有子文件夹
subdirs=$(find "$folder" -mindepth 1 -type d)

# 统计总共的子文件夹数量
total_subdirs=$(echo "$subdirs" | wc -l)

# 初始化计数器
deleted_files=0

# 遍历每个子文件夹
while IFS= read -r subdir; do
    # 获取子文件夹名称
    subdir_name=$(basename "$subdir")

    # 显示删除进度
    printf "Deleting .opus files in %s... " "$subdir_name"

    # 删除子文件夹内的 .opus 文件，并统计删除的文件数量
    deleted_count=$(find "$subdir" -type f -name "*.opus" -delete -print | wc -l)
    deleted_files=$((deleted_files + deleted_count))

    # 显示已删除的文件数量
    printf "%d files deleted\n" "$deleted_count"

done <<< "$subdirs"

# 显示总共删除的文件数量
echo "Total $deleted_files .opus files deleted."
