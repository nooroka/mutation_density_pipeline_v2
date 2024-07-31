import glob

# Получаем список файлов txt в текущем каталоге
files = ["filtered_data0.8_loop5_39.txt","output_loop5_filtered_0.8_39.bed"]

# Проверяем, что у нас есть как минимум два файла
if len(files) < 2:
    print("Необходимо как минимум два файла для выполнения операции.")
else:
    # Считываем первый файл
    first_file = files[0]
    # Считываем второй файл
    second_file = files[1]

    # Создаем множество для хранения значений первого столбца второго файла
    second_file_values = set()

    # Читаем строки из второго файла и собираем значения первого столбца
    with open(second_file, 'r') as file:
        for line in file:
            values = line.strip().split()
            second_file_values.add(values[0])

    # Открываем файл для записи результата
    output_filename = f'matching_lines_in_{first_file}'
    with open(output_filename, 'w') as output_file:
        # Читаем строки из первого файла и проверяем значения первого столбца
        with open(first_file, 'r') as file:
            for line in file:
                values = line.strip().split()
                if values[0] in second_file_values:
                    # Записываем строку в файл результата
                    output_file.write(line)

    print(f"Строки с совпадающим значением первого столбца были записаны в {output_filename}.")
