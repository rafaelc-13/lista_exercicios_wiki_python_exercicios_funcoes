'''5)Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais:
-taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem.
-custo, que é o custo de um item antes do imposto.
 A função “altera” o valor de custo para incluir o imposto sobre vendas.'''

from biblioteca import somaImposto

valor = int(input("Digite o valor do preço sem impostos: R$"))
somaImposto(valor)
