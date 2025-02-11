
print('Cadastro')
nome = input('Informe seu nome')
pais = input('Qual seu país ?')
idade = int(input('Qual sua idade ?'))

# Forma de print mais antiga
print("Seja bem vindo %s" % nome)

# Forma de print mais atual que a versão anterior
print("Seu país é: {0}".format(pais))

# Mais atual
print(f'Você nasceu em {2025 - idade}')


"""
Todo input recebe o valor de string
Cast -> Transforma um dado em outro tipo de dado. int(idade), transformando idade em um valor inteiro.


"""