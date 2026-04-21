# 5. Gängige Programmierfehler
## 5.1 Klassen von Bugs 
Häufige Fehler sind: 
- Unsachgemäße Verwendung der dynamischen Speicherzuweisung und -Freigabe.  
  Kann zu Speicherlecks, Dangling Pointern und Segmentierungsfehlern führen. 
  Speicherlecks entstehen, wenn Speicher zugewiesen aber nicht freigegeben wird. 
  Dangling Pointer sind Pointer, die auf Speicher verweisen, der nicht zugewiesen ist. Das führt zu UB
  Segmentierungsfehler treten auf, wenn eine Anwendung versucht auf Speicher zuzugreifen, für den sie keine
  Berechtigung hat. 

- Fehlen von Code Konventionen für die Speicherverwaltung
  Wenn Pointer Typen (Smart Pointer / Raw Pointer) inkonsistent von verschiedenen Entwicklern verwendet werden. 
  
- Ineffiziente und redundante Speichernutzung
  Unnötiges Kopieren großer Objekte oder nicht freigeben führt zu großem Speicherplatz. Das kann in Extremfällen
  zu out-of-memory Fehlern führen 


  
**Common Vulnerabilities and Exposures** 
CVE weist konkreten Instanzen von Sicherheitslücken in Produkten IDs zu, während die Common Weakness Enumerations die zugrunde liegenden 
Mechaniken, wie BufferOverflow typisieren. 

Das Common Vulnerabilities Scoring System (CVSS) weist jeder Sicherheitslücke auf Grundlage von Angriffsvektoren,
Komplexität, Berechtigungsanforderung, Umfang, Integrität und Verfügbarkeit eine Punktzahl zu. 

CPE ist die Common Platform Enumeration, womit sich Betriebssysteme und Hardware typisieren lassen, sodass Sicherheitslücken geordnet werden
können, je nachdem auf welchen Plattformen sie auftreten. 


Schlechte Codepraxis ist ein allgemeiner Begriff, der sich auf unerwünschte oder unprofessionelle Praxis bezieht. 
Ein Anti-Pattern ist eine bereits bekannte und als unwirksam oder schädliche gesehene Implementierungsform ist. 
Schlechte Praxis ist zum Beispiel: 
- Hardcoding von Values und Anmeldedaten
  Es stellt ein Sicherheitsrisiko dar, wenn der Code offengelegt oder gemeinsam genutzt wird, was zu unberechtigtem Zugriff führen kann. 

- Verfrühte Optimierung
  Kann zu komplexem Code führen, der schwer zu lesen und zu pflegen ist. Es ist besser erst kleinen schlanken code zu schreiben und diesen dann 
  zu optimieren. 

- Magic Numbers
  Numerische Werte mit unklarer Bedeutung / Besser benannte Konstanten

- Gottobjekte
  Klassen oder Module, die mit Abhängigkeiten und Verantwortlichkeiten überladen sind.

- Kopieren und Einfügen von nicht verstandenem und getestetem Code

- Inkonsistente oder unklare Namensgebung
  Führt zu schwer lesbarem Code und damit zu Fehlern.

- Schreiben von übermäßig komplexem / verschachteltem Code
  Ebenfalls schwerer zu Lesen, Verstehen und Warten.

- Ignorieren von Fehlerbehandlung und -protokollierung
  Erschwert Fehlersuche

- Fehlende Dokumentation oder Kommentierung des Codes
  Erschwert Verständnis


**Klassifizierung von Bugs** 
Bugs beziehen sich eher auf funktionale Probleme, während Sicherheitslücken sich auf ausnutzbare Sicherheitsprobleme beziehen. 
Bugs können zu abstürzen oder unerwartetem Verhalten führen, stellen aber nicht zwingend Sicherheitslücken dar. 
Softwarebugs können wie folgt klassifiziert werden: 
- Funktionelle Bugs (Ganzer Komponenten)
- Bugs auf Komponentenebene (innerhalb von Funktionen)
- Bugs auf Integrationsebene (Treten erst bei Kombination von Komponenten auf )
- Mängel bei der Benutzerfreundlichkeit (Verhalten der Software führt zu schlechter Nutzerfreundlichkeit, ohne funktionelle Probleme zu machen )
- Leistungsmängel
- Sicherheitsmängel
- Kompatibilitätsmängel
- Syntaxfehler

