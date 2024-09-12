import csv

# Nome do arquivo txt de entrada e do arquivo csv de saída
arquivo_txt = '/home/bruno-souza/Área de trabalho/Ajuste-Colunas/arquivos/resultado_efeitos.txt'
arquivo_csv = '10_efeitos.csv'

# Criar um conjunto para armazenar os números das linhas que contêm arquivos .pdf
linhas_com_pdf = set()

# Abrir o arquivo de texto e processar cada linha para encontrar as referências de arquivos .pdf
with open(arquivo_txt, 'r') as f:
    for linha in f:
        if '.pdf:' in linha:
            # Extraindo o número da linha antes de ".pdf"
            numero_linha = int(linha.split('.pdf:')[0])
            linhas_com_pdf.add(numero_linha)

# Criar o arquivo CSV com 1636 linhas
with open(arquivo_csv, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for i in range(1, 1 + 1636):
        # Escrever 1 se o número da linha estiver no conjunto, caso contrário 0
        writer.writerow([1 if i in linhas_com_pdf else 0])

print(f"Arquivo '{arquivo_csv}' gerado com sucesso!")