import re

def busca_sobrenome(nome):
    nome_tratado = (nome.strip()).upper()
    resultado_pesquisa = re.search(r'SILVA', nome_tratado)
    
    return {
        "CONTROLE": bool(resultado_pesquisa),
        "GRUPO": resultado_pesquisa.span() if resultado_pesquisa == True else None
        #.Span retorna a posição da ocorrência em REGEX
        #DEVEMOS TER UM RETORNO DE NONE, PARA O CASO DE NÃO ENCONTRAR O PADRÃO
    }
#====================================================================
nome = input("INFORME SEU NOME: ")
resultado_busca_sobrenome = busca_sobrenome(nome)

if resultado_busca_sobrenome["CONTROLE"]:
    print(f"""VOCÊ POSSUI SILVA NO SOBRENOME 
(POSIÇÃO: {resultado_busca_sobrenome["GRUPO"]})""")
else:
    print("VOCÊ NÃO POSSUI SILVA NO SOBRENOME!!")
