# Protokół HTTP

## Budowa żądania HTTP

- Metoda żądania HTTP
- Adres URL zasobu
- Wersji protokołu - HTTP/1.1
- Nagłówki
- Wiadomość

### Metody żądań HTTP

Protokół HTTP ma 8 metod żądania. Najważniejsze z nich to:

**`POST`** - Żądania tego typu powinny przesyłać dane z formularzy, tworzyć nowe zasoby itp. (CREATE)

**`GET`** - Żądania tego typu głużą do odczytu zasobu. (READ)

**`PUT`** - Żądania tego typu służą do aktualizacji zasobów. (UPDATE)

**`DELETE`** - Żądania tego typu powinny usuwać zasoby. (DELETE)

### Adres URL zasobu

Budowa adresu URL:

`protocol`://`host`/`path`?`query params`

Przykładowy adres URL

`https`://`js.lazysolutions.pl`/`jpiti/json.html`?`name=Jan`

### Nagłówki

Pozostałe informacje zapisane w parach atrybut-wartość oddzielonych znakiem `:` np. ciasteczka, informacje o kliencie z którego zostało wysłane żądanie(wersja przeglądarki), adresie ip z którego zostało wysłane żądanie itp.

### Wiadomość

W większośći przypadków żądania nie posiadają wiadomośći. Wyjątkiem jest metoda `POST` która może zawierać dane z formularza w wiadomości.

## Budowa odpowiedzi HTTP

- Wersja protokołu - HTTP/1.1
- Status odpowiedzi HTTP
- Nagłówki
- Treść odpowiedzi

### Statusy żądania HTTP

🟡`100` do `199` - Odpowiedź informacyjna

🟢`200` do `299` - Odpowiedź udana

🟢`300` do `399` - Przekierowanie

🔴`400` do `499` - Błąd po stronie klienta

🔴`500` do `599` - Błąd po stronie serwera

### Nagłówki odpowiedzi HTTP

Struktura jest taka sama jak w żądaniach HTTP. Nagłówki odpoweidzi HTTP zawierają np. informacje na temat typu dokumentu przesłanego w wiadomośći w atrybucie `Content-type`.

Wybrane typy treści odpowiedzi(`Content-type`):
- application/json
- application/xml
- image/gif
- image/jpeg
- image/png
-	text/css
- text/csv
- text/html
- text/javascript (obsolete)
- text/plain
- text/xml


### Wiadomość

Dokument typu zdefiniowanego w nagłówku odpowiedzi.

## Przykład żądania i odpowiedzi

Większość przeglądarek udostępnia narzędzia developerskie umożlwiające wyświetlenie danych.

Instrukcja dla google chrome:
1. Wciśnij prawy przycisk myszy w dowolnym miejscu na stronie. Wybierz opcję zbadaj.

![image](https://user-images.githubusercontent.com/37069490/164784622-115ff060-4b60-4e38-b935-d40c1ec0c507.png)

2. Z prawej strony wiświetli się narzędzie developerskie. Wybierz zakładkę Network

![image](https://user-images.githubusercontent.com/37069490/164784736-c21e1faa-7d66-41dc-a26d-7d886147d995.png)
![image](https://user-images.githubusercontent.com/37069490/164784924-1a658e9a-e7a2-4c9a-b837-b4aeaeb6ac66.png)

3. Odśwież stronę i wybierz dokument który ma nazwę jak domena steony.

![image](https://user-images.githubusercontent.com/37069490/164785094-e8b75bd4-7949-4c05-bf4d-b19e28b15300.png)
![image](https://user-images.githubusercontent.com/37069490/164785140-328ac335-f2ee-4146-aee5-6d5d7558fe87.png)



