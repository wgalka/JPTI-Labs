# Laravel

## Tworzenie projektu za pomocą composera

```powershell
composer create-project laravel/laravel nazwa_projektu
```
! Projekt zostanie utworzony w folderze w którym wywołamy polecenie

## Uruchamianie serwera

```powershell
php artisan serve --host=127.0.0.1 --port=8080 
```
! Wywołując polecenie należy zwrócić uwagę czy jest wywoływane w głównym folderze projektu(w folderze w którym znajduje się plik artisan )

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
Utworzenie zasobu - CREATE 🟢201 🔴404
```php                        
Route::post($uri, $callback); 
```
Odczytanie zasobu - READ 🟢200 🔴404
```php                        
Route::get($uri, $callback);  
```    
Aktualizacja zasobu - UPDATE 🟢200 🔴404
```php
Route::put($uri, $callback);
```
Usunięcie zasobu - DELETE 🟢200 🔴404
```php
Route::delete($uri, $callback);
```


