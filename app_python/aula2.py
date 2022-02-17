# Aula sobre operadores aritimétricos e outras coisas
a = float(input('Entre com o primeiro valor: '))
b = float(input('Entre com o segundo valor: '))
# O comando int transforma uma string em um inteiro, pois não é possivel fazer operações entre um int e uma string.
# O comando input serve para interagir com o usuário.
#print(type(a),(b)) # 'type' serve para mostrar o qual o tipo da variável e print escreve uma mensagem
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
resultado = ('Soma: {soma} '
             '\nSubtração: {subtracao} '
             '\nMultiplicação: {multiplicacao} '
             '\nDivisão: {divisao} '
             '\nResto: {resto}'
             .format(soma=soma,
                     divisao=divisao,
                     subtracao=subtracao,
                     multiplicacao=multiplicacao,
                     resto=resto))
# Abrir a chaves e colocar o '.format' você pode colocar um valor de uma variável. Exs:
#resultado = (´Soma: {}' .format(soma)) --> Desse modo vc tem que colocar as variáveis em ordem.
#resultado = ('Soma: {soma}' .format(soma=soma)) --> Desse modo vc da nome a cada chave mas tem que especificar qual variável cada nome representa 'soma=soma'
# lê: soma recebe soma. Além disso, desse jeito as variáveis não precisam estar na ordem.
print(resultado)
