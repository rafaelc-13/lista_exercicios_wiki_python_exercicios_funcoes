def matriz(n1):
    lista=[]
    for x in range(1,n1+1):
        resul = x * str(x)
        print(resul,' ')

def matriz_1 (n1):
    lista = ''
    for x in range (1,n1+1):
        lista = lista + str(x)
        print(lista)

def soma (n1,n2,n3):
    soma = n1 + n2 + n3
    print(f'A soma é: {soma}')

def resposta (booley):
    if booley.lower() == "s" or booley.lower() == "sim":
        print("P = positivo")

    elif booley.lower() == "n" or booley.lower() == "não":
        print("N = negativo")

def somaImposto (valor):
    imposto = 1.20
    taxaimposto = imposto * valor
    print(f'O valor pós impostos é R${taxaimposto}')

def convertor_hora (hora_input,minutos_input):
    while hora_input > 24:
        hora_input = int(input("Horas inválidas, tente novamente.\n Digite as horas: "))
    else:
        if hora_input > 12:
            hora_input -= 12
            print(f"As horas são {hora_input}:{minutos_input}p.m")
        elif hora_input <= 12:
            print(f"As horas são {hora_input}:{minutos_input}p.m")

def valorPagamento (valor_prestacao,dias_atraso):
    if dias_atraso > 0:
        multa = valor_prestacao*0.03
        juros = valor_prestacao*(0.001 * dias_atraso)
        valor_total = valor_prestacao + multa + juros
        return valor_total
    else:
        return valor_prestacao

def casas_decimais (numero):
    c=0
    for x in str(numero):
        c+=1
    return c
                        #s =str(numero)
                        #return len(s)

def reverso (numero):
    invert = numero[::-1]
    return invert

def lancar_dado():
    import random
    return random.randint(1, 6)