Sicherheitslücken können ebenfalls klassifiziert werden: 
- Nach den OWASP Kriterien
- Über Bugs Framework (vier Dimensionen: Verhalten, Verwendung, Ziel und Umfang)
  Verhalten beschreibt, was die Sicherheitslücke bewirkt oder ermöglicht.
  Verwendung beschreibt, wie sie ausgenutzt werden kann.
  Ziel beschreibt, warum die Lücke besteht, oder was sie erreichen soll.
  Umfang beschreibt, wo sie sich auswirkt oder zutrifft.


Bugs sind in aller Regel Folgen menschlichen Fehlverhaltens. Ursache dafür kanns sein: 
- Mangel an Wissen

- Mangelndes Bewusstsein

- Menschliches Versagen

- Menschliche Voreingenommenheit bzw. inkorrekte Annahmen

- Menschliche Emotionen


Das kann vermieden werden durch: 
- Information

- Informationsaustausch im Team

- Sicherheitsrichtlienien befolgen

- Code Audits

- Testen

- Software regelmäßig aktualisieren/patchen


Umgebungsfaktoren können sich auch auf die Sicherheit auswirken: 
Dazu gehören: 
- Das Netzwerk kann Integrität und Vertraulichkeit der Daten beeinträchtigen

- Die Hardware kann Leistung, Zuverlässigkeit und Kompatibilität beeinflussen.

- Das Betriebssystem kann Benutzerfreundlichkeit und Sicherheit beeinträchtigen.


Diese Umgebungsfaktoren können aus verschiedenen Gründen Bugs verursachen: 
- Änderungen können Funktionalitäten und Abhängigkeiten ändern, die sich auf die Sicherheit auswirken.
- Interaktion und Integration kann neue Herausforderungen bieten, da über Abhängigkeiten unsicherer Code integriert werden kann.
- Variationen. Software kann in unterschiedlichen Umgebungen unterschiedlich funktionieren.

  Um diese Faktoren zu vermeiden sollten Entwickler:
  - Änderungen und Updates Überwachen
  - Wechselwirkungen überprüfen
  - Software auf verschiedene Umgebungen optimieren.


Der Schweregrad von Bugs hängt ab von: 
- Typ
- Ort und Umfang
- Häufigkeit

Der Schweregrad von Bugs wird in der Regel wie folgt bestimmt: 
- Identifizierung des Bugs
- Bewertung der Auswirkungen auf Funktionalität
- Zuweisung eines Schweregrads
- Priorisierung der Behebung
- Regelmäßige erneute Behebung

Eine typische Skala für die Schwere ist: 
Blocker S1: Software kann nicht verwendet werde 
Kritisch S2: Fehler in geschäftskritischer Funktion
Schwer S3: Fehler in wesentlichem Teil, der aber nicht Nutzung und Testen verhindert
Geringfügig S4: Kleiner Teil der Funktionalität wird beeinträchtigt führt aber z.Bsp. nur zu kosmetischen Problemen 
Trivial S5: Vernachlässigbare Auswirkungen 

Statische Analysetools zur Behebung von Fehlern sind: 
- Compiler
- Linter (Stil und Qualität)
- Code Analyser (Struktur und Logik, können Komplexitäts und Redundanzfehler finden)

Dynamische Analysetools sind: 
- Debugger
- Profiler (Messen von Leistung und Effizienz, können Memory Leaks nd Ressourcenverbrauch finden)
- Test-Tools

Code-Review 
- Peer-Review überprüft Code durch andere Entwickler
- Expert-Review überprüft Code durch (externe) Experten
- Formal-Review überprüft Coe nach einem definierten Prozess oder Verfahren 

# 6. Projektmanagement
## 6.1 Der SDLC
**Lebenszyklus des Projektmanagementes (PMLC)** 
Am häufigsten verwendete Version entwickelt vom PMI (Project Management Institue) folgt einer linearen Struktur und basiert auf dem Wasserfallmodell. 

*Phase 1: Initiierung*
Der Zweck des Projektes wird auf Grundlage der der Anforderungen der Interessengruppen festgelegt. 

*Phase 2: Planung*
Planung ist die Entwicklung eines Projektplans und -umfangs entsprechend des gewählten Managementprozesses, dem Zeitplan und den Endzielen 

*Phase 3: Ausführung*
Ausführung umfasst die Erledigung von Aufgaben, einschließlich der Ressourcenzuweisungen und der eigentlichen Projektdurchführung. 

*Phase 4: Überwachung und Kontrolle* 
Überwachung der Arbeit anhand von Dokumenten und die Schätzung von wichtigen Zielen. 

