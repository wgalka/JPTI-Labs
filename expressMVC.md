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
 ┣ 📜package-lock.json
 ┗ 📜package.json
 ```
