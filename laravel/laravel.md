# Laravel

## Tworzenie projektu za pomocą composera

```powershell
composer create-project laravel/laravel nazwa_projektu
```
❗Projekt zostanie utworzony w folderze w którym wywołamy polecenie

## Uruchamianie serwera

```powershell
php artisan serve --host=127.0.0.1 --port=8080 
```
Po uruchomieniu serwera i wpisaniu w przeglądarke adresu hosta i portu otworzy się strona przywitalna frameworku Laravel.

❗Wywołując polecenie należy zwrócić uwagę czy jest wywoływane w głównym folderze projektu(w folderze w którym znajduje się plik artisan )

## Trasowanie

```
📦routes
 ┣ 📜api.php
 ┣ 📜channels.php
 ┣ 📜console.php
 ┗ 📜web.php
```

**api.php** - trasy powinny być bezstanowe uwierzytelniane tokenami. Nie powinny mieć dostępu do sesji.(REST API)

**channels.php** - trasy obsługujące sterowanie zdarzeniami(wymiana informacji w czasie rzeczywistym np. czat, powiadomienie użytkownika(notification) o wysłaniu przetworzonego pliku bez konieczności ponownego przeładowania strony)

**console.php** - polecenia wywoływane z konsoli np. domyślnie zdefiniowana trasa 'inspire' może być wywołana przez nastepujące polecenie `php artisan inspire`. przykładowe użycie to np. skrypt czyszczący bazę danych czy wczytujący seed.

```php
Artisan::command('cleardatabase {db_name}', function ($db_name) {
    //TODO usuwanie bazy danych
    $this->info("Database cleared ".$db_name);
})->purpose('Clearing database');
```

**web.php** - Trasy które zapewniają stan sesji, ochronę CSRF i szyfrowanie plików cookie.(Żądanie-Odpowiedź)

Tworzenie routingu w pliku web.php:

*Fasada jest wzorcem projektowym upraszczającym złożony zestaw klas lub bibliotekę w uproszczony interfejs w tym przypadku komunikacja klient-server za pomocą protokołu HTTP udostepnia prosty interfejs np. `Route::get('/', function)`*

Wybrane interfejsy oraz przykładowe `status code odpowiedzi` succes/failure:

CREATE - Utworzenie zasobu 🟢201 🔴404
```php                        
Route::post($uri, $callback); 
```
READ - Odczytanie zasobu 🟢200 🔴404
```php                        
Route::get($uri, $callback);  
```    
UPDATE - Aktualizacja zasobu 🟢200 🔴404
```php
Route::put($uri, $callback);
```
DELETE - Usunięcie zasobu 🟢200 🔴404
```php
Route::delete($uri, $callback);
```

**Co podać jako `$uri`?**

Statyczna ścieżka w postaći łańcucha znaków.
```php
Route::get('/search', $function);
```

`named parameters` czyli elementy w ścieżce które są dynamicznie generowane np. w podanym niżej przykładzie routing obsłuży następujące żądania: 
- /search/jan
- /search/marek
- /search/zbigniew
- itp.

```php
Route::get('/search/{name}', $function);
```

Jeśli `named parameter` ma być opcjonalny należy użyć symbolu `?` po nazwie parametru przez co obsłuży następujące żądania:
- /search
- /search/jan
- /search/marek
- /search/zbigniew
- itp.
```php
Route::get('/search/{name?}', $function);
```

**Co podać jako `$callback`?**

Funkcję anonimową (funkcje bez nazwy)
```php
Route::get('/', function () {
    return 'Hello world!';
});
```
Tablicę w której pierwszy argument to klasa kontrolera obsługująca dany routing a drugi parametr to łańcuch znaków wskazujący metodę w klasie kontrolera:
```php
Route::get('/', [UserController::class, 'printhello']);
```

**Jak przetwarzać `named parameters`?**

Aby przetwarzać informacje z `named parameters` funkcja `$callback` powinna przyjmować parametry o tej samej nazwie:
```php
Route::get('/user/{nickname}/post/{post}', function ($nickname, $post) {
    return "Post: ".$post." Created by ".$nickname;
});
```

**Jak przetwarzać `query parameters`?**

`query parameters` są to dane przesyłane w URL żądania HTTP po znaku `?` w postaci `nazwa=wartość`:
```url
https://127.0.0.1:8080/hello?name=Jan&forname=John
```
W laravelu dostęp do `query parameters` można uzyskać używając obiektu Request w funkcji podawanej jako `$callback`. W poniższym przykładzie żądanie zwraca wartość parametru name zefiniowanego w `query parameters`. Jeśli nie da się odczytać tej wartośći zostanie zwrócony łąńcych znaków "No query parameters".
```php
Route::get('/user', function (Request $request) {
    try {
        return $request->query('name');
    } catch (Exception $e) {
        return "No query parameters";
    }
});
```
Najważniejsze metody obiektu `Request`:


1. Co to `named parameters`?
2. Co to `query parameters`?
3. Co to funkcja anonimowa?
4. Jakie metody HTTP odpowiadają operacjom CRUD?
