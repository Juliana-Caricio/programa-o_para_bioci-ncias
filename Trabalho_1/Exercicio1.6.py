import pandas as pd
df = pd.read_excel("/Users/Juliana/Documents/Juliana/programacao/Juliana Caricio - WHO POP TB some.xlsx")
normal = df["Population (1000s)"]/100
deaths = df["TB deaths"]/normal
print("Taxa de morte normalizada por 100.000 habitantes:\n", deaths)