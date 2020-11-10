valores = [9,3,4,7,-1,5,7]
lista = [9,3,4,7]

def valor_lista(valores):
    lista = []
    for i in valores:
        if i != -1:
            lista.append(i)
        if i == -1:
            break
print("Lista:", lista)

def quantidade(lista):
    tamanho = len(lista)
    print("Quantidade de valores lidos:", tamanho)


def ordem_da_lista(lista):
    ordem = lista[:]
    print("Lista na ordem:", ordem)


 def ordem_invertida(lista):
     print("Lista invertida:")
     for i in reversed(lista):
         print(i)

 def soma_da_lista(lista):
     soma = sum(lista)
     print("Soma dos valores:", soma)

def media_dos_valores(lista):
    media = (sum(lista))/len(lista)
    print("Media dos valores:", media)


def acima_da_media(lista):
    v = 0
    for i in lista:
        while i <= len(lista)-1:
            if lista[i] > (sum(lista)) / len(lista):
                v = v +1
        else:
            i = i+1
    print(v)








