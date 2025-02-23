from random import randint
from time import sleep
from re import fullmatch

def validacao (entrada_usuario):
    return bool(fullmatch(r'[0-5]{1}',entrada_usuario))

"""
PROGRAMA DEDICADO A CRIAÇÃO DE UM SIMPLES JOGO DE ADIVINHA, ONDE É GERADO UM VALOR ALEATÓRIO
E O USUÁRIO TEM QUE DESCOBRIR O VALOR
"""
num_aleatorio = randint(0, 5)
#==================================================
print(f"""{"-=-"*12}
PENSEI EM UM VALOR ENTRE 0 E 5 
- SOMENTE VALORES INTEIROS
POR FAVOR TENTE DESCOBRIR
{"-=-"*12}""")
#==========================================================================
while True:
    numero_usuario = input('QUAL VALOR VOCÊ ACHA QUE PENSEI: ').strip()#ENTRADA JOGADOR
    if validacao(numero_usuario):
        numero_int_usuario = int(numero_usuario)
        break
    else:
        print("POR FAVOR, INFORME UM VALOR VÁLIDO (ENTRE 1 E 5)")
#==========================================================================
print('PROCESSANDO...')
sleep(3)
if numero_int_usuario == num_aleatorio:
    print('VOCÊ VENCEU, PARABENS!!!')
else:
    print(f'VOCÊ PERDEU!!! TINHA PENSADO NO VALOR {num_aleatorio}')
#=================================================================
"""
ABAIXO SERÁ FEITO DE OUTRO MODO, APENAS PARA PRÁTICA DE UMA CONDIÇÃO SIMPLIFICADA
"""

# print(f'VOCÊ VENCEU, PARABENS!!!' if numero_usuario == num_aleatorio 
# else f'VOCÊ PERDEU!!! TINHA PENSADO NO VALOR {num_aleatorio}')
