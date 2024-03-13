#!/bin/bash

# 获取脚本所在的当前目录
CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# 搜索并删除名字中包含“大航海”的mp3文件，同时打印出每个被删除的文件名
find "$CURRENT_DIR" -type f -name '*大航海*.mp3' -exec echo "Deleting file: {}" \; -exec rm {} \;

echo "All .mp3 files containing 大航海 have been deleted from $CURRENT_DIR"