import pandas as pd
from Bio import SeqI0
tabela = pd.read_excel("/Users/Juliana/Documents/Juliana/programacao/Tabela_1.xlsx")
desconhecido = SeqI0.parse("/Users/Juliana/Documents/Juliana/programacao/Rdesconhecidus.fasta", "fasta")
conhecido = SeqI0.parse("/Users/Juliana/Documents/Juliana/programacao/VectorBase-48_RprolixusCDC_AnnotatedProteins.fasta", "fasta")
