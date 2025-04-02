class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print('eat')

# Animal: Parent, Base
# mammals and fish: Child, Sub


class Mammal(Animal):
    def walk(self):
        print('walk')


class fish(Animal):
    def swim(self):
        print('swim')


print(isinstance(Animal(), Animal))
obj = object()

print(issubclass(Animal, Animal))

# Method Overrides


class Bird(Animal):
    def __init__(self):
        super().__init__()
        print('Bird Constructor')
        self.wings = 2

    def fly(self):
        print('fly')


bird = Bird()
print(bird.age)
print(bird.wings)
