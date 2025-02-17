# Precisamos conhecer o loop for para usar o range
# Precisamos conhecer o range para trabalharmos melhor 


# O range gera sequência numéricas em ordem especificadas. OBS: O último valor não entra qunado utiliza o range 

# Forma 1 -> vai de 0 a 10 incrementando de um em um
''' range(valor de parada)'''
for num in range (11):
    print(num)


# Forma 2 -> vai de 1 a 10 incrementando de um em um.
''' range(valor de início, valor de parada)''' 
for num in range(1, 11):
    print(num)


# Forma 3
''' range(valor de início, valor de parada, e vai de dois em dois) '''
for num in range(1, 11, 2):
    print(num)


# Forma 4 inversa 
''' range(Começa pelo 10, vai até o 1 , decrementando de um em um). Para ir até o 0 precisa colocar range(10, -1, -1) '''
for num in range(10, 0, -1):
    print(num)