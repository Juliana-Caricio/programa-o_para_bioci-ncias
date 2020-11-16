from Bio import SeqIO
arquivo = open("Rdesconhecidus.fasta", "r")
for i in SeqIO.parse(arquivo, "fasta"):
    if i.id == "gene_4173":
        a = i.seq
    elif i.id == "gene_14620":
        b = i.seq
    elif i.id =="gene_11243":
        c = i.seq
    elif i.id == "gene_9071":
        d = i.seq
    elif i.id == "gene_3778":
        e = i.seq
print( a,"\n", b,"\n", c,"\n", d,"\n",e)

from Bio.Blast.Applications import NcbiblastxCommandline
sequencia = input(str("sequencia conhecida:"))
meuOutPut = "blast.txt"
blastx = "/Users/Juliana/Documents/Juliana/programacao/blastx.exe"
meu_comando = NcbiblastxCommandline( query = str(a), subject = sequencia, outfmt = 6, out = meuOutPut, evalue = 0.05, cmd = blastx)
print("Executando busca local:")
stdout, stderr = meu_comando()
print("Fim da execucao:")
blast_result = open(meuOutPut, "r")
resultado = blast_result.read()

import pandas as pd
result = pd.read_csv("blast.txt", sep="\t", names=["qseqid","sseqid","pident","length","mismatch","gapopen","qstart","qend","sstart","send","evalue","bitscore"])
maximo_score = resultado.sort_values("bitscore")
print(maximo_score.iloc[[-1]])







