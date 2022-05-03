# Model View Controller

Jest to wzorzec służący do organizacji struktury aplikacji. 
Ma trzy główne składowe:
- Model - reprezentacja danych(np. Modele frameworku 'mongoose')
- View - interfejs użytkownika (np. szablony 'express-handlebars')
- Controler - logika aplikacji

Najczęściej pliki odpowiadające za dane składowe przechowuje się w folderach pochodzących od ich nazw. Przykładowa struktura aplikacji wyglądać może następująco:
```
📦Example_MVC_App
 ┣ 📂controllers   <<<
 ┣ 📂models        <<<
 ┣ 📂node_modules
 ┣ 📂views         <<<
 ┣ 📜.gitignore
 ┣ 📜index.js
 ┣ 📜package-lock.json
 ┗ 📜package.json
 ```

## Uruchamianie serwera w trybie developerskim(restartowanie serwera przy zmianach w plikach)

Zainstaluj pakiet nodemon
```ComandPrompt
npm install nodemon
```

Aby uruchomić serwer wpisz w konsoli:
```comandprompt
nodemon
```

`nodemon` w pliku `package.json` wyszuka wartość pola `"main"` i uruchomi wskazany plik.

## Tworzenie struktury aplikacji i konfiguracja
![image](https://user-images.githubusercontent.com/37069490/166559869-271bcff8-1bb4-452b-a30a-944ca74eeb23.png)

### 1. Utwórz folder np. `example-app`.
<details>
 <p>
<img src="https://user-images.githubusercontent.com/37069490/166429976-fa5e6130-2750-4c6a-bda5-b4ccaa6a152e.png" alt="img"/>
 </p>
</details>

### 2. Zainicjalizuj projekt node.
```
npm init
```

<details>

Po wpisaniu komendy w konsoli należy uzupełnić podstawowe informacje na temat aplikacji (opis, autor itp.). Przejście konfiguracji utworzy plik `package.json` w folderze aplikacji.

<img src="https://user-images.githubusercontent.com/37069490/166431404-8e2b141b-9d54-4236-87cc-9c583e0326a9.png" alt="img"/>

</details>

### 3. Zainstaluj niezbędne pakiety.
```
npm install express
```
```
npm install express-handlebars
```
```
npm install express-session
```
```
npm install mongoose
```
```
npm install nodemon
```
```
npm install body-parser
```
[`express`](https://expressjs.com/) - framework do tworzenia aplikacji internetowych oraz REST API w Node.js
 
[`express-handlebars`](https://handlebarsjs.com/guide/#what-is-handlebars) - silnik szablonów ułatwiający dunamiczne generowanie treści dla użytkownika aplikacji.
 
[`express-session`](http://expressjs.com/en/resources/middleware/session.html) - warstwa pośrednicząca umożliwia nadzorowanie w frameworku express stanu sesji połączonego użytkownika.

[`body-parser`](http://expressjs.com/en/resources/middleware/body-parser.html) - warstwa pośrednicząca umożliwia odczytanie wiadomości przesyłanej przez protokół HTTP metodą POST.

[`mongoose`](https://mongoosejs.com/) - bliblioteka ułatwiająca pracę z bazą danych MongoDB. Ułatwia połączenie z bazą danych, wymianę informacji wraz z nadzorem poprawności (klasy modelowe).
 
[`nodemon`](https://nodemon.io/) - Blibloteka ułatwiająca tworzenie aplikacji. Restartuje serwer aplikacji przy zapisaniu pliku.
 
<details>
<img src="https://user-images.githubusercontent.com/37069490/166433438-af9fc029-c02d-4fb0-bdfb-287a357d89f4.png"/>
</details>

### 4. Utwórz plik `config.json` i zapisz w nim dane dostępowe do bazy danych itp..

<details>
 
<img src="https://user-images.githubusercontent.com/37069490/166440247-488c1f7b-d3eb-47db-b7d6-f05c3fe17fe3.png" alt="img"/>

</details>

### 5. Utwórz foldery przechowujące:
 - Modele
 - Widoki
 - Kontrolery
 - Pliki statyczne
 - Routing

 <details>
 
📂controllers - Folder przechowujący skrypty odpowiedzialne za logikę aplikacji.

📂models - Folder na klasy modelowe np. stworzone w bibliotece 'mongoose'

📂public - Folder na pliki statyczne zawierający podpoldery:
 ┣ 📂css
 ┣ 📂font
 ┣ 📂js
 ┗ 📂img

📂routes - Folder na skrypty odpowiedzialne za trasowanie żądań HTTP (przekazywanie żądań do odpowiedniego kontrolera)

📂views - Folder na szablony np. biblioteki 'express-handlebars' wraz z podfolderami:
 ┣ 📂layouts - Folder na szablony zawierajace układ strony
 ┗ 📂partials - Folder na elementy strony np. pasek nawigacji
 
<img src="https://user-images.githubusercontent.com/37069490/166444177-f02a241e-da53-4041-ae23-9b5e6e39d5a2.png" alt ="img"/>

</details>

### 6. Utworzenie skryptu uruchamiającego serwer oraz konfiguracja frameworków.
```javascript
// Import konfiguracji z pliku config.json. Plik powinien automatycznie sparsować się na obiekt JS
const config = require('./config.json');

// Import frameworku 'express'
const express = require('express');
const app = express();
const PORT = config.PORT;

// Import biblioteki do obsługi sesji
const session = require('express-session');
app.use(session({
    secret: 'secret',
    saveUninitialized: true,
    resave: true
}));

// Import biblioteki mongoose oraz konfiguracja
const mongoose = require('mongoose');
mongoose.connect(config.Mongo_URL, { useUnifiedTopology: true, useNewUrlParser: true })
    .then(() => console.log(`Połączono z bazą danych : ${config.Mongo_URL}`))
    .catch(err => console.log(`Błąd połączenia. Sprawdź czy serwer działa poprawnie oraz link do bazy jest prawidłowy. ${config.Mongo_URL}`));

// Pokazujemy frameworkowi express gdzie znajduje się plik z routingiem (metody obsługujące żądania)
app.use('/', require('./routes/routes'));

//  Import silnika szablonów 'express-handlebars' i jego konfiguracja.
const handlebars = require('express-handlebars')
app.engine('hbs', handlebars.engine({
    // Szablon główny. W szablonie występuje znacnzik {{{body}}} - do tego znacnzika będzie 'wklejana' zawartość innych szablonów 
    defaultLayout: 'main',
    // Zdefiniowanie rozszerzenia plików szablonów. Najszęściej .hbs lub .handlebars
    extname: '.hbs'
}));
app.set('view engine', 'hbs');

// Pokazanie frameworkowi express gdzie znajdują się pliki statyczne (css, zdjęcia na stronie głównej itp.)
app.use(express.static('public'))

// Metoda use jest wykonywana jeśli żadne z zaprogramowanych żądań nie pasuje
app.use((req, res) => {
    // Ustawienie typu wiadomości zdefiniowany w nagłówku HTTP
    res.type('text/plain')
    // Ustawienie statusu odpowiedzi HTTP
    res.status(404)
    // Ustawienie Treści wiadomości HTTP
    res.send('404 - Not Found')
})

// Metoda która jest wywołana gdy wystąpi błąd serwera
app.use((err, req, res, next) => {
    console.error(err.message)
    res.type('text/plain')
    res.status(500)
    res.send(`500 - Server Error`)
})

// Wywołanie słuchacza żądań HTTP
app.listen(PORT, console.log(`Server uruchomiony na porcie: ${PORT}`))
```
<details>
 
Należy utworzyć plik `index.js` lub inny wskazany w pliku `package.json` w polu "main". Przykładowa zawartość pliku znajduje się powyżej.

<img src="https://user-images.githubusercontent.com/37069490/166448293-6db05d2d-92be-4e72-863c-babf736b8e8b.png" alt="..."/>

</details>

### 7. Utworznie pliku z routingiem i konfiguracja serwera.
```javascript
const express = require('express');
const userController = require('../controllers/userController');
const router = express.Router();

// Import pakietu 'body-parser'. Kiedyś pakiet był częścią frameworku https://www.npmjs.com/package/body-parser
var bodyParser = require('body-parser')
// application/json parser - będziemy używać do przetwarzania JSON
var jsonParser = bodyParser.json()
// application/x-www-form-urlencoded parser - będziemy używać do przetwarzania danych z formularzy HTML
var urlencodedParser = bodyParser.urlencoded({ extended: false })

router.get('/', function (req, res) {
    res.render('index')
});

// Zwrócenie widoku (gdy otrzymamy żądanie HTTP metodą GET)
router.get('/register', userController.registerView);
// Obsługa formularza (gdy otrzymamy żądanie HTTP metodą POST)
router.post('/register', urlencodedParser, userController.registerUser);

router.get('/users', userController.usersView)

router.get('/login', userController.loginView);
router.post('/login',urlencodedParser, userController.login);

router.delete('/delete/:id', userController.delete)

module.exports = router;
```
<details>

Należy utworzyć plik `routes.js` w folderze `routes`.
 
Dzięki `app.use('/', require('./routes/routes'));` w pliku `index.js` serwer będzie wiedział gdzie szukać pliku z trasowaniem.
 
<img src="https://user-images.githubusercontent.com/37069490/166449422-711d6a68-b60a-4ca0-b516-51ec86507a21.png" alt="..."/>
 
</details>

### 8. Dodanie plików statycznych których zamierzamy używać w aplikacji

<details>

Należy pobrać bootstrap z linku - https://github.com/twbs/bootstrap/releases/download/v5.1.3/bootstrap-5.1.3-dist.zip
 
W pobranym archiwum znajdują się dwa foldery `css` oraz `js`. Należy je wypakować do katalogu `public` projektu.
 
<img src="https://user-images.githubusercontent.com/37069490/166453452-67b17cf0-ca6f-4934-991a-fc4465b62bbd.png" alt="..."/>

Oraz ikony bootstrap - https://github.com/twbs/icons/archive/v1.8.1.zip
 
W pobranym archiwum należy odnaleźć folder `font` i wypakować jego zawartość do katalogu `font` w projekcie.
 
<img src="https://user-images.githubusercontent.com/37069490/166453811-e2c23ba2-d45e-4e2f-aa07-f011b03d91ee.png" alt="..."/>
 
<img src="https://user-images.githubusercontent.com/37069490/166454828-91bcc555-aed2-4e44-987f-e4c6211e51c0.png" alt="..."/>

</details>

### 9. Utworzenie klas Modelowych.
```Javascript
// Importowanie biblioteki 'mongoose'
const mongoose = require("mongoose");
// Utworzenie schematu danych. Informacje na temat tworzenia znajdziesz w dokumentacji https://mongoosejs.com/docs/guide.html
const UserSchema = new mongoose.Schema({
  // JSON będzie zawierał pole login. 
  login: {
    //   Wartość pola login powinna być typu String
    type: String,
    // Login jest wymagany. Jeśli będziemy próbować zapisać obiekt do bazy danych bez loginu powinien wystąpić wyjątek.
    required: true,
    // Login też powinien być unikatowy. Przy próbie zapisania tego samego loginu powinien pojawić się wyjątek.
    unique: true
  },
  password: {
    type: String,
    required: true
  },
  date: {
    type: Date,
    default: Date.now
  }
});
// Dokumenty na podstawie schematu będą zapisywane w kolekcji "User"(1 parametr funkcji)
const User = mongoose.model("User", UserSchema);
// export powoduje że importtując plik User.js w innych plikach JavaScript obiekt User będzie widoczny.
module.exports = User;
```
<details>

Należy utworzyć plik `User.js` w katalogu `models`. Model tworzymy na podstawie dokumentacji: https://mongoosejs.com/docs/guide.html

</details>

### 10. Utworzenie kontrolera.
```javascript
const User = require("../models/User");

// Utworzenie klasy kontrolera
class UserController {
    constructor() { }

    // Funkcje statyczne będą dostępne bez tworzenia obiektu i takie same pomiędzy obiektami.
    static registerView = (req, res) => {
        res.render("register");
    }

    static loginView = (req, res) => {
        res.render("login");
    }

    static async registerUser(req, res) {
        // Odczytanie danych z formularza i utworzenie obiektu na podstawie modelu User.js
        let data = req.body
        console.log(`Dane odczytane z formularza: ${JSON.stringify(data)}`)
        // Tworzymy obiekt na podstawie naszego modelu. Jeśli jest prosty framework odszuka po kluczach odpowiednie pola.
        let user = new User(data);
        console.log(`Utworzony obiekt: ${JSON.stringify(user)}`)
        // Zapisanie obiektu w bazie danych.
        try {
            // Funkcja save() jest asynchroniczna - zwraca obietnicę że się wykona. Jeśli chcemy poczekać aż wykona się do końca należy użyć instrukcji await
            await user.save()
        } catch (err) {
            //  Jeśli komunikat błędu zaczyna się od "E11000 duplicate key error"
            if (err.message.startsWith("E11000 duplicate key error")) {
                // wyrenderuj widok register i przekaż komunikat błędu do szablonu
                res.render('register', { error: "Login is taken" });
                return
            } else {
                console.log("Błąd zapisu użytkownika: " + err.message)
            }
        }
        // Przekierowanie użytkownika do 'jakiejś trasy' np. wyświetlającej użytkowników
        res.redirect('/');
    }

    static async usersView(req, res) {
        // Pobranie z bazy Kolekcji Użytkowników
        let data = await User.find().lean()
        // Przekazanie danych do widoku
        console.log("Czy zalogowano:" + req.session.loggedin)
        res.render('usersTable', { data: data, islogged: req.session.loggedin })
    }

    static async login(req, res) {
        let data = req.body
        console.log(data)
        let user = await User.find({ login: data.login }).lean()
        console.log(user)
        // Jeśli znaleziono jednego użytkownika o tym lognie
        if (user.length == 1) {
            // Ustawienie zmiennych sesyjnych
            req.session.loggedin = true;
            req.session.login = user.login;
            res.redirect('/users')
            // W przeciwnym wypadku przenosimy użytkownika do rejestracji
        } else {
            res.redirect('/register')
        }
    }

    static async delete(req, res) {
        console.log(req.session.loggedin)
        if (req.session.loggedin) {
            // Odczyt named parameter
            let id = req.params.id
            // Usunięcie użytkownika o danym id (https://mongoosejs.com/docs/api/model.html)
            await User.deleteOne({ _id: id })
            res.redirect('/users')
        } else {
            // res.redirect('/login')
        }
    }
}

module.exports = UserController;
```
<details>

Należy utworzyć plik `UserController` w folderze `controllers`. Klasa kontrollera powinna zawierać funkcje obsługujące odpowiednie trasy zdefiniowane w aplikacji.

<img src="https://user-images.githubusercontent.com/37069490/166460948-bd5ac62e-e4c5-41c3-82bd-cfcfa49d75b3.png" alt="..."/>
 
</details>

### 11. Utworzenie widoków.

1 Szablon strony.

```handlebars
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

    <!-- Bootstrap Icons -->
    <link href="/font/bootstrap-icons.css" rel="stylesheet">

    <title>MVC - Example</title>
  </head>
  <body>
    <!-- W ten sposób importujemy szablony z folderu views/partials. Poniżej został importowany plik navbar.hbs -->
    {{>navbar}}
    <!-- W miejsce 'body' będą wstawiane treści np. z pliku views/index.hbs -->
    {{{body}}}
    {{>footer}}

    <!-- Bootstrap Bundle with Popper -->
    <script src="/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
  </body>
</html>
```

2 Utworzenie navigacji.

```handlebars
<nav class="navbar navbar-expand-lg navbar-light bg-light border-bottom">
    <div class="container">
        <a class="navbar-brand" href="#">MVC-Example</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                    <a class="nav-link" aria-current="page" href="/users">Users</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" aria-current="page" href="/login">Login</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/register">Register</a>
                </li>
            </ul>
        </div>
    </div>
</nav>
```

3 Utworzenie stopki strony.

```handlebars
<footer class="footer border-top fixed-bottom">
      <div class="container d-flex flex-wrap justify-content-between align-items-center py-3 my-4">
        <div class="col-md-4 d-flex align-items-center">
            <span class="text-muted">© 2021 Company, Inc</span>
        </div>

        <ul class="nav col-md-4 justify-content-end list-unstyled d-flex">
            <li class="ms-3"><a class="text-muted" href="https://www.twitter.com/"><i class=" bi-twitter"></i></a></li>
            <li class="ms-3"><a class="text-muted" href="https://www.instagram.com/"><i class=" bi-instagram"></i></a></li>
            <li class="ms-3"><a class="text-muted" href="https://www.facebook.com/"><i class=" bi-facebook"></i></a></li>
        </ul>
      </div>
</footer>
```

4 Utworzenie widoku strony głównej

```handlebars
<main class="container">
    <h1>Hello world!</h1>
</main>
```

5 Utworzenie widoku logowania

```handlebars
<div class="container mt-2">
    <div class="col-md-4 offset-md-4">
        {{!-- Routing do funkcji obsługującej logowanie --}}
        <form action="/login" method="POST">
            <div class="mb-3 needs-validation">
                <label for="exampleInputLogin1" class="form-label">Login</label>
                                                    {{!-- Jeśli jest błąd dodajemy klasę in-valid --}}
                <input type="text" class="form-control {{#if error}}is-invalid{{/if}}" name="login" id="exampleInputLogin1"
                    required>
                {{!-- Jeśli do szablonu przekażemy zmienną error silnik wyrenderuje komunikat z błędem --}}
                {{#if error}}
                <div class="invalid-feedback">
                    {{error}}
                </div>
                {{/if}}
            </div>
            <div class="mb-3">
                <label for="exampleInputPassword1" class="form-label">Password</label>
                <input type="password" class="form-control is-valid" name="password" id="exampleInputPassword1"
                    required>
            </div>
            <button type="submit" class="btn btn-primary">Login</button>
        </form>
    </div>
</div>
```

6 Utworzenie widoku rejestracji

```handlebars
<div class="container mt-2">
    <div class="col-md-4 offset-md-4">
        {{!-- Routing do funkcji obsługującej rejestracje --}}
        <form action="/register" method="POST">
            <div class="mb-3 needs-validation">
                <label for="exampleInputLogin1" class="form-label">Login</label>
                                                    {{!-- Jeśli jest błąd dodajemy klasę in-valid --}}
                <input type="text" class="form-control {{#if error}}is-invalid{{/if}}" name="login" id="exampleInputLogin1"
                    required>
                {{#if error}}
                <div class="invalid-feedback">
                    {{error}}
                </div>
                {{/if}}
            </div>
            <div class="mb-3">
                <label for="exampleInputPassword1" class="form-label">Password</label>
                <input type="password" class="form-control is-valid" name="password" id="exampleInputPassword1"
                    required>
            </div>
            <button type="submit" class="btn btn-success">Sign in</button>
        </form>
    </div>
</div>
```

7 Utworzenie widoku wyświetlającego użytkowników

```handlebars
<main class="container">
    {{!-- Warunek if data zawiera jakieś dane --}}
    {{#if data}}
    <table class="table">
        <thead>
            <tr>
                <th scope="col">Login</th>
                <th scope="col">Password</th>
                {{!-- Jeśli zalogowany --}}
                {{#if islogged}}
                <th scope="col">Action</th>
                {{/if}}
            </tr>
        </thead>
        <tbody>
            {{!-- Pętla iterująca po obiektach w tablicy data (obiekty klasy User) --}}
            {{#each data as |user|}}
            <tr>
                {{!-- 'this' wskazuje na obiekt w obecnej iteracji --}}
                <td>{{this.login}}</td>
                <td>{{this.password}}</td>
                {{!-- ../ literał służy do przechodzenia o kontekst wyżej(wyjście z pętli i dostęp do zmiennej islogged) --}}
                {{#if ../islogged}}
                <td><button onclick="removeUser()" id="{{this._id}}" class="btn btn-danger">Delete</a></td>
                {{/if}}
            </tr>
            {{/each}}
        </tbody>
    </table>
    {{else}}
    <h1>No registered users</h1>
    <a href="/register">Register first user.</a>
    {{/if}}

    {{!-- Skrypt wysyłający HTTP request metodą delete po wciśniećiu przycisku --}}
    <script>
        function removeUser(){
            // https://developer.mozilla.org/pl/docs/Web/API/Event
            console.log(event.currentTarget.id)
            let xhr = new XMLHttpRequest()
            // Routing który usuwa użytkowników
            const url=`/delete/${event.currentTarget.id}`;
            // Wysłanie żądania metodą 'DELETE'
            xhr.open("DELETE", url);
            // Obsługa zdarzenia po otrzymaniu odpowiedzi serwera
            xhr.onload = function(){
                console.log(xhr.status)
                // Odświeżenie strony
                window.location.reload();
            }
            xhr.send();
        }
    </script>
</main>
```

<details>
 
<img src="https://user-images.githubusercontent.com/37069490/166461276-62c8f1d9-4c9c-4ea5-a858-035a2ce591a4.png" alt="..."/>
 
</details>

***
1. Utwórz model reprezentujący post użytkownika.
    - autor postu (id użytkownika)
    - treść postu
    - data wpisu
    - temat
    - komentarze
2. Utwórz routing umożliwiający operacje CRUD dla postów.
    - użytkownik zalogowny może dodać post
    - użytkownik zalogowany może napisać komentarz
    - użytkonik będący autorem posta może go usunąć
    - użytkownik zalogowany może komentować post
    - użytkownik niezalogowany może przeglądać posty
3. Utwórz odpowiednie widoki
    - Formularz edycji/tworzenia posta
    - Widok postu i jego komentarzy
    - Widok wyświetlający wszystkie posty w uproszcozny sposób np. same teamty
4. Utwórz kontrolery odpowiedzialny za komunikację pomiędzy użytkownikiem a serwerem w zakresie operacji CRUD i wyświetlania postów. Kontroler powinien sprawdzać poprawność danych przed zapisaniem ich do bazy oraz czy użytkownicy podiadają wymagane uprawnienia.
