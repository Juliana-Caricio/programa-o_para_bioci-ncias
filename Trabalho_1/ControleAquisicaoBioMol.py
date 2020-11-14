def controle_aquisicao_biomol():
    lista  = [0]
    while lista[-1] != "-1":
        x = input("Digite relacao de materias:")
        lista.append(x)
    lista2 = lista[1:-1]
    tupla = [tuple(x.split(' ')) for x in lista2]
    dicionario = dict(tupla)
    print(dicionario)
    from OperacoesCompra.py import OperacoesCompra()



controle_aquisicao_biomol()
