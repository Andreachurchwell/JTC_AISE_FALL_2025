# class Pet:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#     def speak(self):
#         return "SOME GENERIC SOUND"
#     def describe(self):
#         return f"{self.name} is a {self.species}"
    
# class Dog(Pet):
#     def speak(self):
#         return 'WOOF!!'
    
# pet = Pet("Louie", "cat")
# print(pet.describe())
# print(pet.speak())

# dog = Dog("Buddy", "dog")
# print(dog.describe())   # from Pet
# print(dog.speak())      # from Dog

# class Cat(Pet):
#     def speak(self):
#         return "Meow!"
    
# cat = Cat("Louie", "cat")
# print(cat.describe())
# print(cat.speak())

# pets = [Dog("Buddy", "dog"), Cat("Louie", "cat")]

# for pet in pets:
#     print(pet.name, "says:", pet.speak())

from abc import ABC, abstractmethod

class Pet(ABC):
    def __init__(self, name, species):
        self.name = name
        self.species = species

    @abstractmethod
    def speak(self):
        pass  # subclasses must fill this in

    def describe(self):
        return f"{self.name} is a {self.species}"
class Cat(Pet):
    def speak(self):
        return "Meow!"
louie = Cat("Louie", "cat")
print(louie.describe())   # inherited from Pet
print(louie.speak())      # defined in Cat 
# p = Pet("Louie", "cat")
