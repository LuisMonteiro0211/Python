print()
num1 = int(input("DIGITE QUAL TABUADA DESEJA: "))
divisao = '='
def tabuada (num):
    controle = 1
    while (controle <=10):
        print(f'{num1} x {controle} = {controle*num}')
        controle +=1
#-----------------------------
print(divisao*15)
tabuada(num1)
print(divisao*15)
