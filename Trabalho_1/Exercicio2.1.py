sequencia = (input('Digite sequencia de nucleotideos:'))
soma = 0
for i in sequencia:
    if str(i).upper() == "G" or str(i).upper() == "C":
        soma = soma + 1
print("GC=", (soma * 100)/len(sequencia))