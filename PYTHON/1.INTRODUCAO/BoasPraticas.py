# [1] Nome de classe sempre com iniciais maiúsculas e quando for composto não separar por underline, mas coloca as iniciais em maiúsculo.

class Futebol:
    pass

class FutebolFlamengo:
    pass

# [2] Nomes para variáveis e funções em minúsculos e caso seja composto separar por underline.

flamengo = 'Time'

def times ():
    pass

# [3] Utilize 4 espaços para identação e não use o tab

# [4] Deixe o espaço de duas linhas em branco; Métodos dentro de uma classe deve ter somente uma linha em branco de espaço.

# [5] Imports devem ser feitos sempre em linhas separadas:

"""
Import errado -> import sys, os

import certo -> import sys
                import os

# Não há problema em usar: from types import Stringtype, ListType
Isso porque você não importa o pacote completo, mas itens separados.

# Caso tenha muitos imports de um mesmo pacote, pode fazer: 

from types import {
    StringType,
    ListType,
    SetType,
    OutroType
} 


"""
# [6] -> Imports devem ser colocados no topo antes de qualquer comentários, variáveis globais 

# [7] não deixe espaços entre funções e variáveis. ex: funcao (  algo  [   1   ]) ou algo ( 2 )

"""[8] Sempre depois de valores com vírgula devemos dar um espaço. Serve para o uso de tuplas 1, 44.
    Lembre-se que valor float é separado por ponto e não por vírgula.
"""


