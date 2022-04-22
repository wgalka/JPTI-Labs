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

`100` do `199` - Odpowiedź informacyjna

`200` do `299` - Odpowiedź udana

`300` do `399` - Przekierowanie

`400` do `499` - Błąd po stronie klienta

`500` do `599` - Błąd po stronie serwera

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

