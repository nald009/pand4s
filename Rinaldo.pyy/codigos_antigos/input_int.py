Lista_pessoas = ["Joyce", "Paula", "Maria", "Guilherme"]

novapessoa = input("Digite o nome da pessoa ")
novapessoa2 = input("digite o nome da segunda pessoa ")
novapessoa3 =input("digite o nome da terceira pessoa ")
novapessoa4 = input("digite o nome da Quarta pessoa ")

Lista_pessoas2 = [novapessoa, novapessoa2]
Lista_pessoas.extend(Lista_pessoas2)
print(Lista_pessoas)

