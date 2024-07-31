#!/bin/bash

# Цикл по всем файлам с именами, содержащими "matched" и расширением ".txt"
for i in {1..24}
do 
	python thres_to_fasta.py ../control/gccoords_percents_${i}_my_40_subtract_from_all.txt ../control/${i}_40.fasta
	python /data/nooroka/grant/punkt1/bioinformatics-cafe/fastaRegexFinder.py -f  ../control/${i}_40.fasta -r '[gG]{3,}\w{1,7}[gG]{3,}\w{1,7}[gG]{3,}\w{1,7}[gG]{3,}' > ../control/${i}_40_loop7.bed
	python target_line_numbers.py ../control/gccoords_percents_${i}_my_40_subtract_from_all.txt ../control/${i}_40_loop7.bed ../control/gccoords_percents_${i}_my_40_subtract_from_all_filtered_without_quadr_loop7.txt 
  # Создаем временный файл
done
