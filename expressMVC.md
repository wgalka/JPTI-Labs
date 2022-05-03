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
<details>

[`express`](https://expressjs.com/)
 
[`express-handlebars`](https://handlebarsjs.com/guide/#what-is-handlebars)
 
[`express-session`](http://expressjs.com/en/resources/middleware/session.html)

[`body-parser`](http://expressjs.com/en/resources/middleware/body-parser.html)

[`mongoose`](https://mongoosejs.com/)
 
[`nodemon`](https://nodemon.io/)
 

<img src="https://user-images.githubusercontent.com/37069490/166433438-af9fc029-c02d-4fb0-bdfb-287a357d89f4.png"/>

</details>
