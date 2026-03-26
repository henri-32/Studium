# 1. Einleitung
## 1.1 Zielsetzung
In der folgenden Arbeit soll zur Teilaufgabe objektorientierter Programmierung (OOP) entsprechend der Aufgabenstellung ein Beispielprogramm entwickelt werden, welches die Prinzipien dieses Paradigmas veranschaulichen kann. Nach Darstellung der theoretischen Grundlagen und Konzepte soll dann auf der Basis des Beispielprogramms, die Umsetzung der beschriebenen Konzepte und ihre Anwendung zur Problemlösung in der Praxis diskutiert werden. 
Der Schwerpunkt soll dabei nicht nur in der technischen Umsetzung, sondern auch in der kritischen Diskussion getroffener Designentscheidungen liegen.
Insbesondere sollen dabei die Möglichkeiten der Nutzung von Vererbung und Methodenüberschreibung zur Spezialisierung von Klassen gezeigt werden, und dabei die expliziten und impliziten Folgen aus diesen Designentscheidungen diskutiert werden. 

## 1.2 Grundidee des Beispielprogramms 
Zur VeranschauUpdatelichung dieser Kernprinzipien wird ein Programm entwickelt, welches als Teil eines hypothetischen Computerspiels verstanden werden kann.
Die Grundidee ist, dass in einer zweidimensionalen Spielwelt segelnde Kriegsschiffe gesteuert werden können, welche auf gegnerische Schiffe schießen und diese versenken können. Zusätzliche Spielobjekte sind Sandbänke, Felsen und Festungen. Das entwickelte Programm konzentriert sich stark auf die semantischen Zusammenhänge zwischen den Objekten, den Schnittstellen, über welche sie miteinander interagieren und die Klassen-/ Vererbungshierarchien, welche genutzt werden um die Semantik zu modellieren. Es bietet dabei keine Implementierung von Spielmechaniken, welche für eine tatsächlich Nutzung notwendig wären, soll aber aufzeigen, wie Userinput, grafische Darstellung oder Belohnungssysteme mit den implementierten Objekten interagieren könnten. 

## 1.3 Verwendete Klassen 
Dazu werden die im Klassendiagramm mit ihren öffentlichen Methoden (API) dargestellten Klassen verwendet.
Bereits an dem Klassendiagramm lassen sich nicht ganz intuitiv und sinnvoll erscheinende Methoden und Beziehungen zwischen den Klassen erkennen (z.Bsp. SandBank erbt eine set_velocity Methode oder CannonBall prüft auf Kollision). Diese werden später kritisch diskutiert. 

![Klassendiagramm](Abbildungen/Klassendiagramm.drawio.png)


# 2. Theoretische Grundlagen
## 2.1 Paradigmen des Programmierens 
Paradigmen des Programmierens beschreiben die grundlegend unterschiedlichen Ansätze, wie man Programme strukturieren und Problemlösungen modellieren kann. Objektorientierte Programmierung ist eine Teilmenge dieser Paradigmen.
Einen Überblick über wichtige Paradigmen liefert Robert Sebesta in seinem Buch "Concepts of Programming Languages" [@sebesta2016].
Es lässt sich grundlegend zwischen imperativen und deklarativen Paradigmen unterscheiden. 
Fundamentale Charakteristik in imperativer Sprache geschriebener Programme ist, dass sie Zustände modellieren, welche sich während der Programmausführung verändern [@sebesta2016, S. 659]. Dieser Kontrollfluss wird dabei mittels expliziter Anweisungen gesteuert. 
Programme, die wiederum einem deklarativen Paradigma folgen, beschreiben das gewünschte Ergebnis und dessen Eigenschaften, während sie die konkrete Ausführung dem System überlassen [@sebesta2016, S. 714]. 
Zu den wichtigsten deklarativen Paradigmen gehören die funktionale und die logische Programmierung.
Funktionale Programmierung basiert auf mathematischen Funktionen. Das hat unter anderem zur Folge, dass (in rein funktionalen Sprachen) Funktionen keine Nebenwirkungen haben, da sie keine nicht-lokalen oder globalen Variablen benötigen [@sebesta2016, S. 660].
Rein funktionelle Sprachen nutzen keine Variablen oder Zuweisungsausdrücke. Wiederholung wird durch Rekursion nicht Iteration modelliert [@sebesta2016, S. 662].
Logische Programmierung basiert hauptsächlich auf formaler Logik 
Programme, die logischer Programmierung folgen stellen dann Sammlungen von Fakten und Regeln dar, welche das System interpretiert. Programme sind dann insofern nutzbar, als dass ihnen Fragen gestellt werden können, welche sie auf Basis der ihnen bekannten Regeln und der formalen Logik beantworten können [@sebesta2016, S. 714].
Zu den wichtigsten imperativen Paradigmen gehören die prozedurale und objektorientierte Programmierung.
Bei prozeduraler Programmierung steht die Ablaufsteuerung des Programms mit sequenzieller Ausführung im Vordergrund und Zustandsänderungen werden über Variablen und Parameter modelliert. Dabei wird mit einer Abfolge von Anweisungen auch die Art und Weise der Programmausführung explizit beschrieben. 
Objektorientierte Programmierung hingegen fokussiert sich auf die Abstraktion von Daten und Datentypen. Dabei werden Daten und Verhalten gekapselt, wodurch Objekte entstehen. Diese können dann miteinander interagieren [@sebesta2016, S. 515]. 

