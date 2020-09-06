refArquivo = open("/Users/Juliana/Documents/Juliana/programacao")
cabecalho = refArquivo.readline()[1:-1]
sequencia = ""
for linha in refArquivo:
    sequencia += linha.replace('\n', '')
print ("Cabecalho: %s" % cabecalho)
print ("Sequencia: %s" % sequencia)
refArquivo.close()
