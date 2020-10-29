import re
from Bio import SeqIO
def contagem(sequencia,motivo):
    gene = str(line.id)
    frequencia = sequencia.count(motivo)
    if frequencia != 0:
        print("Identificador: ", gene, "Contagem: ", frequencia, sep="")


motivo = str(input("Digite motivo de DNA ou aminoacido:"))
if re.search('^[ACGT]+$', motivo):
    fasta = SeqIO.parse("sequencias.fasta", "fasta")
    for line in fasta:
        sequencia = str(line.seq)
        contagem(sequencia,motivo)
else:
    print("Sequencia de aminoacidos")
    fasta = SeqIO.parse("TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins (1).fasta", "fasta")
    for line in fasta:
        sequencia = str(line.seq)
        contagem(sequencia, motivo)