## 2.2 Objektorientierte Programmierung

### 2.2.1 Kapselung  
Kapselung bedeutet, dass Daten und die auf diese Daten bezogenen Methoden in einer Einheit gebündelt werden. Dies unterstützt die technische Trennung von Implementierung und Schnittstelle. [@voigt2010] stellen dar, dass die Nähe von Methoden zu den Daten, auf welchen sie operieren, eine zentrale Charakteristik von Objektorientierung ist. 
Dabei ist Kapselung kein Konstrukt, welches exklusiv in objektorientierter Programmierung verwendet wird. In anderen Paradigmen findet die Kapselung unter anderem durch Modul- und Dateigrenzen statt [vgl @voigt2010, S. 172]. Bei objektorientierter Programmierung wird die Kapselung durch Sprachmechanismen explizit unterstützt, da auf die gekapselten internen Repräsentationen einer Einheit nur noch über definierte Schnittstellen zugegriffen werden kann. 
 
Kapselung wurde im Beispielprojekt vielfach in Form von Klassendefinitionen umgesetzt. Besonders deutlich zeigt sich das Prinzip in der Basisklasse GameObject, wo "property" Methoden genutzt werden.  

![Klassendefinition von GameObjects](Abbildungen/GameObject_init_private_member.png){ width=50% }

Die Kapselung im Sinne von Bündelung der Daten zu einer Einheit findet statt, indem diese als Attribute der Instanz zugeordnet werden. Damit befinden sie sich nicht mehr frei im globalen Namensraum, sondern sind der Instanz der Klasse GameObject zugeordnet. In der Klassendefinition ist "self" der Parameter, welcher die objektorientierte Instanzierungsmechanik in Python repräsentiert. Zugriffe von außen folgen der Syntax "instanzname.attribut". Damit sind die internen Repräsentationen nicht mehr im globalen Namensraum verfügbar (wie hier zum Beispiel x, y), sondern an die jeweilige Instanz gebunden. Das gilt sowohl für Attribute, als auch Methoden. Attribute sind damit in Python jedoch nicht schreib- oder lesegeschützt. 
Im Beispielprogramm werden bei der Instanzierung der Instanzattribute diese zusätzlich durch das "_" Präfix per Konvention als "private" gekennzeichnet.
Das macht deutlich, dass auf diese Attribute nicht von außerhalb der Klasse zugegriffen werden soll. Während einigen Sprachen, wie C++ versuchte Zugriffe von außen durch den Compiler verhindern, erfolgt der Schutz vor Zugriff von außen in Python, bei privaten Attributen vor allem über Konvention. Daher sind Lesezugriffe auf Attribute (je nach Implementierung mit mehr oder weniger Aufwand) immer möglich. Regelmäßig möchte man Schreibzugriffe ausschließlich über definierte Schnittstellen ermöglichen, um zum Beispiel Typsicherheit zu gewährleisten oder die Menge erlaubter Eingabewerte zu definieren. Ein Beispiel dafür sind im Beispielprogramm die x und y Attribute von GameObjects, welche deren Position in der Spielwelt repräsentieren. Hier ist es nicht gewünscht, dass diese von außen manuell verändert werden können. Stattdessen sollen GameObjects einmal an einer definierten Position instanziert werden. Während der Programmausführung darf von außen nur noch die Schnittstelle der Instanzmethode set_velocity(self) zur Positionsänderung genutzt werden, wodurch dieser Zugriff auf Gültigkeit geprüft werden kann. 

