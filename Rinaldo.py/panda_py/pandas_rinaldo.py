import pandas as pd

tabela = pd.read_csv("dados_vendas_60_linhas.csv")
# print(tabela)

primeiras_linhas = pd.DataFrame.head(tabela)

# head: primeiras 5 linhas
# Tail: ultimas 5 linhas
# Describe: resumo de dados da tabela

# pd.dataframe.tail(tabela que eu quero) *5 ultimos da tabela
# pd.dataframe.head(tabela que eu quero) *5 primeiros da tabela
# descricao = pd.DataFrame.describe(tabela)
# print(primeiras_linhas)

ultimas_linhas = pd.DataFrame.tail(tabela)

# print(ultimas_linhas)

descricao = pd.DataFrame.describe(tabela)

print(descricao)