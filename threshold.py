import glob

# Пороговое значение для первой колонки
threshold = 0.8

# Получаем список файлов txt в текущем каталоге
files = glob.glob('gccoordsmax/max*39*loop5.txt')

# Открываем файл для записи результата
with open('filtered_data0.8_loop5_39.txt', 'w') as output_file:
    # Цикл по всем файлам txt
    for file in files:
        # Читаем каждую строку из текущего файла
        with open(file, 'r') as input_file:
            lines = input_file.readlines()
        
        # Извлекаем имя файла без расширения
        filename = file.split('.')[0]
        
        # Фильтруем строки и записываем в файл filtered_data.txt
        for line_number, line in enumerate(lines, start=1):
            # Разделяем строку на значения
            values = line.strip().split()
            
            # Проверяем значение первой колонки (предполагается, что оно числовое)
            if float(values[1]) > threshold:
                # Записываем строку с добавлением названия файла и номера строки
                output_file.write(f"{filename}_{line_number}\t{line}")

print("Файлы были отфильтрованы. Результаты записаны в filtered_data0.8_loop5_39.txt")
