# Migracje

Migracje w frameworku Laravel znajdują się w lokalizacji: `database\migrations`.
![image](https://user-images.githubusercontent.com/37069490/166918721-ee45b335-4f09-487c-9c19-b9a9f6c013b6.png)

Wyołanie migracji:
```comandprompt
php artisan migrate
```
Wysołując to polecenie począwszy od najstarszej migracji zostanie wywołana metoda `up()`.
