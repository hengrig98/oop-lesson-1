# Lion class in separate file and imported
from common.Lion import Lion

# child class to Lion class(PARENT)...Lion(PARENT) moved to #common folder
class Cat(Lion):

    legs = 6
    eyes = 2

    def __init__(self, name, age, breed) -> None:
        
        self.name = name
        self.age = age
        self.breed = breed

    def meow(self):
        print('Meeeooow')

    # This is a static method, meant to be called directly from the class
    @staticmethod
    def run():
        print('I am running!')


class Turtle(Lion):

    legs = 4
    eyes = 2

    def __init__(self, name, age, breed) -> None:
        
        self.name = name
        self.age = age
        self.breed = breed

    def meow(self):
        print('Meeeooow')

    # This is a static method, meant to be called directly from the class
    @staticmethod
    def run():
        print('I am running!')

    def jump(self):
        print('I cant jump')


vasya = Cat('Vasya', 6, 'short-hair')
Jerry = Turtle('Jerry', 5, 'tort.')

# print(Lion.feeds_offspring)
# print(Cat.feeds_offspring)
# print(vasya.feeds_offspring)
# print(message)
# say_hello()

# Cat.run()
# vasya.run()
# Lion.bio()
# vasya.bio()
# Cat.bio()
Jerry.jump()
vasya.jump()




