# 7. - Design Desicion für die Benutzerverwaltung

## Inhaltsverzeichnis

  - [Verwendung der Flask-Login-Erweiterung](#verwendung-der-flask-login-erweiterung)
    - [Meta](#meta)
    - [Problemstellung](#problemstellung)
    - [Entscheidung](#entscheidung)
      - [Warum Flask-Login?](#warum-flask-login)
      - [Betrachtete Optionen](#betrachtete-optionen)
      - [Warum Flask-Login über anderen Erweiterungen?](#warum-flask-login-über-anderen-erweiterungen)
    - [Quellen](#quellen)



  ## Verwendung der Flask-Login-Erweiterung

### Meta

Status
: **Entscheidung getroffen**

Updated
: 01-Nov-2023

### Problemstellung

In meinem Projekt stand die Implementierung einer zuverlässigen und sicheren Benutzerverwaltung im Vordergrund. Ich hatte die Herausforderung, Benutzern das Erstellen, Bearbeiten und Löschen von Aufgaben und Listen zu ermöglichen, wobei gleichzeitig die Sicherheit und die individuellen Kontrollmöglichkeiten gewahrt bleiben sollten. Es war auch wichtig sicherzustellen, dass Benutzer nur auf ihre eigenen Daten zugreifen können.

### Entscheidung

#### Warum Flask-Login?

Nach einer oberflächlichen Prüfung verschiedener Flask-Erweiterungen für die Benutzerverwaltung habe ich mich dafür entschieden, die Flask-Login-Erweiterung zu verwenden. Die Entscheidung für Flask-Login basiert auf mehreren wichtigen Faktoren:

**1. Bewährte und weit verbreitete Erweiterung:** Flask-Login hat sich als eine gut etablierte und weit verbreitete Erweiterung für die Benutzerverwaltung in Flask-Anwendungen erwiesen. Sie wird von einer aktiven Entwicklergemeinschaft unterstützt und hat sich in zahlreichen Projekten bewährt.

**2. Flexibilität und Anpassbarkeit:** Flask-Login bietet eine bemerkenswerte Flexibilität und Anpassbarkeit. Ich konnte es nahtlos in meine bestehende Flask-Anwendung integrieren und die Funktionalität nach meinen spezifischen Anforderungen gestalten. Zudem habe ich bereits Erfahrung in einem früheren Projekt (Die App von Gymbrothers) mit Flask-Login gesammelt, was mir bei der Implementierung geholfen hat.

**3. Sicherheit:** Die Sicherheit der Benutzerdaten ist von höchster Bedeutung. Flask-Login enthält Sicherheitsfunktionen wie sicheres Sitzungsmanagement und Passwort-Hashing, die zur Gewährleistung des Datenschutzes und der Sicherheit der Benutzer beitragen.

**4. Benutzerkontrolle:** Flask-Login ermöglicht eine präzise Kontrolle darüber, welche Benutzer auf welche Daten zugreifen können. Dies war für mich von großer Relevanz, da ich sicherstellen wollte, dass Benutzer ausschließlich auf ihre eigenen Aufgaben und Listen zugreifen können.

**5. Dokumentation und Unterstützung:** Flask-Login bietet eine umfassende Dokumentation und wird von einer aktiven Community unterstützt. Dies erleichtert die Entwicklung und Wartung meiner Benutzerverwaltung erheblich.

Es ist erwähnenswert, dass meine Bewertung aufgrund von Zeitbeschränkungen vorläufig ist, da ich nicht alle verfügbaren Erweiterungen gründlich prüfen konnte. Dennoch basiert meine Entscheidung auf einer soliden ersten Einschätzung und meiner vorherigen Erfahrung mit Flask-Login, die sich als äußerst hilfreich erwiesen hat.


### Betrachtete Optionen:

| Erweiterung           | Bekanntheit und Verbreitung | Flexibilität und Anpassbarkeit | Sicherheit | Benutzerkontrolle | Dokumentation und Unterstützung |
| ---------------------  | ---------------------------- | ------------------------------ | ---------- | ----------------- | -------------------------------- |
| Flask-HTTPAuth         | ✔️                           | ✔️                             | ✔️         | ✔️                | ✔️                               |
| Flask-Login            | ✔️                           | ✔️                             | ✔️         | ✔️                | ✔️                               |
| Flask-Praetorian       | ❌                           | ✔️                             | ✔️         | ✔️                | ❌                               |
| Flask-User             | ❌                           | ✔️                             | ✔️         | ✔️                | ✔️                               |

**Flask-HTTPAuth**: Diese Erweiterung ist bekannt und weit verbreitet. Sie bietet Flexibilität, Sicherheit und Benutzerkontrolle. Die Dokumentation und Unterstützung sind ebenfalls gut.

**Flask-Login**: Flask-Login ist ebenfalls bekannt und weit verbreitet. Es zeichnet sich durch Flexibilität und Anpassbarkeit aus und bietet starke Sicherheitsfunktionen. Die Benutzerkontrolle ist granular, und die Dokumentation ist umfassend.

**Flask-Praetorian**: Obwohl weniger bekannt, bietet diese Erweiterung Flexibilität und Sicherheit. Die Benutzerkontrolle ist ebenfalls effektiv. Die Dokumentation und Unterstützung sind jedoch begrenzt.

**Flask-User**: Flask-User ist weniger bekannt, aber bietet Flexibilität und Sicherheit. Die Benutzerkontrolle ist effektiv, und die Dokumentation ist hilfreich.

**Anmerkung**: Aufgrund zeitlicher Einschränkungen habe ich nicht alle verfügbaren Erweiterungen gründlich bewertet. Diese Bewertungen basieren auf meiner ersten Annahme und können sich bei einer detaillierteren Untersuchung ändern.


#### Warum Flask-Login über anderen Erweiterungen?

- **Flask-HTTPAuth**: Obwohl Flask-HTTPAuth für die Authentifizierung nützlich ist, fehlt ihm die tiefergehende Benutzerverwaltung, die Flask-Login bietet. Ich benötigte jedoch umfassendere Benutzerverwaltungsfunktionen.

- **Flask-Praetorian**: Nach einer kurzen Recherche fiel mir auf das Flask-Praetorian ist leistungsstark, aber für meine Anforderungen möglicherweise überdimensioniert. Es bietet Funktionen für die Token-Authentifizierung, die ich nicht benötigte. 






**Quellen:**

1. Flask-Login Dokumentation. Verfügbar unter: [https://flask-login.readthedocs.io/en/latest/](https://flask-login.readthedocs.io/en/latest/)

2. Real Python - "Using Flask-Login for User Management with Flask." Verfügbar unter: [https://realpython.com/using-flask-login-for-user-management-with-flask/](https://realpython.com/using-flask-login-for-user-management-with-flask/)