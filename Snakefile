SAMPLES = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"]

rule all:
     input:
        expand("merged2/quadr738_chain180424_merged2_sorted_{number}fi_40_snp.bed",number = SAMPLES),
        expand("comp/comp{number2}hg19_gene.fasta.fai", number2 = SAMPLES),
        expand("comp/comphg19{number3}_gene_GCmerged.fasta",number3 = SAMPLES),
        expand("../punkt1/merged/quadr7_chain180424_merged2_sorted_{number3}_40.bed",number3 = SAMPLES),
        expand("meanquadr/meanquadrhg19{number3}_my_40_snp.txt",number3 = SAMPLES),
        expand("results/results_hg19_percents_{number3}_my_40.txt",number3 = SAMPLES),
        expand("gccoords/gccoords_percents_{number3}_my_40_snp.txt",number3 = SAMPLES),
        expand("densities/densitiesGSM40_percent-1206_snp.txt")
                                                                                        

rule filter:
    input:
      "../punkt1/merged/quadr738_chain180424_merged2_sorted_{number}_40.bed" 
    output: 
      "merged2/quadr738_chain180424_merged2_sorted_{number}fi_40_snp.bed"
    shell:
      "python filter.py {input} {output} {wildcards.number}"
rule bedtools:
    input:
      "comp/comp{number2}hg19_gene.bed"
    output:
      "comp/comp{number2}hg19_gene.fasta"
    shell:
       "bash script6.sh {input} {output}"
rule script3:
    input:
      rules.bedtools.output
    output:
      "comp/comp{number2}hg19_gene.fasta.fai"
    shell:
       "bash script3.sh {input} {output}"
rule script4:
    input:
       "../punkt1/GSM/GSM_hg196_un_{number3}_40_my.bed",
       "../punkt1/merged/quadr7_chain180424_merged2_sorted_{number3}_40.bed"
    output:
       "comp/comphg19{number3}_gene_GCmerged.fasta",
    shell:
       """
       bash script4.sh {input} {output}
       """
rule mean: 
    input:
      "../punkt1/merged/quadr7_chain180424_merged2_sorted_{number4}_40.bed"
    output:
      "meanquadr/meanquadrhg19{number4}_my_40_snp.txt"
    shell:
      """
      python mean.py {input} {output}
      """

rule cat:
     input:
       x1 = expand("meanquadr/meanquadrhg19{number3}_my_40.txt", number3 = SAMPLES),
       x2 = "comp/comphg19{number3}_gene_GCmerged.fasta"
     output:
       "results/results_hg19_percents_{number3}_my_40_snp.txt"
     shell:
       """
       cat {input.x1} > meanquadr/meanquadrhg19_my_40_snp.txt
       python windowrun13.py meanquadr/meanquadrhg19_my_40_snp.txt {input.x2}  {output} {wildcards.number3}
       """ 


rule coordsgc:
     input:
        rules.cat.output
     output:
        "gccoords/gccoords_percents_{number3}_my_40_snp.txt"
     shell:
        """
        python coordsgc13.py {input} {output}
        """

rule script2:
     input:
        "../punkt1/merged/quadr7_chain180424_merged2_sorted_{number3}_40.bed",
        rules.coordsgc.output
     output:
        "densities/densitiesGSM40_percent{number3}-1206_snp.txt"
     shell:
         """
         python script2.py {input} {wildcards.number3} {output}
         """
rule cat2:
     input:
        expand("densities/densitiesGSM40_percent{number3}-1206_snp.txt",number3 = SAMPLES)
     output:
        "densities/densitiesGSM40_percent-1206_snp.txt"
     shell:
        "cat {input} > {output}"

