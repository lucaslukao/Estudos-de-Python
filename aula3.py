# # Os condicionais do Python
#Calculando a média
a = int(input('Digite a nota do primeiro bimestre: '))
if a > 10:
    a = int(input('Digite uma nota menor ou igual a 10: '))
b = int(input('Digite a nota do segundo bimestre: '))
if b >10:
    b = int(input('Digite uma nota menor ou igual a 10: '))
c = int(input('Digite a nota do terceiro bimestre: '))
if c > 10:
    c = int(input('Digite uma nota menor ou igual a 10: '))
d  = int(input('Digite a nota do quarto bimestre: '))
if d > 10:
    d = int(input('Digite uma nota menor ou igual a 10: '))
media = (a + b + c + d) / 4
print('Média: ' ,media)
# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('Média: ', media)
# else:
#     print('Você informou algum valor maoir que 10.')



# a = int(input('Escreva o primeiro valor: '))
# b = int (input('Escreva o segundo valor: '))
# c = int(input("Escreva o terceiro valor: "))
#
# if a > b and a > c: # --> com o 'and' voce pode adicionar um condição
# # O 'if' válida se a informação é verdadeira, logo se a for maior que b aparece o print e se for menor nao aparece.
# # Para escrever dentro do if tem que dar 4 espaços ou tab.
#     print('O maior valor é: {}' .format(a))
# elif b > a and b > c: # Seria junção de elfe com if. Serve para colocar mais condições.
#     print("O maior valor é: {}".format(b))
# else:
#     print("O maior valor é: {}" .format (c))
# # O 'else' seria um 'se não', se a informação que estiver acima não for verdade execute else.
# # Tem que estar em sequência para funcionar

