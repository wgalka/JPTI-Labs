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

## Przykładowy JSON zawierający dane na temat użytkownika aplikacji
```JSON
{
    "users": [
        {
            "id": 123,
            "name": "Jan",
            "lastname": "Kowalski",
            "adress": {
                "street": "Azaliowa",
                "postalcode": "35-000",
                "city": "Radom"
            },
            "active": true,
            "hobbies": null
        },
        {
            "id": 672,
            "name": "Marek",
            "lastname": "Nowak",
            "adress": {
                "street": "Wrzosowa",
                "postalcode": "38-000",
                "city": "Chełm"
            },
            "active": false,
            "hobbies": [
                "Skiing",
                "Art",
                "Diving"
            ]
        }
    ]
}
```

Te same dane w formacie XML
```XML
<?xml version="1.0" encoding="UTF-8"?>
<root>
   <users>
      <element>
         <active>true</active>
         <adress>
            <city>Radom</city>
            <postalcode>35-000</postalcode>
            <street>Azaliowa</street>
         </adress>
         <hobbies null="true" />
         <id>123</id>
         <lastname>Kowalski</lastname>
         <name>Jan</name>
      </element>
      <element>
         <active>false</active>
         <adress>
            <city>Chełm</city>
            <postalcode>38-000</postalcode>
            <street>Wrzosowa</street>
         </adress>
         <hobbies>
            <element>Skiing</element>
            <element>Art</element>
            <element>Diving</element>
         </hobbies>
         <id>672</id>
         <lastname>Nowak</lastname>
         <name>Marek</name>
      </element>
   </users>
</root>
```
