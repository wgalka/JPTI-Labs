# Komentarz liniowy
'''
Komentarz blokowy
'''

"""Ciąg znaków"""

# Instrukcja print służy do wypisywania łańcychów znaków w konsoli
print('Hello world')

# Instrukcja input przechwytuje tekst wpisany przez użytkownika do konsoli i zapisanie pod wartością x
x = input("Podaj wartość zmiennej:")

# Literały znakowe https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-stringprefix
print(f"""\
Wartość zmiennej podanej przez użytkownika: {x}\
""")
print("Wartość zmiennej podanej przez użytkownika:\t" + str(x))
print("Wartość zmiennej podanej przez użytkownika:\t%s" % x)

# Utworzenie zmiennej przechowującą wartość 3.4
var1 = 3.4
var2 = "Hello World!"
var3 = 'Hello' + 'World'

## INSTRUCKEJ STERUJĄCE
x, y = 0, 1
print(x, y)
print(x < y)
print(x <= y)
print(x > y)
print(x >= y)
print(x == y)
print(x != y)
x, y = True, False
if x or y:
    print('x or y')

if x and x:
    print('x and x')
elif x or y:
    print('x or y')
elif y and y:
    print('y or x')
else:
    print('else')

# Instrukcja match jest dostępna od Python 3.10!
x = input("Match input:")
match int(x):
    case 1:
        print('x = 1')
    case 2:
        print('x = 2')

# break
# continue
# return

## PĘTLE
# W pythonie istnieją dwa rodzaje pętli for i while

for i in range(5):
    print(i)

i = 40
while i < 51:
    print(i)
    i += 1


## FUNKCJE

# Utworzenie funkcji wypisującecj w konsoli Hello World
def my_function():
    print('Hello World')


# Wywoładnie stworzonej funkcji
my_function()


# Funkcja z dwoma parametrami z tym że x jest pozycyjnym argumentem
# y jest argumentem domyślnym(nie musimy podawać jego wartości przy wywołaniu funkcji)
def dzielenie(x, y=2):
    return x / y


# Wywołanie funkcji sum i wypisanie wyniku w konsoli
print("Wynik funkcji dzielenie:", dzielenie(6))
print("Wynik funkcji dzielenie:", dzielenie(6, 4))
print("Wynik funkcji dzielenie:", dzielenie(x=2, y=4))
print("Wynik funkcji dzielenie:", dzielenie(y=2, x=4))


# Funkcja z niewiadomą liczbą parametrów
def suma(*args):
    result = 0
    for arg in args:
        result += arg
    return result


# Wywołanie funkcji z niewiadomą liczbą parametrów
print("Wynik funkcji suma:", suma(1))
print("Wynik funkcji suma:", suma(1, 2, 3))
print("Wynik funkcji suma:", suma(1, 2, 3, 4))


# Funkcja z niewiadomą liczbą nazwanych parametrów oraz zwracająca kilka wartości
def polaczwyrazy(**kwargs):
    retult_values = ''
    for arg in kwargs.values():
        retult_values += arg
    result_keys = ''
    for arg in kwargs.keys():
        result_keys += arg
    return retult_values, result_keys


# Wywołanie funkcji z niewiadomą liczbą nazwanych parametrów
x, y = polaczwyrazy(p="I", y=" ", t="Love", h=" ", o='Python', n='!')
print(x)
print(y)

# Kilka wartości funkcja zwraca za pomocą krotki  https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
d = polaczwyrazy(p="I", y=" ", t="Love", h=" ", o='Python', n='!')
print(d)

## STRUKTURY DANYCH
# TUPLE
krotka = (1, 2, 3, 4)  # tuple()
print(krotka.count(2))
print(krotka.index(2))
print(len(krotka))
print(krotka[2:])
print(krotka[2:4])
print(krotka[-1])

# LIST
lista = [0, 1, 2, 3, 4]  # list()
lista.append(5)
lista.pop()
lista.remove(2)
print('lista:', lista)

# SET
zbior = {1, 2, 3, 'ala'}  # set()
zbior.add(4)
zbior2 = {2, 3, 4}
print(zbior.difference(zbior2))
print(zbior.intersection(zbior2))
print(zbior.union(zbior2))

# DICTIONARY
keys = [chr(i) for i in range(65, 91)]
values = [0 for i in range(len(keys))]
slownik = dict(zip(keys, values))
print(slownik)
print(slownik.get('H'))
slownik['C'] = 5
print(slownik)
slownik = {"jeden": 1, 'dwa': 2, 'trzy': 3, 'cztery': 4}  # dict()

## WYJĄTKI
x = input("Podaj liczbę:")
try:
    print(10 / x)
except Exception as e:
    print(e)
    x = int(x)
finally:
    print(10 / x)
    print('Koniec obliczeń')

Owoce = ['banan', 'pomidor', 'cebula', 'mandarynka', 'granat']

for i in range(len(Owoce)):
    Owoce[i] = Owoce[i].capitalize()

Owoce.sort(reverse=True)

print(Owoce)
print(min(Owoce))
print(max(Owoce))


## KLASY
class Rectangle:
    def __init__(self, a, b):
        self.__a = a
        self.b = b

    def area(self):
        return self.__calculate_area()

    def __calculate_area(self):
        return self.__a * self.b

    def perimeter(self):
        return 2 * self.__a + 2 * self.b

    def __str__(self):
        return "Prostokąt o bokach" + str(
            self.__a) + " " + str(
            self.b) + " ma pole =" + str(
            self.area())


x = Rectangle(3, 4)
print(x)


class Trapeze(Rectangle):
    def __init__(self, a, b, c, d):
        super().__init__(a, b)
        self.c = c
        self.d = d

    def area(self):
        return ""

    def __calculate_h(self):
        pass

    def perimeter(self):
        return self.__a + self.b + self.c + self.d

    def __str__(self):
        return f"Trapez o bokach {self.__a} {self.b} {self.c} {self.d}  ma pole = {self.area()} oraz obwód = {self.perimeter()}"


z = Trapeze(1, 2, 3, 4)
print(z)
