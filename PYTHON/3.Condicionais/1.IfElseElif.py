# Estruturas condicionais 

idade = 26

# O escopo é a indentação com 4 espaços. 
if idade < 18:
    print(f'Idade: {idade}. Você é menor de idade')
elif idade == 18:
    print(f" Idade: {idade}. Você tem exatamento 18 anos")
elif idade == 60:
    print("Você é maior de idade, mas não vamos divulgar sua idade heinn hahaha brincadeira.")
else:
    print(f'Idade: {idade}. Você é maior de idade')

