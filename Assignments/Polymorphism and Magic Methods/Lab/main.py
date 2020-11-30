class Cat:
    def sound(self):
        print('Meow')


def makeSound(animalType):
    animalType.sound()


cat = Cat()
makeSound(cat)