![Kontrollierter Zugriff über Instanzmethode](Abbildungen/GameObjects_set_velocity.png){ width=80% }

Über eine Instanzmethode update(self) werden die Attribute _x und _y auf Basis von _speed und _heading transformiert. 
Um diesen Designansatz konsequent zu stärken wurden im Beispielprogramm folgende Instanzmethoden in der Klasse GameObjects definiert:

![Kontrollierter Zugriff auf Instanzattribute durch Getter Methoden](Abbildungen/getter_GameObjects.png "Kontrollierter Zugriff auf Instanzattribute durch Getter Methoden"){ width=50% }

Durch den "property decorator" wird der Zugriff auf ein Attribut über eine Methode vermittelt, ohne, dass sich die Syntax für den zugreifenden Nutzer ändert. 
Ein Ausdruck wie instanz.x stellt nun einen Lesezugriff auf das instanz._x Attribut dar, während die Zuweisung instanz.x = ... ungültig wird, da der Zugriff intern über eine Methode erfolgt, welcher kein Wert zugewiesen werden kann. Damit ist mit einer Mischung aus Konvention (instanz._x = ... ist immer noch möglich) und technischer Umsetzung mittels "property decorator" eine Trennung zwischen interner Repräsentation und externer Nutzung erreicht.    

### 2.2.2 Abstraktion  
Abstraktion ist ein Konzept, welches die Details, **wie** etwas funktioniert vor dem Nutzer versteckt, während ihm gleichzeitig ermöglicht wird, komplexe Funktionalität zu nutzen. Das Gesamtsystem wird also als Model in seiner Komplexität reduziert und auf wesentliche Eigenschaften beschränkt. 
Zur Veranschaulichung gibt es das Modell der Abstraktionsgrenze. Auf der einen Seite dieser Grenze steht die Nutzung der Abstraktion und auf der anderen Seite die Implementierung. Die Abstraktionsgrenze wird während der Softwareentwicklung definiert und die richtige Wahl der Abstraktionsebenen stellt ein wichtiges Qualitätsmerkmal dar [vgl. @jue].
Abstraktion findet dabei auf unterschiedlichsten Ebenen statt und auch sie ist weder ein exklusives Konzept der objektorientierten Programmierung, noch der Informatik selbst. 
Sie ist jedoch ein zentrales Konzept der Informatik und objektorientiertes Programmierung ermöglicht es, sehr granulare Abstraktionen zu definieren und stellt vor allem ein Mittel gegen Komplexität dar [@sebesta_2016, S. 473]. 
Abstraktion und Kapselung wirken ähnlich, was dadurch verstärkt wird, dass sie oft durch dieselben Sprachmechanismen umgesetzt werden. 
So führt eine Klassendefinition gleichzeitig zur Kapselung ihrer Attribute (Verbergen im technischen Sinne der Sichtbarkeit) und zu Abstraktion, da für den Nutzer zugrunde liegende Implemtierungsmechanismen abstrahiert werden und dieser nur noch die Konstruktor Methode aufrufen muss (Verbergen im Sinne von Komplexitätsreduktion durch Vereinfachung).
Es können in der Informatik zwei grundlegende Abstraktionsarten unterschieden werden. Zum einen gibt es die Abstraktion von Daten und zum anderen die Abstraktion von Prozessen [@sebesta_2016, S. 473]. Die Abstraktion von Daten zeigt sich bereits auf der Ebene grundlegender Datentypen von Programmiersprachen. So wird zum Beispiel ein String in Python als abstrakter Datentyp bereitgestellt, dessen nicht unerheblich komplexe interne Repräsentation und Speicherverwaltung dem Nutzer verborgen bleibt.
Im Beispielprogramm zeigt sich Datenabstraktion vor allem an der Verwendung der von Enum erbenden Subklasse DamageState. 

