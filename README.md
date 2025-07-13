# Criação e ajustes das colunas para o banco de dados 

#### UFPB - Universidade Federal da Paraíba
#### LabGov

Autor: Bruno Souza da Costa  
Contatos: [e-mail](brun.souz4@gmail.com) | [linkedin](https://www.linkedin.com/in/bruno-souza-a74396214/)

### Esse código foi utilizado para automatizar a criação das colunas de valores booleanos (0 e 1) para o banco de dados utilizado na análise de relatórios de auditoria interna governamental.

A metodologia completa utilizada para a criação dessas colunas pode ser encontrada no [link](https://docs.google.com/document/d/1SqfNRUad_ccG6rAjSugxbDS6db2O_lf-TVVCaA3C6TM/edit?usp=sharing).

A análise dos relatórios de auditoria interna governamental se encontra no [link](https://github.com/BruninSouza/relatorios_auditoria_interna_governamental?tab=readme-ov-file).

## 🗂️ Estrutura do Projeto

```bash
projeto/
├── arquivos/                   # Pasta onde os arquivos criados seguindo a metodologia citada anteriormente estão inseridos
├── codigos/                    # Pasta onde os códigos de automação estão inseridos
├── csv-gerados/                # Pasta onde são inseridos os arquivos csv gerados pelos códigos de automação
├── .gitignore                  # Especifica arquivos que devem ser ignorados pelo sistema de controle de versão
├── colunas_combinadas.xslx     # BD das colunas combinadas gerado automaticamente
├── README.md                   # Este arquivo
└── script.sh                   # Script que executa todas as operações necessárias para criação do BD 
```

## 🧪 Requisitos

- Sistema operacional Linux
- python 3.x instalado

## Como Usar

Clone este repositório:

```bash
git clone https://github.com/BruninSouza/Ajuste-Colunas.git
```
Abra-o na IDE de sua escolha e execute no terminal:

```bash
chmod +x script.sh
```

Issa dará permissão de execução para o arquivo de script, após isso execute novamente no terminal:

```bash
./script.sh
```

## Funcionamento dos códigos de automação (exemplos)

### Criação dos  arquivos CSV referente as colunas

```python
import csv # Biblioteca que permite criar arquivos csv

# Nome do arquivo txt de entrada e do arquivo csv de saída
arquivo_txt = 'nome_do_arquivo'
arquivo_csv = '00_nome_coluna.csv'

# Criar um conjunto para armazenar os números das linhas que contêm arquivos .pdf
linhas_com_pdf = set()

# Abrir o arquivo de texto e processar cada linha para encontrar as referências de arquivos .pdf
with open(arquivo_txt, 'r') as f:
    for linha in f:
        if '.pdf:' in linha:
            # Extraindo o número da linha antes de ".pdf"
            numero_linha = int(linha.split('.pdf:')[0])
            linhas_com_pdf.add(numero_linha)

# Criar o arquivo CSV com numero de linhas especificado
with open(arquivo_csv, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Nome da coluna']) # Faz a primeira linha do csv possuir o nome da coluna desejada

    # 343 pode ser substituido por qualquer valor para se adequar ao tamanho requerido do BD
    for i in range(1, 1 + 343): 
        # Escrever 1 se o número da linha estiver no conjunto, caso contrário 0
        writer.writerow([1 if i in linhas_com_pdf else 0])

print(f"Arquivo '{arquivo_csv}' gerado com sucesso!")
```

### Juntar todas colunas num único Banco de Dados

```python
import pandas as pd 
import glob

# Lista todos os arquivos CSV na pasta csv-gerados e ordena alfabeticamente
caminho_arquivos = sorted(glob.glob("csv-gerados/*.csv"))

# Lista para armazenar cada DataFrame
dataframes = []

# Itera sobre cada arquivo CSV ordenado e adiciona ao dataframe
for arquivo in caminho_arquivos:
    df = pd.read_csv(arquivo)
    dataframes.append(df)

# Junta todos os DataFrames por colunas
df_combined = pd.concat(dataframes, axis=1)

# Salva o DataFrame combinado em um novo arquivo CSV
df_combined.to_csv("./csv-gerados/dataframe.csv", index=False)

# Converte o arquivo CSV gerado para o formato XLSX
df_combined.to_excel("./dataframe.xlsx", index=False)

print("Arquivos combinados com sucesso em ordem alfabética e convertidos para XLSX!")
``` 