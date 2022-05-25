### JPiTI

1. Utwórz plik zadania.html o nastepującej zawartości
```
<!DOCTYPE html>
<html lang="pl">

<head>
    <meta charset="UTF-8">
    <title>Zadania JS</title>
    <style>
        table,
        th,
        td {
            padding: 5px;
            border: 2px solid black;
            border-collapse: collapse;
        }
    </style>
</head>

<body>
    <h1>Javascript</h1>
    <p style="color: red; font-weight:bold;">Zadania pisane kolorem czerwonym są dla chętnych</p>
    <p>Do zadań od 2 do 7 utwórz odpowiednie pliki do rozwiązania zadań.</p>
    <h2>Zadanie 1</h2>
    <p>
        Utwórz osadzony skrypt Javascript wypisujący w treści strony i w konsoli napis "Hello World!".
    </p>
    <script>
    </script>
    <h2>Zadanie 2</h2>
    <p>Utwórz zewnętrzny skrypt w którym:
    <ul>
        <li>utworzysz tablicę dwuwymiarową zawierającą w pierwszym wierszu nagłówki:
            <ul>
                <li>nazwę bryły geometrycznej</li>
                <li>liczbę wierzchołków</li>
                <li>liczbę boków</li>
            </ul>
            a w kolejnych wierszach nazwy figur i wartości (minimum 5 figur)
        </li>
        <li>wykorzystując pętlę wypisz w postaci tabeli zawartośc tablicy w treści strony</li>
        <li>skrypt wypisujący tablicę powinien działać nawet przy dodaniu do tablicy nowych kolumn lub wierszy</li>
        <li style="color: red;">wypisz zawartość tablicy w odwrotnej kolejnosći.</li>
        <li style="color: red;">wypisz zawartość tablicy za pomocą innych pętli</li>
    </ul>
    </p>
    <script src="zadanie2.js"></script>

    <h2>Zadanie 3</h2>
    <p>Utwórz skrypt który po wciśnięciu poniższego przycisku zmieni jego tło na żółte a po ponownym wciśnięciu na
        czerwone</p>
    <p style="color: red;">Modyfikuj style przycisku tak by dawał mniejszy cień po wciśnięciu.</p>
    <button id="btn-zad3">Button</button>
    <script src="zadanie3.js"></script>

    <h2>Zadanie 4</h2>
    <p>Utwórz skrypt który po wciśnięciu przycisku dodaj doda wpisane słowo. A po wciśnięciu przycisku usuń usunie
        element na wybranej pozycji. </p>
    <input id="input-add" type="text"><button id="btn-add">Dodaj</button>
    <input id="input-remove" type="text"><button id="btn-remove">Usuń ten index</button>
    <p id="zad4-output">Miejsce na wyświetlenie zawartosci tablicy</p>
    <script src="zadanie4.js"></script>

    <h2>Zadanie 5</h2>
    <p>Utwórz kalkulator który sprawdzi czy bardziej opłaca kupić się dwie małe pizze czy jedną dużą. W zależności od
        rezultatu zaznacz bardziej opłacalną opcję kolorem zielonym.</p>
    <table>
        <thead>
            <th></th>
            <th>pizza duża</th>
            <th>pizza mała x2</th>
        </thead>
        <tbody>
            <tr>
                <th>średnica</th>
                <td><input id="pizza-xxl-input"></td>
                <td><input id="pizza-s-input"></td>
            </tr>
        </tbody>
    </table>
    <br>
    <button id="calculate">Oblicz</button>
    <script src="zadanie5.js"></script>

    <h2>Zadanie 6</h2>
    <p>przeanalizuj działanie funkcji działających na łańcuchach znaków
        https://www.tutorialstonight.com/js/javascript-string-methods.php#:~:text=JavaScript%20String%20Methods%201%20charAt%20in%20javascript.%20The,4%20endsWith%20in%20javascript.%20...%20More%20items...%20
    </p>
    <script src="zadanie6.js"></script>
    <h2>Zadanie 7</h2>
    <p>Bazując na wiedzy z poprzedniego zadania utwórz skrypt walidujący dane w formularzu i wyświetlający alert
        komunikujący odpowiednie błędy. Login ma spełniac założenia:
    <ul>
        <li>ma zawierać znak @</li>
        <li>po znaku @ ma wystąpić przynajmneij jedna kropka</li>
        <li>nie powinien zawierać polskich znaków</li>
    </ul>
    Hasło na spełniac następujące założenia:
    <ul>
        <li>minimum 8 znaków</li>
        <li>przynajmniej jedna wielka i mała litera</li>
        <li>przynajmniej jedna cyfra</li>
        <li>przynajmniej jeden znak specjalny</li>
    </ul>
    </p>
    <form>
        <label for="uname"><b>User</b></label>
        <input type="text" placeholder="jankowalski@domena.pl" name="uname" required>
        <br>
        <label for="psw"><b>Password</b></label>
        <input type="password" placeholder="hasło" name="psw" required>
        <br>
        <button type="submit">Login</button>
    </form>
    <script src="zadanie7.js"></script>
    <h2>Zadanie 8</h2>
    <p> Na podstawie <a href="https://github.com/wgalka/JPTI-Labs/blob/main/expressMVC.md">Link</a> i zasobów sieci
        internet opisz konfigurację frameworka express pod tym zadaniem</p>
</body>

</html>
```

2. Rozwiąż zadania.
