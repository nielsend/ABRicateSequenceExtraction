# ABRicate Sequence Extraction

The ABRicate Sequence Extraction script takes the output from [ABRicate](https://github.com/tseemann/abricate) and FASTA files to return the nucleotide sequences in a FASTA format.

Any [ABRicate](https://github.com/tseemann/abricate) database can be used with this program:
* resfinder
* PlasmidFinder
* Virulence Finder Database (vfdb)
* Custom database
* Etc

To use the script:
```./ABRicateSequenceExtraction.py [ABRicate Output] [Directory with Fastas (include any '/')] > [Output in fasta format]``` 

***A best practice is to filter any ABRicate output by the %COVERAGE and %IDENTITY values before running this script***

To avoid confusion with multiple gene targets having duplicates in a FASTA file, the FASTA 'hit' detected by ABRicate is named in the following format: 
```>[gene]~~~[Accession]~~~[Genome Start Position]~~~[Genome End Position]~~~[File Name]```

Standard Out View:
![Standard Out View](https://github.com/nielsend/ABRicateSequenceExtraction/blob/master/ABRSeqExtractOutput.png)
