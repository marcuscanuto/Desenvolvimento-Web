# Loop For é uma estrutura de repetição

nome = 'Aprendendo o loop for'
lista = [1,2,3,4,5,6,7,8,9,10]

# Ele vai percorrer todo a variável nome e em cada índice/caractere vai ser imprimido na tela inclusive os espaços
for letra in nome:
    print(letra)

# Percorre a lista passando por cada índice
for numero in lista:
    if numero > 9:
        print('A lista está organizada em ordem crescente e chegamos no final dela com o valor 10')
    else:
        print(numero)


"""O enumerate retorna um objeto do tipo enumerate e ele pega a string por exemplo e transforma em uma tupla

 (0, A), (1, p), (1, r)

 """
# Pode imprimir o índice e o valor correspoondente 
for indice, valor in enumerate(nome):
    print(f'No índice {indice} o valor é {valor}')


# Quando não precisamos de um valor, podemos descartar usando o underline
for _ , valor in enumerate(nome):
    print('Usamos o underline para descartar valores que não iremos usar, nesse caso não precisamos do índice')


# Imprime a tupla
for tupla in enumerate(nome):
    print(tupla)


# Pegando entrada do usuário
qtd = int(input('Quantas vezes esse loop deve rodar ?'))

# O range fala para começar em 1 e ir até a quantidade da variável qtd
# Esse + 1 é porque o range ele não vai até o último.
for rodar in range(1, qtd + 1):
    print(f'Rodando {rodar} vezes')


# Se quisermos imprimir sem querar a linha podemos usar o end=''
for letra in nome:
    print(letra, end='')

