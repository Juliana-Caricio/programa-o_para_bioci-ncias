import pandas as pd
df = pd.read_excel("/Users/Juliana/Documents/Juliana/programacao/Juliana Caricio - WHO POP TB some.xlsx")
crescente = df.sort_values(by=["TB deaths"])
print(crescente)
