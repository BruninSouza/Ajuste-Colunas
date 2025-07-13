import pandas as pd
import glob

caminho_arquivos = sorted(glob.glob("csv-gerados/*.csv"))

dataframes = []

for arquivo in caminho_arquivos:
    df = pd.read_csv(arquivo)
    dataframes.append(df)

df_combined = pd.concat(dataframes, axis=1)

df_combined.to_csv("./csv-gerados/colunas_combinadas.csv", index=False)

df_combined.to_excel("./colunas_combinadas.xlsx", index=False)

print("Arquivos combinados com sucesso em ordem alfabética e convertidos para XLSX!")