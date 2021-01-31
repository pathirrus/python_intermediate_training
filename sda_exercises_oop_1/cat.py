class Cat:
    def __init__(self, name: str, sound="miau"):
        self.name = name
        self.sound = sound

    def make_sound(self) -> str:
        return f'Name is {self.name} sound: {self.sound}'
