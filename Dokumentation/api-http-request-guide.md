Überblick aller Befehle für die API


**GET**

HTTP-Anfrage:
```
GET
http://127.0.0.1:5000/api/todos
```

**POST**

HTTP-Anfrage:
```
POST
http://127.0.0.1:5000/api/todos

Request Body:
{
    "description": "Buy groceries"
}
```

**PATCH**

HTTP-Anfrage:
```
PATCH
http://127.0.0.1:5000/api/todos/ID

Request Body:
{
    "description": "Meeting with boss",
    "complete": true
}
```

**DELETE**

HTTP-Anfrage:
```
DELETE
http://localhost:5000/api/todos/delete/ID
```

Bitte beachte, dass du "`ID`" in den `PATCH`- und `DELETE`-Anfragen durch die tatsächliche ID des ToDos ersetzen musst, das du aktualisieren bzw. löschen willst.