SAMPLES = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"]

rule all:
     input:
        expand("merged/quadr738_chain180424_merged2_sorted_{number}.bed",number = SAMPLES),
        expand("GSM/GSM_hg386_un_{number}.bed",number = SAMPLES),
        expand("GSM/GSM_hg196_un_{number}.bed",number = SAMPLES),
  

rule count1:
     input:
         "GSM3003540/GSM3003540_quadr_7_6.bed"
     output: 
         "quadr7_chain180424.bed"
     shell:
         "python count.py {input} {output}"
rule split4:
     input: 
       rules.count1.output
     output:
      x1 = "quadr7_chain180424+.bed",
      x2 = "quadr7_chain180424-.bed"
     shell:
        "python split4.py {input} {output.x1} {output.x2}"
         
rule merge:
     input:
       rules.split4.output
     output:
       x1 = "quadr7_chain180424_merged+.bed",
       x2 = "quadr7_chain180424_merged-.bed"
     shell:
          """
          bash merge.sh {input[0]} {input[1]}  {output.x1} {output.x2}
          """
rule cat:
     input:
       rules.merge.output
     output:
       "merged/quadr7_chain180424_merged2.bed"
     shell:
        """
        cat {input}> {output}
        """
rule bedtools:
     input:
        rules.cat.output
     output:
        "merged/quadr7_chain180424_merged2_sorted.bed"
     shell:
        """
        bedtools sort -i {input} > {output}
        """

rule split:	
     input:
        rules.bedtools.output
     output:
       	"merged/quadr7_chain180424_merged2_sorted_{number}.bed"
     shell:
        """
        python split.py {input} {output} {wildcards.number}
        """
        
rule split2:
     input:
        "GSM3003540/GSM3003540_quadr_7_6.bed"
     output:
        "GSM/GSM_hg196.bed"
     shell:
        """
        python split2.py {input} {output}
        """
rule uniq:
     input:
         rules.split2.output
     output:
         "GSM/GSM_hg196_un.bed"
     shell:
         "uniq {input} > {output}"
rule run1:
     input:
        rules.uniq.output
     output:
        "GSM/GSM_hg386_un.bed",
     shell:
        """
        bash run.sh {input} {output}
        """
rule sp32:
     input:
        rules.run1.output
     output:
        "GSM/GSM_hg386_un_{number}.bed"
     shell:
        """ 
        python split3.py {input} {output} {wildcards.number}
        """
rule sp31:
     input:
        rules.uniq.output
     output:
        "GSM/GSM_hg196_un_{number}.bed"
     shell:
        """
        python split3.py {input} {output} {wildcards.number}
        """
rule run2:
     input: 
         rules.split.output
     output:
         "merged/quadr738_chain180424_merged2_sorted_{number}.bed"
     shell:
         "bash run.sh {input} {output}"

