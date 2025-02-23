def conversor_temperatura(temperatura):
    #Converter para FAHRENHEIT
    fahrenheit = (temperatura * 1.8) + 32
    #Conversor para KELVIN
    kelvin = temperatura + 273.15

    dicionario = {'Kelvin':kelvin, 
                  'Fahrenheit':fahrenheit}
    return dicionario
#----------------------------------------------------
print('')
tempe = float(input("DIGITE UMA TEMPERATURA EM °C: "))

temperatura_convertida = conversor_temperatura(tempe)

print(f'A TEMPERATURA {tempe:.1f}° CONVERTIDA É\n'
      f'- FAHRENHEIT: {temperatura_convertida['Fahrenheit']:.1f}\n'
      f'- KELVIN: {temperatura_convertida['Kelvin']:.1f}')