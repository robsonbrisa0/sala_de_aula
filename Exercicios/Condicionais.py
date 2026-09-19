
'''

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
def calcular_desconto(valor_compra:float, e_cliente_vip:bool): 

    if(e_cliente_vip or valor_compra>200):
      desconto = 15      
      vlrFinal = valor_compra - (valor_compra * (desconto/100))

      return print(f"Você recebeu {desconto}% de desconto! Valor final da sua compra é R$ {vlrFinal:.2f}X".replace(",", "X").replace(".", ",").replace("X", "."))
    
      
    else:
      desconto = 5      
      vlrFinal = valor_compra - (valor_compra * (desconto/100))
      return print(f"Você recebeu {desconto}% de desconto! Valor final da sua compra é R$ {vlrFinal:.2f}X".replace(",", "X").replace(".", ",").replace("X", "."))

calcular_desconto(150, False)

print("\n#Fim--------------------------------------------\n")

#---------------------------------------------------------------

#Exec07-----------------------------------------------------------

print("\n# 7. Classificação Acadêmica--------------------\n")
def conceito_nota(nota:float): 

    if(nota>=9 and nota<=10):

      return print("Você atingiu o conceito A")
    
    elif(nota>=7 and nota<=8.9):

      return print("Você atingiu o conceito B")
    
    elif(nota>=5 and nota<=6.9):

      return print("Você atingiu o conceito C")
          
    else:
       return print("Você atingiu o conceito F")
      
conceito_nota(9.2)

print("\n#Fim--------------------------------------------\n")

#---------------------------------------------------------------

#Exec08-----------------------------------------------------------

print("\n# 8. Validador de Triângulos--------------------\n")
def tipo_triangulo(a, b, c): 

    if(a + b > c and a + c > b and b + c > a):
      return print("Equilátero, Isósceles ou Escaleno")
    
    else:
       return print("Não é um triângulo")
      
tipo_triangulo(1,2,10)

print("\n#Fim--------------------------------------------\n")

#---------------------------------------------------------------

#Exec09-----------------------------------------------------------

print("\n# 9. Calculadora de Imposto de Renda Progressivo----\n")
def calcular_imposto(salario:float): 

    if(salario<=2000):
      return 0.0
    
    elif(salario<=4000):
       salario_final = salario-2000
       return salario_final*0.1
    
    else:
       salario_final = salario-4000
       return 200+(salario_final*0.2)
      
imposto = calcular_imposto(5000)
print(imposto)

print("\n#Fim-------------------------------------------------\n")

#---------------------------------------------------------------
'''
#Exec10-----------------------------------------------------------

print("\n# 10. Validador de Ano Bissexto---------------------\n")
def e_bissexto(ano:int): 

    if((ano%4==0 and ano%100!=0) or (ano%400==0) ):
          return True
    else:
       return False
      
anoBi = e_bissexto(2016)
print(anoBi)

print("\n#Fim-------------------------------------------------\n")

#---------------------------------------------------------------