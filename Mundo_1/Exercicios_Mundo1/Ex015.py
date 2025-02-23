
def aluguel_carro(km_rodado, dias):
    dia = 60
    km = 0.15
    #É cobrado R$0.15 por KM rodado
    preco_km = km_rodado * km
    #R$60,00 Por dia Alugado
    preco_dia = dia * dias
    #---------------------------------
    preco_final = preco_km + preco_dia
    #<><><><><><><><><><><><><><><><><>
    dicionario = {'Preco_KM': preco_km,
                  'Preco_Dia':preco_dia,
                  'Preco_Final':preco_final, 
                  'Dia': dia,
                  'KM':km}
    #----------------------------------
    return dicionario

print('')
pergunta_km = float(input("INFORME A QUANTIDADE DE KM PERCORRIDOS: "))
pergunta_dia = int(input("INFORME QUANTOS DIAS FICOU ALUGADO: "))

resultado = aluguel_carro(pergunta_km, pergunta_dia)

print('')
print(f'O VALOR FINAL A SER PAGO É: R${resultado["Preco_Final"]:.2f}\n'
      f'{'INFORMAÇÕES':=^30}\n'
      f'PREÇO POR DIA: R${resultado["Dia"]}\n'
      f'PREÇO POR KM RODADO R${resultado["KM"]}\n'
      f'\n'
      f'- FOI ALUGADO POR {pergunta_dia} DIAS, GERANDO UM TOTAL DE R${resultado["Preco_Dia"]:.2f}\n'
      f'- FOI RODADO UM TOTAL DE {pergunta_km}KM, GERANDO UM TOTAL DE R${resultado["Preco_KM"]:.2f}\n'
      f'{'':=^30}')