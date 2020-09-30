import pandas as pd
df = pd.read_excel("/Users/Juliana/Documents/Juliana/programacao/Valores_CT.xlsx")
coef_m = -3.397186047
coef_b = 58.53223295
ct = df.iloc[:, -1]
df["Quantity"] = 10 * ((ct - coef_b)/coef_m)
print(df)
