**Lektion 1 Security by Design** 

SDLC 
1. Definition der Anforderungen 
2. Design 
3. Umsetzung
4. Tests
5. Betrieb

Grundsätze von Secure-by-Design 
- Least-Privilege-Prinzip 
- Open-Design-Prinzip 
- Secure-Defaults-Prinzip 
- Fail-Securely-Prinzip 

OWASP Top 10 
1. Zugriffskontrolle defekt
2. Kryptografische Fehler
3. Injektion
4. Unsicheres Design 
5. Fehlkonfiguration der Sicherheit 
6. Anfällige/veraltete Komponenten
7. Identifizierungs und Authentifizierungsfehler 
8. Software und Datenintegritätsfehler 
9. Sicherheitsprotokollierungs und Überwachungsfehler 
10. Serverseitige Anforderungsfälschung

**Lektion 2 Privacy by Design** 
Sieben Grundprinzipien von Privacy by Design 
1. Proaktiv nicht reaktiv 
2. Datenschutz als Standardeinstellung
3. In das Design eingebetteter Datenschutz
4. Volle Funktionalität bei Datenschutz
5. Schutz über den gesamten Lebenszyklus
6. Sichtbarkeit und Transparenz für gewöhnliche Nutzer
7. Respekt für die Privatsphäre von Nutzern 

Beispiele organisatorischer Datenschutzmaßnahmen
- Erstellung leicht verständlicher Bestimmungen 
- Bennenung einer Person im Team, die in der Organisation für 
	Privatsphäre verantwortlich ist
- Beschränkung des Zugriffs auf personenbezogene Daten durch 
	Organisationsanweisung

Eigenschaften von Zero-Knowledge-Beweisen 
- Vollständigkeit (Bei wahrer Aussage wird überzeugt) 
- Korrektheit (Bei falscher Aussage kann nicht überzeugt werden) 
- Nichtoffenlegung (Die verifizierende Partei erfährt nichts, als dass 
	die Aussage wahr ist) 



**Lektion 3 Tests und Audits** 
Die Testpyramide besteht aus 
1. Unit-Tests
2. Integrationstests
3. E2E-Tests

Andere Tests die nicht Teil der Pyramide sind sind zum Beispiel UI oder explorative Tests. 
Diese beziehen sich eher auf die Nutzeroberfläche, während E2E das gesamte System aus der Perspektive der Endnutzer testet. 

Fehler beim schreiben von Unit-Tests
- Testen von fremdem Code 
- Testen der Datenbankverbindung
- Tests im Nachhinein schreiben 
- Tests nach Refactor nicht aktualisieren
- Tests schreiben, die weder Unit noch Akzeptanztests sind 

Praktiken beim Schreiben von Integrationstests
- Definition des Umfangs und der Ebene des Tests
	Dazu gehören Bottom-up Top-down Sandwich und Big Bang Strategien
- Wahl geeigneter Instrumente und Frameworks
- Schreiben sauberen Testcodes der den Prinzipien des TDD folgt 
- Verwenden von Mocks um externe Abhängigkeiten zu simulieren
- Gleichgewicht zwischen Geschwindigkeit und Umfang 
- Effektive Verwaltung der Testumgebung 

Ansätze für Systemtests sind 
- Funktionstests 
- Leistungstests
- Sicherheitstests
- non-destructive Tests 
- destructive Tests (Lasttests bis zur Belastungsgrenze) 
- Statische Tests 
- E2E-Tests

Gängige Arten von Sicherheitstests sind
- Sicherheitslücken-Scans
- Penetrationstests
- SAST
- DAST 
- Interaktive Anwendungssicherheitstests
- Sicherheitsaudits 

Tools für Sicherheitstests sind z.Bsp. 
- Webapplikationsscanner
- Netzwerkscanner 
- Codeanalysetools
- Fuzzingtools
-Proxy-Tools 

**Lektion 4 Sicherheit der Softwarelieferkette** 
Wichtige Bereiche der Sicherheit im Entwicklungsprozess sind 
1. Paketsicherheit (Sicherheit der Pakete und Abhängigkeiten) 
2. Containersicherheit 
3. CI/CD 

Tools Paketsicherheit 
- GitHub Actions
- Bright Security
- UpGuard 

Gefahren für Container
- Manipulation von Images 
- Veraltete Komponenten 
- Unsichere Kommunikation 

Schritte zur Sicherung von Containern 
- Verwendung vertrauenswürdiger Quellen 
- Regelmäßiges Scannen 
- Verschlüsselung und Signierung von Images 
- Sicherer Zugriff auf Registries 
- Überwachung und Prüfung der Registries auf Manipulation 


Wahl der Programmiersprache anhand von
- Anforderungen des Projekts
- Verwendeten Technologien 
- Aktuellen und künftigen Nutzbarkeit der Sprache 
- Verfügbarkeiten von Bibliotheken 
- Komplexität der Sprache 
- Vielseitigkeit der Sprache 

Beispiele für schlechte Programmierung 
- Feste Codierung von Werten und Anmeldedaten 
- Verfrühte Optimierung 
- Magic Numbers 
- Gottobjekte 
- Kopieren von nicht verstandenem Code 
- inkonsistente Namensgebung 
- übermäßig komplexer Code 
- Ignorieren von Fehlerbehandlung und Protokollierung
- Fehlende Doku/Kommentierung 

	 
- 



