from Bio import SeqIO
from Bio.Blast.Applications import NcbiblastxCommandline
records = SeqIO.index("Rdesconhecidus.fasta", "fasta")
x = records.get_raw("gene_1").decode()
y = str(x)
blastx = "/Users/Juliana/Documents/Juliana/programacao/blastx.exe"
txt = "/Users/Juliana/Documents/Juliana/programacao/blast.txt"
comando_blastx = NcbiblastxCommandline(cmd= blastx, query= x, subject="VectorBase-48_RprolixusCDC_AnnotatedProteins.fasta", outfmt=0, out="blast.txt")
stdout, stderr = comando_blastx()
blast_result = open("blast.txt", "r")
linhas = blast_result.read()
print(linhas)