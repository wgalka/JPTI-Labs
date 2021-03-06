# MongoDB

MongoDB jest nierelacyjną bazą danych(NoSQL).

Dane przechowywane są za pomocą:

   - Kolekcji
   - Dokumentów

**Kolekcje** - grupy dokuemntów. Dokumenty w kolekcji nie muszą mieć takiej samej struktury. W odniesiueniu do relacyjnych baz danych odpowiadają tabelom.

**Dokument** - rekord w kolekcji(w odniesieniu do relacyjnych baz danych - wiersz w tabeli) w MongoDB ma strukturę podobną do JSON.

Dokumenty składają się z pól czyli par `nazwa: wartość`
```JSON
{
   name: "Value"
}
```
Bazę można przechowywać za darmo w chmurze: https://www.mongodb.com/atlas/database

lub Lokalnie tworząc servwer bazodanowy:  https://www.mongodb.com/try/download/community

## Tworzenie klastra i bazy danych w chmurze
   
![img](https://user-images.githubusercontent.com/37069490/164544317-65d71f29-d271-407a-9fb1-2d2843b230a1.png)

![img](https://user-images.githubusercontent.com/37069490/164545067-3713c45a-a7ea-407a-8f9f-c69ceb1c2fe9.png)

![img](https://user-images.githubusercontent.com/37069490/164545301-7ad63327-08d7-44ad-ac44-95f646884867.png)

![img](https://user-images.githubusercontent.com/37069490/164545407-81cd17ce-0dfd-4dfc-bbba-756551adf000.png)

Przeglądanie zawartości bazy danych

![img](https://user-images.githubusercontent.com/37069490/164546223-071753d3-4697-4e97-8f03-cd35ee0a2b62.png)

![img](https://user-images.githubusercontent.com/37069490/164546577-1ecb9230-b1d0-4ef5-bca9-aba071ce6e72.png)

Tworzenie bazy danych

![img](https://user-images.githubusercontent.com/37069490/164547877-602c01b5-534d-41f7-a5c1-601be79f58f7.png)

![img](https://user-images.githubusercontent.com/37069490/164548099-9deaba05-cf51-437f-8020-047a7cb4c245.png)

![img](https://user-images.githubusercontent.com/37069490/164548247-c8e9cb78-f269-4d21-b06b-35e2b87f8b2b.png)

## Lokalna baza danych

1. Zainstaluj serwer bazodanowy z domyślnymi ustawieniami.(dalej, dalej, dalej).
2. W likalizacji `C:/Program Files/MongoDB/Server/5.0/bin` znajduje się plik `mongo.exe` który uruchamia serwer bazodanowy.
3. Na pulpicie po winien znajdować się skrót do narzędzia MongoDB Compass (GUI do obsługi bazy danych)

    ![image](https://user-images.githubusercontent.com/37069490/164791680-ab21bc9b-18a7-47f9-8566-e0cb89d6b53e.png)

    Jeśli nie ma skrótu Dodatek Compass znajdziesz w lokalizacji `C:\Users\<STUDENT>\AppData\Local\MongoDBCompass`:
    
    Przejsdz do folderu APPDATA (windows + R) i wpisz `%localappdata%`
    
    ![image](https://user-images.githubusercontent.com/37069490/165908632-96aa4e48-7c63-465f-aa73-0db259b8fafd.png)
    
    Zlokalizuj folder `MongoDBCompass` i plik uruchamiający aplikacje:
    
    ![image](https://user-images.githubusercontent.com/37069490/165908843-d84e9502-9759-4b37-9361-92e6d21a867c.png)

5. Połącz się z bazą danych klikając Connect

Tworzenie bazy danych

![image](https://user-images.githubusercontent.com/37069490/164791884-841761fc-6a96-40e3-886e-9e70660bd016.png)

![image](https://user-images.githubusercontent.com/37069490/164791952-92b598be-e7b5-44a1-8e7f-499224de306d.png)

<!-- 1. Utwórz konto na https://www.mongodb.com/
2. Utwórz klaster `Cluster0`
3. Na klastrze `Cluster0` utwórz bazę `home_db` a w niej kolekcję `sensors`.
4. W kolekcji sensors utwórz dokument reprezentującą mieszkanie i dane z różnych czujników które znajdowałyby się w danych pomieszczeniach. Przykładowe założenia:
    - Mieszkanie może mieć pewną nazwę jednoznacznie je indetyfikującą(id)
    - Dokument reprezentuje stan mieszkania w danym momencie.
    - Mieszkanie skłąda się z wielu pokoji.
    - Pomieszczenia mają pewne wymiary.
    - W pomieszczeniach jest pewna temperatura.
    - W pomieszczeniach jest pewna wilgotność powietrza.
    - W pomieszczeniach jest pewna ilość źródeł światła o których wiemy czy są włączone czy nie.
    - W pomieszczeniach możemy znać temperaturę grzejników. -->


