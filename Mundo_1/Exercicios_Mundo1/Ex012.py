def calculo (valor_total, desconto):
    desconto_porcentagem = desconto/100 #Conversão da porcentagem em valor decima
    desconto_final = valor_total*desconto_porcentagem #Retorna o valor em reais do desconto passado
    valor_final = valor_total - desconto_final #Retorno o valor final do produto com desconto
    #Retorno de um dicionario para poder acessar mais de um valor
    dicionario = {"desconto_final": desconto_final,"valor_final":valor_final}

    return dicionario
#--------------------------------------------------------------------------------------------------
print()
print('BEM VINDO A CALCULADORA DE DESCONTO!!')
valor_produto = float(input("INFORME O VALOR DO PRODUTO R$ "))
desconto_produto = float(input("INFORME A PORCENTAGEM DE DESCONTO: "))

final = calculo(valor_produto, desconto_produto)
print(f'{'':=^80}')
print(f'O VALOR DO PRODUTO É {valor_produto} PORÉM APLICANDO {desconto_produto}% DE DESCONTO\n'
      f' O PRODUTO SAI POR R${final["valor_final"]:.2f}, COM UM DESCONTO DE R${final["desconto_final"]:.2f}')
