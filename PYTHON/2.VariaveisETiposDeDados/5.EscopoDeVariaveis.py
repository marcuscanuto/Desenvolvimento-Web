# Escopo pode ser entendido como uma limitação/espaço

# 1 - Variáveis Globais: São reconhecidas/escopo em todo o programa
# 2 - Variáveis locais: São reconhecidas em bloco onde foi declaradam, seu escopo está limitado a esse bloco.


numero = 2
print(f"Variável global numero: {numero} é reconhecida em todo o programa")

# O python é uma linguagem de tipagem dinâmica, isso significa que ao declararmos uma variável não colocamos o tipo dela. 

if numero > 10:
    # Variável local, só é reconhecida dentro do escopo. 
    novo =+ 1


# print(novo) -> esse comando iria dar erro porque a variável não é reconhecida fora do escopo
print(novo)

