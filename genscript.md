# JPiTI

1. Dodać routing obsługijący żądanie post wysyłające dane w postaci JSON w treści żądania HTTP.

```Javascript
// Import pakietu 'body-parser'. Kiedyś pakiet był częścią frameworku https://www.npmjs.com/package/body-parser
var bodyParser = require('body-parser')
// application/json parser - będziemy używać do przetwarzania JSON
var jsonParser = bodyParser.json()

router.post('/save_data',jsonParser, function(req,res){
    // odczytanie ciała żądania (JSON który został wysłany z pliku ranomsensordata.js)
    let data = req.body
    // TODO: zapis danych do bazy danych

    // wypisanie danych w konsoli
    console.log(data)
    // Odesłanie odpowiedzi na zadane żądanie HTTP z kodem statusu 201
    res.status(201);
    res.send()
})
```

2. Utworzyć skrypt `genData.js` o następującej zawartości:

```Javascript
// Importuje bibliotekę standardową http. Jeśli używamy protokołu https należy użyć biblioteki https
const https = require('http');

// metoda która zostanie wykonana po otrzymaniu odpowiedzi od servera
function onResponse(res) {
    console.log('Status Code:', res.statusCode);
}

// metoda która zostanie wywołana w przypadku błędu
function onError(err) {
    console.log("Error: ", err.message);
}

// Generowanie wartości temperatury.
function* generate() {
    while (true) {
        var rand = Math.sqrt(-2.0 * Math.log(Math.random())) * Math.cos(Math.PI * 2 * Math.random());
        yield rand * 10 + 10;
    }
}

// Utworzenie generatora temperatury. Wywołując metodę next() otrzymamy kolejne wartości iteratora.
let generator = generate()

// funckja wysyłająca żądania do bazy danych
function doRequest() {
    let temp = generator.next().value
    // Dane w postaci JSON które chcemy wysłać do aplikajci
    const data = JSON.stringify({
        temperature: temp,
    });
    console.log(data)
    // Opcje protokołu http(nagłówki, nazwa hosta, adres zasobu itp.)
    const options = {
        hostname: '127.0.0.1',
        port: "8080",
        path: '/save_data',
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Content-Length': data.length
        }
    };

    const req = https.request(options, onResponse)
    req.on("error", onError);
    // Wysłanie danych żądania
    req.write(data);
    req.end();
}

// Funckja setInterval będzie wywoływać funkcję doRequest co 5 sekund
const id = setInterval(doRequest, 5000)

// Funkcja setTimeout wywoła funckję clearInterval która zakończy wwsyłanie żądań HTTP po 80 sekundach
setTimeout(function () { clearInterval(id), console.log("Function stopped after 80 seconds!") }, 80000)
```
3. Po uruchomieniu skryptu poleceniem `node genData.js` do naszej aplikacji będą wysyłane żądania co 5 sekund z losową wartością temperatury.

![image](https://user-images.githubusercontent.com/37069490/172256611-be041e73-4db0-4e82-a626-46f84b723695.png)

