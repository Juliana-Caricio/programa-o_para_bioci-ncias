def Operacoes():
    lista = [0]
    while lista[-1] != "-1":
        x = input("Digite relacao dos materiais: ")
        lista.append(x)
        while lista[-1] != "-1":
            y = input("Digite relacao dos materiais: ")
            lista.append(y)
            while lista[-1] != "-1":
                z = input("Digite relacao dos materiais: ")
                lista.append(z)
    lista2 = lista[1:-1]
    i = 0
    j = 2
    l = []
    s = 1
    while i < len(lista2):
        print("Produto: ", lista2[i])
        print("Quantidade do produto: ", lista2[j])
        l.append(int(lista2[s]))
        i = i+3
        j = j+3
        s = s+3
    total = sum(l)
    print("Valor total de compras:", total)









Operacoes()