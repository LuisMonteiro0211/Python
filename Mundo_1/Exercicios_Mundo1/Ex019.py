import random

def validacao(variavel_analisada, tipo_verificacao):
    #----------------------------------------------
    if tipo_verificacao == 1:
        return variavel_analisada.isdigit()
    if tipo_verificacao == 2:
        return variavel_analisada.isspace() or variavel_analisada == ""
#----------------------------------------------------------------------------------
def formulario():
    quantidade_alunos = int(input('INFORME A QUANTIDADE DE ALUNOS: '))
    quantidade_sorteado = int(input('QUANTOS ALUNOS DESEJA SORTEAR: '))
    if quantidade_sorteado >= quantidade_alunos:
        print('ERRO... O VALOR DE SORTEIO É MAIOR QUE O DE ALUNOS!!')
        formulario()
    dicionario = {'Quant_alunos': quantidade_alunos, 'Quant_sorteados':quantidade_sorteado}
    return dicionario
#-----------------------------------------------------------------------------------
def escolha(lista, quantidade_alunos):
    lista_sorteado = random.sample(lista,k=quantidade_alunos) #Parâmetro K é a quantidade de elementos a serem sorteados
    return lista_sorteado
    #--------------------------------------------------------------------------------
lista_alunos = []
contador = 1
controle = False
final = formulario()
quantidade_alunos = final['Quant_alunos']
quantidade_sorteados = final['Quant_sorteados']  
#--------------------------------------------------------------------------------
while contador <= quantidade_alunos:
    # comment: Inserir nome dos alunos e adicionar a lista de alunos
    nome_aluno = input(f'{contador}° ALUNO: ')
    if validacao(nome_aluno, 2):    
        print('VALOR NÃO ACEITO!!') 
    elif validacao(nome_aluno, 1):
        print('VALOR NÃO ACEITO!!')
    else:
        lista_alunos.append(nome_aluno)
        contador += 1
# end while
escolha_final = escolha(lista_alunos, quantidade_sorteados)
print("-----------------------------------------------------------")
print(f'OS ALUNOS ESCOLHIDOS FORAM: {', '.join(escolha_final).upper()}')
