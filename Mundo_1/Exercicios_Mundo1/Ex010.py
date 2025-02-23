dolar = 3.27

def conversor(valor):
    return valor/dolar
# end def
print('')
valor = float(input("QUANTOS REAIS VOCÊ TEM NA CARTEIRA: "))
#------------------------------------------------------------------------------------
print(f'COM O VALOR DE  R${valor}, VOCÊ PODE COMPRAR ${conversor(valor):.2f} DE DÓLAR')

#RETORNAR EM DICIONARIO COM VÁRIAS COTAÇÕES DE VARIAS MOEDAS