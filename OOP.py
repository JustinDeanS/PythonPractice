# OOP Practice
# Vehicle  --> Car, Bicycle, Motorcycle, Train, Airplane

class Animal:
    def __init__ (self, name):
        self.name = name
    
    def get_name(self):
        print(f'{self.name}')

    def test(self):
        print('test if it works in other classes')

class Dog(Animal):
    def sound(self):
        print('woof')
    
    def get_name(self):
        print(f'{self.name}')
    
    def show(self):
        print(f'I am {self.name}')
    

class Horse(Animal):
    def sound(self):
        print('neigh')

    def get_name(self):
        print(f'{self.name}')
    

class Bird(Animal):
    def __init__ (self, name, color):
        super().__init__(name)
        self.color = color

    def sound(self):
        print('bwak')

    def get_color(self):
        print(f'Bird is {self.color}')

    def get_name(self):
        print(f'{self.name}')
    
    def test(self):
        print('test if it works in other classes BIRD CVLASS')

fish = Animal('Tim')
fish.get_name()
fish.test()

dog1 = Dog('Bandit')
dog1.sound()
dog1.test()
# dog1.get_name()
# dog1.show()

# horse1 = Horse('Dean')
# horse1.sound()
# horse1.get_name()

bird1 = Bird('James', 'Red')
bird1.get_color()
bird1.test()
# bird1.sound()
# bird1.get_name()
    





