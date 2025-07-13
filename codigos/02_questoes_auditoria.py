import csv

arquivo_txt = './arquivos/resultado_questao_auditoria.txt'
arquivo_csv = 'csv-gerados/02_questoes_auditoria.csv'

linhas_com_pdf = set()

with open(arquivo_txt, 'r') as f:
    for linha in f:
        if '.pdf:' in linha:
            numero_linha = int(linha.split('.pdf:')[0])
            linhas_com_pdf.add(numero_linha)

with open(arquivo_csv, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['a. Questões de Auditoria'])
    for i in range(1, 1 + 343):
        writer.writerow([1 if i in linhas_com_pdf else 0])

print(f"Arquivo '{arquivo_csv}' gerado com sucesso!")