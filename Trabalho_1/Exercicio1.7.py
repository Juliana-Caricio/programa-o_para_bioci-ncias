import pandas as pd
df = pd.read_excel("/Users/Juliana/Documents/Juliana/programacao/Juliana Caricio - WHO POP TB some.xlsx")
col = df.iloc[:, -1]
maior = col.max()
menor = col.min()
print("Maior numero de mortes:", maior, "\nMenor numero de mortes:", menor)
