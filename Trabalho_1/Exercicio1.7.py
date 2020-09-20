import pandas as pd
df = pd.read_excel("/Users/Juliana/Documents/Juliana/programacao/Juliana Caricio - WHO POP TB some.xlsx")
colunas = df.iloc[[1, 2, 5, 8, 10],2:3]
soma = colunas.sum()
media = colunas.mean(axis=0)
print("Total de mortes dos BRICS:", soma, "\nMedia das mortes dos BRICS:", media)
