# 1. Security by Design
## 1.1 IT Support und Shift left 
SDLC (Software Developement Life Cycle) 
Anforderungsdefinition -> Design -> Umsetzung -> Tests -> Betrieb

"Shift Left" heißt Softwaretests und Sicherheitsmaßnahmen nach links auf der Zeitachse zu verschieben, da sie hier günstiger einfacher und besser umsetzbar sind.  

Bei sicheren Produkten ist die Sicherheit des Kunden ein zentrales Geschäftsziel, nicht nur ein technisches Merkal. 
Secure-by-Design Produkte beginngen mit dem Ziel bevor die Entwicklung beginnt. 
Secure-by-Default sind Produkte die standardmäßig sicher sind und bei denen keine Konfigurationsänderungen für Sicherheits nötig sind und Sicherheitsfunktionen ohne zusätzliche Kosten verfügbar sind. 

Die drei Grundlegenden **Sicherheitsprinzipien** im Bereich Security by Desing sind: 
- Integrität 
- Vertraulichkeit
- Verfügbarkeit

Gemeinsame Grundsätze, die diese Prinzipien umsetzen sind unter anderem: 
- Least-Privilege-Principle
  Benutzer erhalten nur die minimalen rechts, die für ihre Arbeit nötig sind.
  
- Open-Design-Principle
  Der Sicherheitsmechanismus sollte öffentlich sein. Das ist das Gegenteil des Ansatzes "Security by Obscurity".
  (Selbst recherchiert:
      Ein System muss auch dann sicher sein, wenn das Design öffentlich bekannt ist. Die Sicherheit darf nur vom Geheimnis der Schlüssel abhängen, nicht vom Geheimnis der Implementierung
  )

  
- Secure-Defaults-Principle
  Die Software sollte standardmäßig sicher sein mit auf hohem Niveau eingestellter Sicherheits Config.

  
- Fail-Securely-Prinzip
  Die Software sollte auf sichere weise ausfallen. So sollten zum beispiel sensible Daten verschlüsselt werden, damit bei Ausfall diese nicht offengelegt werden.

## 1.2 Infrastructure as Code (IaC)
Die Infrastruktur wird wie die entwickelte Software betrachtet und genauso in Form von Code verwaltet. Die gesamte Config wird im Repo aufbewahrt und mit CI/CD Tools automatisch auf Stabilität und Sicherheit getestet. 
Sie kann dabei deklarativ konfiguriert werden und bietet eine Fallback Ebene. 
IaC hilft bei Sicherheitsaspekten, da Konfigurationen schnell geändert werden können. 
Software-definierte Netzwerke (SDN) sind einfacher zu verwalten. Infrastrukturkomponenten können durch deklarative und domänenspezifische Sprachen konfiguriert werden, es gibt aber auch Tools, die z.Bsp. Python unterstützen. 

## 1.3 Vorteile früher Berücksichtigung von IT-Sicherheit 
OWASP Top 10 ist eine renomminierte List der wichtigen Sicherheitslücken und Risiken für Webanwendungen.

- Zugriffskontrolle defekt
  Wenn ein user einfach die ID in der URL ändern könnte und damit fremde Userdaten bekommt
   
- Kryptografische Fehler
  Wenn Passwörter z.Bsp. im Klartext gespeichert werden, oder Kryptografie entschlüsselt wird.
  
- Injektion
  Ungeprüfte Eingaben werden als Code interpretiert. 
  
- Unsicheres Design
  Nicht nur Implementierung sondern ganzes Design ist unsicher, wenn zum Beispiel jeder über eine Email Anforderung ein Passwort zurücksetzen kann.

  
- Fehlkonfiguration der Sicherheit
  Server läuft z.Bsp. mit DEBUG=True oder /admin ist öffentlich erreichbar.

  
- Anfällige und veraltete Komponenten
  Verwendung unsicherer Libraries

  
- Identifizierungs- und Authentifizierungsfehler
  Login Session Handling fehlerhaft. Die ID bleibt zum beispiel gleich oder es gibt keine Rate Limits.

  
- Software- und Datenintegritätsfehler
    Manipulierte Software oder Daten werden akzeptiert, wenn zum Beispiel ein update Pfad verändert wird und fremde Software geladen wird.

   
- Sicherheitsprotokollierungs- und Überwachungsfehler
  Angriffe werden nicht erkannt, weil zum beispiel bei 1000 fehlgeschlagenen Logins nichts geloggt wird. So wird Brute Force übersehen.

    
- Serverseitige Anforderungsfälschung
  Ein Angreifer bringt den Server dazu Requests an Ziele seiner Wahl auszuführen, indem er deine Netzwerkrechte nutzt.


###  Cross-Site Request Forgery
Bei CSRF wird eine gültige Session des Nutzers für eine gültige Anfrage an ein Zielsystem durch den Angreifer genutzt. Die gültigen Session Daten werden in den Cookies
Des Nutzers gespeichert. Wenn er im Anschluss die Seite des Angreifers aufsucht, wird das dort versteckte Formular mit den Cookies des Nutzers an die Bank gesendet. 
Es befindet sich also keine Schadsoftware im Zielsystem. 

