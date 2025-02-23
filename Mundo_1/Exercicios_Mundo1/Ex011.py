def parede(altura, largura):
    area = altura*largura
    quant_litros = area/2
    final = {"area": area, "quantidade": quant_litros}
    return final
# end def
#-------------------------------------------------------------
print("")
print('BOAS VINDAS AO CALCULO DE CONSUMO DE TINTA')
altura = float(input("INFORME A ALTURA DA PAREDE: "))
largura = float(input("INFORME A LARGURA DA PAREDE: "))

resultado = parede(altura, largura)

print(f'COM BASE NAS INFORMAÇÕES TEMOS QUE: \n'
      f'- SUA PAREDE TEM {altura} DE ALTURA \n'
      f'- SUA PAREDE TEM {largura} DE LARGURA \n'
      f'- GERANDO ASSIM UMA AREA DE {resultado["area"]} M2\n'
      f'==============================================\n'
      f'COM ISSO PODEMOS CALCULAR OS GASTOS DE: \n'
      f'{resultado["quantidade"]} DE LITROS DE TINTA')
