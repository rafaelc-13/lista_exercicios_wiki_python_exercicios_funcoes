'''
7)Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento,
 que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela.
  Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero
   para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá
    a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso,
     cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
'''
from biblioteca import valorPagamento
quantidade_prestacoes = 0
total_pago = 0
while True:
    valor_prestacao = float(input("Qual valor da sua prestação atualmente? "))
    if valor_prestacao == 0:
        break
    atraso = int(input("Quantas parcelas você tem em atraso? "))
    valor_a_pagar = valorPagamento(valor_prestacao,atraso)
    quantidade_prestacoes += 1
    total_pago += valor_a_pagar
    print(f"Valor a ser pago é: R${valor_a_pagar}")

print(f"Relatório do dia:")
print(f"Quantidade de prestações pagas: {quantidade_prestacoes}")
print(f"Valor total pago no dia: R${total_pago}")

