# Aufgabe 5. - Datenmodell nach den Änderungen
# Inhaltsverzeichnis
- [Einleitung](#einleitung)
- [Altes Datenmodell](#altes-datenmodell)
  - [Tabelle `todo`](#tabelle-todo)
  - [Tabelle `list`](#tabelle-list)
- [Neues Datenmodell](#neues-datenmodell)
  - [Tabelle `User`](#tabelle-user)
  - [Tabelle `Todo`](#tabelle-todo)
  - [Tabelle `List`](#tabelle-list)
- [Wodurch hebt sich das neue Datenmodell besonders vom vorherigen ab?](#wodurch-hebt-sich-das-neue-datenmodell-besonders-vom-vorherigen-ab)
- [Quellen](#quellen)





# Einleitung

Die Webanwendung verwendet ein Datenmodell, das Beziehungen zwischen den Entitäten (Tabellen) definiert, um die Verwaltung von Aufgaben (To-Dos) und Listen zu ermöglichen. Im Folgenden wird das ursprüngliche Datenmodell mit dem erweiterten Modell und den Beziehungen zwischen den Entitäten beschrieben.

In diesem Teil unserer Projektdokumentation werden wir eine eingehende Analyse des Datenmodells in unserer Webanwendung durchführen. Wir werden uns insbesondere auf die Unterschiede zwischen dem ursprünglichen Baseline-Datenmodell und dem erweiterten Datenmodell konzentrieren. Das ursprüngliche Datenmodell diente als Ausgangspunkt für unsere Webanwendung, aber wir haben es erheblich erweitert, um zusätzliche Funktionen zur Benutzerverwaltung und -kontrolle hinzuzufügen.

In den folgenden Abschnitten werden wir die Veränderungen im Datenmodell im Detail betrachten und die Vorteile des neuen Modells hervorheben. Wir werden auch auf die Beziehungen zwischen den verschiedenen Tabellen im Datenmodell eingehen und erläutern, wie diese Änderungen die Benutzerfreundlichkeit, Sicherheit und Individualisierung in unserer Anwendung verbessern.

Der Übergang von einem einfachen Datenmodell zu einem erweiterten Modell mit Benutzerverwaltung ist entscheidend, um die Anforderungen und Erwartungen unserer Benutzer zu erfüllen. In diesem Kontext werden wir die Schlüsselmerkmale des erweiterten Datenmodells hervorheben und die positiven Auswirkungen auf die Benutzererfahrung erläutern.

Lassen Sie uns nun tiefer in die Analyse des Datenmodells eintauchen und die Veränderungen im Detail untersuchen.


## Altes Datenmodell

### Tabelle `todo`

- `id` (PK) - Eindeutige Identifikation der Aufgabe
- `complete` - Ein boolescher Wert, der angibt, ob die Aufgabe abgeschlossen ist oder nicht
- `description` - Eine Zeichenfolge, die die Beschreibung der Aufgabe enthält

Die Tabelle `todo` hatte eine n:n Beziehung mit der Tabelle `list`, die durch die Tabelle `todo_list` vermittelt wurde. Das bedeutet, dass eine Aufgabe in mehreren Listen enthalten sein konnte.

### Tabelle `list`

- `id` (PK) - Eindeutige Identifikation der Liste
- `name` - Eine Zeichenfolge, die den Namen der Liste enthält

Die Tabelle `list` hatte ebenfalls eine n:n Beziehung mit der Tabelle `todo`, die durch die Tabelle `todo_list` vermittelt wurde. Jede Liste konnte mehrere Aufgaben enthalten.

## Neues Datenmodell

### Tabelle `User`

- `id` (PK) - Eindeutige Identifikation des Benutzers
- `username` - Eine Zeichenfolge, die den Benutzernamen enthält (einzigartig)
- `password` - Eine Zeichenfolge, die das Passwort des Benutzers sicher speichert

Die Tabelle `User` hat eine eine-zu-viele Beziehung zu den Tabellen `Todo` und `List`. Das bedeutet, dass ein Benutzer mehrere Aufgaben und Listen erstellen und besitzen kann.

### Tabelle `Todo`

- `id` (PK) - Eindeutige Identifikation der Aufgabe
- `complete` - Ein boolescher Wert, der angibt, ob die Aufgabe abgeschlossen ist oder nicht
- `description` - Eine Zeichenfolge, die die Beschreibung der Aufgabe enthält
- `user_id` (FK) - Ein Fremdschlüssel, der auf den Benutzer verweist, der die Aufgabe erstellt hat

Die Tabelle `Todo` hat eine n:n Beziehung zur Tabelle `List`, die durch die Tabelle `todo_list` vermittelt wird. Das bedeutet, dass eine Aufgabe in mehreren Listen enthalten sein kann, aber auch einem bestimmten Benutzer zugeordnet ist.

### Tabelle `List`

- `id` (PK) - Eindeutige Identifikation der Liste
- `name` - Eine Zeichenfolge, die den Namen der Liste enthält
- `user_id` (FK) - Ein Fremdschlüssel, der auf den Benutzer verweist, dem die Liste gehört

Die Tabelle `List` hat eine eine-zu-viele Beziehung zum Benutzer in der Tabelle `User`. Jede Liste gehört einem bestimmten Benutzer. Die Tabelle `List` hat ebenfalls eine n:n Beziehung zu Aufgaben in der Tabelle `Todo`, vermittelt durch die Tabelle `todo_list`.

Mit diesem erweiterten Datenmodell können Benutzer Konten erstellen, ihre eigenen Aufgaben und Listen verwalten, und die Beziehungen stellen sicher, dass Aufgaben und Listen Benutzern zugeordnet sind.


## Wodurch hebt sich das neue Datenmodell besonders vom vorherigen ab?

1. **Benutzerverwaltung**: Mit dem neuen Modell können Benutzer ihre eigenen Konten erstellen, sich einloggen und Dinge wie Aufgaben und Listen verwalten. Das bedeutet, dass die Anwendung nun weiß, wer welchen Inhalt erstellt hat.

2. **Kontrolle über eigene Sachen**: Jeder Benutzer hat die Kontrolle über seine eigenen Aufgaben und Listen. Kein anderer Benutzer kann auf Ihre Sachen zugreifen oder diese ändern. Das ist so ähnlich wie Ihr eigenes privates Tagebuch.

3. **Individuelle Anpassung**: Jeder Benutzer kann seine Aufgaben und Listen auf seine Art erstellen und anpassen. Das bedeutet, dass die Anwendung sich an Ihre Bedürfnisse anpasst.

4. **Mehr Sicherheit**: Da die Anwendung die Benutzer voneinander trennt, ist Ihre private Information sicherer. Niemand kann in Ihre Sachen schauen, es sei denn, Sie erlauben es.

5. **Keine anonymen Aufgaben mehr**: Mit dem neuen Modell kann die Anwendung sicherstellen, dass jede Aufgabe einem Benutzer gehört. Anonyme Aufgaben sind nicht erlaubt, was die Anwendung zuverlässiger macht.

6. **Einfache Bedienung**: Benutzer können sich abmelden und ihre Konten aus der Datenbank löschen. Das macht die Anwendung benutzerfreundlicher.



## Quellen

1. "Einführung in die Webentwicklung" - Hochschule für Wirtschaft und Recht Berlin. Online verfügbar unter [https://hwrberlin.github.io/fswd/fswd-intro.html#31-the-data-model](https://hwrberlin.github.io/fswd/fswd-intro.html#31-the-data-model). Abgerufen am [01.11.2023].

   Alexander Eck (HWR). Besonders der Abschnitt mit dem Titel "The Data Model" ist relevant für die in dieser Arbeit behandelten Themen.
<br>
<br>
<br>








