import pandas as pd
import sys
tabela = sys.argv[1]
coef_m = float(sys.argv[2])
coef_b = float(sys.argv[3])
df = pd.read_excel(tabela)
df["Quantity"] = 10 * ((df["CT"] - coef_b)/coef_m)
print(df)



import pandas as pd
import sys
tabela = sys.argv[1]
coef_m = float(sys.argv[2])
coef_b = float(sys.argv[3])
df = pd.read_excel(tabela)
col = df.iloc[:, 1:3]
df_q = pd.DataFrame()
df_q["Quantity"] = 10 * ((df["CT"] - coef_b)/coef_m)
qf_final = pd.concat([col, df_q], axis=1)
df_final.to_excel("/Users/Juliana/Documents/Juliana/programacao/Valores_CT.xlsx", sheet_name="Tabela")
print(df_final)

python teste.py/Users/Juliana/Documents/Juliana/programacao/Valores_CT.xlsx -3.4 58.5

