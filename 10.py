'''10)Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12.
Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.
Se você tirar 2, 3 ou 12 na primeira jogada,isto é chamado de "craps" e você perdeu.
Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto".
Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.'''
from biblioteca import lancar_dado
dado_1 = lancar_dado()
dado_2 = lancar_dado()
resultado = dado_1 + dado_2

if resultado == 7 or resultado == 11:
    print("Você é um natural, e GANHOU!!!")
elif resultado == 2 or resultado == 3 or resultado == 12:
    print("Você é um crap, e PERDEU!!!")
else:
    cont = 0
    goal = resultado
    print(f"Seu objetivo é repetir um {goal}.")

    while True:
        dado_1 = lancar_dado()
        dado_2 = lancar_dado()
        resultado = dado_1 + dado_2
        print(f"Você tirou um {resultado}!")
        cont +=1

        if resultado != goal:
            if resultado == 7:
                print("Você tirou um 7 antes de ganhar! Perdeu!")
                break
        else:
            print(f'Parabéns, depois de {cont} pontos, você tirou um {resultado}!')
            break



#n jogadas
#if 1ªjogada == 7 or 11: voce é um natural, e ganhou!
#elif 1ª jogada == 2 or 3 or 12: você é um crap, e perdeu!
# else: 1 ponto
#objetivo: jogar até repetir o valor da primeira jogada, mas se tirar um 7 antes, perde.
