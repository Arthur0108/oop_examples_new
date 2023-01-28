class Hero:

    population = 0

    def __init__(self, name):
        self.name = name
        print(f'Identification {self.name}')

        Hero.population += 1

    def __del__(self):
        print(f'{self.name} is is gone.')

        Hero.population -= 1

        if Hero.population == 0:
            print(f'{self.name} be the last.')

        else:
            print(f'We have {Hero.population} heroes.')

    def say_hi(self):
        print(f'Hello people, my name is {self.name}!')

    def how_many():
        print(f'We have {Hero.population} heroes!')

    how_many = staticmethod(how_many)


hero_1 = Hero('SuperMan')
hero_1.say_hi()
Hero.how_many()

hero_2 = Hero('SpiderMan')
hero_2.say_hi()
Hero.how_many()

hero_3 = Hero('Batman')
hero_3.say_hi()
Hero.how_many()

print('\nHere Heroes help people!\n')
print('The heroes saved everyone. Let\'s let them rest!')
del hero_1
del hero_2
del hero_3

Hero.how_many()
