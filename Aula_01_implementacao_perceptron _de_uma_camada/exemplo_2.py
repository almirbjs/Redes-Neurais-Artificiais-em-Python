import time

import numpy as np
# Exemplo utilizando as bibibliotecas de IA
inicio=time.time()
entrada = np.array([1,7,5])
pesos = np.array([0.8,0.1,0]) # Os pesos podem ser chamados de sinapses
def soma(e,p):
    return e.dot(p) # dot product / produto escalar - não precisa utilizar o for para percorrer um array

s= soma(entrada,pesos)

def stepfuncion(soma):
    if (soma >= 1): # Se for maior que 1 o neuronio e ativado
        print("Neuronio Ativado")
        return 1
    else:
        print("Neuronio não ativado!")
        return 0
r= stepfuncion(s)

fim=time.time()
tempo_execucao=(fim - inicio)*1000

print(f"A função levou {tempo_execucao} segundo para ser executada.")