#!/bin/bash

# Output file name
output_file="head_loop5.fasta"

# Clear the output file (if it exists)
> "$output_file"

# Loop over each text file in the current directory
for file in max*loop5.txt; do
  echo "File: $file" >> "$output_file"
  awk '{if (NR<=5) print FILENAME, $4}' "$file" >> "$output_file"
done
