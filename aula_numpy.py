import numpy as np

array_letras = np.array(['a', 'b', 'c', 'd', 'e'])

print(array_letras)
#acessando posição especifica
print(array_letras[0])  
#acessando partes do array
print(array_letras[0:2])

#criando um arraya de inteiros 
preco = np.array([20, 40, 25, 35, 30])
print('preco', preco)

#aumentando o preço de todos os valores do array em 10%
novos_precos = preco * 1.1
print('valor aumentado:> ', novos_precos)
