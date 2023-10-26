#!/bin/bash

#creating an index to speed up mapping
#bwa index sacCer3.fa

# for sample in *.fastq
# do
#     echo "Aligning sample:" $sample
#     bwa mem -t 4 -R "@RG\tID:${sample}\tSM:${sample}" \
#         sacCer3.fa ${sample} > ${sample}.sam
# done

# for sam_file in *.sam
# do
#     echo "Make bams:" $sam_file
#     samtools sort -o ${sam_file}.bam -O bam ${sam_file}
# done

# for bam_file in *.bam
# do
#     echo "Indexing bams:" $bam_file
#     samtools index ${bam_file} > ${bam_file}.bai
# done


#freebayes -f sacCer3.fa -L bam_files_list.txt --genotype-qualities -p 1 > yeast_variants.vcf

#vcffilter -f "QUAL > 20" yeast_variants.vcf > filtered_yeast_variants.vcf

#vcfallelicprimitives -k -g filtered_yeast_variants.vcf > decomp_yeast_variants.vcf

snpEff ann R64-1-1.105 decomp_yeast_variants.vcf > ann_yeast_variants.vcf


