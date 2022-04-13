#### Języki Programowania i Technologie Internetowe (JPiTI) <sub>2021-2022</sub>
# Node.JS

## NVM - node version manager https://github.com/nvm-sh/nvm
Node Version Manager jest aplikacją umożliwiającą używanie kilku wersji node.js
Można go pobrać ze strony: https://github.com/coreybutler/nvm-windows/releases/download/1.1.9/nvm-setup.zip

Po zainstalowaniu programu w wielrszu poleceń systemu windows dostepne będzie polecenie nvm:
![image](https://user-images.githubusercontent.com/37069490/163036369-5cd05169-d731-41a9-8c3a-4857384e2665.png)

By zainstalować najnowszą wersję node.js należy użyć polecenia `nvm install latest`
![image](https://user-images.githubusercontent.com/37069490/163039212-9bc72f50-6fb7-4f47-a7db-317377d9a7f8.png)

By zainstlować konkretną wersję node.js należy zamiast latest podać numer wersji np. `nvm install 16.14.2`:
![image](https://user-images.githubusercontent.com/37069490/163039457-a2e19862-73ca-40b7-995b-ae79877ddb41.png)

By wyświetlić listę zainstalowanych wersji użyj polecenia `nvm list`:
![image](https://user-images.githubusercontent.com/37069490/163041498-9980279d-defd-472e-b776-5cbf1ce3c385.png)

By aktywować konkretną wersję node.js należy użyć polecenia `nvm use nr_wersji`:
![image](https://user-images.githubusercontent.com/37069490/163043983-4bed70de-aa46-4934-89c0-559fb7459fe1.png)

Po aktywacji konkretnej wersji aby sprawdzić czy jest ona aktywna użyj polecenia `node`:
![image](https://user-images.githubusercontent.com/37069490/163044765-66bb4f86-1a44-40c1-a43e-8fb3cc89af5c.png)

## Node.js

Zamiast korzystać z narzędzia nvm node.js można pograć i zainstalować bezpośrednio ze strony 
https://nodejs.org/en/.

### NPM - Node package manager
npm to powszechnie wykorzystywany menedżer pakietów Node (za jego pomocą zainstalujemy np pakiet
Express). npm nie jest akronimem (dlatego nazwy tej nie zapisuje się wielkimi literami) jak nazwy
PHP, GNU, WINE i inne;
Ogólnie rzecz biorąc, menedżer pakietów służy do instalowania pakietów i zarządzania zależnościami.

!Dostępny jest też konkurencyjny popularny menedżer pakietów o nazwie Yarn,
wykorzystujący tę samą bazę danych pakietów, z której korzysta npm.

**npm jest instalowany wraz z Node.**

Do instalacji pkietów służy polecenie `npm install -g nazwa_pakietu` np:
![image](https://user-images.githubusercontent.com/37069490/163167221-c594de5b-6041-43e2-b7f7-6424ad313f3f.png)
opcja -g wskazuje że pakiet powinien być zainstalowany globalnie. Użycie polecenia bez tej opcji utworzy folder node_modules w folderze w którym zostało wywołane polecenie.

### Konsola Node
Konsolę node można wywołać poleceniem `node` i używać jako kalkulatora lub pisać skrypt linia po linii:
![image](https://user-images.githubusercontent.com/37069490/163172542-10ac9d96-da97-4fee-b3b0-32ec382e6cc3.png)

By zapisać skrypt w konsoli należy wpisać `.save nazwa_skryptu.js` skrypt zostanie zapisany w folderze w którym została uruchomiona konsola:
![image](https://user-images.githubusercontent.com/37069490/163173429-89229173-8bfd-48bd-bde5-16fe3eb57b3c.png)

By załadować skrypt służy polecenie `.load URL_do_skryptu.js`:
![image](https://user-images.githubusercontent.com/37069490/163173862-20b2ca14-9e3f-42ae-a90f-e559bfb586ae.png)

### Uruchamianie skryptów bez konsoli:
By uruchomić skrypt zapisany w pliku można użyć polecenia `node nazwa_skryptu.js`:

_hello.js_
```javascript
const prompt = require('prompt-sync')({sigint: true}); // Wymaga modułu prompt-sync. 
var imie = prompt("Podaj imię:")
console.log(`Hello ${imie}!`)
```

### Tworzenie serwera
```javascript
var http = require('http'); // import modułu HTTp

var server = http.createServer(function (req, res) {
    res.writeHead(200, { 'Content-Type': 'text/plain' }); // Utworzenie nagłówka HTTP
    res.write('Hello World!'); // Treść odpowiedzi HTTP
    res.end();
})
// 'Słuchacz' oczekujący na żądania HTTP
server.listen(8000, "127.0.0.1", () => { console.log("Uruchomiono serwer!(Ctrl+C - exit)") }) 
```
Skrypt uruchomi lokalny serwer pod adresem 127.0.0.1:800. Wpisując ten adres w przeglądarce zostanie uruchomiona funkcja createServer która zwróci napis Hello World!.

### Trasowanie - przetwarzanie żądań http

```javascript
var http = require('http'); // import modułu HTTP

var server = http.createServer(function (req, res) {
    const path = req.url // Odczytanie adresu URL żądania HTTP
    console.log("HTTP REQUEST: ", path)
    switch (path) {
        case '':
            res.writeHead(200, { 'Content-Type': 'text/plain' })
            res.end('Index.html')
            break
        case '/hello':
            res.writeHead(200, { 'Content-Type': 'text/plain' })
            res.end('Hello World!')
            break
        default:
            res.writeHead(404, { 'Content-Type': 'text/plain' })
            res.end('ERROR 404 - Not Found')
            break
    }
})
// 'Słuchacz' oczekujący na żądania HTTP
server.listen(8000, "127.0.0.1", () => { console.log("Uruchomiono serwer!(Ctrl+C - exit)") }) 
```
Powyższy przykład obsługuje 3 adresy URL:
| URL | case |
|---|---|
| http://127.0.0.1:8000/ | case '': |
| http://127.0.0.1:8000/hello | case '/hello': |
| Wszystkie inne żądania | default: |

Brak opcji `default` spowoduje przerwanie działania aplikacji w przypadku wysłania nieprawidłowego żądania HTTP

### Odczytanie dokumentu html i zwrócenie jako odpowiedź

```javascript
var http = require('http') // import modułu HTTP
var fs = require('fs') // import modułu fs

var server = http.createServer(function (req, res) {
    const path = req.url // Odczytanie adresu URL żądania HTTP
    console.log("HTTP REQUEST: ", path)
    switch (path) {
        case '/':
            fs.readFile("static/index.html", (e, data)=>{
                if(e){ // jeśli wystąpi wyjątek zwrócimy odpowiedni komunikat
                    res.writeHead(500, { 'Content-Type': 'text/plain'})
                    res.end("Internal Server Error: "+e)
                }else{ // jeśli odczyt będzie prawidłowy zwracamy odczytany dokument
                    res.writeHead(200, { 'Content-Type': 'text/html'})
                    res.end(data)
                }
            })
            break
        case '/hello':
            res.writeHead(200, { 'Content-Type': 'text/plain' })
            res.end('Hello World!')
            break
        default:
            res.writeHead(404, { 'Content-Type': 'text/plain' })
            res.end('ERROR 404 - Not Found')
            break
    }
})
// 'Słuchacz' oczekujący na żądania HTTP
server.listen(8000, "127.0.0.1", () => { console.log("Uruchomiono serwer!(Ctrl+C - exit)") }) 
```




1. Utwórz skrypt pytajacy użytkownika o wagę w kg oraz wzrost w metrach. Na podstawie danych oblicz wskaźnik bmi i wypisz informacje w konsoli.

![image](https://i.redd.it/n08d5h8v4id21.jpg)
