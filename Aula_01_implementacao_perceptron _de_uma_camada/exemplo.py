import time

entrada = [-1,7,5]
pesos = [0.8,0.1,0]

# Exemplo sem utilizar as bibibliotecas de IA
def soma(e,p):
    s=0
    for i in range(3):
        print(entrada[i])
        print(pesos[i])
        s+= e[i] * p[i]

    return s

s= soma(entrada,pesos)

def stepfuncion(soma):
    if (soma >= 1): # Se for maior que 1 o neuronio e ativado
        print("Neuronio Ativado")
        return 1
    else:
        print("Neuronio não ativado!")
        return 0
r= stepfuncion(s)


