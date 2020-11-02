nome = input("Digite seu nome completo:")
nota_1 = input("Digite 1º nota:")
nota_2 = input("Digite 2° nota:")
nota_3 = input("Digite 3° nota:")
faltas = input("Digite numero de faltas:")
media = (nota_1 + nota_2 + nota_3)/3
p_faltas = (faltas*100)/80
if p_faltas <= 25 and media >= 7.0:
    print("Situacao final: Aprovado")
elif p_faltas > 25 and media >= 7.0:
    print("Situacao final: Reprovado por falta")
elif media < 7.0 and p_faltas <= 25:
    print("situacao final: Reprovado por media")
elif p_faltas > 25 and media < 7.0:
    print("Situacao final: Reprovado por falta ")
