import pandas as pd
from Bio.Blast.Applications import NcbiblastxCommandline
seq_desconhecida = input("sequencia desconhecida:")
seq_proteinas = input("proteina Trypanosoma cruzi:")
blast_x = "/Users/Juliana/Documents/Juliana/programacao/blastx.exe"
arquivo_blast = r"/Users/Juliana/Documents/Juliana/programacao/Arquivo Blasta.TAC3.txt"
comparacao = NcbiblastxCommandline(cmd = blast_x ,query = seq_desconhecida, subject = seq_proteinas, evalue = 0.05, outfmt = 6, out = arquivo_blast)
stdout, stdeer = comparacao()
blast_resultado = pd.read_cvs("/Users/Juliana/Documents/Juliana/programacao/Arquivo Blasta.TAC3.txt",)
maximo = blast_resultado.sort_values("Bitscore")
print(maximo.iloc[[-1]])

