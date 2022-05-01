# Desafio da semana
#
# Jogo de Craps. Faça um programa de implemente um jogo de Craps.
# O jogador lança um par de dados, obtendo um valor entre 2 e 12.
# Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.
# Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu.
# Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto".
# Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
# Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
import random
def games():

    list_number_one=[7,11]
    list_number_two=[2,3,12]
    list_number_three=[4,5,6,8,9,10]
    round=1

    while round>0:
        value_random = random.randrange(2, 13)
        print(value_random)
        if round >1:
            if value_random ==7:
                print("Você perdeu")
                break
            elif numbers_save == value_random:
                print("finaliza jogo")
                break
        if value_random in list_number_one:
            print("Você ganhou")
            break
        elif value_random in list_number_two:
            print("Você perdeu")
            break
        elif value_random in list_number_three:
            numbers_save=value_random
            round+=1
            print("Pontuou",numbers_save)

games()