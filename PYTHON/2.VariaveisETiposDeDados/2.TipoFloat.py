# Tipo real ou decimal 
# OBS: O separador de casas decimais na programação é o ponto e não a vírgula. 

tupla = 1, 44
valor = 1.44

print(f"Número separado por vírgula não é número decimal. Tipo: {type(tupla)} -> {tupla}")


print(f"Número separado por ponto é um numero decimal Tipo: {type(valor)} -> {valor}")

# Podemos fazer a dupla atribuição

valor1, valor2 = 1, 44
print(f"A vírgula pode ser usada para fazer dupla atribuição Valor1: {valor1} Valor2: {valor2}")

# Convertendo um float para um int 
resultado = int(valor)
print(f"Convertendo um float para um int: {resultado}. tipo do dado depois da conversão: {type(resultado)}")

# Podemos trabalhar com números complexos. 
# Para criar um valor complexo basta atribuir o "j". Exemplo: 5j.

num_complexo = 5j
print(f"O valor do número complexo é: {num_complexo} e seu tipo é {type(num_complexo)}")

