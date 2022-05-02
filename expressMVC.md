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


