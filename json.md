# JSON (JavaScript Object Notation)

W porównaniu do formatu wymiany danych XML, JSON pozwala na przesłanie tej samej informacji używając mniejszej ilości znaków (XML musi zawierać tagi zamukające itp.)

Obecnie jest domyślnym formatem wymiany danych większości aplikajci oraz używany do przechowywania ustawień aplikacji.

Jest niezależeny od JavaScript. Dzięki parserom dane przesyłane są w formacie tekstowym a następnie zamieniane na strukturę danego języka umożliwiającą naturalny dostęp do składowych.

Pliki json posiadają rozszerzenie `.json` np. `package.json`

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

⚠️W odniesieniu do baz danych używane jest pojęcie [`JSON Documents`](https://www.ibm.com/docs/en/db2/11.5?topic=json-client-access-documents) gdzie zdefiniowane jest więcej typów danych. BSON jest formatem używanym w MongoDB do zapisu danych. 

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

## JSON Schema

W dużych projektach chcemy mieć pewność że JSON ma określoną strukturę. W tym celu wykorzystuje się [JSON Schema](https://json-schema.org/learn/getting-started-step-by-step).

JSON schema to dokumenty JSON opisujące jak powinna wyglądać struktura przesyłanego JSON. Definiujemy ją za pomocą słów kluczowych:
- `$schema` - określa z jakim standardem został stworzony schemat
- `$id` - URL do schematu (w ramach laboratorium można udostępnić schemat na github lub darmowym hostingu)
- `title` i `description` - Opis niemający wpływu na walidację JSON.
- `type` - definiuje jaki typ danych ma być w miejscu wystąpienia
- `properties` - definiuje jakie właściwości ma mieć dany JSON. `"properties": {"nazwaWłaściwości" : {"type": "typWłaściwości"}}`
- `required` - wskazuje które właściwości musi posiadać JSON
```json
{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "$id": "https://raw.githubusercontent.com/wgalka/JPTI-Labs/main/helpers/json/schema.json",
    "type": "object",
    "properties": {
        "users": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "nick": {
                            "type": "string"
                        },
                        "age": {
                            "type": "integer"
                        },
                        "hobbies": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                }
                            ]
                        }
                    },
                    "required": [
                        "nick",
                        "age",
                        "hobbies"
                    ]
                }
            ]
        }
    },
    "required": [
        "users"
    ]
}
```
Dla powyższego przykładu poprawna będzie poniższa struktura JSON
```json
{
    "users": [
        {
            "nick": "Nickname123",
            "age": 12,
            "hobbies": [
                "Skiing",
                "Climbing"
            ]
        },
        {
            "nick": "Nickname12",
            "age": 12,
            "hobbies": null
        }
    ]
}
```
Do walidacji dokumentów potrzebny jest walidator: https://json-schema.org/implementations.html

Na potrzeby laboratorium by sprawdzić poprawność JSON z utworzonym schematem można skorzystać ze strony: https://www.jsonschemavalidator.net/

## Przetwarzanie JSON w Javascript

Przed przesłaniem obiektu JavaScript należy przekształcić go na łańcuch znaków do czego służy metoda `JSON.stringify()`:
```Javascript
let jsonobj = {id : 1, nickname:"Example1", emal: "mailme@login.com", password:"123456"}

let jsonstring = JSON.stringify(jsonobj)

console.log(jsonstring)
```
Przekształcanie JSON na obiekt Javascript:
```Javascript
let jsonobj = JSON.parse(jsonstring)
```
Dostęp do składowych obiektu:
```Javascript
let jsonobj = {id : 1, nickname:"Example1", emal: "mailme@login.com", password:"123456", hobbies:["Skiing","Cooking","Rafting"]}

// Odczyt id
let id = jsonobj.id
console.log(id)
// Odczyt tablicy hobbies
let hobbies = jsonobj.hobbies
console.log(hobbies)
// Odczyt pierwszego hobby
let hobby = jsonobj.hobbies[0]
console.log(hobby)
```

Zmiana danych obiektu JSON:
```Javascript
let jsonobj = {id : 1, nickname:"Example1", emal: "mailme@login.com", password:"123456", hobbies:["Skiing","Cooking","Rafting"]}
jsonobj.id = 4
jsonobj.hobbies = null

let jsonstring = JSON.stringify(jsonobj)

console.log(jsonstring)
```

❗Nazwy pól w obiekcie JSON mogą zawierać znak `-` który przez Javascript jest traktowany jako operator. By odwołać się do takiego pola można w następujący sposób: `jsonobj['my-key']`

1. Zaprojektować strukturę JSON reprezentującą mieszkanie i dane z różnych czujników które znajdowałyby się w danych pomieszczeniach. Przykładowe założenia:
    - Mieszkanie może mieć pewną nazwę jednoznacznie je indetyfikującą(id)
    - Dokument JSON reprezentuje stan mieszkania w danym momencie. Informacje o tym w jakim można przechowywać w polu jako `timestamp` - jest to liczba milisekund która upłynęła od 1 stycznia 1970 00:00:00 UTC.
    - Mieszkanie skłąda się z wielu pokoji.
    - Pomieszczenia mają pewne wymiary.
    - W pomieszczeniach jest pewna temperatura.
    - W pomieszczeniach jest pewna wilgotność powietrza.
    - W pomieszczeniach jest pewna ilość źródeł światła o których wiemy czy są włączone czy nie.
    - W pomieszczeniach możemy znać temperaturę grzejników.

2. Utworzyć dwa przykładowe różne mieszkania.
3. Utworzyć stronę z formularzem który wczyta dane konkretnego mieszkania a następnie wyświetli dane na jego temat w czytelny sposób. Wykorzystać framework Bootstrap do stworzenia interfejsu lub inne frameworki. Np. jeśli światło jest zaświecone na stronie przy danym pokoju pojawia się  [ikona żarówki](https://icons.getbootstrap.com/icons/lightbulb/) jeśli jest zgaszone to [inna ikona](https://icons.getbootstrap.com/icons/lightbulb-off/)
4. \*Utworz JSON Schema walidujący zaprojektowaną strukturę.
5. ``` if (przedmiot === "JPiTI"){ goto("Laboratorium 7 MongoDB") } ```


W Javascript metoda `Date.now()` zwraca datę w postaci timestamp w obecnej chwili
```Javascript
let timenow = Date.now()

console.log(timenow)
```

Aby wczytać dane z pliku użyj funkcji `require`
```Javascript
let jsonobj = require('./flats.json')
console.log(jsonobj);
```
