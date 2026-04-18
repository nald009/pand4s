import pandas as pan

tabela = pan.read_csv('Netflixdados/netflix_titles.csv')
#print(tabela)

primeiros = pan.DataFrame.head(tabela)

#print(primeiros)

ultimos = pan.DataFrame.tail(tabela)
#print(ultimos)

desc = pan.DataFrame.describe(tabela)
#print(desc)

infosimportantes = tabela[['title','type','country']]

#print(infosimportantes)

titulo_obra = tabela[['title']]

print(titulo_obra)

df = pan.DataFrame(infosimportantes) #criação da tabela

df.to_csv('infos_importantes') #salvando a tabela