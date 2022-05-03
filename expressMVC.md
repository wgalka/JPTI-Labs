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
<p>
 
Należy utworzyć plik `index.js` lub inny wskazany w pliku `package.json` w polu "main". Przykładowa zawartość pliku znajduje się powyżej.

<img src="https://user-images.githubusercontent.com/37069490/166448293-6db05d2d-92be-4e72-863c-babf736b8e8b.png" alt="..."/>
</p>
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
<p>
Należy utworzyć plik `routes.js` w folderze `routes`.
 
Dzięki `app.use('/', require('./routes/routes'));` w pliku `index.js` serwer będzie wiedział gdzie szukać pliku z trasowaniem.
 
<img src="https://user-images.githubusercontent.com/37069490/166449422-711d6a68-b60a-4ca0-b516-51ec86507a21.png" alt="..."/>
</p>
</details>
