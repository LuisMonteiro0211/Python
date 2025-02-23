import math

def conversor_manual (valor):
    valor_convertido = str(valor)
    corte_string = valor_convertido.split('.')
    final = corte_string[0]
    return final

def conversor_func(valor):
    final = math.trunc(valor)
    return final

def divisao_inteira(valor):
    final = valor//1
    return final

pergunta = float(input('INFORME UM VALOR PARA CONVERTER: '))

final = conversor_manual(pergunta)
final2 = conversor_func(pergunta)
final3 = divisao_inteira(pergunta)

print(f'A PORÇÃO INTEIRA DO NÚMERO {pergunta} É IGUAL A: {final}, {final2}, {final3:.0f}')
