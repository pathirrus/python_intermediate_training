# class CalculatorCisco:
#     def __init__(self, type_calc='cisco'):
#         self.type_calc = type_calc
#
#     def show_calculator_type(self):
#         print(f'calculator type: {self.type_calc}')
#
#     @staticmethod
#     def add_two_numbers(a: int, b: int) -> int:
#         return a + b
#
#
# def main():
#     print(CalculatorCisco.add_two_numbers(2, 3))  # metoda statyczna moze byc na klasie NIE uzywa self
#     # CalculatorCisco.show_calculator_type() # boom
#     calcutor = CalculatorCisco()  # tworzenie obiektu
#     calcutor.show_calculator_type()  # niestatyczna
#     print(calcutor.add_two_numbers(2, 5))  # metoda statyczna byc na obiekcie ale NIE uzywa self


from abc import ABC, abstractmethod


class Osoba(ABC):
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def __str__(self):
        return f"{self.imie} ma {self.wiek} lat"

    @abstractmethod
    def pokaz_finanse(self):
        pass


class Pracownik(Osoba):
    def __init__(self, imie, wiek, stawka, liczba_godzin):
        super().__init__(imie, wiek)
        self.stawka = stawka
        self.liczba_godzin = liczba_godzin

    def pokaz_finanse(self):
        return self.stawka * self.liczba_godzin


class Student(Osoba):
    def __init__(self, imie, wiek, stypendium):
        super().__init__(imie, wiek)
        self.stypendium = stypendium

    def pokaz_finanse(self):
        return self.stypendium


def main():
    pracownik = Pracownik('mike', 29, 20, 168)
    pracownik2 = Pracownik('mike2', 29, 50, 168)
    student = Student('sarah', 29, 505)
    student2 = Student('sarah2', 29, 520)
    person_list = [pracownik, pracownik2, student, student2]
    for person in person_list:
        print(person.pokaz_finanse())


# class PracujacyStudent(Osoba):
#     def __init__(self, imie, wiek, stawka, liczba_godzin, stypendium):
#         super().__init__(imie, wiek)
#         self.stawka = stawka
#         self.liczba_godzin = liczba_godzin
#         self.stypendium = stypendium
#     def pokaz_finanse(self):
#         return self.stawka * self.liczba_godzin + self.stypendium
# def main():
#     pracujacy_student = PracujacyStudent("Monika", 24, 95, 70, 550)
#     print(pracujacy_student.pokaz_finanse())


# def main():
#     pracujacy_student = PracujacyStudent("Monika", 24, 95, 70, 550)
#     pracownik = Pracownik('mike', 29, 20, 168)
#     pracownik2 = Pracownik('mike2', 29, 50, 168)
#     student = Student('sarah', 29, 505)
#     student2 = Student('sarah2', 29, 520)
#     person_list = [pracownik, pracownik2, student, student2, pracujacy_student]
#     for person in person_list:
#         print(person.pokaz_finanse())  # polimorfizm
#
#
# if __name__ == "__main__":
#     main()


# class Student(Osoba):
#     def __init__(self, imie, wiek, stypendium):
#         if self.czy_imie_poprawne(imie):
#             Osoba.__init__(self, imie, wiek)
#             self.stypendium = stypendium
#
#     def pokaz_finanse(self):
#         return self.stypendium
#
#     @classmethod
#     def stworz_ze_stringa(cls, napis):
#         imie, wiek, stypendium = napis.split()
#         wiek, stypendium = int(wiek), float(stypendium)
#         if cls.czy_imie_poprawne(imie):  # Student.czy_imie_poprawne(imie)
#             return cls(imie, wiek, stypendium)  # Student(imie, wiek, stypendium)
#
#     @staticmethod
#     def czy_imie_poprawne(imie):
#         if imie[0].isupper() and len(imie) > 3:
#             return True
#         return False
