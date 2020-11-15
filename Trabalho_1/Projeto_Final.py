def Projeto_Final():
    import pandas as pd
    tabela = pd.read_excel("/Users/Juliana/Documents/Juliana/programacao/Tabela_1.xlsx")
    coluna1 = tabela.iloc[:, 1]
    coluna2 = tabela.iloc[:, 2]
    coluna3 = tabela.iloc[:, 3]
    coluna4 = tabela.iloc[:, 4]
    soma1 = sum(coluna1)
    soma2 = sum(coluna2)
    soma3 = sum(coluna3)
    soma4 = sum(coluna4)
    coluna_nova1 = pd.DataFrame()
    coluna_nova1["Rap_1A_CPM"] = (coluna1 * 1000000) / soma1
    coluna_nova2 = pd.DataFrame()
    coluna_nova2["Rap_2A_CPM"] = (coluna2 * 1000000) / soma2
    coluna_nova3 = pd.DataFrame()
    coluna_nova3["Rap_1B_CPM"] = (coluna3 * 1000000) / soma3
    coluna_nova4 = pd.DataFrame()
    coluna_nova4["Rap_2B_CPM"] = (coluna4 * 1000000) / soma4
    tabela_nova1 = pd.concat([tabela, coluna_nova1, coluna_nova2, coluna_nova3, coluna_nova4], axis=1)

    coluna5 = tabela_nova1.iloc[:,5]
    coluna6 = tabela_nova1.iloc[:,6]
    coluna7 = tabela_nova1.iloc[:,7]
    coluna8 = tabela_nova1.iloc[:,8]
    media_A = pd.DataFrame()
    media_A["Cond_A_CPM_media"] = (coluna5 + coluna6)/2
    media_B = pd.DataFrame()
    media_B["Cond_B_CPM_media"] = (coluna7 + coluna8)/2
    tabela_nova2 = pd.concat([tabela_nova1,media_A, media_B], axis=1)
    print(tabela_nova2)

    genes_xA = tabela_nova2['Cond_A_CPM_media'].nlargest()
    genes_xB = tabela_nova2['Cond_B_CPM_media'].nlargest()
    print("Genes mais expressos da condicao A:","\n", genes_xA,"\n", "Genes mais expressos da condicao B: ","\n", genes_xB)





Projeto_Final()

