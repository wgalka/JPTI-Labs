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
```javascript
const express = require('express')
const app = express()

app.use((req, res) => {
    res.type('text/plain')
    res.status(404)
    res.send('404 - Nie znaleziono')
})

app.use((err, req, res, next) => {
    console.error(err.message)
    res.type('text/plain')
    res.status(500)
    res.send('500 - Błąd serwera')
})
app.listen(port, () => console.log(
    `Example app listening on http://localhost:3000; ` +
    `naciśnij Ctrl-C, aby zakończyć.`))
```
