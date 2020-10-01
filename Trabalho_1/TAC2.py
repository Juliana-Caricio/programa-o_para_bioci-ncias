def quantidade_absoluta(coef_m, coef_b, tabela):
    import pandas as pd
    df = pd.read_excel(tabela)
    df["Quantity"] = 10 * ((df["CT"] - coef_b)/coef_m)
    print(df)

quantidade_absoluta(-3.397186047, 58.53223295, "/Users/Juliana/Documents/Juliana/programacao/Valores_CT.xlsx")

def quant_absoluta(coef_m, coef_b, tabela):
    import pandas as pd
    df = pd.read_excel(tabela)
    col = df.iloc[:, 1:3]
    df_q = pd.DataFrame()
    df_q["Quantity"] = 10 * ((df["CT"] - coef_b)/coef_m)
    df_final = pd.concat([col, df_q], axis=1)
    df_final.to_excel("/Users/Juliana/Documents/Juliana/programacao/Valores_CT.xlsx", sheet_name="Tabela")
    print(df_final)

quant_absoluta(-3.397186047, 58.53223295, "/Users/Juliana/Documents/Juliana/programacao/Valores_CT.xlsx")

