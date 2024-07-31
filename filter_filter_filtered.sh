#!/bin/bash

# Цикл по всем файлам с именами, содержащими "matched" и расширением ".txt"
for i in {1..24}
do 
	python thres_to_fasta.py ../control/gccoords_percents_${i}_my_40_subtract_from_all_filtered_without_quadr_loop5.txt  ../control/${i}_40_without_quadr_loop5.fasta
	python /data/nooroka/grant/punkt1/bioinformatics-cafe/fastaRegexFinder.py -f  ../control/${i}_40_without_quadr_loop5.fasta -r '[Cc][Gg]' > ../control/${i}_40_loop5_without_quadr.bed
	python target_line_numbers.py  ../control/gccoords_percents_${i}_my_40_subtract_from_all_filtered_without_quadr_loop5.txt ../control/${i}_40_loop5_without_quadr.bed ../control/gccoords_percents_${i}_my_40_subtract_from_all_filtered_without_quadr_and_CG_loop5.txt 
  # Создаем временный файл
done
