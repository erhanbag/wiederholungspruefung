# Aufgabe 6. - API-Dokumentation

Dies ist die Dokumentation für eine RESTful API, die mit Flask erstellt wurde. Die API bietet Endpunkte zum Verwalten von Aufgaben (Todos) für authentifizierte Benutzer. Die API unterstützt grundlegende Operationen wie das Auflisten, Erstellen, Aktualisieren und Löschen von Aufgaben. Sie umfasst auch die Benutzerauthentifizierung mittels grundlegender Authentifizierung.

## Inhaltsverzeichnis

- [Authentication](#authentication)
- [Endpoints](#endpoints)
  - [List Todos](#list-todos)
  - [Create Todo](#create-todo)
  - [Update Todo](#update-todo)
  - [Delete Todo](#delete-todo)

## Authentication <a name="authentication"></a>

Für diese API ist eine Benutzerauthentifizierung mittels grundlegender Authentifizierung erforderlich. Um auf die Endpunkte zugreifen zu können, müssen Sie Ihren Benutzernamen und Ihr Passwort angeben. Die API überprüft Ihre Anmeldeinformationen anhand des bereitgestellten Benutzernamens und Passworts.

## Endpoints <a name="endpoints"></a>

### List Todos <a name="list-todos"></a>

**GET /api/todos/**

Rufen Sie eine JSON-Ausgabe der Aufgaben ab, die mit dem authentifizierten Benutzer verknüpft sind.

#### Request

- Method: GET
- Authentication: Required

#### Antwort

- Statuscode: 200 OK

 Status Code: 200 OK

Example Response Body:
```json
{
  "todos": [
    {
      "complete": false,
      "description": "Buy groceries",
      "id": 1,    
      "user_id": 123
    },
    {
      "complete": true,
      "description": "Finish work report",
      "id": 2,
      "user_id": 123
    }
    // Hier sind z.B weiter Todos
  ]
}
```

### Create Todo <a name="create-todo"></a>

**POST /api/todos/**

Erstellen Sie eine neue Aufgabe für den authentifizierten Benutzer.

#### Request

- Method: POST
- Authentication: Required
- Request Body:

Example Request Body:
```json
{
  "description": "Walk the dog"
}
```

#### Response

- Status Code: 201 Created

Example Response Body:
```json
{
  "message": "New todo added successfully."
}
```

- Status Code: 400 Bad Request

Example Response Body (If 'description' is missing or empty):
```json
{
  "error": "Description is required."
}
```

### Update Todo <a name="update-todo"></a>

**PATCH /api/todos/{todo_id}**

Aktualisieren Sie eine vorhandene Aufgabe für den authentifizierten Benutzer.

#### Request
- Method: PATCH
- Authentication: Required
- URL Parameter: {todo_id} - ID of the todo item to update

Example URL: `/api/todos/1`

- Request Body:

Example Request Body:
```json
{
  "description": "Updated description",
  "complete": true
}
```

#### Response

- Status Code: 200 OK

Example Response Body:
```json
{
  "message": "Todo with ID 1 updated successfully."
}
```

- Status Code: 404 Not Found

Example Response Body (If the specified todo item is not found):
```json
{
  "error": "Todo item not found."
}
```

- Status Code: 403 Forbidden

Example Response Body (If the user does not have permission to change the owner):
```json
{
  "error": "You do not have permission to change the owner."
}
```

- Statuscode:  400 Bad Request

Beispiel-Antwortkörper (Wenn die 'user_id' im Anfragekörper auf einen nicht vorhandenen Benutzer zeigt):
```json
{
  "error": "The specified user does not exist."
}
```

### Delete Todo <a name="delete-todo"></a>

**DELETE /api/todos/delete/{todo_id}**

Löschen Sie eine Aufgabe für den authentifizierten Benutzer.


#### Request

- Method: DELETE
- Authentication: Required
- URL Parameter: {todo_id} - ID of the todo item to delete

Example URL: `/api/todos/delete/1`

#### Response

- Status Code: 200 OK

Example Response Body:
```json
{
  "message": "Todo with ID 1 deleted successfully."
}
```

- Status Code: 404 Not Found

Example Response Body (If the specified todo item is not found):
```json
{
  "error": "Todo item not found."
}
```

- Status Code: 403 Forbidden

Example Response Body (If the user does not have permission to delete the todo item):
```json
{
  "error": "You do not have permission to delete this todo item."
}
```

Diese API bietet grundlegende Funktionen zur Verwaltung von Aufgaben für authentifizierte Benutzer. Benutzer können ihre Aufgaben auflisten, neue erstellen, bestehende Aufgaben aktualisieren und bei Bedarf löschen. Stellen Sie sicher, dass Sie authentifiziert sind, bevor Sie Anfragen an diese Endpunkte senden.

**Hinweis**: Um Anfragen and die API senden zu können wie POST GET PATCH oder DELETE, muss die Tatsächliche Anmeldeinformation vom User genutzt werden, also der Username und das Passwort. Dazu kann man den Usernamen und das Passwort innerhalb des gewählten API Testers als "Basic-Auth" einrichten.

Die API wurde von mir mit dem API Tester Insomnia getestet -> https://insomnia.rest/


## Quellen
https://tedboy.github.io/flask/generated/flask.jsonify.html
https://www.youtube.com/watch?v=uBiQEL43AQU