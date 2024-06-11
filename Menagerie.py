#Menagerie version 1.0
#Author: Harley O'Connor Mount
#2024



from Bio import Entrez
from Bio import SeqIO


import sys

if len(sys.argv) != 3:
    print("Usage: python Menagerie.py <query> <max_records>")
    sys.exit(1)

query = sys.argv[1]
max_records = int(sys.argv[2])

def get_accessions_from_query(query, max_records):
    Entrez.email = "Q5S7Z@example.com"  # Always tell NCBI who you are
    handle=Entrez.esearch(db="nucleotide", term=query, retmax=max_records)
    records=Entrez.read(handle)
    return records

accessions=get_accessions_from_query(query, max_records)
accessions_list=accessions["IdList"]


def get_sequence_by_accession(accession):
    Entrez.email = "Q5S7Z@example.com"  # Always tell NCBI who you are
    handle=Entrez.efetch(db="nucleotide", id=accession, rettype="fasta", retmode="text")
    record=SeqIO.read(handle, "fasta")
    return record


accessions_sequences_list=[]
for accession in accessions_list:
    sequence=get_sequence_by_accession(accession)
    accessions_sequences_list+=[sequence]

sample_seq=str(get_sequence_by_accession("NC_045512.2"))





print(accessions_list)
print(accessions_sequences_list)