# 1. Einleitung
## 1.1 Zielsetzung
In der folgenden Arbeit soll zur Teilaufgabe objektorientierter Programmierung (OOP) entsprechend der Aufgabenstellung ein Beispielprogramm entwickelt werden, welches die Prinzipien dieses Paradigmas veranschaulichen kann. Nach Darstellung der theoretischen Grundlagen und Konzepte soll dann auf der Basis des Beispielprogramms, die Umsetzung der beschriebenen Konzepte und ihre Anwendung zur Problemlösung in der Praxis diskutiert werden. 
Der Schwerpunkt soll dabei nicht nur in der technischen Umsetzung, sondern auch in der kritischen Diskussion getroffener Designentscheidungen liegen.
Insbesondere sollen dabei die Möglichkeiten der Nutzung von Vererbung und Methodenüberschreibung zur Spezialisierung von Klassen gezeigt werden, und dabei die expliziten und impliziten Folgen aus diesen Designentscheidungen diskutiert werden. 

## 1.2 Grundidee des Beispielprogramms 
Zur Veranschaulichung dieser Kernprinzipien wird ein Programm entwickelt, welches als Teil eines hypothetischen Computerspiels verstanden werden kann.
Die Grundidee ist, dass in einer zweidimensionalen Spielwelt segelnde Kriegsschiffe gesteuert werden können, welche auf gegnerische Schiffe schießen und diese versenken können. Zusätzliche Spielobjekte sind Sandbänke, Felsen und Festungen. Das entwickelte Programm konzentriert sich stark auf die semantischen Zusammenhänge zwischen den Objekten, den Schnittstellen, über welche sie miteinander interagieren und die Klassen-/ Vererbungshierarchien, welche genutzt werden um die Semantik zu modellieren. Es bietet dabei keine Implementation von Spielmechaniken, welche für eine tatsächlich Nutzung notwendig wären, soll aber aufzeigen, wie Userinput, grafische Darstellung oder Belohnungssysteme mit den implementierten Objekten interagieren könnten. 

## 1.3 Verwendete Klassen 
Das Beispielprogramm weist folgende Grundmechaniken auf, welche in diesen Basisklassen abgebildet werden:

- Gameobjects bzw. modellieren Objekte, welche in der Spielwelt miteinander interagieren
  (Zur Veranschaulichung von Vererbung, Komposition, Kapselung und Methodenüberschreibung)

- Das DamageModel bildet ein minimalistisches Schadensmodell für einige Objekte ab.
  (Zur Veranschaulichung von Mehrfachvererbung und Methodenüberschreibung)

- Das CollisionModel ist ein Modul, welches ein Interface für Kollissionsituationen zwischen Gameobjects bietet
  (Zur Veranschaulichung von Abstraktion. Weiterhin notwendig, um die verschiedenen Methoden der Klassen schlüssig miteinander zu verbinden)

Die semantischen Objekte werden durch hiervon abgeleitete Subklassen implementiert und interagieren dabei wie folgt miteinander:

- Schiffe:
  Schiffe lassen sich durch den/die Spieler in der 2D Welt bewegen und sind in der Lage Kanonenkugeln abzufeuern.
  Sie implementieren außerdem ein minimalistisches Schadensmodell, sodass sie in ihren Fähigkeiten eingeschränkt oder "verloren gehen" können.

- Kanonenkugeln:
  Kanonenkugeln können Schiffe und Festungen beschädigen.

- Sandbänke und Felsen:
  Sie sind passive Spielelemente, welche bei Kollision unterschiedliche Folgen auf die Fähigkeiten der Schiffe haben. 

# 2. Theoretische Grundlagen
## 2.1 Paradigmen des Programmierens 
Paradigmen des Programmierens beschreiben die grundlegend unterschiedlichen Ansätze, wie man Programme strukturieren und Problemlösungen modellieren kann. Objektorientierte Programmierung ist eine Teilmenge dieser Paradigmen.
Einen Überblick über wichtige Paradigmen liefert Robert Sebesta in seinem Buch "Concepts of Programming Languages".[@sebesta2016]
Es lässt sich grundlegend zwischen imperativen und deklarativen Paradigmen unterscheiden. 
Fundamentale Charakteristik in imperativer Sprache geschriebener Programme ist, dass sie Zustände modellieren, welche sich während der Programmausführung verändern. [@sebesta2016, S. 659]Dieser Kontrollfluss wird dabei mittels expliziter Anweisungen gesteuert. 
Programme, die wiederum einem deklarativen Paradigma folgen, beschreiben das gewünschte Ergebnis und dessen Eigenschaften, während sie die konkrete Ausführung dem System überlassen. [@sebesta2016, S. 714] 
Zu den wichtigsten deklarativen Paradigmen gehören die funktionale und die logische Programmierung.
Funktionale Programmierung basiert auf mathematischen Funktionen. Das hat unter anderem zur Folge, dass (in rein funktionalen Sprachen) Funktionen keine Nebenwirkungen haben, da sie keine nicht-lokalen oder globalen Variablen benötigen. [@sebesta2016, S. 660]
Rein funktionelle Sprachen nutzen keine Variablen oder Zuweisungsausdrücke. Wiederholung wird durch Rekursion nicht Iteration modelliert. [@sebesta2016, S. 662]
Logische Programmierung basiert hauptsächlich auf formaler Logik 
Programme, die logischer Programmierung folgen stellen dann Sammlungen von Fakten und Regeln dar, welche das System interpretiert. Programme sind dann insofern nutzbar, als dass ihnen Fragen gestellt werden können, welche sie auf Basis der ihnen bekannten Regeln und der formalen Logik beantworten können. [@sebesta2016, S. 714]
Zu den wichtigsten imperativen Paradigmen gehören die prozedurale und objektorientierte Programmierung.
Bei prozeduraler Programmierung steht die Ablaufsteuerung des Programms mit sequenzieller Ausführung im Vordergrund und Zustandsänderungen werden über Variablen und Parameter modelliert. Dabei wird mit einer Abfolge von Anweisungen auch die Art und Weise der Programmausführung explizit beschrieben. 
Objektorientierte Programmierung hingegen fokussiert sich auf die Abstraktion von Daten und Datentypen. Dabei werden Daten und Verhalten gekapselt, wodurch Objekte entstehen. Diese können dann miteinander interagieren. [@sebesta2016, S. 515] 

## 2.2 Objektorientierte Programmierung
### 2.2.1 Abstraktion 
### 2.2.2 Kapselung
### 2.2.3 Vererbung / Komposition 
### 2.2.4 Polymorphie

