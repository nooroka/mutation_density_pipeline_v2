#!/bin/bash

# Проверяем, что передан входной файл и выходной файл
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 input_file output_file"
    exit 1
fi

input_file=$1
output_file=$2

# Используем awk для нахождения и подсчета дубликатов
awk '
{
    count[$1]++
    if (count[$1] == 2) {
        duplicates[$1] = $0
    }
}

END {
    for (item in duplicates) {
        print duplicates[item], count[item]
    }
}' "$input_file" > "$output_file"
