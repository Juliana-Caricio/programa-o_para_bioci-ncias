peso = float(input("Peso(kg):"))
altura = float(input("Altura(m):"))
IMC = (peso/(altura**2))
if IMC < 18.5:
    print(IMC, "Condicao: Abaixo do Peso")
elif IMC >= 18.5 or IMC <= 25:
    print(IMC, "Condicao: Peso Normal")
elif IMC > 25 or IMC <= 30:
    print(IMC, "Condicao: Acima do Peso")
elif IMC > 30:
    print(IMC, "Condicao:Obeso")


