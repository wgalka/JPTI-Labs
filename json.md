# JSON (JavaScript Object Notation)

W porównaniu do formatu wymiany danych XML, JSON pozwala na przesłanie tej samej informacji używając mniejszej ilości znaków (XML musi zawierać tagi zamukające itp.)

Obecnie jest domyślnym formatem wymiany danych większości aplikajci oraz używany do przechowywania ustawień aplikacji.

Jest niezależeny od JavaScript. Dzięki parserom dane przesyłane są w formacie tekstowym a następnie zamieniane na strukturę danego języka umożliwiającą naturalny dostęp do składowych.

## Podstawowe struktury JSON:

### Object (obiekt)
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

### Array (tablica)

```JSON
[]
```
**Tworzenie wartości w tablicy**
```JSON
["aple", "onion", "pear"]
```

❗W pliku JSON może znajdowac się tylko jeden główny obiekt lub tablica(korzeń jak w formacie XML).

❗Obiekt i tablica mogą zawierać inne obiekty lub tablice.

❗w odróżnieniu od Javascript nazwy pól zapisujemy w `"`. W JSON nie używamy znaków `'`

❗pary atrybut wartość odzielamy `,`.

❗po ostatniej wartośći nie może być znaku `,`

❗W formacie JSON nie ma komentarzy

## Typy danych w JSON

### String (łańcuch znaków)

```JSON
{
  "text1":"Wartości tekstowe zapisujemy w podwójnych cudzysłowiach"
}
```

### Number

```JSON
{
  "val1": 10
  "val2": 200.99
}
```

### Bolean

```JSON
{
  "val1": true
  "val2": false
}
```
### Object

```JSON
{
  "obj": {
      "name": "Jan",
      "age": 34
  }
}
```

### Array
```JSON
{
  "arr": [1, 2, 3, 4]
}
```

### Null
```JSON
{
  "questions": null
}
```
