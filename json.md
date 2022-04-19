# JSON (JavaScript Object Notation)

W porównaniu do formatu wymiany danych XML, JSON pozwala na przesłanie tej samej informacji używając mniejszej ilości znaków (XML musi zawierać tagi zamukające itp.)

Obecnie jest domyślnym formatem wymiany danych większości aplikajci oraz używany do przechowywania ustawień aplikacji.

Jest niezależeny od JavaScript. Dzięki parserom dane przesyłane są w formacie tekstowym a następnie zamieniane na strukturę danego języka umożliwiającą naturalny dostęp do składowych.

## Podstawowe struktury JSON:

### Obiekt
```JSON
{}
```
**Tworzenie pól w obiekcie** 
```JSON
{
  "name": "value",
  "imie": "Jan",
  "nazwisko": "Kowalski"
}
```

### Tablica

```JSON
[]
```
**Tworzenie wartości w tablicy**
```JSON
["aple", "onion", "pear"]
```


❗w odróżnieniu od Javascript nazwy pól zapisujemy w `"`. W JSON nie używamy znaków `'`
❗pary atrybut wartość odzielamy `,`.
❗po ostatniej wartośći nie może być znaku `,`
