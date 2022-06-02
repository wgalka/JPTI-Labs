## KLASY
class Triangle:
    '''
    Dokumentacja klasy. Przechowywana jest w prywanym 'Magicznym' polu __doc__

    Istnieje wiele wzorów tworzenia dokumentacji w języku Python. Najpopularniejsze z nich to:
    GOOGLE STYLE Python DOCSTRING https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
    NUMPY STYLE Python DOCSTRING https://numpydoc.readthedocs.io/en/latest/format.html
    '''

    # Prywatne pole statyczne klasy.
    # '__' jest modyfikatorem Private
    # '_' jest modyfikatorem Protected
    # brak znaku oznacza że pole/metoda jest publiczna
    __class_instances = 0

    # Konstruktor
    def __init__(self, a, b, c):
        # Private pole klasy
        self.__a = a
        # Protected pole klasy
        self._b = b
        # Public pole klasy
        self.c = c
        # Aktualizacja statycznego pola przy tworzeniu obiektu
        self.__class_instances += 1

    # Zachowanie przy usuwaniu obiektu danej klasy przez użytkownika lub mechanizm garbage collector
    def __del__(self):
        self.__class_instances -= 1

    ## Gettery i Settery bez których dostęp do pola prywatnego oznaczonego '__' jest niemożliwy poza daną klasą.
    # getter pola a
    @property
    def a(self):
        return self.__a

    # setter pola a
    @a.setter
    def a(self, value):
        if value > 0:
            self.__a = value
            return
        raise ValueError("Długość boku 'a' powinna być większa od 0.")

    @a.deleter
    def a(self):
        print("Nie możesz usunąć tej właściwośći!")

    ## Gettery i Settery bez których dostęp do pola chronionego oznaczonego '_' jest niemożliwy poza klasą oraz klasą dziecziczącą.
    # getter pola b
    @property
    def b(self):
        return self._b

    # setter pola b
    @b.setter
    def b(self, value):
        if value > 0:
            self._b = value
            return
        raise ValueError("Długość boku 'b' powinna być większa od 0.")

    ## Pole c jest publiczne.

    # Publiczna metoda wypisująca ilość instancji danej klasy
    def number_of_instances(self):
        print(f'Stworzono {self.__class_instances} instancji klasy')

    def area(self):
        return self.__calculate_area()

    def __calculate_area(self):
        return self.__a * self._b

    def perimeter(self):
        return 2 * self.__a + 2 * self._b

    # Magic method
    def __str__(self):
        return f"Prostokąt o bokach: {self.__a} {self._b} {self.c}"

# TODO: Jak poniżej
# help(print)
# @staticmethod
# @classmethod

# Wywołanie konstruktora i stworzenie obiektu klasy triangle
x = Triangle(1, 2, 3)
# Wywołując instrukcje print wywoływana jest 'Magiczna' metoda __str__
print(x)
help(Triangle)
# Wypisanie dokumentacji
print("Dokumentacja:", x.__doc__)
print(x.a)
x.a = 3
del x.a
x.c = 4
# del x.c
x.number_of_instances()
print(x)

# class Trapeze(Triangle):
#     def __init__(self, a, b, c, d):
#         super().__init__(a, b)
#         self.c = c
#         self.d = d
#
#     def area(self):
#         return ""
#
#     def __calculate_h(self):
#         pass
#
#     def perimeter(self):
#         return self._a + self.b + self.c + self.d
#
#     def __str__(self):
#         return f"Trapez o bokach {self._a} {self.b} {self.c} {self.d} " \
#                f" ma pole = {self.area()} oraz obwód = {self.perimeter()}"


# z = Trapeze(1, 2, 3, 4)
# print(z)