![](Abbildungen/enum.png){ width=40% }

Im Beispielprogramm wird die Mechanik zwar hauptsächlich zur semantischen Strukturierung, Einschränkung des Wertebereichs, sowie zur Vermeidung von Stringvergleichen genutzt, gleichzeitig handelt es sich bei den Attributen um Variablen mit den typisierten Eigenschaften eines Enums. Für den Leser sind die Ausdrücke immer noch leicht als Wörter interpretierbar, während sie im Vergleich zu einem String auf Datenebene unterschiedlich repräsentiert sind, was u.a. numerische Vergleiche ermöglicht.
Prozessabstraktion wird am deutlichsten mit Methodendefinitionen/-aufrufen an verschiedenen Stellen (z.Bsp. s.o. set_velocity Methode von GameObjects) angewendet. Dem Aufrufer muss hierbei lediglich die Signatur der Methode bekannt sein. Dadurch kann die kognitive Last beim Aufrufer reduziert werden, da lediglich die Schnittstelle bekannt sein muss und die Komplexität der Implemantation nicht immer Auswirkung auf die Nutzung der Schnittstelle hat. 

### 2.2.3 Vererbung/Komposition
Einer der großen Vorteile objektorientierter Programmierung, welcher sich durch Kapselung, Abstraktion und Schnittstellendefinitionen ergibt, ist, dass Teile von Programmcode sehr einfach wiederverwendet werden können. Dies kann neben der Nutzung von Schnittstellen als Client durch Vererbung oder Komposition umgesetzt werden, deren Verhältnis häufig mit den Ausdrücken "Ist ein" und "hat ein" beschrieben wird [@salim_nodate].
Im Beispielprogramm ist beides an verschiedenen Stellen implementiert. 
So erben mehrere Klassen von der Klasse Gameobject.

![](Abbildungen/Klassendefinition_Rocks.png){ width=80%}

Das führt dazu, dass bei rock_1 = rock(...) rock_1 Zugriff auf alle Attriute und Methoden von GameObjects ermöglicht. 
Semantisch und technisch bedeutet dies, dass Rock ein GameObject **ist**. Während Rock keine weitergehende Funktionalität biete, als Gameobjects erweitert die Klasse Ship die von GameObjects bereitgestellten Attribute und Methoden, was als Spezialisierung bezeichnet wird. Spezialisierung kann auch in Form von Komposition erfoglgen. 
Dies ist auf zwei leicht unterschiedliche Arten im Code umgesetzt. Zum einen gibt es die eigenständige Klasse Cannon, deren Funktionalität von anderen Klassen integriert wird, indem Klassenattribute von Ship und Fortress als Cannon instanziert werden.

![](Abbildungen/Implementierung_cannon.png){ width=60% }

Nun **hat** Ship ein Cannon Objekt und die Attribute und Methoden von Cannon werden durch das Instanzattribut self._cannon von Ship bereitgestellt. 
Mit shipinstance._cannon.capacity lässt sich nun auf das Cannon Attribut capacity zugreifen. Dass dieser direkte Zugriff möglich ist, zeigt, dass die interne Struktur öffentlich ist und keine strikte Kapselung stattfindet. 
Das oben bereits angeführte Beispiel DamageState wurde im Beispielprogramm nicht im globalen Namensraum definiert, sondern als verschachtelte Klasse innerhalb von DamageModel. Dies sorgt für eine zusätzliche semantische Bindung an die äußere Klasse. Während Cannon sinnhaft durch unterschiedliche Klassen mittels Komposition integriert werden kann, gehört der DamageState klar zu dem Damage Model. Das wird dem Nutzer spätestens klar, wenn er zur Komposition über den Namensraum DamageModel auf DamageState zugreifen müsste. Die Definition innerhalb einer anderen Klasse führt jedoch nicht zur Komposition, da hierdurch noch keine Objektbeziehung hergestellt und noch keine Funktionalität übernommen wird. Erst wenn, wie im Beispiel, eine Instanz von DamageState einem Instanzattribut von DamageModel zugewiesen wird, besteht die Objektbeziehung und es kann von Komposition gesprochen werden. Diese ist technisch identisch mit der Komposition von Cannon/Ship. 

