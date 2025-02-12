# Assume dois valores: Verdadeiro ou falso => True or False

# Sempre com as iniciais maiúsculas 

ativo = True
print(f" O usuário está ativo ? {ativo}")

comprou = False
print(f"O usuário realizou a compra ? {comprou}")

# Para fazer negações usamos o not. Troca o valor de verdairo para falso e de falso para verdadeiro.
print(f"Trocando o valor de ativo -> {not ativo}")


# Operação or. Precisa de dois valores falsos para ser falso.
print(True or True)

# Operadores lógico também retorna valores booleanos.
print(f"6 é maior que 4 ? resposta: {6 > 4}")
print(f"6 é menor que 4 ? resposta: {6 < 4}")
print(f"6 é igual que 4 ? resposta: {6 == 4}")
print(f"6 é menor ou igual que 4 ? resposta: {6 <= 4}")

# Operador AND. Só vai ser verdadeiro se todos forem verdadeiros.
print(ativo and ativo)

print(type(True))


print(type(ativo))

print(dir(ativo))