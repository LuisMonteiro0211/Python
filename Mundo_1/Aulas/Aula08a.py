import math

print()
num = int(input("DIGITE UM NÚMERO: "))
raiz = math.sqrt(num)
#Número com casas decimais
print(f'{raiz:.2f}')
#Numero usando a função de aredondamento
print(f'{math.ceil(raiz)}')