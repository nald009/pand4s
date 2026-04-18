import pandas as pd

tabelaa = pd.read_csv("dataset_vendas_80_linhas.csv")
# print(tabelaa)

primeiras_linhaas = pd.DataFrame.head(tabelaa)
# print(primeiras_linhaas)

ultimas = pd.DataFrame.tail(tabelaa)
# print(ultimas)

desc = pd.DataFrame.describe(tabelaa)
print(desc)

print("oi")