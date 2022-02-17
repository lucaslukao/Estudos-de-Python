# Listas
lista = [12, 10, 5, 7] # Pode se colocar uma string numa lista de números, mas não é recomendado, vai dar erro ao fazer uma operção.
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara'] # Cada palavra, separada por uma vírgula é um elemento da lisa, que são numerados a apartir do zero, ou seja, cachorro = 0.
lista_animal[0] = 'macaco'
print(lista_animal)


#print(lista_animal[1])
#print(min(lista_animal)) # sum = soma os valores dentro de uma lista. max = mostra o valor máximo de uma lista, se for uma lista de string pega a maior palavra em ordem alfabética.   min = o contrário so max.
#nova_lista = lista_animal * 3 # Vai repetir a lista animal 3 x.
#print(nova_lista)
# lista.sort()
# lista_animal.sort() # ".sort()" ordena a lista.
# print(lista)
# print(lista_animal)
# lista_animal.reverse() # "reverse" ordena de forma reversa ao "sort".
# print(lista_animal)




#lista_animal.pop(0) # " .pop() " remove o último valor da lista, ou então você coloca o valor que quer remover dentro do parênteses
#print(lista_animal)
#lista_animal.remove('elefante') # "remove" remove aquilo que vc colocar dentro do parênteses.
#print(lista_animal)





# Tlupas: a grande diferença é que não pode mudar um elemento da tupla
tupla = (1, 10, 12, 14)
print(len(tupla)) # "len" mostra quantos elementos tem
tupla_animal = tuple(lista_animal) # "tuple" converte uma lista para uma tuple, mas é necessário criar uma variável para receber esse valor.
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)    # "list" converte uma tupla em uma lista
print(type(lista_numerica))
print(lista_numerica)
