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
### Typy danych
```javascript
var var5;
console.log(var5, typeof (var5));
var5 = "ABC";
console.log(var5, typeof (var5));
var5 = 123;
console.log(var5, typeof (var5));
var5 = 1.99;
console.log(var5, typeof (var5));
var5 = true;
console.log(var5, typeof (var5));
var5 = [1, 2, 3, 4];
console.log(var5, typeof (var5));
var5 = { 'name': 'Jan', 'forname': 'Kowalski' };
console.log(var5, typeof (var5));
var5 = new Set();
console.log(var5, typeof (var5));
var5 = null;
console.log(var5, typeof (var5));
var5 = function () {return "Hello"}
console.log(var5, typeof (var5));
```
### Operatory porównania
```javascript
let x = 12;
let y = '12';

console.log(`${x} == ${y}`, x == y);
console.log(`${x} != ${y}`, x != y);
console.log(`${x} > ${y}`, x > y);
console.log(`${x} >= ${y}`, x >= y);
console.log(`${x} < ${y}`, x < y);
console.log(`${x} <= ${y}`, x <= y);
console.log(`${x} === ${y}`, x === y);
console.log(`${x} !== ${y}`, x !== y);
```

### Operatory logiczne
```javascript
let t = true;
let f = false;

console.log(`!${t}`, !t);
console.log(`${t} || ${f}`, t || f);
console.log(`${t} == ${f}`, t && f);
```
### Operator trujargumentowy
Operator trujargumentowy to skrócona wersja zapisu instrukcji if ... else
```javascript
let a = 10

a > 5? console.log("a > 5"):  console.log("a <= 5");
```

### Operatory arytmetyczne
```javascript
let num1 = 10;
let num2 = 2;

console.log(`${num1} + ${num2} = `,num1 + num2);
console.log(`${num1} - ${num2} = `,num1 - num2);
console.log(`${num1} * ${num2} = `,num1 * num2);
console.log(`${num1} / ${num2} = `,num1 / num2);
console.log(`${num1} ** ${num2} = `,num1 ** num2);
console.log(`${num1} % ${num2} = `,num1 % num2);
```

### Tablice
```javascript
let tab = ['apple', 'banana', ["smoczy", "owoc"]];

console.log(tab[0]);
console.log(tab[2]);

console.log(tab[2][1]);
```

### if ... else
```javascript
const input = prompt("Wpisz wartość:");

if(input > 10){
    console.log("input > 10")
} else{
    console.log("input <= 10")
}
```

### for
```javascript
for(let i = 0; i<10;i++){
    console.log('Iteracja:', i)
}
```
### for in
```javascript
let words = ["apple", 'banana', 'kiwi', 'mango']
for (let i in words) {
    console.log('Iteracja:', i)
}
```
### while
```javascript
while (i!= 'q'){
    var i = prompt("Wpisz q by okno przestało się pojawiać:");
}
```
### do while
```javascript
do{
    var i = prompt("Wpisz z by okno przestało się pojawiać:");
} while(i != 'z')
```

### funckje
```javascript
function multiplication(a, b) {
    return a * b;
}

// Funkcja anonimowa to funkcja bez identyfikatora w postaci nazwy
let multiplication = function (a, b) {
    return a * b;
}

// Notacja strzałkowa (Arrow function expression)
let multiplication = (a,b)=> {return a*b};
```
### klasy
```javascript
class Bulb{
    // pole prywatne
    #manufacturer;
    #light = false;
    constructor(lumens, power, manufacturer){
        this.lumens = lumens;
        this.power = power;
        this.#manufacturer = manufacturer;
    }

    // getter
    get getmanufacturer(){
        return this.#manufacturer;
    }

    // setter
    set setManufacturer(name){
        this.#manufacturer = name;
    }

    // Metoda
    isOn(){
        return this.#light;
    }

    powerOn(){
        this.#light = true;
    }
}


// Utworzenie obiektu danej klasy
let obj = new Bulb(1607,230,"Phil");

// Wywołanie funkcji na obiekcie
obj.powerOn();
```
Więcej na temat klas: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes

### Dostęp i modyfikacja elementów DOM
```javascript
<h2 id="test">Dostęp i modyfikacja</h2>
<script>
    let elementH2 = document.getElementById("test");
</script>
```
#### Wypisanie wartości obiektu DOM
```javascript
console.log(elementH2.innerHTML);
```
Wybrane metody wyszukujące pożądane obiekty: `getElementById()` `getElementsByClassName()` `getElementsByTagName()` `getElementsByName()`
#### Modyfikacja zawartości znacnzika
```javascript
elementH2.innerHTML = "Zmodyfikowano zawartość"
```
#### Modyfikacja styli elementu
```javascript
elementH2.style.color = "#FF0000";
```


