from sda_exercises_oop_1 import movable
class Cat:
    def __init__(self, name: str, sound="miau", eaten_mouse=0):
        self.name = name
        self.sound = sound
        self.eaten_mouse = eaten_mouse

    def make_sound(self) -> str:
        return f'Name is {self.name} sound: {self.sound}'

    def eat_mouse(self) -> int:
        self.eaten_mouse += 1
        print(f'Zjadłem {self.eaten_mouse} myszy')
        return self.eaten_mouse

    def move(Movable):