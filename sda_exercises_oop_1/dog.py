class Dog:
    def __init__(self, name: str, sound="hau"):
        self.name = name
        self.sound = sound

    def make_sound(self) -> str:
        return f'Dog name is {self.name} sound: {self.sound}'
