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


def get_taxonomy_by_accession(accession):
    Entrez.email = "Q5S7Z@example.com"  # Always tell NCBI who you are
    handle = Entrez.efetch(db="taxonomy", id=accession, rettype="gb", retmode="text")
    records = [record for record in SeqIO.parse(handle, "gb")]
    if records:
        first_record = records[0]
        taxonomy = first_record.annotations.get("taxonomy", "")
        return taxonomy
    else:
        return "Taxonomy information not found"

taxonomy_list=[]
for accession in accessions_list:
    taxonomy=get_taxonomy_by_accession(accession)
    taxonomy_list+=[taxonomy]

info_dictionary={}

for i in range(len(accessions_list)):
    sequence=str(accessions_sequences_list[i].seq) #accessions_sequences_list.seq
    accession=accessions_list[i]
    description=str(accessions_sequences_list[i].description) #accessions_sequences_list[i].description
    info_dictionary[accession]={"sequence":sequence, "description":description}



