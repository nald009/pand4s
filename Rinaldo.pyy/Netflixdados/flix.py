import pandas as pam

tabela = pam.read_csv('Netflixdados/netflix_titles.csv')
#print(tabela)

importantinfo = tabela[['title', 'type', 'duration']]
titulo = tabela[['title']]
print(titulo)

tipo = tabela[['type']]
print(tipo)

duração = tabela[['duration']]
print(duração)

importantinfo.to_csv('importantinfoo')