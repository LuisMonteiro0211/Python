import re
import typing

def pergunta_nome():
    padrao_input = re.compile(r'^[a-zA-Zà-úÀ-Ú ]+$')
    while True:
        nome = input("INFORME SEU NOME COMPLETO: ").strip()
        if re.match(padrao_input, nome):
            print(f"******NOME ACEITO COM SUCESSO******\nBEM VINDO {nome.upper()}!!!")
            break
        else:
            print(f"NOME INFORMADO '{nome}' INVALIDO!! SÃO PERMITIDOS APENAS LETRAS E ESPAÇOS \nDIGITE NOVAMENTE\n")

    return nome

def fatiamento (nome_completo):
    nome_fatiado = nome_completo.split()
    #typing.reveal_type(nome_fatiado)
    primeiro_nome = nome_fatiado[0]
    ultimo_nome = nome_fatiado[-1] if len(nome_fatiado) >1 else "SOBRENOME NÃO INFORMADO"
    return {
        "PRIMEIRO_NOME":primeiro_nome.upper(),
        "ULTIMO_NOME":ultimo_nome.upper()
    }

nome_valido = pergunta_nome()
fatiamento_nome = fatiamento(nome_valido)
print(f"""
-PRIMEIRO NOME: {fatiamento_nome["PRIMEIRO_NOME"]}
-ULTIMO NOME: {fatiamento_nome["ULTIMO_NOME"]}
""")
