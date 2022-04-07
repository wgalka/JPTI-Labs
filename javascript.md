#### Języki Programowania i Technologie Internetowe (JPiTI) <sub>2021-2022</sub>
# JavaScript
Skrypy Javascript na stronach umieszcza się wewnątrz znacznika `<script></script>`. Znacznik możemy umieścić w sekcji `<head>` lub `<body>`.
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Javascript</title>
    </head>
    <body>
        <script>
            console.log("Hello World!");
            document.write("Hello World!");
        </script>
    </body>
</html>
```
Możliwe jest umieszczanie skryptów w osobnym pliku z rozszerzeniem `js`. Aby wczytać skrypt należy do znacnzika `<script>` dodać atrybut `src=`.
```html
<script src="urldopliku.js"></script>
```

### Deklaracja zmiennych
```javascript
let var1 = "ABC";
var var2 = 123;
const var3 = 3.14;
```
### Wypisywanie informacji w konsoli i w treści strony podczas wczytywania dokumentu
```javascript
 let var4 = "Hello World!";

console.log(var1);
document.write(var4);
```


___
1. Utwórz plik about_js.html. Utwórz nagłówek pierwszego stopnia z zawartością JavaScript. W paragrafach pod nagłowkiem umieść informacje:
    - Co to JavaScript?
    - Do czego można wykorzystać Javascript?
    - Czym różni się deklarowanie zmiennych za pomocą `let` `var` `const`?
    - Wymień podstawowe typy danych języka JavaScript.
    - 
2. W pliku about_js.html pod paragrafami utwórz nagłówek drugiego poziomu zawierający napis Zadanie 2. Pod nagłówkiem utwórz skrypt który wypisze w treści napis "Hello World!". Kolejne rozwiązania zadań twórz w podobny sposób.
3. Utwórz zmienną `sentence` zawierającą napis "pies kot kura kaczka krowa koń". Wypisz zawartość zmiennej w treści strony.
4. Utwórz stałą `e` zawierającą przybliżoną wartość liczby eulera.
5. Utwórz zmienną var1 przechowującą wartość 1000 oraz zmienną var2 przechowującą wartość "1000". Porównaj zmienna operatorem == oraz === wynik porównania wypisz w treści strony.
6. Utwórz pętlę która wypisze w treści strony kolejne potęgi liczby 2 oddzielone `/` do wartości 4085.
7. Utwórz tablicę dwuwymiarową przechowującą następujące dane znajdujące się w poniższej tabeli. Wypisz dane w konsoli Javascript. Następnie wypisz w treści strony na podstawie danych zdania "Temperatura w [nazwa pomieszczenia] wynosi [temperatura] &ordm; C"

| 1 | Kuchnia | 24 |
|---|---------|----|
| 2 | Salon   | 20 |
| 3 | Pokój 1 | 27 |

8. Utwórz funkcję `ctf()` która zamienia stopnie celecjusz na stopnie farenheita. °F = (°C × 9/5) + 32 Wykorzystaj funkcję by zamienić temperaturę w tablicy z poprzedniego zadania. Nastepnie wypisz w treści strony na podstawie danych zdania "Temperatura w [nazwa pomieszczenia] wynosi [temperatura] &ordm; F"
9. Dodaj wiersz do tablicy z zadania 7 i sprawdź czy po modyfikacji skrypty w zadaniu 7 oraz 8 nadal działają poprawnie.
10. Utwórz klasę reprezentującą wybrany element układu elektronicznego np. rezystor, kondensator, diodę.... Przetestuj działanie składowych klasy.
11. Utwórz obiekt JSON przechowujący informacje o składowych atmosferycznych oraz innych danych w danym pomieszczeniu. Np. informacja o temperaturze, ciśśnieniu, czy światło jest zapalone, czas, itp.
12. Utwórz `<div id='zad12'></div>`. Wykorzystaj javascript by zmienić zawartość znacznika div na "Hello World!". Zmień wielkość oraz kolor napisu wykorzystując javascript.
13. Utwórz formularz w którym użytkownik będzie miał możliwość wpisania wagi w kilogramach oraz wzrostu w metrach. Stwórz skrypt który odczyta dane z formularza po wciśnięciu przysiku, obliczy wartość BMI i ustawi różne kolory tła w zależności o wynika.


