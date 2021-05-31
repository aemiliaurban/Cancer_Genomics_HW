# Cancer_Genomics_HW
## Homework 1

1. Download data from https://www.ncbi.nlm.nih.gov/assembly/GCF_000001405.13/ in .fasta format and homework data from https://gear.embl.de/data/.exercise/
2. Index the file
```console
bwa index genome.fasta
```
3. Align the files and create a SAM file
```console
bwa mem genome.fasta tu.r1.fq.gz tu.r2.fq.gz > tumor.sam
```
4. Convert the SAM file to BAM file
```console
samtools view -O BAM -o tumor.bam tumor.sam
```
5. Sort and index the BAM file
```console
samtools sort -T temp -O bam -o tumor.sorted.bam tumor.bam
samtools index tumor.sorted.bam
```
6. Get the depth
```console
samtools depth tumor.sorted.bam > tumor.sorted.coverage
```
7. Find the x chromosome and select the 20M to 40M region
```console
grep "CM000685" tumor.sorted.coverage > tumor.x.coverage
awk '{ if ($2 >= 20000000 && $2 <= 40000000) print $0 }' tumor.x.coverage > tumor.regiongs.coverage
```
8. Repeat the steps for the WT files
9. Run plot.py

## Homework 2
1. Fetch data here: https://gear.embl.de/data/.slides/deletion.tsv.gz
2. Run the Machine_Learning.py file
