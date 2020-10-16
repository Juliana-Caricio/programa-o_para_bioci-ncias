seq = (input("Digite a sequencia de DNA:"))
coordenada1 = (input("Digite coordenada do exon1:")).split(":")
coordenada2 = (input("Digite coordenada do exon2:")).split(":")
exon1 = seq[int(coordenada1[0])-1:int(coordenada1[-1])-1]
exon2 = seq[int(coordenada2[0])-1:int(coordenada2[-1])-1]
seq_final = exon1 + exon2
print(seq_final)

