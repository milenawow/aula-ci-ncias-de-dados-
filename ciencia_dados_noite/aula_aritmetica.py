import math
# Declaração variaveis do tipo int
a = 5
b = 2

# Realizando a operação de adição
adicao = a + b 
print ('Adição: '+str(adicao))

# Realizando operação de subtração
subtracao = a - b 
print('subtração : ' + str(subtracao))

#Realizando operação de multiplicação
multiplicacao = a * b
print('multiplicação:  ' + str(multiplicacao))

#Realizando a operação de divisão
divisao = a / b 
print('divisao: ' +str(divisao)) 

#Realizando operação de modulo (Resto da divisão)
#ele vem do que sobra da divisão, ex: 8/2 > 4 = 0, entao logo o resto vai ser zero
modulo = a % b 
print('modulo:  ' +str(modulo))

#Realizando operação de potenciação
potencia = a ** b
print('potenciação: ' +str(potencia))

# Realizando operação de divisão por inteiro
divisaoInteiro = a // b
print('divisão Inteiro: ' +str(divisaoInteiro)) 

# Realizando operação de raiz
raiz = math.sqrt(9)
print('raiz: ' + str(raiz))
