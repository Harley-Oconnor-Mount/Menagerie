#Menagerie version 1.0
#Author: Harley O'Connor Mount
#2024

#Debug
barcode="COI_sample.fasta"
search_term="Ursus americanus[orgn] or Ursus thibetanus[orgn]"

#Disable warnings
defaultW = getOption("warn")
options(warn = -1)

#install dependencies
if(require(ape) == FALSE) {install.packages("ape"); library(ape)}
if(require(phangorn) == FALSE) {install.packages("phangorn"); library(phangorn)}
if(require(spider) == FALSE) {install.packages("spider"); library(spider)}
if(require(rentrez) == FALSE) {install.packages("rentrez"); library(rentrez)}
if(require(ggplot2) == FALSE) {install.packages("ggplot2"); library(ggplot2)}
if(require(taxize) == FALSE) {install.packages("taxize"); library(taxize)}
if(require(gplots) == FALSE) {install.packages("gplots"); library(gplots)}
if(require(BiocManager) == FALSE) {install.packages("BiocManager"); library(BiocManager)}
if(require(Biostrings) == FALSE) {BiocManager::install("Biostrings"); library(Biostrings)}

#take user argument(s)
args = commandArgs(trailingOnly=TRUE)

search_term=args[1]
barcode=args[2]
outgroup_accession=args[3]
maximum_hit_value=args[4]
exclusion_list=args[5]

#store list of flagged phrases as variable
#used for regular expression matching
flagged_phrases='\\bPREDICTED\\b|\\bHypothetical\\b|\\bc\\.f\\.\\b|
\\bcloning vector\\b|\\bclone\\b|\\bsynthetic construct\\b|
\\benvironmental sample\\b|\\bhybrid\\b|\\bcell-line\\b|
\\b*-like\\b|\\bUNVERIFIED\\b|\\baff\\.\\b'

#determine barcode type from barcode
barcode_name=readLines(barcode)[c(T,F)] #read in barcode

if(grepl("COI", barcode_name, ignore.case = TRUE)) {
    search_term=paste0()
    barcode_type="COI"} #search for COI

#run query
result=rentrez::entrez_search(db = "nucleotide",
                              term = search_term,
                              retmax = 1000)
print(result)
print(flagged_phrases)