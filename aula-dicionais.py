#aula_dicionais.py
#aula sobre adicionarios no python

#Os principais elementos sintaticos sao {} chaves, virgula : dois pontos
# em dicionarios temos o conceito de CHAVES:VALOR
#criando um dicionario vazio, precisa apenas de abrir CHAVES()
#note que nas listas usamos os COLCHETES[]
dicionario_vazio = {}

#criando um dicionario com valores
dicio_preenchido = {'nome':'milena', 'idade':17 }
print(dicio_preenchido)

#acessando o valor de uma CHAVE em especifico
aux_nome = dicio_preenchido['nome']
print('mostrando o valor da chave nome: ', aux_nome)

#Acessando uma chave especifico que NÃO existe
profissao = dicio_preenchido.get('prof', 'não encontrado')
print(profissao)

#para adicionar ou modificar um elemento no dicionario usamos e atribua 
dicio_preenchido['idade'] = 18
print ('Alterando a idade: ',dicio_preenchido)

#Adicionando uma nova chave e valor
dicio_preenchido['profissao'] = 'motoqueiro'
print('incluindo uma nova chave-valor: ', dicio_preenchido)

#Removendo um elemento especifico
aux_idade = dicio_preenchido.pop('idade')

print('idade removido > ', dicio_preenchido)
print('mesmo removida podemos guardar o valor em outro local', aux_idade)

#para excluir o dicionario usamos o comando del
#por motivos de segurança nao usaremos o comando

# quando pegamos im dicionario que não sabemos as benditas chaves
# temos uma forma facil de identificar usando a função keys()
todas_chaves = dicio_preenchido.keys()
print('Todas as chaves do dicionario: ',todas_chaves)

#temos uma forma facil de identificar os valores, usando a função values
todao_valores = dicio_preenchido.values()
print('todas os valores do dicionario: ',todao_valores)

#podemos fazer iteração no dicionario para acessar de forma individual o par chave-valor
for chave, valor in dicio_preenchido.item():
    print(chave, ' - ', valor)