### 2.2.5 Polymorphie und Methodenüberschreibung 
Der Begriff Polymorphie ist im Kontext von Software nicht ganz eindeutig, und wird in unterschiedlichen Quellen verschieden streng ausgelegt. Im sprachlichen Sinn bedeutet Polymorphie Vielgestaltigkeit. Die Polymorphie dient dabei bei objektorientierter Programmierung vor allem der "flexiblen Auswahl geeigneter Methoden identischen Namens anhand des Objekttyps und der Argumentenliste" [@steyer2024, S. 176]. [@kang2010, S. 28] definieren Polymorphismus praxisorientiert als die Fähigkeit von Typ A zu erscheinen und nutzbar zu sein, wie ein anderer Typ B. 
Diese Definition scheint viele Mechaniken objektorientierter Programmierung zu beschreiben. 
Um das Konzept differenziert darzustellen, soll zunächst einmal negativ abgegrenzt werden.
Im Beispielprogramm die Methode shoot() sowohl als Instanzmethode der Klasse Cannon, als auch als Instanzmethode der Klasse Ship implementiert. 

![Instanzmethode der Klasse Ship](Abbildungen/shoot_ship.png){ width=60% }

![Instanzmethode der Klasse Cannon](Abbildungen/shoot_cannon.png){ width=70% }

Die Sinnhaftigkeit dieser Implementierung wird später kritisch diskutiert. 
Wird nun die Methode shoot() durch den Nutzer auf einer Instanz aufgerufen, gibt es zwei Methoden mit identischem Namen. Die ausgeführte Implementierung wird während der Laufzeit durch den Interpreter aufgelöst. Das entspricht auf den ersten Blick der Definition von Polymorphismus, da eine Auswahl der Methode bei identischem Namen anhand des Objekttypes stattfindet. 
Es ist jedoch zu bedenken, dass zwar die beiden Implementierungen von shoot() in ihrer Definition den gleichen Namen tragen, es sich faktisch jedoch um zwei unterschiedliche Methoden, welche nicht über die gleiche Schnittstelle abstrahiert sind, sondern isoliert und gekapselt in unterschiedlichen Klassen und Namensräumen definiert werden. 
ship.shoot() und cannon.shoot() rufen zwei unterschiedliche Methoden mit unterschiedlicher Definition auf, welche im Beispielprogramm nicht technisch strukturell verbunden, sondern lediglich semantisch eng miteinander verknüpft sind, da shipinstance.shoot() intern cannoninstance.shoot() aufruft. 

- [ ] Das hier ist eher Diskusion(
Hier zeigt sich die relativ lockere Kapselung in Pythonprogrammen. Technisch ist es möglich shipinstance._cannon.shoot() mit Parametern aufzurufen, wobei das Ergebnis bis auf die Syntax des Aufrufs keinerlei Bezug zu der Objektinstanz von Ship hat. Hätte man _cannon nicht als privates Attribut definiert und shoot() einen docstring angehängt, der lediglich erklärt, dass x und y die Startkoordinaten der Kanonenkugel sind und heading die Richtung, könnte der Aufruf zu allem Übel für den Nutzer sogar noch sinnvoll erscheinen.)

Polymorphie im engeren Sinn findet sich im Beispielprogramm an der update() Methode. Diese wird als erstes in der Basisklasse GameObject definiert.

![GameObject Methode](Abbildungen/GameObject_update.png){ with=70% }

Anschließend ebenso in den davon erbenden Klassen Rock und Ship. 

![Rock Methode](Abbildungen/Rock_update.png){ width=50% }

![Ship Methode](Abbildungen/Ship_update.png){ width=75%}

