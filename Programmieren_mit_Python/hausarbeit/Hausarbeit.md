# 1. Einleitung

In der folgenden Arbeit soll zur Teilaufgabe objektorientierter Programmierung (OOP) entsprechend der Aufgabenstellung ein Beispielprogramm entwickelt werden, welches die Prinzipien dieses Paradigmas veranschaulichen kann. Nach Darstellung der theoretischen Grundlagen und Konzepte soll dann auf der Basis des Beispielprogramms, die Umsetzung der beschriebenen Konzepte und ihre Anwendung zur Problemlösung in der Praxis diskutiert werden. 
Der Schwerpunkt soll dabei nicht nur in der technischen Umsetzung, sondern auch in der kritischen Diskussion getroffener Designentscheidungen.
Insbesondere sollen dabei die Möglichkeiten der Nutzung von Vererbung und Methodenüberschreibung zur Spezialisierung von Klassen gezeigt werden, und dabei die expliziten und impliziten Folgen aus diesen Designentscheidungen diskutiert werden. 

# 2. Theoretische Grundlagen
## 2.1 Paradigmen des Programmierens 
Paradigmen des Programmierens beschreiben die grundlegend unterschiedlichen Ansätze, wie man Programme strukturieren und Problemlösungen modellieren kann. Einen Überblick über wichtige Paradigmen liefert Robert Sebesta in seinem Buch "Concepts of Programming Languages".[@sebesta2016]
Es lässt sich grundlegend zwischen imperativen und deklarativen Paradigmen unterscheiden. 
Fundamentale Charakteristik in imperativer Sprache geschriebener Programme ist, dass sie Zustände modellieren, welche sich während der Prozessausführung verändern. [@sebesta2016, S. 659]Dieser Kontrollfluss wird dabei mittels expliziter Anweisungen gesteuert. 
Programme, die wiederum einem deklarativen Paradigma folgen, beschreiben das gewünschte Ergebnis und dessen Eigenschaften, während sie die konkrete Ausführung dem System überlassen. [@sebesta2016, S. 714] 
Zu den wichtigsten deklarativen Paradigmen gehören die funktionale und die logische Programmierung.
Funktionale Programmierung basiert auf mathematischen Funktionen. Das hat unter anderem zur Folge, dass Funktionen keine Nebenwirkungen haben, da sie keine nicht-lokalen oder globalen Variablen benötigen. [@sebesta2016, S. 660]
Rein funktionelle Sprachen nutzen keine Variablen oder Zuweisungsausdrücke. Wiederholung wird durch Rekursion nicht Iteration modelliert. [@sebesta2016, S. 662]
Logische Programmierung basiert hauptsächlich auf formaler Logik 
Programme, die logischer Programmierung folgen stellen dann Sammlungen von Fakten und Regeln dar, welche das System interpretiert. Programme sind dann insofern nutzbar, als dass ihnen Fragen gestellt werden können, welche sie auf Basis der ihnen bekannten Regeln und der formalen Logik beantworten können.[@sebesta2016, S. 714]
Zu den wichtigsten imperativen Paradigmen gehören die prozedurale und objektorientiere Programmierung. 



# 3. Beispielprogramm
## 3.1 Grundidee und Anforderungen 
