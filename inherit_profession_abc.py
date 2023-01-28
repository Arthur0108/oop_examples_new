from abc import ABCMeta, abstractmethod


class Profession(metaclass=ABCMeta):
    def __init__(self, name, skill, wage):
        self.name = name
        self.skill = skill
        self.wage = wage
        print(f'We have a profession {self.name}.')

    @abstractmethod
    def info(self):
        print(f'Profession: {self.name}, skill: {self.skill}, wage: {self.wage}. ', end=' ')


class Military(Profession):
    def __init__(self, name, skill, wage, uniform):
        Profession.__init__(self, name, skill, wage)
        self.uniform = uniform
        print(f'{self.name} profession is very dangerous.')

    def info(self):
        Profession.info(self)
        print(f'The military has {self.uniform} color uniforms.')


class Doctor(Profession):
    def __init__(self, name, skill, wage, instrument):
        Profession.__init__(self, name, skill, wage)
        self.instrument = instrument
        print(f'{self.name} profession is very responsible.')

    def info(self):
        Profession.info(self)
        print(f'Doctors has instrument {self.instrument}.')


class Programmer(Profession):
    def __init__(self, name, skill, wage, assistant):
        Profession.__init__(self, name, skill, wage)
        self.assistant = assistant
        print(f'{self.name} profession is very interesting.')

    def info(self):
        Profession.info(self)
        print(f'The best assistant to a programmer is a {self.assistant}:)')


m = Military('Commando', 'Sniper', 150000, 'Multicam')
d = Doctor('Therapist', 'Treatment', 20000, 'Phonendoscope')
p = Programmer('Developer', 'Website development', 'Normal', 'Computer')
print()

various_professions = [m, d, p]
for vp in various_professions:
    vp.info()
