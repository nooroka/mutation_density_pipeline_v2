#!/bin/bash

# Путь к папке с файлами
folder_path="/data/nooroka/grant/punkt3/gccoords"
# Маска для поиска файлов
file_mask="gccoords_percents_*_my_39_subtract_from_all_loop5.txt" # Измените на нужную вам маску

# Цикл по всем файлам в папке, соответствующим маске
for file in "$folder_path"/$file_mask
do
    # Проверяем, что это файл
    if [[ -f "$file" ]]; then
        # Сортируем файл по 5-й колонке и сохраняем результат в тот же файл
        sort -k 3 "$file" -o "$file"
    fi
done
