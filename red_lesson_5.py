#5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
#    - как минимум один атрибут должен быть с уровнем доступа private.
#    Соответственно, для получания значений этого атрибута нужно использовать методы get и set



class Warrior:
    def __init__(self,name,age,armor,representative):
        self.name=name
        self.age=age
        self.armor = armor
        self._representative= representative

    def run(self):
        return f'{self.name} is running'

    def hit(self):
        return '{self.name} is hitting with a weapon'

    def get_name(self):
        return f'My name is {self.name}'

    def get_age(self):
        return f'I am {self.age} years old'

    def get_representative(self):
        return f'I am from {self._representative} family'

    def set_representative(self,new_representative):
        self._representative = new_representative




class Swordsman(Warrior):
    def __init__(self,name,age,armor,weapon,representative):
        super().__init__(name,age,armor,representative)
        self.weapon=weapon

    def make_lunge(self):
        return f'{self.name} is making lunge with {self.weapon}'



class Horseman(Warrior):
    def __init__(self,name,age,armor,weapon,horse,representative):
        super().__init__(name,age,armor,representative)
        self.weapon=weapon
        self.horse=horse

    def ride_horse(self):
        return f'{self.name} is ridding horse'

    def stop_horse(self):
        return '{self.name}  stopped the horse'






