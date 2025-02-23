import random
from time import sleep
contador = 0
contagem_erros = 0
controle = 1
dado = "🎲"

def validacao(variavel_analisada, tipo_verificacao):
    if tipo_verificacao == 1:
        return variavel_analisada.isspace() or variavel_analisada == ""

def cabecalho():
    while True:
        quantidade_alunos = int(input("QUANTOS ALUNOS SERÃO CADASTRADOS: "))
        if quantidade_alunos > 0:
            break
        else:
            print("VALOR INFORMADO TEM QUE SER MAIOR QUE ZERO")
    return quantidade_alunos

def cadastro_aluno(quantidade_alunos):
    global contagem_erros
    lista_alunos=[]
    contador = 1
    while contador <= quantidade_alunos:
        nome_aluno = input(f"NOME DO {contador}° ALUNO: ")
        nome_final = nome_aluno.strip()

        if validacao(nome_final, 1) == False:
            print("CADASTRO REALIZADO!!")
            lista_alunos.append(nome_final)
            contador +=1
        else:
            print("NOME INVÁLIDO! DIGITE NOVAMENTE")
            contagem_erros +=1
    print("----------------------------------------------------------")
    print(f"FORAM CADASTRADOS UM TOTAL DE {quantidade_alunos} ALUNOS")
    return lista_alunos

def embaralhar (lista_original):
    global contador
    contador +=1 #Variável de conrole para informa quantos sorteios foram feitos
    random.shuffle(lista_original)#Retorna a lista já modificada
    lista_final = ", ".join(lista_original).upper()# Junta cada elemento da lista com uma virgula
    return lista_final#Retorna a lista já formatada

def escolha(texto):
    return int(input(f"{texto}"))
#------------------------------------------------------------------------------------------------
print("BEM VINDO AO SORTEIO DE ALUNOS!!")
quantidade_alunos = cabecalho()
lista_alunos = cadastro_aluno(quantidade_alunos)
lista_copia = lista_alunos.copy()#Backup da lista
#---------------------------------------------------------------------------------
print()
print('PÓS CADASTRO DOS ALUNOS:  ')
texto = "DESEJA VISUALIZAR A LISTA ANTES DE SORTEA | 1 - SIM 2 - NÃO: "
if escolha(texto) == 1:
    print()
    print("LISTA ANTES DO SORTEIO!!")
    print(", ".join(lista_copia).upper())#Mostra a lista original/backup
    print("-"*30)
    print("LISTA APÓS SORTEIO!!")
    print(embaralhar(lista_alunos))#Chama a função embaralhar e retorna a lista final dos alunos
else:
    'Caso o usuário não deseje visualizar a lista antes do sorteio, essa condição mostra ela já embaralhada'
    print("-"*30)
    print("LISTA APÓS SORTEIO!!")
    print(embaralhar(lista_alunos))
#----------------------------------------------------------------------------------
texto = "DESEJA EMBARALHAR NOVAMENTE? | 1 - SIM 2 - NÃO: "
while True:
    if escolha(texto)== 1:
        print("EMBARALHADO NOVAMENTE!!")
        sleep(2)
        print(embaralhar(lista_alunos))
    else:
        print("ENCERRANDO O PROGRAMA...")
        sleep(3)
        break
#Mosta um relatório final com as informações obtidas durante a seção de sorteio
print("*"*50)
print("GERANDO UM RELATÓRIO FINAL...")
print()
print(f"{dado*10}-RELATÓRIO FINAL-{dado*10}")
print()
print(f"LISTA DE ALUNOS ORIGINAL: ")
#Mosta a lista na ordem original que foi digitada
for nome in lista_copia:
    print(f"- {nome.upper()}")
print()
print(f"- FORAM FEITOS UM TOTAL DE {contador} SORTEIOS") #Quantidade de sorteios feitos
print(f"- FORAM FEITOS UM TOTAL DE {contagem_erros} ERROS DURANTE O CADASTRO")
print("ESSA FOI A LISTA FINAL PARA APRESENTAÇÃO: ")
for nome in lista_alunos:
    print(f"{controle}°- {nome.upper()}")
    controle +=1
print()
print("OBRIGADO PELA ESCOLHA DO PROGRAMA!!!!")
