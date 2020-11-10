def funcao_lambda():
    frase = input("Digite uma frase:")
    lista_v = ["A","E","I","0","U"]
    lista_n = ["0","1","2","3","4","5","6","7","8","9"]
    lista = lista_v + lista_n
    frase = frase.upper()
    vogal = lambda x: x in lista_v
    consoante = lambda x: x not in lista
    numero = lambda x: x in lista_n
    for x in frase:
        if vogal(x) == True:
            print(x, ' e uma vogal')
        elif consoante(x) == True:
            print(x, ' e uma consoante')
        elif numero(x) == True:
            print(x, ' e um numero')
funcao_lambda()


