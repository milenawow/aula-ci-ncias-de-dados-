#lista vazia
lista_material_escolar = []
lista_material_valor = []
#laço de repetição e o meetodo input
for material in range(2):
    item = str(input("diga nome dos materiais escolar: ")) 
    lista_material_escolar.append(item)

for valor in range(2):
    preco =float(input("diga os valores dos materials: "))
    lista_material_valor.append(preco)

print("minha lista de materiais e lista de valor de materiais")
print(lista_material_escolar)
print(lista_material_valor)

salario = [s_lapis, s_caderno]
ssalario_max = max(salario)
salario_min = min(salario)

