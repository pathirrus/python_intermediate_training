from sda_exercises_oop_1.cat import Cat
from sda_exercises_oop_1.dog import Dog
from sda_exercises_oop_1.animal import Animals


class Vet:

    @staticmethod
    def say_cat_hello(cat: Cat):
        print(f"Witaj {cat.name}")

    @staticmethod
    def say_dog_hello(dog: Dog ):
        print(f"Siemanko {dog.name}")

    @staticmethod
    def say_animal_hi(animal: Animals):
        print(f"Dzień dobry {animal.name}!")