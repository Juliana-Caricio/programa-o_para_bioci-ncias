import pandas as pd
df = pd.read_excel("/Users/Juliana/Documents/Juliana/programacao/Juliana Caricio - WHO POP TB some.xlsx")
media = df.mean(axis=0)
mediana = df.median(axis=0)
print("media =", media, "mediana =", mediana)
