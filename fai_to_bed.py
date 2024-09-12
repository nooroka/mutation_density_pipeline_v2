def fai_to_bed(fai_file, bed_file):
    with open(fai_file, 'r') as f, open(bed_file, 'w') as out:
        for line in f:
            fields = line.strip().split('\t')
            sequence_name = fields[0]
            sequence_length = fields[1]
            chrom_start = 0
            chrom_end = sequence_length
            out.write(f"{sequence_name}\t{chrom_start}\t{chrom_end}\n")

# Путь к файлу .fai
fai_file = '../hg19_new.fna.fai'

# Путь к выходному файлу .bed
bed_file = '../hg19_new.fna.bed'

# Вызов функции
fai_to_bed(fai_file, bed_file)
