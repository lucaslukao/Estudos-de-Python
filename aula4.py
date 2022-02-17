# Comandos de repetições
# ---> Comando 'while'
#
# a = 0
# while a <= 10: # Seria 'enquanto'
#     print(a)
#     a += 1

# ## -----> O while resolve o problema da aula passada melhor que o if
# a = float(input('Digite sua nota: '))
# while a > 10:
#     a = int(input('Nota inválida. Entre com um valor menor ou igual a 10: '))


#Calculando a média
a = float(input('Digite a nota do primeiro bimestre: '))
while a > 10:
    a = float(input('Digite uma nota menor ou igual a 10: '))
b = float(input('Digite a nota do segundo bimestre: '))
while b >10:
    b = float(input('Digite uma nota menor ou igual a 10: '))
c = float(input('Digite a nota do terceiro bimestre: '))
while c > 10:
    c = float(input('Digite uma nota menor ou igual a 10: '))
d  = float(input('Digite a nota do quarto bimestre: '))
while d > 10:
    d = float(input('Digite uma nota menor ou igual a 10: '))
media = (a + b + c + d) / 4
print('Média: ' ,media)


# a = int(input('Entre com um valor: '))
# for num in range (a + 1):
#     div = 0
#     for x in range (1, num+1): # --> O 'for' seria: enquanto, é usado para repetições. O 'in range' percorre todos os algorismos dentro do parênteses)
#         resto = num % x
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#         print(num)
# print('Esse são os números primos dentro desse valor.')

# ----> Para ver se um número é primo.
# a = int(input('Escreva um número: '))
#
# div = 0
# for x in range (1, a+1): # --> O 'for' seria: enquanto, é usado para repetições. O 'in range' percorre todos os algorismos dentro do parênteses)
#     resto = a % x
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print('O número {} é primo.' .format(a))
# else:
#     print('O número {} não é primo' .format(a))
