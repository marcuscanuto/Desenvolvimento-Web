"""
Um dado é considerado string sempre que estiver:

1 - Aspas simples. Ex: 'Texto', '12', 'True', 
2 - Aspas duplas. Ex: "texto", "123" ...
3 - Estiver entre aspas simples triplas. Ex: ''' texto ''' ...
"""
# 4 - Estiver entre aspas duplas triplas. Ex: """ Texto """

nome = 'Testando string'
print(nome)
print(type(nome))

# Em caso de aspas no meio de nomes é preciso envolver entre aspas duplas.
bar = "Ginas'S Bar"
print(bar)

# \n quebra linha
sobrenome = 'User \nda Silva'
print(sobrenome)

# Podemos fazer a mesma coisa acima com as três aspas duplas
sobrenome1 = """Novo
usuário
"""
print(sobrenome1)


# Colocando tudo em maiúsculo 
print(dir(nome))
print(nome.upper())


# Colocando tudo em minúsculo 
print(nome.lower())


# Pega cada palavra do texto e coloca em um arrya
print(nome.split())

# Colocando tudo em minúsculo 
print(nome.lower())

# O python cria uma lista de caracteres por padrão que começa a conta do zero.
# ['T', 'e', 's', 't', 'a', 'n', 'd', 'o', ' ', 's', 't', 'r', 'i', 'n', 'g'] => Testando string
# Para mostrar um determinado caractere basta colocar o índice. 
print(f'Mostrando a primeira letra do nome "Testando string:" {nome[0]}')


# Acessar esse nome começando do índice zero ao índice 4. Isso é conhecido como slice de string 
print(f"Acessar esse nome começando do índice 0 ao índice 4: {nome[0:4]}") 

# Acessar esse nome começando do índice 8 ao índice 15. 
print(f"Acessar esse nome começando do índice 8 ao índice 15: {nome[8:15]}")


# Pegar pelo índice depois de separar o texto e colocar no array
print(nome.split()[0])


#Para começar do primeiro elemento e ir até o último
print(f"começar do primeiro elemento e ir até o último {nome[::]}")


# De trás para frente com o -1
print(f" De trás para frente  {nome[:: -1]}")

# Substitui letras em uma string
print(f"Substituindo letra em um string, onde estiver o T maiúsculo será substituido pelo D: {nome.replace('T', 'D')}")

