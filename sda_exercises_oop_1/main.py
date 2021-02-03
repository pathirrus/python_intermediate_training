from sda_exercises_oop_1.cat import Cat
from sda_exercises_oop_1.dog import Dog


def main():
    cat_object = Cat("Filemon")
    # sound = cat_object.make_sound()
    cat_object2 = Cat("Bonifacy", "miałmiał")
    cat_object3 = Cat("Kitek")
    cat_object4 = Cat("Mruczek", "meow")

    # list_cats = [cat_object, cat_object2, cat_object3, cat_object4]
    # for cat in list_cats:
    #     cat_sound = cat.make_sound()
    #     print(cat_sound)

    cat_object.eat_mouse()
    cat_object.eat_mouse()
    cat_object.eat_mouse()

    print("Teraz bedzie zarl drugi kot")
    cat_object3.eat_mouse()

    dog_object = Dog("Burek", "wowwow")
    dog_object1 = Dog("Ciapek", "wowwow")
    dog_object2 = Dog("Buli", "wowwow")

    print(dog_object.make_sound())

    anima_list = [cat_object4, cat_object, cat_object2, dog_object2, dog_object1]
    for animal in anima_list:
        animal_sound = animal.make_sound()
        print(animal_sound)


if __name__ == "__main__":
    main()