### Cross-Site Scripting (XSS) 
Hier wird bösartiger Code in eine Website oder Anwendung eingeschleust. Es gibt drei Arten von XSS 
1. Reflektiertes XSS
   In einem bösartigen Link oder einer bösartigen E-Mail befindet sich code, der in die URL oder Formulardaten eingebettet ist. Wenn Nutzer auf den Link klicken wird der Code an den
   Webserver gesendet, der ihn an den Browser das Nutzers zurückgibt. Der Browser führt den Code dann aus, als ob er Teil der Website wäre.

2. Gespeicherte XSS
   Bösartiger Code wird auf dem Webserver gespeichert. Wenn man zum Beispiel eine Kommentarfunktion auf der Website hat, kann dort durch Angreifer ein kommentar eingebunden werden, der   Code enthält. Wenn Nutzer den Kommentar aufrufen, wird z.Bsp. versucht ein Bild mit ungültigen Quellcode zu laden, wo ihm Fehlerfall dann das Skript ausgeführt wird.

3. DOM-basiertes XSS
   Angreifer ändern Struktur oder Inhalt des DOM mit Code, er im Browser von Benutzern ausgeführt wird. Wenn zum beispiel eine Website einen Inhalt der Seite auf Grundlage eines URL Parameters anzeigt, kann die URL durch Angreifer erstellt werden, wo sich das skript in der URL befindet, da dieses durch die Webseite aufgerufen wird, für den Inhalt. 

### Server-Side Request Forgery (SSRF) 
Hier wird die Serverseitige Anwendung durch Angreifer dazu gebracht, Anforderungen an eine dritte Stelle zu stellen. Das wird gemacht um Rechte des angegriffenen Servers für Zugriffe zu nutzen, die ohne die Rechte nicht möglich wären. 

### Eingabevalidierung
Eingabevalidierung ist ein wirksames Mittel gegen Injektionsangriffe. Injektionsangriffe ist, wenn über Inputfelder oder Inputpfade fremder Code ausgeführt wird. 

### Maßnahmen im Prozess 
Unsicheres Design kann durch Bedrohungsmodellierung bei Definition der Anforderungen verhindert werden. 
Injektion kann durch Eingabevalidierung bei der Implementierung verhindert werden. 
Softwarefehler können durch IaC bei der Implementierung verhindert werden. 
Kryptographische Fehler können durch Sicherheitstests beim testen erkannt werden. 
Bei defekter Zugriffskontrolle kann auch im Betrieb durch das Least-Privilege Prinzip Schadensbegrenzung betrieben werden. 

# Privacy by Design 
Das Konzept Privacy by Design wurde von Ann Cavoukian entwickelt und umfasst sieben Grundprinzipien: 
1. Proaktiv, nicht reaktiv
   Jedes Produkt sollte so konzipiert sein, dass Risiken zu Beginn des Entwicklungsprozesses erkannt werden werden, statt
   nachträglich behoben werden zu müssen.
2. Datenschutz als Standardeinstellung
   Personenbezogene Daten sollten automatisch geschützt sein.
3. In das Design eingebetteter Datenschutz
4. Volle Funktionalität-Positivsumme, nicht Nullsumme
   Es soll ein Gleichgewicht zwischen Datenschutz, Funktionalität, Benutzerfreundlichkeit und Sicherheit gefunden werden.
5. Ende-zu-Ende-Sicherheit Schutz über den gesamten Lebenszyklus
   Daetnschutz sollte über den gesamten Zyklus in das Produkt integriert werden.
6. Sichtbarkeit und Transparenz
   Gewöhnliche Benutzer sollten die Möglichkeit haben, zu überprüfen, ob angegebene Maßnahmen mit den tatsächlichen Maßnahmen übereinstimmen.
7. Respekt für Privatsphäre von Benutzern
   Die Interessen und Wünsche von Benutzern sollten an erster Stelle stehen. Benutzer sollten immer die Möglichkeit haben, ihre privaten Daten zu verwalten.

Die **Datenschutz-Grundverordnung** fordert die frühzeitige Integration von geeigneten technischen und organisatorischen Maßnahmen zum Schutz personenbezogener Daten.
Die Erfahrung zeigt dabei, dass technische Maßnahmen mehr Wirkung entfalten, da menschliche Fehler weniger zum Tragen kommen.

Beispiele für organisatorische Datenschutzmaßnahmen sind:
   - Erstellung leicht verständlicher Datenschutzbestimmungen
   - Bennenung von einer Person, die im Unternehmen für den Datenschutz verantwortlich ist.
   - Beschränkung des Zugriffs auf  personenbezogene Daten durch eine Organisationsanweisung

   Beispile für technische Datenschutzmaßnahmen sind:
   - Verschlüsselung
   - Verwendung von Zugriffskontrolle und Authentifizierung
   - Anwendung von Anonymisierung oder Pseudonymisierung um den Umfang personenbezogener Daten zu reduzieren
   - Implementierung datenschutzfreundlicher Technologien, wie differentielle Privatheit und homophorbe Verschlüsselung

