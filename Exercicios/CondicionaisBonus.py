#Exec01-----------------------------------------------------------

print("\n# 1. Sistema de Avaliação Acadêmica Multicritério ---------------\n")
def avaliar_estudante(p1, p2, frequencia, entregou_trabalho_extra): 

    media = (p1+p2)/2

    if(frequencia < 75):
          return f"Olá, sua média é {media}, a sua frequencia ficou em {frequencia}. Mas você Reprovou por Frequência :-("
    else:
       if(media >= 7.0):
           return f"Olá, sua média é {media}, a sua frequencia ficou em {frequencia}. Você foi Aprovado Direto ;-D"
       elif(media >= 5.0 or media <= 6.9 and entregou_trabalho_extra):
        ponto = 1
        mediafinal = media + ponto

        if(mediafinal >= 7.0):
               return f"Olá, sua média é {media} + {ponto} ponto do trabalho extra, sua media ficou {mediafinal}, a sua frequencia ficou em {frequencia}. Você foi Aprovado graças ao Trabalho Extra. B-)"
        else:
               return f"Olá, sua média é {media}, a sua frequencia ficou em {frequencia}. Você ficou em Exame Final ^_^"
       else:
           return f"Olá, sua média é {media}, a sua frequencia ficou em {frequencia}. Você foi Reprovado por Nota :-/"

         
resultado = avaliar_estudante(8.0, 9.0, 70, False)
print(resultado)

print("\n#Fim-------------------------------------------------------------\n")

#---------------------------------------------------------------

#Exec02-----------------------------------------------------------

print("\n# 2. Análise do Quadrante e Origem Cartesiana -------------------\n")
def localizar_ponto(x, y):
     if(x == 0 and y == 0):
          return "Origem"
     elif(x == 0 and y != 0):
          return "Eixo Y"
     elif(x > 0 and y > 0):
          return "Q1"
     elif(x < 0 and y < 0):
          return "Q3"
     elif(x != 0 and y == 0):
          return "Eixo X"
     elif(x < 0 and y > 0):
          return "Q2"
     else:
          return "Q4"
     
resultado = localizar_ponto(-3,-4)
print(resultado)
     
print("\n#Fim-------------------------------------------------------------\n")

#---------------------------------------------------------------

#Exec03-----------------------------------------------------------

print("\n# 3. Simulador de Tarifação Telefônica em Rolo -------------------\n")
def calcular_fatura_telefone(minutos, gigas, e_estudante):
    
    plano_base = 50
    min_excedente = (minutos-100) * 0.5    
    giga_excedente = (gigas - 5) * 10
    fatura_total = plano_base + min_excedente + giga_excedente

    if(e_estudante == True and fatura_total):
       print (min_excedente)
       print (giga_excedente)
       print (fatura_total)
       return "Fatura Final: R$ 60.00"
    
    else:
       print (min_excedente)
       print (giga_excedente)
       print (fatura_total)
       return "Fatura Final: R$ 50.00"
    


resultado = calcular_fatura_telefone(80, 4, False)
print(resultado)

     
print("\n#Fim-------------------------------------------------------------\n")

#---------------------------------------------------------------
