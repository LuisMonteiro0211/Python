from datetime import date
from typing import TypedDict
from time import sleep
import re

class Dicionario(TypedDict):
    controle: bool
    ano_usuario: int
        
def validacao_bissexto(entrada_usuario: str) -> bool:
    padrao = re.compile(r'([0-9]{1,4})|(EXIT)')
    return bool(re.fullmatch(padrao,entrada_usuario))#RETORNA CASO O PADRÃO SEJA ENCONTRADO OU NÃO

def mensagem_tempo(tempo: int, mensagem: str) -> None:
    print(f"\n{mensagem}")
    sleep(tempo)

def entrada_usuario()-> str:
    while True:
        entrada_usuario = input(f'''|{"="*11}-CÁLCULO ANO-{"="*11}|
QUER SABER SE ALGUM ANO É BISSEXTO?
- INFORME UM ANO PARA O CÁLCULO
- INFORME 0 PARA USAR O ANO ATUAL
- INFORME "EXIT" PARA SAIR DO PROGRAMA
-> ''').strip().upper()
        if validacao_bissexto(entrada_usuario):
            return entrada_usuario
        else:
            print("POR FAVOR, INFORME NÚMEROS OU EXIT")

def calculo_bissexto(ano_informado: int)-> Dicionario:
    print(ano_informado)
    ano_usuario = ano_informado if ano_informado != 0 else date.today().year
    return Dicionario(controle=(ano_usuario%4 ==0 and ano_usuario%100 !=0) or (ano_usuario%400 == 0), 
                      ano_usuario= ano_usuario)

def main():
    while True:
        info_user = entrada_usuario()
        if info_user == "EXIT":
            mensagem_tempo(2, "ENCERRANDO PROGRAMA...")
            break
        else:
            ano_bissexto = calculo_bissexto(int(info_user))
            if ano_bissexto["controle"]:
                print(f"\n O ANO INFORMADO {ano_bissexto['ano_usuario']} É UM ANO BISSEXTO")
            else:
                print(f"\n O ANO INFORMADO {ano_bissexto['ano_usuario']} NÃO É UM ANO BISSEXTO")
        while True:
            nova_tentativa = input(f"\n DESEJA FAZER OUTRO CÁLCULO?\n1-SIM\n2-NÃO\n")

            if nova_tentativa == "2":
                mensagem_tempo(2, "ENCERRANDO PROGRAMA...")
                break
            elif nova_tentativa == "1":
                break
            else:
                print("OPÇÃO INFORMADA INVÁLIDA, POR FAVOR INFORME NOVAMENTE")
                
if __name__ == "__main__":
    main()
