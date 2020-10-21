from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
multifasta = SeqIO.parse("/Users/Juliana/Documents/Juliana/programacao/sequencias.fasta", "fasta")
numero = 0
for line in multifasta:
    numero = numero + 1
    gravar = SeqRecord(line.seq, line.id)
    SeqIO.write(gravar, 'Sequência_%d.fasta' % numero, "fasta")
