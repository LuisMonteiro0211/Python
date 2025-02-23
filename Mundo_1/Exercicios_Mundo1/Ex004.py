print("")
algo = input("DIGITE ALGO: ")
final = algo.upper()
def divisao():
    print("=================================================================================")
#--------------------------------------------------
print(f'1 - A PALAVRA DIGITADA COMO PADRÃO É UMA {type(algo)}')
divisao()

print(f'2 - O ITEM DIGITADO ({final}) É APENAS LETRAS: {algo.isalpha()}')
divisao()

print(f'3 - O ITEM DIGITADO ({final}) É APENAS NUMEROS: {algo.isnumeric()}')
divisao()

print(f'4 - O ITEM DIGITADO ({final}) É FORMADO APENAS POR ESPAÇO: {algo.isspace()}')
divisao()

print(f'5 - O ITEM DIGITADO ({final}) É ALFANUMERICO: {algo.isalnum()}')
divisao()

print(f'6 - O ITEM DIGITADO ({final}) É POSSIVEL DE IMPRIMIR NO CONSOLE: {algo.isascii()}')
divisao()

print(f'7 - O ITEM DIGITADO ({final}) ESTÁ ESCRITO APENAS EM CAPSLOK : {algo.isupper()}')
divisao()

print(f'8 - O ITEM DIGITADO ({final}) ESTÁ ESCRITO APENAS EM MINUSCULO: {algo.islower()}')
divisao()

print(f'9 - O ITEM DIGITADO ({final}) ESTÁ CAPITALIZADO: {algo.istitle()}')
divisao()

print(f'10 - O ITEM DIGITADO ({final}) É FORMADO APENAS POR NUMEROS: {algo.isdigit()}')
#Somente faz a verificação de números de 0 a 9