*Phase 5: Abschluss* 
Die Effizienz der Arbeit während des Projektes wird bewertet und es werden Schlussfolgerungen für die Zukunft gezogen. 

**Software-Development-Life-Cycle (SDLC)**
Der SDLC ist ein Prozess, der Software in der höchsten Qualität und den niedrigsten Kosten in der kürzest möglichen Zeit produziert. 
Die Modellierung des SDLC ist aus drei Gründen notwendig 
1. Es hilft Erwartungen in realistische Bahnen zu lenken
2. Es dient als Grundlage für das Verständnis von Programmiertechnologien
3. Das allgemeine Verständnis über die Entwicklung eines Softwareprojekts liefert Informationen, die für seine Planung und Ressourcenmanagement hilfreich sind.

Die Phasen des SDLC umfassen typischerweise: 
1. Planung
2. Analyse der Anforderungen
3. Design
4. Umsetzung und Testen
5. Wartung und Unterstützung

Neben dem Wasserfall und agilen Methoden kommen das *Inkremental-* und das *Spiralmodell* zum Einsatz.
Das SDLC Modell sollte anhand der Anforderungen des zugrunde liegenden Projektes ausgewählt werden. 

Während der PMLC das übergeordnete Projekt managed, technologieunabhängig ist und sich auf externe Seiten, wie Personal, Kosten und Ressourcen, bezieht sich der SDLC auf die technische Umsetzung des Produkts. Er befasst sich mit den Einzelheiten der Softwareentwicklung des Produkts. 

**Software Systemdesign** 
Er ist der Prozess der Erstellung eines Systemprojekts. Grundlage davon ist eine Softwareanforderungsanalyse (SRA). Die Prinzipien des Systemdesigns können in folgende Gruppen unterteilt werden: 

SOLID Principles: 
 - Single Responsibility
 - Open/Closed Principle
 - Liskov-Substitution Principle
 - Interface Segregation
 - Dependency Inversion 

 DRY Principles: 
 Don't repeat yourself 

 KISS Principles:
 Keep it stupid simple 

 YAGNI Principles: 
 You aren't gonna need it 

 **Entwicklung nach agilen Methoden** 
 Die Wasserfallmodelle eignen sich gut für kleine oder gut planbare Projekte. 
 Da allerdings immer eine Phase zuende gebracht werden muss, bevor die nächste Phase beginnt, kann es im schlimmsten Fall passieren, dass das Ergebnis eine Phase oder des ganzen Produkts nicht den Erwartungen entspricht. 
 Soll innovative oder ergebnisoffene Software entwickelt werden, kommen agile Methoden zum Einsatz. Sie gewährleisten Prozessflexibilität und bessere iterative Kontrolle. 

 Der Grundgedanke ist, dass zunächst mit dem Standardprodukt begonnen wird und dieses dann iterativ zusamen mit dem Kunden an die Kundenbedürfnisse angepasst wird. 
 Es werden zeitlich begrenzte Phasen "Sprints/Timeboxes" definiert. Zu Beginn dieser Phasen werden Aufgaben festgelegt, die zusammen mit dem Kunden priorisiert werden. Am Ende des Sprints bewerten Kunden und Anbieter zusammen die Arbeit. Das erleichtert Kostenzufriedenheit und bindet die Kunden eng in den Entwicklungsprozess ein, was zu erhöhter Kundenzufriedenheit führen kann.

 **Scrum**
 ist ein Framework, was für Projekte konzipiert ist, die schnelle Ergebnisse fordern und tolerant gegenüber Änderungen sind. Das Projekt wird in "Product Items" zerlegt, die im "Product Backlog" gesammelt werden. Scrum verlangt, dass die Teams klein und funktionsübergreifend sind. 
 
 Die Grundstruktur von Scrum-Prozessen umfasst etwa fünf Hauptmeetings: 
 1. Backlog-Refinement-Meeting
 2. Sprint Planung
 3. tägliche Meetings
 4. Sprint Nachbesprechung
 5. Sprint Retrospetkive

**Lean**
fügt agilen Prozessen ein Workflow-Schema hinzu, damit die Iterationen die gleiche Qualität haben. Mit diesem Workflow-Schema werden alle Aufgaben bearbeitet. Das hat Vorteile für die Struktur, ist aber für große und heterogene Aufgaben ungeeignet. 
Lean unterscheidet strikt zwischen 
A) Was ist der Kunde bereit zu zahlen (Value)
B) alles andere (Waste)

