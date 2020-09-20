import pandas as pd
df = pd.read_excel("/Users/Juliana/Documents/Juliana/programacao/Juliana Caricio - WHO POP TB some.xlsx")
mult = df.mul([1, 1, 100000], axis=1)
loc = mult.iloc[:, -1]
div = loc.div([21472, 200362, 1393337, 757, 1704, 1252140, 25834, 10608, 142834, 193, 52776, 1133], axis=0)
print("Taxa de morte por 100000 habitantes :\n", div)
