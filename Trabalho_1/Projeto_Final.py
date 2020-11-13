import pandas as pd
tabela = pd.read_excel("/Users/Juliana/Documents/Juliana/programacao/Tabela_1.xlsx")
coluna1 = tabela.iloc[:,1]
soma1 = sum(coluna1)
coluna_nova = pd.DataFrame()
coluna_nova["Rap_1A_Normal"] = (coluna1*1000000)/soma1
tabela_nova = pd.concat([tabela,coluna_nova], axis=1)
print(tabela_nova)

