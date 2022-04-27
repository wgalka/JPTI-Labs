# Express

## Inicjalizacja projektu node.js
```comandprompt
npm init
```
![image](https://user-images.githubusercontent.com/37069490/165591165-73c8403e-f76f-4bc7-ab6b-4ab8305c2805.png)

## Instalacja frameworku express
```comndprompt
npm install express
```
![image](https://user-images.githubusercontent.com/37069490/165591433-51974081-4b21-4d44-ab86-8f0187d83f9f.png)

## Utworzenie pliku uruchamiajacego aplikację
Utwórz plik index.js(nazwa może być dowolna jednak należy pamiętać że przy innej nazwie należy zmienić wartość w pliku package.json) o nastepującej zawartości:
```javascript
const express = require('express')
const app = express()

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

## Uruchomienie aplikacji
```comandprompt
node .\