## 2.1 Verschlüsselung
Es kann zwischen **symmetrischer** und **asymmetrischer** Verschlüsselung unterschieden werden.

### Symmetrische Verschlüsselung
Symmetrische Verschlüsselungsalgorithmen beruhen auf **Substitution** und **Transposition**. 
Substitution ist das Ersetzen eines Zeichens durch ein anderes Zeichen. Das kann monoalphabetisch (Das gleiche Alphabet für die gesamte Nachricht)
oder polyalphabetisch (Mehrere Alphabete für verschiedene Teile der Nachricht) erfolgen. 
Transposition wird die Reihenfolge der Zeichen entsprechend vordefinierter Regeln geändert. Das kann ohne Schlüssel (Ein festgelegtes Muster wird zum Umordnen verwendet)
oder mit Schlüssel (je nach Schlüssel anderes Muster) erfolgen. 
Substitution und Transposition werden in der Praxis gemeinsam verwendet.  
Bei symmetrischer Verschlüsselung verwenden Ver- und Entschlüsselung denselben Schlüssel. 

Es gibt zwei Haupttypen von symmetrischen Verschlüsselungsverfahren 
**Blockchiffren** 
Sie verschlüsseln Daten in Blöcken fester Größe. 
Ihre Sicherheit hängt stark davon ab, mit welchem Modus die Blöcke für die Verschlüsselung verarbeitet werden. 
Das können einfache Aufteilungen sein(unsicher)oder Cipher Block Chaining oder Chipher Feedback, die den Chiffretext des vorherigen Blocks als Eingabe für den nächsten Block verwenden. 

**Stromchiffren**
Hier werden Daten bit- oder byteweise verschlüsselt. 

Block- und Stromchiffren garantieren Vertraulichkeit, nicht aber Integrität oder Authentizät. Dafür müssen die Chiffren mit digitalen Signaturen versehen werden. Das wird als authentifizierte Verschlüsselung bezeichnet. 
Ein MAC (Message Authentification Code) ist ein Datensatz, der zur Überprüfung der Authentizität und Integrität verwendet wird. 
Er wird berechnet, indem eine geheimer Schlüssel und eine Nachricht als Eingaben auf einen kryptografischen Algorithmus angewendet werden, der eine Datei erzeugt(MAC). Dieser MAC wird an eine Nachricht angehängt und dem Empfänger zugesandt. Der kann bei bekanntem Schlüssel und Algorithmus ebenfalls den MAC berechnen, um zu Überprüfen, ob die Nachricht zwischendurch verändert wurde. 

### Asymmetrische Verschlüsselung
Hier werden verschiedene Schlüssel für Ver- und Entschlüsselung verwendet. Ein Schlüsselpaar (einmal öffentlich, einmal privat) wird mathematisch erzeugt. 
Der private Schlüssel ist mathematisch schwer vom öffentlichen abzuleiten. Der öffentliche Schlüssel kann frei verteilt werden. Der private Schlüssel dient zur Entschlüsselung. 
Asymmetrische Verschlüsselung nutzt Funktionen, die in die eine Richtung leicht und in die andere schwer zu berechnen sind. Sie haben aufgrund der mathematischen Komplexität eine sch
lechtere Performanz und längere Schlüssel, als symmetrische Verschlüsselung. 

Symmetrische Verschlüsselung ist deutlich schneller und braucht kürzere Schlüssel für die gleiche Sicherheitskraft. 
Dafür besteht das Problem, dass der Schlüssel sicher ausgetauscht werden muss. 
Das Problem besteht bei asymmetrischer Verschlüsselung nicht, hier muss man allerdings feststellen, welcher öffentliche Schlüssel wem gehört. 

In der praxis wird beides kombiniert. Eine Partei wählt einen zufälligen Schlüssel für ein symmetrisches Verfahren, verschlüsselt in asymmetrisch mit dem öffentlichen Schlüssel der anderen Partei und sendet ihr den Text, den diese mit ihrem privaten Schlüssel entschlüsseln kann. Jetzt haben beide sicher einen Key ausgetauscht für symmetrisches Verfahren, dass auf die ganze Nachricht angewendet werde kann. Damit hat man die performance für die Nachricht aber den Schlüssel sicher über asymmetrische Verfahren ausgetauscht. 

Weiterhin gibt es spezialisierte Schlüsselaustauschprotokolle, die das Problem des hybriden Ansatzes lösen, dass hier nur eine Parte den geheimen Schlüssel wählt, während die andere Partei keine Kontrolle darüber hat. Hier wird der Schlüssel gemeinsam ausgewählt. 

**Hashing** kann für zusätzliche Sicherheit genutzt werden. 
Eine Hashfunktion kann eine Eingabe unterschiedlicher Länge verarbeiten und eine kurze Ausgabe mit fester Länge berechnen. Das ist der Hash-Wert. Wenn zwei Eingaben denselben Wert ergeben ist das eine Kollision. Das ist zwar immer möglich, bei kryptografischen Hash-Funktionen jedoch nicht effizient zu berechnen. 

  


  
