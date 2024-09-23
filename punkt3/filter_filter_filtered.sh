#!/bin/bash

# Цикл по всем файлам с именами, содержащими "matched" и расширением ".txt"
for i in {1..24}
do 
	python thres_to_fasta.py ../control/gccoords_percents_${i}_my_39_subtract_from_all_filtered_without_quadr_loop7.txt  ../control/${i}_my_39_subtract_from_all_filtered_without_quadr_loop7.fasta
	python /data/nooroka/grant/punkt1/bioinformatics-cafe/fastaRegexFinder.py -f  ../control/${i}_my_39_subtract_from_all_filtered_without_quadr_loop7.fasta -r '[Cc][Gg]' > ../control/${i}_my_39_subtract_from_all_filtered_without_quadr_loop7_target.bed 
	python target_line_numbers.py ../control/gccoords_percents_${i}_my_39_subtract_from_all_filtered_without_quadr_loop7.txt    ../control/${i}_my_39_subtract_from_all_filtered_without_quadr_loop7_target.bed ../control/gccoords_percents_${i}_my_39_all_control3.txt 
  # Создаем временный файл
done
