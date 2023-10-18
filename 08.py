'''8)Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.'''
from biblioteca import casas_decimais

valor = int(input("Digite um numero: "))
quantidade = casas_decimais(valor)
print(quantidade)
