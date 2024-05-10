#for i in {1..24}

   #./liftOver quadr7_chain180424_merged2_sorted_${i}.bed hg19ToHg38.over.chain quadr738_chain180424_merged2_sorted_${i}.bed unMapped
./liftOver  $1 hg19ToHg38.over.chain $2 unMapped 

