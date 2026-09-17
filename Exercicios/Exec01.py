
print("###########################################################")


def formatar_saudacao(nome:str, cidade:str):
    return f"Olá {nome}, seja bem-vindo(a) ao {cidade}!"
mensagem = formatar_saudacao("Robson", "Senac")
print(f"\n1) {mensagem}\n")

#---------------------------------------------------------------

def calcular_perimetro(largura:float, altura:float):
    return 2*(largura+altura)
area = calcular_perimetro(5.0, 10.0)

print(f"2) A área do perimetro é {area}\n")

#---------------------------------------------------------------

def fahrenheit_para_celsius(temp_f:float):
    return (temp_f - 32) * (5 / 9)

fahrenheit = 68
celsius = fahrenheit_para_celsius(fahrenheit)

print(f"3) {fahrenheit}°F é o mesmo que {celsius}°C\n")

#---------------------------------------------------------------

def calcular_gorjeta_por_pessoa(conta:float, porcentagem_gorjeta:float, pessoas:int):

    gorjeta = (conta*(porcentagem_gorjeta/100))/pessoas

    return gorjeta

print(f"Cada pessoa deve cotribuir com {gorjeta} para gorjeta\n")

#---------------------------------------------------------------


print("###########################################################")
