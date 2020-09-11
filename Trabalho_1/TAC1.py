refArquivo = open("\Users\Juliana\Documents\Juliana\programacao\TcCLB.FASTA")
identificador = refArquivo.readline()[1:16]
sequencia = ""
for linha in refArquivo:
    sequencia += linha.replace('\t', '')
print ("identificador: %s" % identificador)
print ("Sequencia: %s" % sequencia)
refArquivo.close()