Dieses Vorgehen nennt sich Methodenüberschreibung. Wenn die in der Basisklasse implementierte Methode von der Subklasse nicht implementiert wird, steht für Instanzen der Subklasse die Implementierung der Basisklasse zur Verfügung. Wird sie in der Subklasse implementiert, überschreibt diese Implementierung für Instanzen der Subklasse die Implementierung der Basisklasse.
Diese Methodenüberschreibung passiert hier bei Rock und Ship auf unterschiedliche Art. 
Rock überschreibt die update() Methode der Basisklasse mit pass. rockinstance.update() nutzt also nicht mehr die Implementierung von GameObject, sondern macht stattdessen nichts. Das ist als Designentscheidung kritisch zu hinterfragen (siehe Diskusion). 
Ship überschreibt ebenfalls die Implemantation von GameObject, ruft allerdings als erstes mit super().update() (in diesem Fall!) diese Implementierung der Basisklasse auf und erweitert bzw. spezialisiert den Methodenaufruf im Vergleich zur Basisklasse. 
In der Datei mainprogramm.py welche einen kleinen Teil des Programmflusses steuern würde, findet folgender Aufruf statt: 

![Callsite von update()](Abbildungen/main_update_call.png){ width=60% }

Bei game_objects handelt es sich um eine Liste, welche alle instanzierten Objekte beinhaltet, welche von GameObjects erben (und damit wie oben dargestellt ein GameObject **sind**).
über diese wird nun iteriert und auf jedes enthaltene Objekt die für dieses Objekt implementierte update() Methode aufgerufen. 
Dabei handelt es sich um eine polymorphe Schnittstelle, da alle Objekte einheitlich angesprochen werden, während die konkrete Ausführung abhängig vom jeweiligen Objekttyp variiert. Dabei wird diese Verhaltensvarianz vom Typ des Objektes implizit mitgebracht.
Die Polymorphie entsteht nicht nur durch die Methodendefinition, sondern durch die einheitliche Nutzung an einer gemeinsamen Schnittstelle. 
Würden die verschiedenen Implementierungen von update() lose verstreut über das Programm, über ihre Instanzen einzeln aufgerufen werden, wäre das Konzept nicht in gleichem Maße umgesetzt. 

### 2.2.6 Abstrakte Klassen und Methoden 
Wenn normale Klassen vereinfacht gesagt Baupläne für den Interpreter zum Instanzieren von Objekten sind, dann sind abstrakte Klassen Baupläne für den Programmierer zum Entwerfen von Klassen.
In Python wird eine Klasse abstrakt, wenn sie von ABC erbt und mindestens eine abstrakte Methode beinhaltet. Das führt dazu, dass diese Klasse nicht mehr direkt instanzierbar ist. Das Prinzip ist im Beispielprogramm sowohl bei GameObject, als auch bei dem DamageModel umgesetzt. Die semantische Sinnhaftigkeit ist beim DamageModel besonders prägnant. Da es als Fähigkeit, bzw. Mechanik eines Objektes modelliert ist, hätte es ohne dieses keine eigenständige Bedeutung. Deswegen ist eine direkte Instanzierung unerwünscht. 
Abstrakte Methoden haben die Eigenschaft, dass sie durch die Klasse, welche von der abstrakten Klasse erbt, implementiert werden **müssen**, wenn die erbende Klasse instanziert werden soll. Damit wird ein Vertrag definiert, der die Konsistenz der Implementierung in dieser Hinsicht garantiert.
Bei dem DamageModel sind die check_for_collision() und apply_damage_to_abilities() Methoden abstrakt. Diese sollen garantieren, dass Objekte, welche das Schadensmodell implementieren, auch prüfen, ob es zu einer Kollision gekommen ist und das Schadensmodell angewendet werden muss.
Diese Methoden sind als klassische abstrakte Methoden ausgelegt, welche lediglich die Schnittstelle und ihre Signatur festlegen.
Bei der oben dargestellten update() Methode der GameObject Klasse ist der abstractmethod decorator ebenfalls sinnvoll. Damit wird garantiert, dass alle von GameObject abgeleiteten Instanzen eine update() Methode zur Verfügung stellen. Deshalb kann über die Liste der GameObjects iteriert werden, ohne dass bei Aufruf die Gültigkeit des update() Aufrufes sichergestellt werden muss. 
Durch diese abstrakte Methode wird außerdem ein Default-Verhalten bereit gestellt, welches übernommen, erweitert oder überschrieben werden kann. 

