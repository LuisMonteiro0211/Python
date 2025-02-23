num1 = int(input('DIGITE UM VALOR: '))
num2 = int(input('DIGITE OUTRO VALOR: '))

soma = num1 + num2
sub = num1 - num2
divi = num1/num2
mult = num1*num2
divint = num1//num2
modulo = num1%num2
pot = num1**num2
#----------------------------------------------------
print(f'SOMA {soma} SUBTRAÇÃO {sub} E A DIVISÃO É {divi:.3}', end=' ')
print(f'A MULTIPLICAÇÃO É {mult}  A DIVISÃO POR INTEIRO É {divint}', end=' ')
print(f'O RESTO DA DIVISÃO É {modulo} E A POTÊNCIA É {pot}')

#No final da linha do print, quando é colocado o END, estamos falando para acressentar ao final a informação apos o igual
#Pois como padrão o final do print no Python é uma quebra de linha
#Do mesmo modo, quando colocamos \n estamos dando o comando para quebra de linha na quele momento