# Express

- <a href="/json.html" style="color: #FFAA00;text-decoration: none;">Laboratorium _</a> <sub>JSON</sub>
- <a href="/http.html" style="color: #FFAA00;text-decoration: none;">Laboratorium _</a> <sub>HTTP</sub>
- <a href="/mongoDB.html" style="color: #FFAA00;text-decoration: none;">Laboratorium _</a> <sub>MongoDB</sub>
- <a href="/node.html" style="color: #FFAA00;text-decoration: none;">Laboratorium _</a> <sub>Node.js</sub>

## Szkielet aplikacji

### Inicjalizacja projektu node.js
```comandprompt
npm init
```
![image](https://user-images.githubusercontent.com/37069490/165591165-73c8403e-f76f-4bc7-ab6b-4ab8305c2805.png)

### Instalacja frameworku express
```comndprompt
npm install express
```
![image](https://user-images.githubusercontent.com/37069490/165591433-51974081-4b21-4d44-ab86-8f0187d83f9f.png)

### Utworzenie pliku uruchamiajacego aplikację
W omówionym pliku definiowany jest routing aplikacji: https://expressjs.com/en/guide/routing.html
Utwórz plik index.js(nazwa może być dowolna jednak należy pamiętać że przy innej nazwie należy zmienić wartość w pliku package.json) o nastepującej zawartości:
```javascript
const express = require('express')
const app = express()

// Funkcja która ma być wywołana po wpisaniu adresu localhost:8000/
app.get('/', function (req,res){
    res.send("Hello world")
})

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
    res.send('500 - Server Error')
   })

// Port pod którym zostanie uruchomiona aplikacja
const port = 8000
app.listen(port, () => console.log(
    `Example app listening on http://localhost:${port} (CTRL + C to exit)`))
```

### Uruchomienie aplikacji
```comandprompt
node .\index.js
```

## Pliki statyczne
W pliku `index.js` dodaj następującą konfigurację(zwróć uwagę na kolejność funkcji, nieprawidłowa kolejność możę doprowadzić że funkcja nigdy nie zostanie wywołana)
```javascript
// Pliki statyczne (css, zdjęcia na stronie głównej itp.)
// W przykładzie będą znajdować się w folderze public(należy utworzyć taki folder)
app.use(express.static('public'))
```

Pliki statyczne będą przechowywane w folderze public według powyższych ustawień.
```
📦app
 ┣ 📂node_modules
 ┣ 📂public
 ┃ ┗ 📂img
 ┃   ┗ 📜mc1.jpg
 ┣ 📂views
 ┣ 📜index.js
 ┣ 📜package-lock.json
 ┗ 📜package.json
```
Dostęp do pliku `mc1.jpg` można uzyskać pod adresem [localhost:8000/img/mc1.jpg](localhost:8000/img/mc1.jpg). W kodzie HTML link do zdjęcia można będzie definiować w następujący sposób:
```
<img src="/img/mc1.jpg" alt="Jakieś zdjęcie">
```
## Routing
### Metody express odpowiedzialne za przetwarzanie odpowiednich żądań
https://expressjs.com/en/guide/routing.html
Najważniejsze metody obiektu app wywoływane gdy do aplikacji trafi żądanie HTTP ze zdefiniowanymi kolejno metodami: POST, GET, PUT, DELETE
```javascript
app.post('/create',function(){})
app.get('/read',function(){})
app.put('/update',function(){})
app.delete('/delete',function(){})
```
### `named parameters`
Parametry w adresie url których wartości mogą być różne definiujemy za pomocą znaku `:` po czym podajemu nazwę parametru.
```javascript
app.get('/post/:user/:id', function (req, res) { res.send(req.params) })
```
Powyższy routing obsłuży następujące adresy:
```
http://localhost:8000/post/marek/1432
http://localhost:8000/post/darek/ASD
...
```


## Przetwarzanie żądań

### Obiekt Request i Response
https://expressjs.com/en/api.html#req
https://expressjs.com/en/api.html#res
```javascript
app.get('/req_test/:id', function (req, res) {
    let result = ""
    result += req.url + "\n"
    result += req.body +"\n"
    result += req.ip +"\n"
    result += req.method +"\n"
    // Odczytywanie parametru name z `query params`
    result += req.query['name'] +"\n"
    // Odczytanie wartosći `named parameters`
    result += JSON.stringify(req.params) +"\n"

    // Ustawienie ciasteczek odpowiedzi
    res.cookie('mojeCiasteczko','Moja wartość')
    // Ustawienie typu wiadomości zdefiniowany w nagłówku HTTP
    res.type('text/plain')
    // Ustawienie statusu odpowiedzi HTTP
    res.status(200)
    // Ustawienie Treści wiadomości HTTP
    res.send(result)
})
```
Wypróbuj powyższe trasowanie na poniższym adresie:
[http://localhost:8000/req_test/12?name=JAN&surname=Kowalski](http://localhost:8000/req_test/12?name=JAN&surname=Kowalski)

## Silnik szablonów
Dostępne silniki szablonów: https://expressjs.com/en/resources/template-engines.html
### Instalacja silnika handlebars

```comandprompt
npm install express-handlebars
```

### Konfiguracja silnika
W pliku index.js należy dodać następujące instrukcje:
```javascript
// Import silnika szablonów handlebars
// Użycie dekonstruktora - z obiektu została pobrana funkcja engine
const { engine } = require('express-handlebars')

// Ustawienie głownego layoutu oraz rozszerzeń szablonów na .hbs.
app.engine('hbs', engine({
    defaultLayout: 'main',
    extname: '.hbs'
}));
// Ustawienie handlebars jako głownego silnika szablonów aplikacji
app.set('view engine', 'hbs');
```
Widoki będą przechowyane w lokalizacji `views`.
Folder `layouts` zawiera szablon główny.
```
📦app
 ┣ 📂node_modules
 ┣ 📂public
 ┣ 📂views
   ┣ 📂layouts
   ┗ 📜main.hbs
```
### Utworzenie domyślnego szablonu
Utwórz plik `main.hbs` w `views\layouts` z następującą zawartością:
```hbs
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Main view</title>
</head>
<body>
    {{{body}}}
</body>
</html>
```
W miejsce {{{body}}} będzie podstawiana treść z szablonów zawierających konkretne treści.

Utwórz plik `index.hbs` w `views` z nastepującą zawartością:
```
📦app
 ┣ 📂node_modules
 ┣ 📂public
 ┣ 📂views
   ┣ 📜index.hbs
   ┣ 📂layouts
   ┗ 📜main.hbs
```
```hbs
<h1> Strona Główna </h1>
```
### Renderowanie szablonu
W pliku index.js zmodyfikuj główny routing.
```javascript
app.get('/', function (req, res) {
    // Jako argument funkcji render podajemy nazwę szablonu z folderu views
    res.render('index')
})
```

### przekazywanie danych do szablonu i wyświetlanie ich
W pliku index.js dodaj routing.
```javascript
app.get('/greet', function (req, res) {
    // Jako drugi argument funkcji render podajemy obiekt z danymi które chcemy przekazać do szablonu
    let name = "Jan"
    res.render('greet', {name: name})
})
```
Utwórz plik `greet.hbs` w folderze `views`. `{{name}}` zostanie zastapione wartością zmiennej `name` przekazanej do szablonu w kodzie wyżej.
```hbs
<h1>Hello {{name}}!</h1>
```

Jeśli chcemy użyć innego szablonu niż `main.hbs` w obiekcie należy dodać pole `layout`
```javascript
app.get('/greet', function (req, res) {
    // Jako drugi argument funkcji render podajemy obiekt z danymi które chcemy przekazać do szablonu
    let name = "Jan"
    res.render('greet', {name: name, layout: 'my_other_layout' }})
})
```

***

1. Utwórz projekt frameworku Express z plikiem uruchamiającym aplikacje routing.js
2. Skonfiguruj ścieżki do plików statycznych i szablonów.
3. Pobierz framework Bootstrap w wersji 5 i umieść w folderze public. Utwórz `layout` który w sekcji head wczyta pliki potrzebne do korzystania z frameworku. W sekcji body menu składające się z przycisków SHOW, CREATE, EDIT
4. Utwórz routing `/` oraz szablon `index.hbs` zawierający przykładową karuzelę bootstrapa.
5. Utwórz szablon `create.hbd` a w nim formularz z polami:
    - nick (wartość tekstowa)
    - hasło (pole na hasło)
    - kierunek (lista wartości: północ, południe itp.)
    - data (kalendarz)

Dokonaj walidacji formularza na stronie https://validator.w3.org/#validate_by_input Jeśli występują jakieś błędy popraw je.
