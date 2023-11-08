Part 2:
Q1: Are the majority of the CpG dinucleotides methylated or unmethylated?
- majority unmethylated

Q2: How does using nanopore for methylation calling differ from bisulfite sequencing in terms of coverage? Which method appears better and why?
- Nanopore coverage is around 35
- Bisulfite coverage is around 50
- nanopore seems to yield less coverage indicating that bisulfite sequencing might be better.

Q3: What can you infer about the two different approaches and their ability to detect methylation changes? 
- ONT is better at detecting methylation changes, because there is a broader spread of methylation differences between the wild-type and tumor samples.

Q4: What is the effect of tumorigenesis on global methylation patterns?
- Tumors have reduced global global methylation.

Part 4: Using IGV to explore differential methylation

Q5: What changes can you observe between the normal and tumor methylation landscape? What do you think the possible effects are of the changes you observed?
- There is a region of the tumor gene that is more methylated, indicating this gene is turned off in tumor samples. If you are turning off a methyltransferase, there will be less methylation globally.

Q6: What does it mean for a gene to be “imprinted”?
- The gene from one parent is silences, so the gene from the other parent is expressed.

Q7: What is happening when you select the option to phase the reads? What is required in order to phase the reads?
- It separates the reads into none (wt), 1 (het), or 2 (hom)

Q8: Can any set of reads be phased? Explain your answer. 
- No, because not all regions have multiple alleles (or have been mutated)













