import csv

arquivo_txt = './arquivos/resultado_manifestacao.txt'
arquivo_csv = 'csv-gerados/14_manifestacao.csv'
linhas_com_pdf = set()

with open(arquivo_txt, 'r') as f:
    for linha in f:
        if '.pdf:' in linha:
            numero_linha = int(linha.split('.pdf:')[0])
            linhas_com_pdf.add(numero_linha)

with open(arquivo_csv, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['m. Manifestação'])
    for i in range(1, 1 + 343):
        writer.writerow([1 if i in linhas_com_pdf else 0])

print(f"Arquivo '{arquivo_csv}' gerado com sucesso!")