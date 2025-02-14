# And, Not, Or e Is

"""
AND -> todos precisam ser vedadeiros para satisfazer a condição 
OR -> Ao menos um precisa ser verdadeiro para satisfazer a condição 
NOT -> Nega a sentença 
IS -> 

"""

# Operadores unários: not
# Operadores binários: and, or e is

ativo = True
logado = False
senha = 1234
nome = 'DEV'


# Operador and
if ativo and logado:
    print('Usuário ativo no sistema')
else:
    print('Usuário não encontrado')

# Operador or
if senha == 123 or senha == 321:
    print('Senha aceita')
else:
    print('senha inválida')

# Operador not

# Está dizendo "Se não for ativo", ele não muda o valor da variável, ele somente nega na operação
if not ativo:
    print("Ative sua conta")
else:
    print("Olá, seja bem-vindo")

# Operador is -> aqui quer dizer logado está/é verdadeiro ?
if logado is True:
    print('Você está logado')
else:
    print('Você não está logado')

"""
 Fica um pouco redundante, pois se você colocar somente if logado: só vai entrar na condição se ele for verdadeiro.
"""

"""
 
 Se colocarmos o dir(string), ele vai retornar algumas funções com o is,
 por exemplo o isupper() que pergunta se a string está com letras maiúsculas e retorna o valor booleano.


 
"""
print(nome.isupper())
# Um é um ? true
print(1 is 1)




