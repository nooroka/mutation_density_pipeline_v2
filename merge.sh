#!/bin/bash
for i in {1..24}
do
  bedtools sort  -i /data/nooroka/grant/punkt3/quadr738fi_${i}.bed | bedtools merge > /data/nooroka/grant/punkt3/quadr738_${i}_merged.bed
done
