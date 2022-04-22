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

## Tworzenie klastra i bazy danych w chmurze
![image](https://user-images.githubusercontent.com/37069490/164544317-65d71f29-d271-407a-9fb1-2d2843b230a1.png)

![image](https://user-images.githubusercontent.com/37069490/164545067-3713c45a-a7ea-407a-8f9f-c69ceb1c2fe9.png)

![image](https://user-images.githubusercontent.com/37069490/164545301-7ad63327-08d7-44ad-ac44-95f646884867.png)

![image](https://user-images.githubusercontent.com/37069490/164545407-81cd17ce-0dfd-4dfc-bbba-756551adf000.png)

## Przeglądanie zawartości bazy danych

![image](https://user-images.githubusercontent.com/37069490/164546223-071753d3-4697-4e97-8f03-cd35ee0a2b62.png)

![image](https://user-images.githubusercontent.com/37069490/164546577-1ecb9230-b1d0-4ef5-bca9-aba071ce6e72.png)

## Tworzenie bazy danych

![image](https://user-images.githubusercontent.com/37069490/164547877-602c01b5-534d-41f7-a5c1-601be79f58f7.png)

![image](https://user-images.githubusercontent.com/37069490/164548099-9deaba05-cf51-437f-8020-047a7cb4c245.png)

![image](https://user-images.githubusercontent.com/37069490/164548247-c8e9cb78-f269-4d21-b06b-35e2b87f8b2b.png)

1. Utwórz konto na https://www.mongodb.com/
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
    - W pomieszczeniach możemy znać temperaturę grzejników.