### Obsługa zdarzeń
```html
<button id="btn">Przycisk</button>
<script>
    var button = document.getElementById('btn');
    function myFunction(){
        alert("Kliknięto przycisk");
    }
    button.addEventListener('click',myFunction);
</script>
```
Więcej na temat metody `addEventListener`: https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener
___
1. Utwórz plik about_js.html. Utwórz nagłówek pierwszego stopnia z zawartością JavaScript. W paragrafach pod nagłowkiem umieść informacje:
    - Co to JavaScript?
    - Do czego można wykorzystać Javascript?
    - Czym różni się deklarowanie zmiennych za pomocą `let` `var` `const`?
    - Wymień podstawowe typy danych języka JavaScript.
    - Czym różni się instrukcja break od continue?
    - Jaka jest różnica pomiędzy `==` a `===` ?
    - Co to funkcja anonimowa?
2. W pliku about_js.html pod paragrafami utwórz nagłówek drugiego poziomu zawierający napis Zadanie 2. Pod nagłówkiem utwórz skrypt który wypisze w treści napis "Hello World!". Kolejne rozwiązania zadań twórz w podobny sposób.
3. Utwórz zmienną `sentence` zawierającą napis "pies kot kura kaczka krowa koń". Wypisz zawartość zmiennej w treści strony.
4. Utwórz stałą `e` zawierającą przybliżoną wartość liczby eulera.
5. Utwórz zmienną var1 przechowującą wartość 1000 oraz zmienną var2 przechowującą wartość "1000". Porównaj zmienna operatorem == oraz === wynik porównania wypisz w treści strony.
6. Utwórz pętlę która wypisze w treści strony kolejne potęgi liczby 2 oddzielone `/` do wartości 4085.
7. Utwórz tablicę dwuwymiarową przechowującą następujące dane znajdujące się w poniższej tabeli. Wypisz dane w konsoli Javascript. Następnie wypisz w treści strony na podstawie danych zdania "Temperatura w [nazwa pomieszczenia] wynosi [temperatura] &ordm; C"
    <style>
        .custom{
            border: 1px solid rgb(255,255,255,150);
            border-collapse: collapse;
            background-color: black;
        }
        .custom td{
            border: 1px solid rgb(255,255,255,150);
            border-collapse: collapse;
        }
    </style>
    <table class="custom">
    <thead>
    </thead>
    <tbody>
    <tr>
        <td> 1 </td>
        <td> Kuchnia </td>
        <td> 24 </td>
    </tr>
    <tr>
        <td> 2 </td>
        <td> Salon </td>
        <td> 20 </td>
    </tr>
    <tr>
        <td> 3 </td>
        <td> Pokój 1 </td>
        <td> 27 </td>
    </tr>
    </tbody>
    </table>
8. Utwórz funkcję `ctf()` która zamienia stopnie celecjusz na stopnie farenheita. °F = (°C × 9/5) + 32 Wykorzystaj funkcję by zamienić temperaturę w tablicy z poprzedniego zadania. Nastepnie wypisz w treści strony na podstawie danych zdania "Temperatura w [nazwa pomieszczenia] wynosi [temperatura] &ordm; F"
9. Dodaj wiersz do tablicy z zadania 7 i sprawdź czy po modyfikacji skrypty w zadaniu 7 oraz 8 nadal działają poprawnie.
10. Utwórz klasę reprezentującą wybrany element układu elektronicznego np. rezystor, kondensator, diodę.... Przetestuj działanie składowych klasy.
11. Utwórz obiekt JSON przechowujący informacje o składowych atmosferycznych oraz innych danych w danym pomieszczeniu. Np. informacja o temperaturze, ciśśnieniu, czy światło jest zapalone, czas, itp.
12. Utwórz `<div id='zad12'></div>`. Wykorzystaj javascript by zmienić zawartość znacznika div na "Hello World!". Zmień wielkość oraz kolor napisu wykorzystując javascript.
13. Utwórz formularz w którym użytkownik będzie miał możliwość wpisania wagi w kilogramach oraz wzrostu w metrach. Stwórz skrypt który odczyta dane z formularza po wciśnięciu przysiku, obliczy wartość BMI i ustawi różne kolory tła w zależności o wyniku.

<img src="https://www.freecodecamp.org/news/content/images/2019/07/panel-1-1.png">