### 2.2.7 Mehrfachvererbung und kooperative Methoden
Mehrfachvererbung findet im Beispielprogramm bei den Klassen Ship und Fortress statt. An diesem Beispiel lässt sich die Komplexität von Mehrfachvererbung und die Notwendigkeit für kooperative Methoden zur sauberen Instanzierung aufzeigen. 
Grundlage ist die Method Resolution Order (MRO) von Python, welche die Reihenfolge festlegt, in welcher die übergeordneten Klassen nach passenden Implementierungen durchsucht werden. Zusätvon der MRO Reihenfolge (zlich werden durch die MRO Konflikte aufgelöst, wenn zwei übergeordnete Klassen, von denen geerbt wird, eine gleichnamige Methode bereitstellten [@steyer2024, S. 208]. Dies ist bei der Instanzierung von Ship und Fortress relevant.

![Ship Initialisierung](Abbildungen/Ship_init.png){ width=80% }

Wird der Konstruktor Ship() aufgerufen, werden zunächst einige Argumente an `super().__init__(...)` weitergegeben. Super ruft die nächste Implementierung von `__init__` in der MRO auf, was basierend auf der Reihenfolge in den Klammern der Klassendefinition GameObject ist. Dort werden die benötigten benannten Parameter an die entsprechenden Argumente gebunden. Die Verwendung von **kwargs ermöglicht eine unbestimmte Menge an unbekannten, benannten Parametern weiterzugeben.

![GameObject Init Methode](Abbildungen/GameObject_kwargs.png){ width=90% }

Diese werden am Ende der Methode wiederum mit super() an die nächste gleichnamige Methode in der MRO weitergegeben

![Ende der Initialisierungs Methode](Abbildungen/GameObject_kooperativ.png){ width=50% }

Im Beispiel handelt es sich bei dem betroffenen Parameter um max_health. Die nächste Implementierung in der MRO ist  `DamageModel.__init__(...)` . Daran wird sichtbar, dass super() technisch nicht die Methode der Elternklasse (was hier ABC wäre) aufruft, sondern die Methode, der als nächstes in der MRO erscheinenden Klasse. Ohne den `super().__init__(...)` Aufruf in GameObject würde die MRO Kette dort enden. Dann könnten keine Parameter an DamageModel weitergegeben werden. In DamageModel wird ebenfalls super() aufgerufen, damit weitere Klassen als zusätzliche Basisklassen möglich bleiben. Auch ist deswegen saubere Mehrfachvererbung unabhängig davon möglich, ob DamageModel oder GameObject in der Parameterliste des Konstruktors zuerst aufgeführt wird. 

# 3. Diskussion
## 3.1 Nutzung von Mehrfachvererbung
Die MRO bringt nicht unerhebliche implizite Komplexität mit sich. Während die Initialisierung mit der MRO sinnvoll verkettet werden kann, stellt sich das für Methoden der Ablaufsteuerung schwieriger dar.  





- [ ] [@haberlein2024] muss aktuell evtl aus Literaturverzeichnis entfernt werden.
- [ ] Spezialisierung als Begriff bei Vererbung noch einbringen
- [ ] Diskusion shoot Methoden
- [ ] Diskusion Rock überschreibt update mit pass hat also weniger Funktionalität (wiederspricht SOLID), was außerdem keinen Sinn macht, weil in GameObjects.update die movable Fähigkeit geprüft wird. Wenn man es allerdings mit super() aufrufen würde, wirkt es als würde rock bei update tatsächlich etwas tun + unnötiger Methodenaufruf, wo ich schon weiß, dass nix bei rum kommt -> Fazit falsche Abstraktionsebene von movable. von da in die Diskussion, dass movable aber Eine Fähigkeit ist, die man verlieren kann also Modellierung tiefer in der Vererbungshirarchie in den Typen auch kritisch ist.
- [ ] Diskusion DamageModel könnte abstract sein, wovon geerbt wird, sodass dann mit **kwargs auch DamageModel.update mit kooperativer Vererbung in die super() aufrufe integriert werden würde.
- [ ] Diskussion kooperative update Methode 