**Kanban** 
Bei Kanban kann bei sich ändernder Priorität von Aufgaben eine gerade bearbeitete Aufgabe verlassen werden. Es gibt im Konzept weniger strenge Struktur, als bei Scrum. 
So können Teammitglieder auch mehrere Aufgaben gleichzeitig erledigen. 
Kanban besteht aus vier Säulen 
1. Für jede Aufgabe wird eine individuelle Karte erstellt, die alle notwendigen Informationen über die Aufgabe enthält. 
2. Die Anzahl der Aufgaben pro Stufe ist begrenzt
3. kontinuierlicher Fluss bedeutet, dass Aufgaben aus einem Rückstand in der Reihenfolge ihrer Dringlichkeit in den Fluss integriert werden.
4. Es gibt eine kontinuierliche Verbesserung des Prozesses

Es geht hierbei um einen kontinuierlichen Arbeitsfluss der optimiert werden soll. Dieser wird weniger im Voraus geplant. Es gibt außerdem ein hartes Limit, dass nur eine maximale Anzahl von Prozessen gleichzeitig bearbeitet werden darf.

## 6.2 Schwachstellen-Management 
Sicherheitslücken haben häufig einen hohen oder kritischen Schweregrad, der zu Remote-Angriffen und vollständigem Verlust der Verfügbarkeit führen können. 

**CVE (Common Vulnerabilitys and Exposures)**
Datenbank für reale Sicherheitslücken z.Bsp. konkrete Lücke in OpenSSL Version X 

**CWE (Common Weakness Enumeration)**
Katalog von Fehlerarten z.Bsp. BufferOverflow

**CVSS (Common Vulnerability Scoring System)**
Misst und kategorisiert den Schweregrad von Sicherheitslücken 

**OWASP** für Websicherheit

Das Managment von Sicherheitslücken besteht aus vier Hauptphasen: 
1. Scannen
   Durch invasive Tests(Simulation echter Angriffe) oder nicht-invasive Tests (Strukturanalyse) s.a. SAST vs. DAST
2. Risikobewertung
   Die beim Scannen entdeckten Sicherheitslücken sollten kategorisiert und priorisiert werden. Siehe CWE.
   Die Betriebsumgebung der Software sollte anhand der CVSS Skala bewertet werden.
3. Reporting
   Die Ergebnisse werden zusammenfassend mit Empfehlungen vorgestellt.
4. Umsetzung von Änderungen

Die Entdeckung von Sicherheitslücken ist erwartbar. Daher sollten sich Unternehmen darauf vorbereiten, zum beispiel durch klare Meldewege, Rollen und Verantwortlichkeiten. 
Es sollte auch noch außen verantwortungsvoll kommuniziert werden. 

## 6.3 Patch-Management 
Es gibt einen mehrstufigen Ansatz Operational Technology (OT) / Industrial Control System (ICS) Patch Management beschrieben wird. 
Er besteht aus sechs Schritten: 
1. Erstellung eines Basisinventars
2. Sammeln von Informationen über Software-Patches und Sicherheitslücken
3. Identifizierung der Relevanz von Sicherheitslücken
4. Review, Genehmigen und Abschwächen des Patch-Managements
   Hier werden die Grundlinien entwickelt, wonach aus den verfügbaren Patches gefiltert wird.
5. Testen und Bereitstellen
6. Dokumentation

## 6.4 Management von Pentest- und Bug-Bounty-Programmen 
Es kann zwischen drei Arten von Pentests unterschieden werden: 
1. White-Box-Pentest: Testerinnen erhalten Zugriff auf Quellcode. So können sowohl externe, als auch interne Angriffe simuliert werden.
2. Black-Box-Pentest: Simulierter Hackerangriff
3. Gray-Box-Pentest: Tester verfügen über Teilinformationen

Ein Pentests besteht aus fünf Phasen: 
1. Vorbereitung
2. Ausarbeitung eines Angriffsplans
3. Spezifizierung des Datentyps
4. Durchführung der Tests
5. Interpretation der Ergebnisse

Ein Pentest Bericht sollte Folgendes Enthalten 
- Fehlerbeschreibung
- Wie er gefunden wurde
- Verwendete Tools
- Bedingungen für das Auftreten des Fehlers
- Eine Datei, die den Bug reproduzieren lässt
- Auswirkungen auf die Organisation
- Vorschläge zur Fehlerbehebung


Ein Bug-Bounty-Programm belohnt das auffinden von Sicherheitslücken. Das ist oft Teil der Sicherheitsstrategie von Unternehmen. 
Pentests sind zeitlich befristete Projekte, während Bounty-Programme unbefristet laufen können. 


