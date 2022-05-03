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

[`express`](https://expressjs.com/) - framework do tworzenia aplikacji internetowych oraz REST API w Node.js
 
[`express-handlebars`](https://handlebarsjs.com/guide/#what-is-handlebars) - silnik szablonów ułatwiający dunamiczne generowanie treści dla użytkownika aplikacji.
 
[`express-session`](http://expressjs.com/en/resources/middleware/session.html) - warstwa pośrednicząca umożliwia nadzorowanie w frameworku express stanu sesji połączonego użytkownika.

[`body-parser`](http://expressjs.com/en/resources/middleware/body-parser.html) - warstwa pośrednicząca umożliwia odczytanie wiadomości przesyłanej przez protokół HTTP metodą POST.

[`mongoose`](https://mongoosejs.com/) - bliblioteka ułatwiająca pracę z bazą danych MongoDB. Ułatwia połączenie z bazą danych, wymianę informacji wraz z nadzorem poprawności (klasy modelowe).
 
[`nodemon`](https://nodemon.io/) - Blibloteka ułatwiająca tworzenie aplikacji. Restartuje serwer aplikacji przy zapisaniu pliku.
 

<img src="https://user-images.githubusercontent.com/37069490/166433438-af9fc029-c02d-4fb0-bdfb-287a357d89f4.png"/>
</details>

### 4. Utwórz plik `config.json` i zapisz w nim dane dostępowe do bazy danych itp..
 <details>
<img src="https://user-images.githubusercontent.com/37069490/166440247-488c1f7b-d3eb-47db-b7d6-f05c3fe17fe3.png" alt="img"/>
 </details

### 5. Utwórz foldery przechowujące:
 - Modele
 - Widoki
 - Kontrolery
 - Pliki statyczne
 - Routing

 <details>
 📂controllers - Folder przechowujący skrypty odpowiedzialne za logikę aplikacji.
 
 📂models - Folder na klasy modelowe np. stworzone w bibliotece 'mongoose'

 📂public - Folder na pliki statyczne
  ┣ 📂css
  ┣ 📂font
  ┣ 📂js
  ┗ 📂img
 
 📂routes - Folder na skrypty odpowiedzialne za trasowanie żądań HTTP (przekazywanie żądań do odpowiedniego kontrolera)
 
 📂views - Folder na szablony np. biblioteki 'express-handlebars'
  ┣ 📂layouts - Folder na szablony zawierajace układ strony
  ┗ 📂partials - Folder na elementy strony np. pasek nawigacji

 <img src="https://user-images.githubusercontent.com/37069490/166444177-f02a241e-da53-4041-ae23-9b5e6e39d5a2.png" alt ="img"/>
 </details>
