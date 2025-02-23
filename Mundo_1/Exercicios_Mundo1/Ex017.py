import math

def negrito (texto):
    formatado = f'\033[1m{texto}\033[0m'
    return formatado
#------------------------------------------------------------------------------------------
def Pitagoras( cat_oposto, cat_adjacente, hipotenusa):
    #--------------------------------------------------------------------------------------
    if (cat_adjacente and cat_oposto and hipotenusa) != 0:
        raise ValueError('NÃO É POSSÍVEL CALCULAR USANDO TODAS AS VARIÁVEIS')
    #------------------------------------
    else:
        if hipotenusa == 0:
            resultado_final = math.isqrt(pow(cat_adjacente, 2)+pow(cat_oposto, 2))
        elif cat_adjacente == 0:
            resultado_final = math.isqrt(abs(pow(hipotenusa, 2)-pow(cat_oposto, 2)))
        elif cat_oposto == 0:
            resultado_final = math.isqrt(abs(pow(hipotenusa, 2)-pow(cat_adjacente, 2)))
    #-------------------------------------
    dicionario = {'FINAL': resultado_final, 
                  'Hipotenusa': hipotenusa, 
                  'Cat_Oposto': cat_oposto, 
                  'Cat_adja': cat_adjacente}
    return dicionario

    #------------------------------------------------------------------------------------
def mensagem (HI, CO, CA, Final):

    return print(f'''
    OLÁ ESTUDANTE, FICO FELIZ EM PODER AJUDAR, APLICANDO A FAMOSA FORMULA DE PITAGORAS
    A² = B²+ C² - TEMOS:
                        
                    . 
                    .   .       
                    .       .   {HI}
                  {CA} .          . 
                    .             .       
                    . . . . . . . . .         
                           {CO}
    #----------------------------------------------------------                
    {HI}² = {CA}²+ {CO}²
    FAZENDO A EQUAÇÃO, TEMOS O RESULTADO DE: {negrito(Final)}
    ''')
#--------------------------------------------------------------------------------------------------

print()
divisor = '📐'
print(f'{divisor*15}{' BEM VINDO A CALCULADORA DE PITAGORAS '}{divisor*15}')
print()
print(f'INFORME {negrito(0)} PARA O VALOR QUE DESEJA CALCULAR: ')
print()

Arg1 = int(input('INFORME O CATETO OPOSTO: '))
Arg2 = int(input('INFORME O CATETO ADJACENTE: '))
Arg3 = int(input('INFORME O HIPOTENUSA: '))
#--------------------------------------------------------------
valor_final = Pitagoras(Arg1, Arg2, Arg3)
msg = mensagem(valor_final['Hipotenusa'], valor_final['Cat_Oposto'], valor_final['Cat_adja'], valor_final['FINAL'])
