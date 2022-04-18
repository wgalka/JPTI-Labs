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

**api.php** - trasy powinny być bezstanowe uwierzytelniane tokenami. Nie powinny mieć dostępu do sesji.

**channels.php** - trasy obsługujące sterowanie zdarzeniami(wymiana informacji w czasie rzeczywistym np. czat, powiadomienie użytkownika(notification) o wysłaniu przetworzonego pliku bez konieczności ponownego przeładowania strony)

**console.php** - polecenia wywoływane z konsoli np. domyślnie zdefiniowana trasa 'inspire' może być wywołana przez nastepujące polecenie `php artisan inspire`. przykładowe użycie to np. skrypt czyszczący bazę danych czy wczytujący seed.

```php
Artisan::command('cleardatabase {db_name}', function ($db_name) {
    //TODO usuwanie bazy danych
    $this->info("Database cleared ".$db_name);
})->purpose('Clearing database');
```

**web.php**

Routing directory:
-
