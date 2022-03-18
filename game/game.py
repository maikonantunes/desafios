# -*- coding: utf-8 -*-

import random

class Questions:
    def __init__(self, resposta=None, pont=None, value_one=None, value_two=None):
        self.resposta=resposta
        self.pont=0
        self.value_one=value_one
        self.value_two=value_two

    def operations_nivel_one(self):
        print("Bem vindo ao nível 1")
        self.value_one=random.choice(range(4))
        self.value_two=random.choice(range(4))
        print(F"Quanto é {self.value_one} + {self.value_two}")
        self.resposta=self.value_one + self.value_two
        try:
            data_user=int(input())
        except ValueError:
            print("Váriavel invalidada! Tente novamente")
            return False
        if self.resposta == data_user:
            self.pont+=1
            print("resposta correta")
            return self.rank()
        else:
            print("resposta errada")
            return select_question()
            
    def operations_nivel_two(self):
        print("Bem vindo ao nível 2")
        self.value_one=random.choice(range(4))
        self.value_two=random.choice(range(4))
        print(f'Quanto é {self.value_one} - {self.value_two}')
        self.resposta=self.value_one - self.value_two
        try:
            data_user=int(input())
        except ValueError:
            print("Váriavel invalidada! Tente novamente")
            return False
        if self.resposta == data_user:
            self.pont+=1
            print("resposta correta")
            return self.rank()
        else:
            print("resposta errada")
            return select_question()


    def operations_nivel_three(self):
        print("Bem vindo ao nível 3")
        self.value_one=random.choice(range(4))
        self.value_two=random.choice(range(4))
        print(F"Quanto é {self.value_one} * {self.value_two}")
        self.resposta=self.value_one * self.value_two
        try:
            data_user=int(input())
        except ValueError:
            print("Váriavel invalidada! Tente novamente")
            return False
        if self.resposta == data_user:
            self.pont+=1
            print("resposta correta")
            return self.rank()
        else:
            print("resposta errada")
            return select_question()
    
    def rank(self):
        if self.pont <=3:
            return self.operations_nivel_one()
        elif self.pont >=4 and self.pont <=6:
            return self.operations_nivel_two()
        elif self.pont >=7 and  self.pont <=10:
            return self.operations_nivel_three()
        elif self.pont >=11:        
            print("Parabéns vc zerou o jogo!!")
            print("Deseja retornar ao jogo? Digite sim para retornar!")
            try:
                back_game=str(input(""))
                if back_game != "sim":
                    print("Fim de jogo")
                    return True
                else:
                    return select_question()
            except ValueError :
                print("Fim de jogo")
        
def select_question():
    perguntas=Questions()
    perguntas.operations_nivel_one()

        
select_question()