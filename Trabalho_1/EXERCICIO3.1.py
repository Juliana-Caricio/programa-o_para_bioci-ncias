valor = [float(i) for i in input("Digite valores:").split()]
media =(sum(valor))/len(valor)
positivos = 0
negativos = 0
for num in valor:
    if num < 0:
        negativos = negativos + 1
    elif num > 0:
        positivos = positivos + 1
porcentagemP = (positivos/len(valor))*100
porcentagemN = (negativos/len(valor))*100
print("Media:", media, "Positivos", positivos, "Negativos", negativos, "Porcentagem de positivos:", porcentagemP, "Porcentagem de negativos:", porcentagemN)

