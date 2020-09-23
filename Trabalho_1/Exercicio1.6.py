import pandas as pd
df = pd.read_excel("/Users/Juliana/Documents/Juliana/programacao/Juliana Caricio - WHO POP TB some.xlsx")
deaths = df.iloc[:, -1]
loc = df.iloc[:, 1:2]
div = loc.div(100)
normal = (deaths/div)
print(normal)
