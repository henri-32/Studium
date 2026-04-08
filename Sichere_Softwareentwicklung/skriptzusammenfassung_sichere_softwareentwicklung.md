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
Bei CSRF wird eine Anfrage an ein Zielsystem mit Logindaten ausgeführt. Es wird eine falsche Website durch das Opfer aufgerufen, wo es Anmeldedaten eingibt. Diese werden von der Schadsoftware automatisch genutzt um eine Anfrage ans Online Banking zu stellen.
Dabei befindet sich keine Schadsoftware im Zielsystem (Bank)



  


  