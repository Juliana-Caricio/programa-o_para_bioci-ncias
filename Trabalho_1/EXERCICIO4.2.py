def calculaAreaRetangulo():
    a = int(input("Digite lado do retangulo:"))
    b = input("Digite outro lado do retangulo:")
    area = 0
    if b == "":
        area = a*a
    else:
        b = int(b)
        area = a*b
    print(area)


calculaAreaRetangulo()