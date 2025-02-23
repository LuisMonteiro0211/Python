pag_Avista = 0.10
pag_Parcel = 0.08

def calculo (valor_total):
    valor_Avista = valor_total*pag_Avista
    valor_Parcel = valor_total*pag_Parcel
    #-------------------------------------
    final_avista = valor_total-valor_Avista
    final_parcel = valor_Parcel+valor_total
    #-------------------------------------
    dicionario = {"Parcelado": final_parcel, 
                  "A_Vista": final_avista, 
                  "Desconto":valor_Avista, 
                  "Acrescimo": valor_Parcel}

    return dicionario
#-------------------------------------------------------------------------------------------
print()
valor_produto = float(input("DIGITE O VALOR DO PRODUTO R$: "))
final =calculo(valor_produto)
#-----------------------------------------------------------------------------------------
print(f'SEGUNDO POLÍTICA DA EMPRESA TEMOS AS SEGUINTES OPÇÕES: \n'
      f'- PARA PAGAMENTO A VISTA VOCÊ TEM {pag_Avista*100:.0f}% DE DESCONTO\n'
      f'- R${valor_produto:.2f} POR {final["A_Vista"]:.2f}\n'
      f'UM TOTAL DE R${final["Desconto"]:.2f} DE DESCONTO\n'
      f'{'':=^50}\n'
      f'- PARA PAGAMENTO PARCELADO VOCÊ TERÁ UM ACRÉSCIMO DE {pag_Parcel*100:.0f}%\n'
      f'- R${valor_produto:.2f} POR {final["Parcelado"]:.2f}\n'
      f'UM TOTAL DE R${final["Acrescimo"]:.2f} DE ACRÉSCIMO')