print(""" 
        ===========================================================                                                    
        = Programa para calcular o Ìndice de Massa Corporal (IMC) =                                                     
        =========================================================== 
      """)

peso = float(input("Informe o seu peso em kilos: "))
altura = float(input("Informe a sua altura em metros: "))

imc = peso/altura**2
# Função para calcular o IMC
def calculo_imc(imc):
  if imc < 18.5:
    return (f"O seu IMC é: {imc:.2f} e indica BAIXO PESO")
  elif imc > 18.4 and imc < 25:
    return (f"O seu IMC é: {imc:.2f} e indica PESO ADEQUADO")
  else:
    return (f"O seu IMC é: {imc:.2f} e indica SOBREPESO")
       
# Imprime a saída da função:
print(calculo_imc(imc))