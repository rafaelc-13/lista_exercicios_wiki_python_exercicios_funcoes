'''
11)Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA
 e devolva uma string no formato D de mesPorExtenso de AAAA.
 Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
'''
def mesPorExtenso(dia, mes, ano):
    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

    if mes >= 1 and mes <= 12:
        mes_extenso = meses[mes-1]
    else:
        return "NULL"

    if dia >= 1 and dia <= 31:
        return f"{dia} de {mes_extenso} de {ano}"
    else:
        return "NULL"

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês em números: "))
ano = int(input("Digite o ano: "))

data_extenso = mesPorExtenso(dia, mes, ano)

if data_extenso != "NULL":
    print(f"A data por extenso é: {data_extenso}")
else:
    print("Data inválida.")
