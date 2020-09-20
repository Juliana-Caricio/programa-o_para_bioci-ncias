import pandas as pd
df = pd.read_excel("/Users/Juliana/Documents/Juliana/programacao/Juliana Caricio - WHO POP TB some.xlsx")
col = df.iloc[:, -1]
soma = col.sum()
print("Total de mortes =", soma)
