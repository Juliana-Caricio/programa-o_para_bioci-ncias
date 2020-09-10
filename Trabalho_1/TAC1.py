refArquivo = open("\Users\Juliana\Documents\Juliana\programacao\Arquivo fasta.txt")
identificador = refArquivo.readline()[1:16]
sequencia = ""
for linha in refArquivo:
    sequencia += linha.replace('\n', '')
print ("identificador: %s" % identificador)
print ("Sequencia: %s" % sequencia)
refArquivo.close()
