import pandas as pd
df = pd.read_excel("/Users/Juliana/Documents/Juliana/programacao/Juliana Caricio - WHO POP TB some.xlsx")
col = df.iloc[:, -1]
media = col.mean(axis=0)
mediana = col.median(axis=0)
print("media de mortes =", media, "\nmediana de mortes =", mediana)
