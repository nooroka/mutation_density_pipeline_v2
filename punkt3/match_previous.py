import glob

# Получаем список файлов txt в текущем каталоге
#files2 = glob.glob('max*39*loop5.txt')
file = "matching_lines_in_filtered_data0.8_loop5_39.txt"
# Создаем словарь для хранения строк по ключу из первого столбца
data_dict = {}

# Читаем строки из всех файлов и заполняем словарь

with open(file, 'r') as input_file:
        for line in input_file:
            values = line.strip().split()
            key = values[0].split('/')[-1]  # Извлекаем ключ из первого столбца
            data_dict[key] = values[1:]  # Сохраняем остальную часть строки

# Открываем файл для записи результата
#output_filename = 'output_results.txt'
   # Проходим по всем ключам и ищем соответствующие файлы
for key, rest_of_line in data_dict.items():
        # Разделяем ключ по символу "_"
        parts = key.split('_')
        # Соединяем все части, кроме последней
        file_name_part = "gccoordsmax/"+'_'.join(parts[:-1]) + '.txt'
        try:
            with open(file_name_part, 'r') as search_file:
                for search_line in search_file:
                    search_values = search_line.strip().split()
                    #print(search_values,data_dict[key])
                    if search_values == data_dict[key]: 
                        file_name_part_split = file_name_part.split(".")[0]
                        output_file_name = str(file_name_part_split)+"_matched"+"."+"txt"
                        output_file = open(output_file_name,"a")
                        # Записываем строку с ключом и остальной частью строки в файл результата
                        line_to_write = "{}\n".format('\t'.join(rest_of_line))
                        output_file.write(line_to_write)
                        output_file.close()
        except FileNotFoundError:
            print(f"Файл {file_name_part} не найден. Пропускаем...")

     
