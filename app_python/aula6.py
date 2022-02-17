# Conjutos
#
# A grande diferença de um conjunto para uma lista e tupla, é que o conjunto é feito com as {} e não aceita duplicidade(dois valores iguais)
# conjunto = {1, 2, 3, 4}
# conjunto.add(5)        # ".add" adiciona um valor no conjunto
# conjunto.discard(2)       # ".discar" tira um valor do conjunto
# print(conjunto)


conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2)    # --> ".union"  junta dois conjutos e junta números que forem iguais.
print('União: ', conjunto_uniao)
conjunto_interseccao = conjunto.intersection(conjunto2)  # "intersection" mostra os pontos comuns dos conjuntos
print('Intersecção: ', conjunto_interseccao)
conjunto_diferenca1 = conjunto.difference(conjunto2)    # ".difference" mostra quais valores tem no primeiro conjunto, que não tem no segundo.
print('Diferença entre 1 e 2: ', conjunto_diferenca1)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença entre 2 e 1: ', conjunto_diferenca2)
conjunto_diff_simetrica =  conjunto.symmetric_difference(conjunto2)   #"symmetric_diffrence" mostra os números que os dois não tem em comum
print('Diferença simétrica: ', conjunto_diff_simetrica)

conjunto_a = {1, 2, 3,}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)   # ".issubset" mostra se o primeiro conjunto está dentro do segundo.
print('A é um subconjunto de B: ', conjunto_subset)
conjunto_superset = conjunto_b.issuperset(conjunto_a)    #".superset" mostra se o primeiro conjunto contém o segundo.
print('B é superconjunto de A: ', conjunto_superset)
# logo a é um subconjunto(subset de b) e b é um super conjunto(superset de a).

lista = ('cahorro', 'cachorro', 'gato', 'gato', 'elefante')
print(lista)
conjunto_animais = set(lista)    # --> "set" converter para um conjunto
print(conjunto_animais)
lista_animais = list(conjunto_animais)   # --> "list" para convereter para uma lista
print(lista_animais)
