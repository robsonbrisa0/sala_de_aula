#Exec00-----------------------------------------------------------

print("\n#Exec01------------------------------------------\n")
def fizz_buzz(numero:int):

    if(numero%3==0 and numero%5==0):
      return print("FizzBuzz")
    
    elif(numero%3==0):
      return print("Fizz")
    
    elif(numero%5==0):
      return print("Buzz")
    
    else:
       return print(numero)

num = 3

fizz_buzz(num)

print("\n#Fim---------------------------------------------\n")

#---------------------------------------------------------------

#Exec01-----------------------------------------------------------

print("\n# 1. Validador de Maioridade---------------------\n")
def verificar_maioridade(idade:int):

    if(idade >=18):
      return print("Maior de idade")
    
    else:
       return print("Menor de idade")

idade = 17

verificar_maioridade(idade)

print("\n#Fim---------------------------------------------\n")

#---------------------------------------------------------------

#Exec02-----------------------------------------------------------

print("\n# 2. Par ou Ímpar--------------------------------\n")
def verificar_par(numero:int):

    if(numero%2==0):
      return print("Par")
    
    else:
      return print("Ímpar")

numero = 17

verificar_par(numero)

print("\n#Fim---------------------------------------------\n")

#---------------------------------------------------------------

#Exec03-----------------------------------------------------------

print("\n# 3. Classificador de Número---------------------\n")
def classificar_numero(numero:int):

    if(numero>0):
      return print("Positivo")
    
    elif(numero<0):
      return print("Negativo")
    
    else:
      return print("Zero")

numero = 0

classificar_numero(numero)

print("\n#Fim--------------------------------------------\n")

#---------------------------------------------------------------

#Exec04-----------------------------------------------------------

print("\n# 4. Aprovado ou Reprovado---------------------\n")
def calcular_resultado(nota1:float, nota2:float):

    media = (nota1 + nota2)/2  

    if(media>=7):
      return print("Aprovado")
    else:
      return print("Reprovado")

media = calcular_resultado(7,7)

print("\n#Fim--------------------------------------------\n")

#---------------------------------------------------------------

#Exec05-----------------------------------------------------------

print("\n# 5. Comparador de Dois Números------------------\n")
def maior_de_dois(n1:int, n2:int):
 
    if(n1>n2):
      return print("O primeiro é maior")
    elif(n2>n1):
      return print("O segundo é maior")
    else:
      return print("São iguais")

Resultado = maior_de_dois(7,8)

print("\n#Fim--------------------------------------------\n")

#---------------------------------------------------------------

#Exec06-----------------------------------------------------------

print("\n# 6. Sistema de Desconto de Loja----------------\n")
def calcular_desconto(valor_compra:float, e_cliente_vip:float):
 
    if(n1>n2):
      return print("O primeiro é maior")
    
    else:
      return print("São iguais")

Resultado = calcular_desconto(7,8)

print("\n#Fim--------------------------------------------\n")

#---------------------------------------------------------------