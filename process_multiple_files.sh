#!/bin/bash

# Проверка наличия аргумента с именем файла
if [ $# -ne 1 ]; then
    echo "Usage: $0 <input_file>"
    exit 1
fi

# Чтение входного файла
input_file="$1"

# Проверка существования файла
if [ ! -f "$input_file" ]; then
    echo "Файл $input_file не существует."
    exit 1
fi

# Чтение данных из файла и выполнение операций для каждой строки
while read -r i j; do
    # Проверка, что i и j не пустые
    if [[ -n $i && -n $j ]]; then
        # Формирование имени входного файла и выходного файла
        input_filename="../control/gccoords_percents_${i}_my_40_subtract_from_all_filtered_without_quadr_and_CG_loop5.txt"
        output_filename="../filtered/max_all_40_${i}_gc_filtered_without_quadr_and_CG_loop5.txt"

        # Проверка существования файла
        if [ ! -f "$input_filename" ]; then
            echo "Файл $input_filename не существует. Пропускаем пару ($i, $j)."
            continue
        fi

        # Сортировка и выборка строк
        sorted_file=$(mktemp)
        sort -nk2 -r "$input_filename" | head -n "$j" > "$output_filename"

        echo "Обработана пара ($i, $j). Результат сохранён в $output_filename."
        
        # Удаление временного файла
        rm "$sorted_file"
    else
        echo "Ошибка в строке файла: '$i $j'. Пропускаем."
    fi
done < "$input_file"
