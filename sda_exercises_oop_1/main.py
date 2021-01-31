from sda_exercises_oop_1.cat import Cat


def main():
    cat_object = Cat("Filemon")
    # sound = cat_object.make_sound()
    cat_object2 = Cat("Bonifacy", "miałmiał")
    cat_object3 = Cat("Kitek")
    cat_object4 = Cat("Mruczek", "meow")

    list_cats = [cat_object, cat_object2, cat_object3, cat_object4]
    for cat in list_cats:
        cat_sound = cat.make_sound()
        print(cat_sound)


if __name__ == "__main__":
    main()
