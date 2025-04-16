#lista vazia
lista_peixes = []

for i in range(8):
 peixe= (input("diga nome do peixe que gosta de comer na semana: ")) 
 lista_peixes.append(peixe)


print("minha lista de peixe")
print(lista_peixes)
if "tambaqui" in lista_peixes: 
 lista_peixes.remove("tambaqui")
 print(lista_peixes)
 