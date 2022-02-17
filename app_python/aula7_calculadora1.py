#--------> Métodos, funções e classes

#---> Métodos:
#
# def soma(a, b):   # "def" seria definição, "soma" é o nome da variável, "a, b" é dois valores que vc colocar e vai retornar a soma deles
#     return a + b
# def subtracao(a, b):
#     return a - b
# def multiplicacao(a , b):
#     return a * b
# def divisao(a , b):
#     return a / b
#
# print(soma(1, 2))
# print((soma(3, 4)))
# print(subtracao(10, 2))
# print(multiplicacao(10, 2))
# print(divisao(10, 2))

class Calculadora:
    def __init__(self, num1, num2):  #"__init__" é um método, toda vez que vc estanciar a classe, vai passar primeiro pelo init. "self" é para representar o objeto
        self.valor_a = num1
        self.valor_b = num2
    def soma (self):
        return self.valor_a + self.valor_b
    def subtracao(self):
        return self.valor_a - self.valor_b
    def multiplicacao(self):
        return self.valor_a * self.valor_b
    def divisao(self):
        return self.valor_a / self.valor_b

calculadora = Calculadora(10, 2)   # Isso é "estanciar"
print (calculadora.valor_a)
print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.multiplicacao())
print(calculadora.divisao())