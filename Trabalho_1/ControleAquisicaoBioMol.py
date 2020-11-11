def controle_aquisicao_biomol():
    x = input("Digite a relacao de produtos:")
    y = x.replace("-1","")
    lista1 = y.split(",")
    tupla = [tuple(x.split(' ')) for x in lista1]
    dicionario = dict(tupla)
    print(dicionario)

controle_aquisicao_biomol()