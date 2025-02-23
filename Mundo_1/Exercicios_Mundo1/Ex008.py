print()
medida = float(input("DIGITE UM VALOR EM METROS: "))

#-----------------------------------------------------0
print()
print(f'O VALOR DE {medida} CONVERTIDO É IGUAL A: \n'
      f'- KM ({medida/1000:.0f})\n'
      f'- HM ({medida/100:.0f})\n'
      f'- DAM ({medida/10:.0f})\n'
      f'- M ({medida})\n'
      f'- DM ({medida*10:0f})\n'
      f'- CM ({medida*100:.0f})\n'
      f'- MM ({medida*1000:.0f})\n')