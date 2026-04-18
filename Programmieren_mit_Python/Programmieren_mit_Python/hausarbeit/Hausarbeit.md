# IU - Internationale Hochschule -- Fernstudium

**Modul:** DLMDWPMP01

**Tutor:** Dr. Thomas Kopsch

**Semester:** 1. Semester -- Vollzeit (Masterzugangsprüfung)

**Studiengang:** Ms.Sc. Informatik

**Hausarbeit**

**Die Herausforderung von Modellierung in der objektorientierten
Programmierung**

Eine kritische Analyse anhand eines Beispielprogramms

Eingereicht am 05.04.2026

**Verfasser:\
**Kirchhoff, Henri

Postweg 16

59597 Erwitte

**E-Mail:** <henrikirchhoff@gmail.com>

**Matrikelnummer:** 10249630

#  Inhaltsverzeichnis {#inhaltsverzeichnis .TOC-Heading}

[1. Einleitung 3](#__RefHeading___Toc561_1536768055)

[2. Theoretische Grundlagen 3](#theoretische-grundlagen)

[2.1 Paradigmen des Programmierens 3](#paradigmen-des-programmierens)

[2.2 Objektorientierte Programmierung
4](#objektorientierte-programmierung)

[2.2.1 Kapselung 4](#kapselung)

[2.2.2 Abstraktion 6](#__RefHeading___Toc571_1536768055)

[2.2.3 Vererbung/Komposition 7](#vererbungkomposition)

[2.2.5 Polymorphie und Methodenüberschreibung
8](#polymorphie-und-methodenüberschreibung)

[2.2.6 Abstrakte Klassen und Methoden
10](#abstrakte-klassen-und-methoden)

[2.2.7 Mehrfachvererbung und kooperative Methoden
11](#mehrfachvererbung-und-kooperative-methoden)

[3. Diskussion von Designentscheidungen
14](#diskussion-von-designentscheidungen)

[3.1 Wann ist ein Objekt eine Klasse?-Probleme intuitiver
Objektmodellierung
14](#wann-ist-ein-objekt-eine-klasse---probleme-intuitiver-objektmodellierung)

[3.2 Vermischung von Typ und Zustand als Modellierungsfehler
14](#vermischung-von-typ-und-zustand-als-modellierungsfehler)

[3.3 Falsche Verantwortungszuordnung durch Vererbung und Komposition
15](#falsche-verantwortungszuordnung-durch-vererbung-und-komposition)

[3.4 Mehrfachvererbung als Quelle von Komplexität
16](#mehrfachvererbung-als-quelle-von-komplexität)

[4. Herausforderungen bei der Modellierung mit objektorientierter
Programmierung
17](#herausforderungen-bei-der-modellierung-mit-objektorientierter-programmierung)

[4.1 Einordnung der behandelten Herausforderungen
17](#einordnung-der-behandelten-herausforderungen)

[4.2 Die Wahl von Abstraktionsebenen
18](#die-wahl-von-abstraktionsebenen)

[4.3 Objektorientierung als verstärkender Faktor von Designfehlern
18](#objektorientierung-als-verstärkender-faktor-von-designfehlern)

[5. Fazit und Reflexion 19](#fazit-und-reflexion)

# 

# 

# **1. Einleitung**

In der folgenden Arbeit soll zur Teilaufgabe objektorientierter
Programmierung (OOP) entsprechend der Aufgabenstellung ein
Beispielprogramm entwickelt werden, welches die Prinzipien dieses
Paradigmas veranschaulichen kann. 
Dazu sollen die theoretischen Grundlagen und Konzepte, mit dem Fokus auf 
Vererbung und Methodenüberschreibung, kurz dargestellt
und am Beispielprogramm veranschaulicht werden.  
Anschließend sollen Designentscheidungen kritisch diskutiert werden 
und die Herausforderungen beim Einsatz objektorientierter Programmierung, 
insbesondere hinsichtlich passender Modellierung von Problemen erörtert werden.
Die Analyse des Beispielprogramms zeigt, dass die zentrale Herausforderung
objektorientierter Programmierung nicht in der technischen Umsetzung,
sondern in der Modellierung des Problemraums liegt.

# **2. Theoretische Grundlagen**

## **2.1 Paradigmen des Programmierens**

Paradigmen des Programmierens beschreiben grundlegende Ansätze, wie
Programme strukturiert und Probleme modelliert werden können.
Objektorientierte Programmierung ist dabei eines von mehreren
Paradigmen. Einen Überblick liefert Sebesta (Sebesta 2016).
Grundsätzlich lässt sich zwischen imperativen und deklarativen
Paradigmen unterscheiden. Imperative Programme modellieren Zustände, die
sich während der Ausführung durch explizite Anweisungen verändern
(Sebesta 2016, S. 659). Deklarative Programme hingegen beschreiben
gewünschte Ergebnisse und deren Eigenschaften, während die konkrete
Ausführung dem System überlassen wird (Sebesta 2016, S. 714). Zu den
wichtigsten imperativen Paradigmen zählen die prozedurale und die
objektorientierte Programmierung. Während prozedurale Programmierung die
Ablaufsteuerung in den Vordergrund stellt, fokussiert sich
objektorientierte Programmierung auf die Bündelung von Daten und
Verhalten in Objekten (Sebesta 2016, S. 515). Diese Unterscheidung ist
für die vorliegende Arbeit insofern relevant, als dass objektorientierte
Programmierung zwar spezifische Strukturierungsmechanismen bereitstellt,
jedoch keine Garantie für eine geeignete Modellierung des Problemraums
liefert.

## **2.2 Objektorientierte Programmierung**

### **2.2.1 Kapselung**

Kapselung bedeutet, dass Daten und die auf diese Daten bezogenen
Methoden in einer Einheit gebündelt werden. Dies unterstützt die
Trennung von Implementierung und Schnittstelle. (Voigt et al. 2010)
stellen dar, dass die Nähe von Methoden zu den Daten, auf denen sie
operieren, eine zentrale Charakteristik objektorientierter
Programmierung ist.

Kapselung ist dabei kein exklusives Konzept objektorientierter
Programmierung, sondern findet sich auch in anderen Paradigmen,
beispielsweise durch Modul- und Dateigrenzen (vgl. Voigt et al. 2010, S.
172). In objektorientierten Sprachen wird sie jedoch gezielt durch
Sprachmechanismen unterstützt, da auf interne Repräsentationen einer
Einheit nur noch über definierte Schnittstellen zugegriffen werden kann.

Im Beispielprogramm wird Kapselung durch Klassendefinitionen umgesetzt.
Attribute und Methoden werden dabei an Instanzen gebunden und sind nicht mehr Teil
des globalen Namensraums. Der Zugriff erfolgt über die definierte Schnittstelle des Namensraumes.

Da Python keine strikte Zugriffskontrolle erzwingt, wird zusätzlich mit
Konventionen gearbeitet (z. B. „\_" für interne Attribute).
Schreibzugriffe werden über Methoden gesteuert, während lesende Zugriffe
über Properties erfolgen. Dadurch entsteht eine Trennung zwischen
interner Repräsentation und externer Nutzung, auch wenn diese technisch
nicht vollständig erzwungen wird.

Am Beispiel der Positionsattribute (\_x, \_y) zeigt sich dieser Ansatz:
Eine direkte Manipulation ist nicht vorgesehen; stattdessen erfolgt die
Veränderung über die Methode set_velocity(), während die eigentliche
Positionsänderung intern im Update-Zyklus berechnet wird. Auf diese
Weise kann die Gültigkeit von Zustandsänderungen kontrolliert werden.

### **2.2.2 Abstraktion**

Abstraktion ist ein Konzept, welches die Details, wie etwas funktioniert
vor dem Nutzer versteckt, während ihm gleichzeitig ermöglicht wird,
komplexe Funktionalität zu nutzen. Das Gesamtsystem wird in seiner
Komplexität auf ein Modell reduziert, also auf wesentliche Eigenschaften
beschränkt. Die Abstraktionsgrenze (Auf der einen Seite steht die
Nutzung, auf der anderen die Implementierung) wird während der
Softwareentwicklung durch den Entwickler definiert und die richtige Wahl
der Abstraktionsebenen stellt ein wichtiges Qualitätsmerkmal dar (vgl.
Jue and Bowman, n.d.). Abstraktion ist ein zentrales Konzept der
Informatik und objektorientiertes Programmieren ermöglicht es,
individuelle, modulare und granulare Abstraktionen zu definieren. Sie
stellt dabei vor allem ein Mittel gegen Komplexität dar (Sebesta 2016,
S. 473). Abstraktion und Kapselung wirken ähnlich, was dadurch verstärkt
wird, dass sie oft durch dieselben Sprachmechanismen umgesetzt werden.
So führt eine Klassendefinition gleichzeitig zur Kapselung ihrer
Attribute (Verbergen im technischen Sinne der Sichtbarkeit) als auch zu
Abstraktion, da für den Nutzer zugrunde liegende
Implementierungsmechanismen abstrahiert werden. Dieser kann diese Methoden über 
den simplen Aufruf der
Konstruktor Methode nutzen (Verbergen im Sinne von Komplexitätsreduktion
durch Vereinfachung). Es kann zwischen der Abstraktion von Daten und von
Prozessen unterschieden werden (Sebesta 2016, S. 473). Im
Beispielprogramm zeigt sich Datenabstraktion vor allem an der Verwendung
der, von Enum erbenden, Subklasse DamageState.

> class DamageModel(ABC):
>
> class DamageState(Enum):
>
> OK = 3
>
> DAMAGED = 2
>
> UNMANEUVERABLE = 1
>
> DESTROYED = 0

*Siehe Anhang B.*

Im Beispielprogramm wird die Mechanik zwar hauptsächlich zur
semantischen Strukturierung, Einschränkung des Wertebereichs, sowie zur
Vermeidung von Stringvergleichen genutzt, jedoch handelt es sich bei den
Attributen um Variablen mit den typisierten Eigenschaften eines Enums.
Für den Leser sind die Ausdrücke immer noch leicht als Wörter
interpretierbar, während sie im Vergleich zu einem String auf Datenebene
unterschiedlich repräsentiert sind, was u.a. numerische Vergleiche
ermöglicht. Prozessabstraktion wird am deutlichsten mit
Methodendefinitionen/-aufrufen an verschiedenen Stellen (z.Bsp. s.o.
set_velocity Methode von GameObjects) angewendet. Dem Aufrufer muss
lediglich die Signatur bekannt sein und die kognitive Last beim Aufrufer
ist nicht zwingend abhängig von der Komplexität der Implementierung.	

### **2.2.3 Vererbung/Komposition**

Einer der großen Vorteile objektorientierter Programmierung, welcher
sich durch Kapselung, Abstraktion und Schnittstellendefinitionen ergibt,
ist, dass Teile von Programmcode sehr einfach wiederverwendet werden
können. Dies wird insbesondere durch Vererbung und Komposion umgesetzt
wird, deren Verhältnis häufig mit den Ausdrücken "Ist ein" und "hat ein"
beschrieben wird (Salim, ohne Datum). Im Beispielprogramm ist beides an
verschiedenen Stellen implementiert. erben mehrere Klassen von der
Klasse GameObject.

> class Rock(GameObject):
>
> def \_\_init\_\_(self, ID: int, x: int, y: int, width: int, height:
> int):
>
> super().\_\_init\_\_(
>
> ID=ID, x=x, y=y, movable=False, width=width, height=height
>
> )

*Siehe Anhang C.*

Das führt dazu, dass Instanzen von Rock alle Attribute und Methoden der Klasse GameObject bereitstellen.	 
Semantisch
und technisch bedeutet dies, dass Rock ein GameObject **ist**. Rock
bietet hier keine über GameObject hinausgehende Funktionalität. Im
Gegensatz dazu erweitert die Klasse Ship die, von GameObjects
bereitgestellten, Attribute und Methoden, was als Spezialisierung
bezeichnet wird. Spezialisierung kann auch in Form von Komposition
erfolgen. Diese ist auf zwei leicht unterschiedliche Arten im Code
umgesetzt. Zum einen gibt es die eigenständige Klasse Cannon, deren
Funktionalität von den Klassen Ship und Fortress integriert wird, indem
Klassenattribute von diesen als Cannon Objekt instanziert
werden.

> self.\_cannon = Cannon(
>
> capacity=cannon_capacity,
>
> collision_model=collision_model,
>
> objects_list=game_objects,
>
> )

*Siehe Anhang C.*

Nun **hat** Ship ein Cannon Objekt und die Attribute und Methoden von
Cannon werden über das Instanzattribut self.\_cannon von Ship
bereitgestellt. Mit shipinstance.\_cannon.capacity lässt sich auf das
Cannon zugehörige Attribut capacity zugreifen. Dass dieser direkte
Zugriff möglich ist, zeigt, dass die interne Struktur öffentlich ist und
keine strikte Kapselung stattfindet. Das oben bereits angeführte
Beispiel DamageState wurde im Beispielprogramm nicht im globalen
Namensraum definiert, sondern als verschachtelte Klasse innerhalb von
DamageModel. Dies sorgt für eine zusätzliche semantische Bindung an die
äußere Klasse. Während Cannon sinnhaft durch verschiedene Klassen
mittels Komposition integriert werden kann, gehört der DamageState
eindeutig zu dem Damage Model. Das wird dem Nutzer spätestens klar, wenn
er zur Komposition über den Namensraum DamageModel auf DamageState
zugreifen müsste. Die Definition innerhalb einer anderen Klasse führt
jedoch nicht zur Komposition, da hierdurch keine Objektbeziehung
hergestellt und keine Funktionalität übernommen wird. Erst wenn, wie im
Beispiel, eine Instanz von DamageState einem Instanzattribut von
DamageModel zugewiesen wird, besteht die Objektbeziehung und es kann von
Komposition gesprochen werden. Diese ist technisch identisch mit der
Komposition von nicht verschachtelten Klassen.

### **2.2.5 Polymorphie und Methodenüberschreibung**

Der Begriff Polymorphie ist im Kontext von Software nicht ganz
eindeutig, und wird in unterschiedlichen Quellen verschieden streng
ausgelegt. Im sprachlichen Sinn bedeutet Polymorphie Vielgestaltigkeit.
Die Polymorphie dient dabei bei objektorientierter Programmierung vor
allem der "flexiblen Auswahl geeigneter Methoden identischen Namens
anhand des Objekttyps und der Argumentenliste" (Steyer 2024, S. 176).
(Kang and Yang 2010, S. 28) definieren Polymorphismus praxisorientiert
als die Fähigkeit als Typ A zu erscheinen und genauso nutzbar zu sein,
wie ein anderer Typ B. Diese Definition scheint viele Mechaniken
objektorientierter Programmierung zu beschreiben. Um das Konzept
differenziert darzustellen, soll zunächst negativ abgegrenzt werden. Im
Beispielprogramm ist die Methode shoot() sowohl als Instanzmethode der
Klasse Cannon, als auch als Instanzmethode der Klasse Ship
implementiert.

> def shoot(self) -\> None:
>
> self.\_cannon.shoot(self.x, self.y, self.\_heading)

Instanzmethode Ship (Siehe Anhang C.)

> def shoot(self, x: int, y: int, heading: int) -\> None:

> aim = heading - 90

> if aim \< 0:
>
> aim += 360
>
> shot = CannonBall(
>
> x=x,
>
> y=y,
>
> collision_model=self.collision_model,
>
> objects_list=self.objects_list,
>
> )
>
> shot.set_velocity(20, aim)

Instanzmethode Cannon (Siehe Anhang C.)

Die Sinnhaftigkeit dieser Implementierung wird später kritisch
diskutiert. Wird nun die Methode shoot() durch den Nutzer
aufgerufen, gibt es augenscheinlich zwei Methoden mit
identischem Namen. Die ausgeführte Implementierung wird während der
Laufzeit durch den Interpreter aufgelöst. Das entspricht auf den ersten
Blick der Definition von Polymorphie, da eine Auswahl der Methode bei
identischem Methodennamen anhand des Objekttyps stattfindet. 
Es handelt sich jedoch um voneinander unabhängige Methoden aus verschiedenen Namensräumen, 
welche im Beispielprogramm nicht technisch strukturell gleich, sondern lediglich semantisch eng
miteinander verknüpft sind. shoot ist dabei nur ein Teil des jeweils vollständigen Namens.
Der tatsächliche Aufruf erfolgt über ship.shoot bzw. cannon.shoot. 

Polymorphie im engeren Sinn findet sich im Beispielprogramm bei der
update() Methode. Diese wird zunächst in der Basisklasse GameObject
definiert.

> \@abstractmethod
>
> def update(self) -\> None:
>
> if self.\_movable:
>
> self.\_apply_velocity()

*Siehe Anhang A.*

Anschließend ebenso in den davon erbenden Klassen Rock und Ship.

> def update(self) -\> None:
>
> pass

Instanzmethode Rock (Siehe Anhang C.)

> def update(self) -\> None:
>
> super().update()
>
> self.check_for_collision()
>
> DamageModel.update(self)
>
> self.apply_damage_to_abilities()

Instanzmethode Ship (Siehe Anhang C.)

Dieses Vorgehen nennt sich Methodenüberschreibung und ist auf zwei
unterschiedliche Arten implementiert.
Rock überschreibt die Methode von GameObject und implementiert eine
eigene, welche sich vollständig anders verhält als die Implementierung der Basisklasse.
Ship überschreibt technisch die Methode von GameObject ebenfalls vollständig mit 
der eigenen Implementierung. Allerdings wird mit der Methode super() in dieser die Implementierung 
von GameObject aufgerufen und anschließend weitere Methodenaufrufe ausgeführt. 
So wird die Implementierung der Basisklasse erweitert, statt vollständig ersetzt.

In der Datei simulation.py welche einen kleinen Teil des
Programmflusses steuern würde, wird die update() Schnittstelle wie folgt
aufgerufen:

> for obj in game_objects:
>
> if obj.is_alive:
>
> obj.update()
>
> else:
>
> objects_to_remove.append(obj)

*Siehe Anhang D.*

Auch hier befinden sich die jeweiligen update Implementierungen in verschiedenen
Namensräumen. Jedoch handelt es sich hier um eine polymorphe Schnittstelle, da alle Objekte
einheitlich angesprochen werden, während die konkrete Ausführung
abhängig vom jeweiligen Objekttyp variiert. 
obj.update() ruft über den selben Namen verschiedene dynamisch an diesen
gebundene Implementierungen auf. Diese Verhaltensvarianz wird
vom Typ des Objektes implizit gehalten und mitgebracht. Polymorphie
entsteht somit nicht durch die Implementierung von Methoden mit gleichem
Namen allein, sondern durch die einheitliche Nutzung dieser an einer
gemeinsamen Schnittstelle.

### **2.2.6 Abstrakte Klassen und Methoden**

Wenn normale Klassen vereinfacht gesagt Baupläne für den Interpreter zum
Instanzieren von Objekten sind, dann sind abstrakte Klassen Baupläne für
den Programmierer zum Entwerfen von Klassen. Dabei sind abstrakte
Klassen nicht direkt instanzierbar. Das Prinzip ist im Beispielprogramm
sowohl beim GameObject, als auch beim DamageModel umgesetzt. Die
semantische Sinnhaftigkeit ist beim DamageModel besonders prägnant. Da
es als Fähigkeit, bzw. Mechanik eines Objektes modelliert ist, hätte es
ohne dieses keine eigenständige Bedeutung. Deswegen ist eine direkte
Instanzierung unerwünscht. Abstrakte Methoden haben die Eigenschaft,
dass sie durch die Klasse, welche von der abstrakten Klasse erbt,
implementiert werden **müssen**, wenn die erbende Klasse instanziert
werden soll. Damit wird ein Vertrag definiert, der die Konsistenz der
Implementierung in dieser Hinsicht garantiert. Bei dem DamageModel sind
die check_for_collision() und apply_damage_to_abilities() Methoden
abstrakt. Diese sollen garantieren, dass Objekte, welche das
Schadensmodell integrieren, auch prüfen, ob es zu einer Kollision
gekommen ist und das Schadensmodell angewendet werden muss. Diese
Methoden sind als abstrakte Methoden ausgelegt, welche lediglich die
Schnittstelle und ihre Signatur festlegen. Die oben dargestellt update()
Methode von GameObject ist ebenfalls abstrakt. Damit wird garantiert,
dass alle von GameObject abgeleiteten Instanzen eine update() Methode
zur Verfügung stellen. Deshalb kann über die Liste der GameObjects
iteriert werden, ohne dass bei Aufruf die Gültigkeit des Aufrufes
sichergestellt werden muss. Durch diese abstrakte Methode wird, anders
als bei den o.g. Methoden, zusätzlich ein Default-Verhalten bereit
gestellt, welches übernommen, erweitert oder überschrieben werden kann.

### **2.2.7 Mehrfachvererbung und kooperative Methoden**

Mehrfachvererbung findet im Beispielprogramm bei den Klassen Ship und
Fortress statt. Grundlegend dafür ist in Python die Method Resolution
Order (MRO), welche die Reihenfolge festlegt, in welcher die
übergeordneten Klassen nach passenden Implementierungen durchsucht
werden. Zusätzlich werden von der MRO Konflikte aufgelöst, wenn zwei
übergeordnete Klassen eine gleichnamige Methode bereitstellen (Steyer
2024, S. 208). Dies ist bei der Instanzierung von Ship und Fortress
relevant, da sowohl GameObject, als auch DamageModel eine
`__``init``_``_(``)` Methode implementieren. Das bedeutet in der Folge, dass Ship bei
der Instanzierung alle von den übergeordneten `__``init``_``_(``)`
Methoden erwarteten Parameter bereitstellen und korrekt weitergeben
muss. 
Diese strukturierte Übergabe der Parameter basiert auf der MRO und 
wird im Beispielprogramm wie folgt mit kooperativen Methoden
umgesetzt:

> class Ship(GameObject, DamageModel):
>
> def \_\_init\_\_(
>
> self,
>
> ID: int,
>
> x: int,
>
> y: int,
>
> width: int,
>
> height: int,
>
> max_health: int,
>
> cannon_capacity: int,
>
> collision_model: CollisionModel,
>
> game_objects: list\[GameObject\],
>
> ) -\> None:
>
> super().\_\_init\_\_(
>
> ID=ID,
>
> x=x,
>
> y=y,
>
> movable=True,
>
> width=width,
>
> height=height,
>
> max_health=max_health,
>
> )
>
> self.\_speed = 5
>
> self.\_collision_model = collision_model
>
> self.\_cannon = Cannon(
>
> capacity=cannon_capacity,
>
> collision_model=collision_model,
>
> objects_list=game_objects,
>
> )

*Siehe Anhang C.*

Wird der Konstruktor von Ship aufgerufen, werden zunächst einige Argumente
an `super().__``init``__(...)` gebunden. super() ruft die nächste
Implementierung von `__``init``__` in der MRO auf, was im Beispiel die
 `__``init``_``_(``)` Methode von GameObject ist.

> class GameObject(ABC):
>
> def \_\_init\_\_(
>
> self,
>
> x: int,
>
> y: int,
>
> movable: bool,
>
> ID: int = 0,
>
> width: int = 10,
>
> height: int = 10,
>
> \*\*kwargs,
>
> ) -\> None:
>
> self.\_ID = ID
>
> self.\_x_pos = x
>
> self.\_y_pos = y
>
> self.\_width = width
>
> self.\_height = height
>
> self.\_is_alive = True
>
> self.\_movable = movable
>
> self.\_speed = 0
>
> self.\_heading = 0
>
> super().\_\_init\_\_(\*\*kwargs)

*Siehe Anhang A.*

Die Verwendung von \*\*kwargs ermöglicht eine
unbestimmte Menge von unbekannten, benannten Parametern weiterzugeben.
Diese werden am Ende der Methode wieder mit super() an die nächste
Implementierung von update() in der MRO weitergegeben.
Im Beispiel wird max_health mittels \*\*kwargs an die 
nächst höhere Implementierung von `__``init``__` weitergegeben. 
Diese folgt der MRO und ist hier in der Klasse
DamageModel zu finden. Daran wird sichtbar, dass super() technisch nicht
zwingend die Methode der Elternklasse (was hier ABC wäre) aufruft,
sondern die Methode, der als nächstes in der MRO folgenden Klasse.
Ohne den `super(``).__``init``__(...)` Aufruf in GameObject würde die
MRO Kette dort enden. Dann könnten keine Parameter an DamageModel
weitergegeben werden und die Initialisierung von mehreren Basisklassen
wäre nicht möglich. In der Implementierung von `__``init``_``_(``)`
in DamageModel wird ebenfalls `super().__``init``__(...)` aufgerufen, damit weitere Klassen als
zusätzliche Basisklassen möglich bleiben.

# **3. Diskussion von Designentscheidungen**

## **3.1 Wann ist ein Objekt eine Klasse? - Probleme intuitiver Objektmodellierung**

Objektorientierte Programmierung ermöglicht es Semantik, Verantwortung
und Verhalten in Objekten zu bündeln. Das weist große Nähe zur
intuitiven Beschreibung realer Objekte (Schiffe, Autos, Tiere etc.) auf.
Alltagsnahe Beispiele wie „Ein Schiff hat eine Kanone und kann damit
schießen" lassen sich leicht als Klassen in eine Vererbungshierarchie
integrieren. Diese Nähe zum intuitiven Verständnis kann jedoch
irreführend sein, da nicht jede sprachlich beschreibbare Entität
sinnvoll als Klasse modelliert werden sollte. Bei Betrachtung der Klasse
Cannon zeigt sich, dass ihre Funktionalität ausschließlich in der
Instanzierung von CannonBall Objekten und semantisch in der Fähigkeit
„Schießen" liegt. Das Verhalten „Schießen" ist dabei eng an die Klassen
Ship und Fortress gebunden. Die Klasse Cannon kapselt kein eigenständiges Verhalten, sondern stellt
lediglich einen indirekten Aufrufmechanismus dar. Daher lässt sich im Beispielprogramm nicht
überzeugend begründen, warum Cannon als eigene Klasse modelliert werden
sollte. Diese Designentscheidung
führt dazu, dass zusätzliche Abstraktion und indirekte Struktur
eingeführt werden, ohne Mehrwert in Form von Komplexitätsreduktion zu
erreichen. Dieses Beispiel verdeutlicht, dass die Existenz einer
semantisch und sprachlich zuverlässig beschreibbaren Entität kein ausreichendes
Argument für ihre Modellierung als Klasse darstellt, sondern hierfür die 
Verantwortung im System ausschlaggebend ist.

## **3.2 Vermischung von Typ und Zustand als Modellierungsfehler**

Die Klasse GameObject hält das Zustandsattribut \_movable, welches als
Bedingung für die Ausführung der Bewegungslogik dient. Die Schwierigkeit
bei der Modellierung dieser Eigenschaft liegt darin, dass semantisch eng
miteinander verbundene Konzepte auf unterschiedlichen Systemebenen
abgebildet werden müssten. Die Zustandsvariable \_movable beschreibt zum
einen die grundlegende Fähigkeit eines Objekttyps, sich in der Spielwelt
bewegen zu können. Zum anderen wird sie als veränderlicher Zustand
verwendet, der dynamisch durch das DamageModel beeinflusst werden kann,
um Manövrierunfähigkeit zu simulieren. Im Beispielprogramm werden somit
Typmerkmal, Verhalten und auf die Spielmechanik bezogener Zustand in
einer einzigen Variable zusammengeführt. Zusätzlich wird diese Variable
auf einer sehr hohen Ebene der Vererbungshierarchie definiert, um eine
einheitliche Schnittstelle für das Schadensmodell bereitzustellen und zu garantieren. Diese
Schnittstelle hat fachlich eine völlig fremde Verantwortung und wird
hier über die Basisklasse in sämtliche davon erbende Objekte strukturell
integriert. Die Auswirkungen dieser Entscheidung zeigen sich
insbesondere in den abgeleiteten Klassen. Objekte wie Rock oder
SandBank, die sich konzeptionell nicht bewegen können, erben trotzdem
Methoden und Attribute zur Bewegungssteuerung. Da dieses Verhalten für
die Objekte nicht sinnvoll ist, wird es durch Überschreiben der Methode
update() verhindert. Der Umstand, dass Funktionalitäten der Basisklasse
entfernt werden müssen, stellt ein starkes Indiz dafür dar, dass keine
ausreichend enge semantische Beziehung zwischen den Klassen besteht, um
eine Modellierung durch Vererbung zu rechtfertigen. Darüber hinaus führt
die Vermischung von Typmerkmal und Zustand zu impliziten Kopplungen im
System. Änderungen an der Schadenslogik wirken sich direkt auf die
Bewegungsfähigkeit aus, obwohl es sich konzeptionell um unterschiedliche
Aspekte handelt. Dies erschwert die Erweiterbarkeit und reduziert
Klarheit. Eine sauberere alternative Modellierung würde diese Ebenen
explizit voneinander trennen. Die grundsätzliche Bewegungsfähigkeit
könnte durch unterschiedliche Basisklassen modelliert werden, während
der aktuelle Bewegungszustand unabhängig davon als dynamische
Eigenschaft der Instanz geführt werden könnte. Die Bewegungslogik selbst
ließe sich ähnlich zur Kollisionslogik als eigenständige
Systemkomponente modellieren, die auf Grundlage der Instanzzustände
arbeitet, anstatt implizit in der Vererbungshierarchie eingebunden zu
sein.

## **3.3 Falsche Verantwortungszuordnung durch Vererbung und Komposition**

Im Beispielprogramm wird DamageModel als eigene Klasse definiert, was
sich im Gegensatz zur Cannonproblematik insofern rechtfertigen lässt,
als dass es eine Spielmechanik mit eigener Zuständigkeit kapselt. Die
Integration in die Klassenhierarchie ist jedoch problematisch. Ship erbt
von GameObject und DamageModel, was impliziert, dass Ship ein
DamageModel ist. Das ist nicht korrekt, da Ship lediglich dessen
Mechanik nutzt. Ein daraus resultierendes Problem ist, dass die
Schadenslogik zwingend Teil aller potenziellen von Ship oder Fortress
erbenden Klassen wird. Auch der Umstand, dass sich die Methoden der
Basisklassen von Ship nicht sinnvoll über super() kombinieren lassen,
spricht dafür, dass die Klassenbeziehungen strukturell unstimmig sind.
Im Gegensatz dazu wird das CollisionModel über Komposition in die
entsprechenden Klassen integriert. Diese Entscheidung vermeidet die beim
DamageModel entstehenden Probleme, ist jedoch in anderer Hinsicht
ebenfalls nicht sinnvoll umgesetzt. Die Kollisionserkennung stellt keine
objektspezifische Eigenschaft dar, sondern modelliert eine systemweite
Mechanik, die mit der Summe aller GameObjects arbeitet. Durch die
Integration in einzelne Objekte wird diese Systemverantwortung
fälschlicherweise dezentralisiert. So erfordert die Instanzierung eines
Ship, dass eine Liste aller existierenden GameObjects übergeben wird.
Dies stellt einen klaren Hinweis für falsche Verantwortungszuordnung
dar. Hierdurch entsteht eine enge Kopplung zwischen globaler Spiellogik
und lokalen Objektinstanzen. Das erschwert die Nachvollziehbarkeit und
Testbarkeit des Systems. Es zeigt sich, dass weder die Verwendung von
Vererbung noch von Komposition per se zu einer geeigneten Modellierung
führt, nur weil ihre Anwendung technisch möglich ist. Entscheidend ist
die korrekte Zuordnung von Verantwortlichkeiten im Gesamtsystem.
Insbesondere Vererbung setzt dabei eine konsistente „ist ein"-Beziehung
voraus, die im vorliegenden Modell nicht gegeben ist.

## **3.4 Mehrfachvererbung als Quelle von Komplexität**

Mehrfachvererbung erzeugt zusätzliche implizite Komplexität. Während
sich die `__``init``__` Methoden der Basisklassen von Ship sinnvoll
kooperativ verknüpfen lassen, führt derselbe Ansatz bei Methoden zur
Ablaufsteuerung in der update() Methode zu strukturellen Problemen.

> def update(self) -\> None:
>
> super().update()
>
> self.check_for_collision()
>
> DamageModel.update(self)
>
> self.apply_damage_to_abilities()

*Siehe Anhang C.*

Hier wird die GameObject Implementierung von update() mit super()
aufgerufen, während die Implementierung von update() der zweiten
Basisklasse DamageModel explizit über die Klasse auf die eigene Ship
Instanz aufgerufen wird. Es wäre auch möglich beides kooperativ in
super() aufzurufen. Allerdings werden hier mehrere Verantwortlichkeiten
verarbeitet, die semantisch voneinander abhängen. Ihre Reihenfolge ist
daher nicht beliebig. Die Bewegung der Objekte in der Spielwelt sollte
abgeschlossen sein, bevor die Kollisionsprüfung erfolgt. Diese ist
wiederum semantische Voraussetzung dafür, dass das Schadensmodell
angewendet wird.

Ein kooperativer Aufruf beider Basisklassenmethoden würde die
semantische Reihenfolge zwingend brechen. Entweder würde das
Schadensmodell vor der Kollisionserkennung, oder die Bewegungslogik nach
der Kollisionserkennung aktualisiert werden. Es zeigt sich, dass eine
gemeinsame Schnittstelle nur dann sinnvoll ist, wenn der gemeinsame
Aufruf der Methoden auch semantisch sinnvoll gebündelt werden kann. Sind
die Verantwortlichkeiten der Basisklassen stark unterschiedlich dürfte
dies regelmäßig nicht der Fall sein. Bei komplexen MRO Strukturen wird
zusätzlich die Aufrufreihenfolge innerhalb von super() implizit und ist
nicht mehr direkt steuerbar. Daher stellt sich die Frage ob die
Abstraktion der Mehrfachvererbung für Aufgaben der Ablaufsteuerung
geeignet ist. Der Nutzer muss der MRO und Klassenhirarchie folgen um
feststellen zu können, welche Aufrufe erfolgen und welche Nebenwirkungen
damit verbunden sind. Die benötigten Informationen sind dabei teilweise
implizit und dezentral im Programm verteilt. Ein expliziter prozeduraler
Methodenaufruf wirkt an der Aufrufstelle zwar weniger elegant, wäre in
diesem Fall aber vermutlich klarer und wartbarer als die beschriebene
Herangehensweise.

# **4. Herausforderungen bei der Modellierung mit objektorientierter Programmierung**

## **4.1 Einordnung der behandelten Herausforderungen**

Die im letzten Kapitel dargestellten Schwierigkeiten erscheinen zunächst
als Folge objektorientierter Mechaniken. Die Zuordnung von Entitäten zu
Klassen ist ausschließlich im Rahmen objektorientierter Programmierung
erforderlich. Die Vermischung von Typ und Zustand wirkt problematisch,
weil Verhalten im Objekttyp verankert werden kann. Die strukturelle
Kopplung durch Vererbung entsteht erst durch die Existenz von
Vererbungsmechanismen, und die Komplexität der Mehrfachvererbung ist ein
spezifisches Problemfeld objektorientierter Programmierung. Bei
genauerer Betrachtung zeigt sich jedoch, dass keines dieser Probleme
technischer Natur ist. Die dargestellten Implementierungen sind
syntaktisch korrekt und lassen sich technisch problemlos ausführen. Die
eigentliche Herausforderung liegt also auf der Ebene der Modellierung.
Objektorientierte Programmierung stellt Werkzeuge zur Verfügung, mit
denen Problemräume strukturiert werden können. Die technisch korrekte
Anwendung dieser Werkzeuge führt jedoch nicht zwangsläufig zu einer
Modellierung, die den zugrunde liegenden Problemräumen gerecht wird.
Während die Implementierung von Vererbungshierarchien in einfachen
Lehrbuchbeispielen wie Autos oder Tieren unproblematisch erscheint,
steigt die Komplexität der Modellierung, sobald Objekte miteinander
interagieren und semantisch unterschiedliche Funktionalitäten
bereitstellen sollen. Das stellt jedoch keine spezifische
Herausforderung objektorientierter Programmierung, sondern eine
Herausforderung beim Programmieren unabhängig vom zugrundeliegenden
Paradigma dar.

## **4.2 Die Wahl von Abstraktionsebenen**

Wie zuvor dargestellt, ist ein Kerngedanke objektorientierter Techniken
die Nutzung von Abstraktionen zur Komplexitätsreduktion. So wie die
Anwendung objektorientierter Techniken nicht automatisch zu korrekter
Modellierung führt, führt auch die Nutzung von Abstraktion nicht
automatisch zum gewünschten Ergebnis der Komplexitätsreduktion. Gerade
am Beispiel der Mehrfachvererbung, welche verschiedene interne
Mechaniken abstrahiert und eine sehr einfache Nutzung an der
Aufruferseite ermöglicht, zeigt sich, dass das implizite Ausblenden
relevanter Programmteile im Ergebnis zu erhöhter Komplexität führen
kann. Die Wahl der Abstraktionsebene ist damit entscheidend. An vielen
Stellen muss abgewogen werden, wie weit abstrahiert werden kann, ohne
dass für den Nutzer notwendige Informationen verloren gehen.
Gleichzeitig muss bewertet werden, ob eine Abstraktion tatsächlich zur
Reduktion von Komplexität beiträgt oder lediglich bestehende
Designfehler verdeckt.

## **4.3 Objektorientierung als verstärkender Faktor von Designfehlern**

Auch wenn die dargestellten Herausforderungen nicht exklusiv auf
objektorientierte Programmierung beschränkt sind, können bestimmte
technische Eigenschaften objektorientierter Programmierung diese
Probleme verstärken. Zum einen werden Designentscheidungen früh im
Programm strukturell verankert. Die Entwürfe von Basisklassen bilden die
Grundlage für alle weiteren Implementierungen. Ihre Passung zum
Problemraum ist damit entscheidend, um darauf aufbauende Klassen
konsistent entwickeln zu können. Designfehler zeigen sich dabei nicht
immer unmittelbar, sondern teilweise erst bei der Implementierung von
Klassen, die tiefer in der Vererbungshierarchie stehen. Zu diesem
Zeitpunkt bestehen strukturelle Kopplungen bereits, die sich nur schwer
wieder auflösen lassen. Es muss daher früh eine vergleichsweise konkrete
Vorstellung davon bestehen, welche Anforderungen das Programm erfüllen
soll. Auch die zukünftige Erweiterbarkeit hängt stark von der Gestaltung
der Klassenbeziehungen ab und muss bereits bei der initialen
Modellierung berücksichtigt werden. Nachträgliche Veränderungen an
Basisklassen gestalten sich insofern schwierig, als dass schon kleine
Änderungen, indirekt über die Subklassen, großen und nicht sofort
offensichtlichen Einfluss auf das System haben. Die Spezialisierung von
Methoden führt dazu, dass Logik teilweise dezentralisiert wird. Bei
Nutzung objektorientierter Mechaniken ergibt sich die
konkrete Ausführung einer Methode nicht mehr nur aus ihrer lokalen
Definition, sondern aus einem Zusammenspiel verschiedener Klassen und
Methoden entlang der Vererbungshirarchie. Das kann Verständnis
erschweren und Fehler verdecken. Die implizite Struktur, welche
objektorientierte Programmierung mit sich bringt, kann somit bei
Designfehlern deren Korrektur erschweren.

# **5. Fazit und Reflexion**
Ursprüngliches Ziel der Arbeit war es, ein Beispielprogramm zu entwickeln, welches relevante
Prinzipien objektorientierter Programmierung veranschaulicht und dabei aufzeigen kann, 
wie diese Prinzipien in der Praxis angewendet werden können, um komplexe Softwarestrukturen 
zu handhaben. Während des Arbeitsprozesses wurden jedoch die bisher beschriebenen Herausforderungen
praktisch erfahren. 
Dies wurde durch den Umstand verstärkt, dass das Beispielprogramm nie als funktionale
oder praktisch nutzbare Implementierung gedacht war. 
So wurden von Beginn an Designentscheidungen mit zwei Zielrichtungen getroffen.
Die Prinzipien und Mechaniken objektorientierter Programmierung sollten in ihren Kernformen im 
Beispielprogramm angewendet werden. 
Außerdem sollte sich dabei ein zumindest sprachlich und semantisch intuitiv nachvollziehbares Modell bilden, 
ohne dass Detailimplementierungen, mit fehlendem Bezug zu den grundlegenden Prinzipien, in den Vordergrund geraten. 
Das entwickelte Beispielprogramm erwies sich (in der vorliegenden Ausarbeitungsstufe) über das geplante Maß 
hinaus, als ungeeignet den Problemraum zu modellieren.  
Insbesondere wurde Vererbung nicht zielführend eingesetzt, um semantisch sinnvolle Klassenbeziehungen darzustellen. 
Eine Demonstration des praktischen Nutzens objektorientierter Programmierung ließ sich daher anhand des Beispiels nur eingeschränkt realisieren.
Da die Analyse der dabei auftretenden Herausforderungen ebenfalls Teil der Aufgabenstellung ist, wurde der Fokus auf deren Untersuchung gelegt.  
Es zeigt sich, dass bereits bei einfachen Problemräumen durch unzureichende Modellierungsentscheidungen komplexe Abhängigkeiten entstehen können. 
Daraus lässt sich ableiten, dass diese Herausforderungen auch in realen, deutlich komplexeren Systemen eine zentrale Rolle spielen.
Die Erkenntnis der Arbeit ist, dass die 
zentrale Herausforderung weniger in der technischen Umsetzung objektorientierter Mechaniken 
liegt, sondern in der Wahl geeigneter Abstraktionsebenen und der Zuordnung von Verantwortlichkeiten 
innerhalb eines Systems.
Als spezifische Herausforderungen der objektorientierten Programmierung stellte sich heraus, 
dass insbesondere beim Umgang mit Vererbung und Mehrfachvererbung, frühe strukturelle Festlegungen
weitreichende Konsequenzen haben die nur schwer revidiert werden können. 
Auch der Umgang mit den Abstraktionsebenen scheint bei objektorientierter Programmierung 
besonders herausfordernd, da viele Prozesse und Daten dezentral im System abstrahiert werden können. 
Diesen Abstraktionen muss der Nutzer folgen können, um Fehler zu erkennen oder
Erweiterungen anzubinden. Falsche Abstraktionsebenen können entgegen dem eigentlichen Ziel 
Komplexität erhöhen, sodass deren Implementierung große strukturelle Auswirkungen
auf die Lesbarkeit und Wartbarkeit des Systems hat, und ihr zielführender Einsatz kritisch 
für verständliche Software ist. 
Aus der abstraktionslastigen Struktur und den strukturellen Kopplungen 
objektorientierter Programmierung folgt auch, dass frühzeitig ein kohärentes Modell
bestehen muss, bei welchem die Klassenbeziehungen untereinander, semantisch und technisch
kongruent, grundsätzlich festgelegt sein sollten.
Diese Herausforderungen könnten überwunden werden, indem die zugrunde liegenden Faktoren 
angemessen berücksichtigt werden. 
Das würde hier eine sorgfältige Wahl der Abstraktionsebenen, klar abgegrenzte Verantwortlichkeiten 
und eine exakt zum Problemraum passende Modellierung bedeuten.  
Trotz der Herausforderungen entstanden im Arbeitsprozess auch Erkenntnisse, welches Potenzial
objektorientierte Programmierung bei geeigneter Anwendung bietet.
So können klar definierte Schnittstellen
umfangreiche Funktionalität schnell und einfach nutzbar machen. Das
Beispielprogramm ist keine geeignete Grundlage um diese Vorteile
ausführlich zu veranschaulichen, da es dafür zu oberflächlich
implementiert ist. Allerdings lässt sich erahnen, dass bei sauberer
Grundlagenarbeit auch bei einem überarbeiteten Beispielprogramm diese
Vorteile zu tatsächlicher Nutzbarkeit führen könnten. So wäre es
möglich, große Mengen an Spielobjekten einfach zu verwalten, da
effizient über diese iteriert werden kann. Aktionen wie Updates oder
Initialisierungen können auf eine, nach Eigenschaften filterbare, Menge
von Objekten einheitlich angewendet werden. Auch könnten etablierte
Implementierungen von Spielmechaniken, wie eine Kollisionserkennung,
von anderen Entwicklern genutzt und nur über derer Schnittstelle an
das eigene Programm angebunden werden könnten.
Abschließend lässt sich festhalten, dass objektorientierte Programmierung komplexe Strukturen zwar abbilden kann und nutzbar macht,
jedoch gleichzeitig hohe Anforderungen an die Qualität der zugrunde liegenden Modellierung stellt. 
Die Wahl der Abstraktionsebenen und die Zuordnung von Verantwortlichkeiten sind dabei entscheidend dafür, ob diese Komplexität reduziert oder unbeabsichtigt erhöht wird.


**Literaturverzeichnis**

Jue, Kylie, and Nick Bowman. n.d. *Welcome to CS106B: Programming
Abstractions!* Accessed March 25, 2026.
<https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1208/lectures/welcome/lecture1_slides.pdf>.

Kang, Eunsuk, and Jean Yang. 2010. *Introduction To C Memory Management
And C++ Object-Oriented Programming*. Vorlesungsskript.
<https://ocw.mit.edu/courses/6-088-introduction-to-c-memory-management-and-c-object-oriented-programming-january-iap-2010/>.

Sebesta, Robert. 2016. *Concepts of Programming Languages, Global
Edition*. 11th ed. Pearson Education, Limited.
<https://ebookcentral.proquest.com/lib/badhonnef/detail.action?docID=5833350.>

Steyer, Ralph. 2024. *Programmieren in Python*. 2. Auflage. Springer.
https://doi.org/<https://doi.org/10.1007/978-3-658-44286-6>.

Voigt, Janina, Warwick Irwin, and Neville Churcher. 2010. "Class
Encapsulation and Object Encapsulation." (Athens, Greece), 171--78.
<https://www.scitepress.org/papers/2010/29247/29247.pdf?utm_source=chatgpt.com>

**Anhangsverzeichnis**

A.  basisklassen.py (S.21)

B.  systemkomponenten.py (S. 25)

C.  spielobjekte.py (S. 27)

D.  simulation.py (S. 33)

**Anhänge**

A. basisklassen.py

from \_\_future\_\_ import annotations

import math as m

from abc import ABC, abstractmethod

from enum import Enum

class GameObject(ABC):

def \_\_init\_\_(

self,

x: int,

y: int,

movable: bool,

ID: int = 0,

width: int = 10,

height: int = 10,

\*\*kwargs,

) -\> None:

self.\_ID = ID

self.\_x_pos = x

self.\_y_pos = y

self.\_width = width

self.\_height = height

self.\_is_alive = True

self.\_movable = movable

self.\_speed = 0

self.\_heading = 0

super().\_\_init\_\_(\*\*kwargs)

def set_velocity(self, speed: int, heading_deg: int) -\> None:

if speed \< 0:

raise ValueError(\"speed may not be negative\")

self.\_speed = speed

if heading_deg \< 0 or heading_deg \>= 360:

raise ValueError(\"heading must be 0 to 359\")

self.\_heading = heading_deg

\@abstractmethod

def update(self) -\> None:

if self.\_movable:

self.\_apply_velocity()

\@property

def x(self) -\> int:

return self.\_x_pos

\@property

def y(self) -\> int:

return self.\_y_pos

\@property

def velocity(self) -\> tuple\[int, int\]:

return (self.\_speed, self.\_heading)

\@property

def can_move(self) -\> bool:

return self.\_movable

\@property

def is_alive(self) -\> bool:

return self.\_is_alive

\@property

def occupied_space(self) -\> set\[tuple\[int, int\]\]:

space = set()

x_max = self.x + self.\_width

y_max = self.y + self.\_height

for i in range(int(self.x), int(x_max)):

for j in range(int(self.y), int(y_max)):

space.add((i, j))

return space

def \_apply_velocity(self) -\> None:

self.\_x_pos += int(self.\_speed \* m.cos(m.radians(self.\_heading)))

self.\_y_pos += int(self.\_speed \* m.sin(m.radians(self.\_heading)))

class DamageModel(ABC):

class DamageState(Enum):

OK = 3

DAMAGED = 2

UNMANEUVERABLE = 1

DESTROYED = 0

def \_\_init\_\_(self, max_health: int, \*\*kwargs) -\> None:

self.\_max_health = max_health

self.\_health = max_health

self.\_damage_state = self.DamageState.OK

super().\_\_init\_\_(\*\*kwargs)

def damage(self, damage: int) -\> None:

self.\_health = max(0, self.\_health - damage)

def update(self) -\> None:

relative_damage = (self.\_health / self.\_max_health) \* 100

if relative_damage \> 50:

self.\_damage_state = self.DamageState.OK

elif relative_damage \> 25:

self.\_damage_state = self.DamageState.DAMAGED

elif relative_damage \> 0:

self.\_damage_state = self.DamageState.UNMANEUVERABLE

else:

self.\_damage_state = self.DamageState.DESTROYED

\@abstractmethod

def apply_damage_to_abilities(self) -\> None:

pass

\@abstractmethod

def check_for_collision(self) -\> None:

pass

B. systemkomponenten.py

from \_\_future\_\_ import annotations

from basisklassen import GameObject

class CollisionModel:

def \_\_init\_\_(self, objects_list: list\[GameObject\]) -\> None:

self.\_objects_list = objects_list

def check_for_collision(

self, object_to_check: GameObject

) -\> GameObject \| None:

position_check_list = \[\]

for i in object_to_check.occupied_space:

position_check_list.append(i)

for obj in self.\_objects_list:

if obj is object_to_check or obj.is_alive is False:

continue

for i in obj.occupied_space:

if i in position_check_list:

return obj

return None

class Cannon:

def \_\_init\_\_(

self,

capacity: int,

collision_model: CollisionModel,

objects_list: list\[GameObject\],

) -\> None:

self.capacity = capacity

self.collision_model = collision_model

self.objects_list = objects_list

def shoot(self, x: int, y: int, heading: int) -\> None:

aim = heading - 90

if aim \< 0:

aim += 360

shot = CannonBall(

x=x,

y=y,

collision_model=self.collision_model,

objects_list=self.objects_list,

)

shot.set_velocity(20, aim)

C. spielobjekte.py

from \_\_future\_\_ import annotations

from basisklassen import DamageModel, GameObject

from systemkomponenten import Cannon, CollisionModel

class Rock(GameObject):

def \_\_init\_\_(self, ID: int, x: int, y: int, width: int, height:
int):

super().\_\_init\_\_(

ID=ID, x=x, y=y, movable=False, width=width, height=height

)

def update(self) -\> None:

pass

class SandBank(GameObject):

def \_\_init\_\_(self, ID: int, x: int, y: int, width: int, height:
int):

super().\_\_init\_\_(

ID=ID, x=x, y=y, movable=False, width=width, height=height

)

def update(self) -\> None:

pass

class CannonBall(GameObject):

def \_\_init\_\_(

self,

x: int,

y: int,

collision_model: CollisionModel,

objects_list: list\[GameObject\],

) -\> None:

super().\_\_init\_\_(x=x, y=y, movable=True)

objects_list.append(self)

self.\_collision_model = collision_model

def check_for_collision(self) -\> None:

collision_object = self.\_collision_model.check_for_collision(self)

if collision_object is None or isinstance(collision_object, SandBank):

return

self.\_is_alive = False

def update(self) -\> None:

super().update()

self.check_for_collision()

class Ship(GameObject, DamageModel):

def \_\_init\_\_(

self,

ID: int,

x: int,

y: int,

width: int,

height: int,

max_health: int,

cannon_capacity: int,

collision_model: CollisionModel,

game_objects: list\[GameObject\],

) -\> None:

super().\_\_init\_\_(

ID=ID,

x=x,

y=y,

movable=True,

width=width,

height=height,

max_health=max_health,

)

self.\_speed = 5

self.\_collision_model = collision_model

self.\_cannon = Cannon(

capacity=cannon_capacity,

collision_model=collision_model,

objects_list=game_objects,

)

def set_heading(self, heading: int) -\> None:

super().set_velocity(self.\_speed, heading)

def check_for_collision(self) -\> None:

collision_object = self.\_collision_model.check_for_collision(self)

if collision_object is None:

return

if isinstance(collision_object, Ship):

self.damage(50)

elif isinstance(collision_object, Rock):

self.damage(1000)

elif isinstance(collision_object, SandBank):

self.damage(0)

self.\_movable = False

elif isinstance(collision_object, Fortress):

self.damage(1000)

elif isinstance(collision_object, CannonBall):

self.damage(40)

def shoot(self) -\> None:

self.\_cannon.shoot(self.x, self.y, self.\_heading)

def apply_damage_to_abilities(self) -\> None:

if self.\_damage_state is self.DamageState.DAMAGED:

self.set_velocity(int(self.\_speed / 2), self.\_heading)

if self.\_damage_state is self.DamageState.UNMANEUVERABLE:

self.\_movable = False

if self.\_damage_state is self.DamageState.DESTROYED:

self.\_is_alive = False

def update(self) -\> None:

super().update()

self.check_for_collision()

DamageModel.update(self)

self.apply_damage_to_abilities()

class Fortress(GameObject, DamageModel):

def \_\_init\_\_(

self,

ID: int,

x: int,

y: int,

width: int,

height: int,

max_health: int,

collision_model: CollisionModel,

game_objects: list\[GameObject\],

) -\> None:

super().\_\_init\_\_(

ID=ID,

x=x,

y=y,

movable=False,

width=width,

height=height,

max_health=max_health,

)

self.\_collision_model = collision_model

self.\_cannon = Cannon(

capacity=500,

collision_model=collision_model,

objects_list=game_objects,

)

def check_for_collision(self) -\> None:

collision_object = self.\_collision_model.check_for_collision(self)

if isinstance(collision_object, CannonBall):

self.damage(50)

def apply_damage_to_abilities(self) -\> None:

if self.\_damage_state is self.DamageState.DESTROYED:

self.\_is_alive = False

def update(self) -\> None:

super().update()

self.check_for_collision()

DamageModel.update(self)

self.apply_damage_to_abilities()

def shoot(self) -\> None:

self.\_cannon.shoot(self.x, self.y, 0)

self.\_cannon.shoot(self.x, self.y, 90)

self.\_cannon.shoot(self.x, self.y, 180)

self.\_cannon.shoot(self.x, self.y, 270)

D. simulation.py

from \_\_future\_\_ import annotations

from basisklassen import GameObject

from spielobjekte import Fortress, Rock, SandBank, Ship

from systemkomponenten import CollisionModel

def create_world() -\> list\[GameObject\]:

game_objects: list\[GameObject\] = \[\]

collision_model = CollisionModel(game_objects)

ship_1234 = Ship(

ID=1234,

x=100,

y=15,

width=15,

height=30,

max_health=150,

cannon_capacity=30,

collision_model=collision_model,

game_objects=game_objects,

)

ship_4312 = Ship(

ID=4312,

x=10,

y=40,

width=15,

height=30,

max_health=150,

cannon_capacity=40,

collision_model=collision_model,

game_objects=game_objects,

)

rock_6543 = Rock(6543, 60, 90, 5, 5)

rock_8756 = Rock(8756, 45, 89, 7, 7)

sandbank_5436 = SandBank(5436, 70, 140, 30, 10)

fortress_4567 = Fortress(

ID=4567,

x=200,

y=200,

width=20,

height=20,

max_health=300,

collision_model=collision_model,

game_objects=game_objects,

)

fortress_9867 = Fortress(

ID=9867,

x=0,

y=0,

width=20,

height=20,

max_health=300,

collision_model=collision_model,

game_objects=game_objects,

)

game_objects.extend(

\[

ship_1234,

ship_4312,

rock_6543,

rock_8756,

sandbank_5436,

fortress_4567,

fortress_9867,

\]

)

return game_objects

def run_game_loop(game_objects: list\[GameObject\]) -\> None:

objects_to_remove: list\[GameObject\] = \[\]

while True:

get_user_input()

for obj in objects_to_remove:

game_objects.remove(obj)

objects_to_remove.clear()

for obj in game_objects:

if obj.is_alive:

obj.update()

else:

objects_to_remove.append(obj)

if \_\_name\_\_ == \"\_\_main\_\_\":

game_objects = create_world()

run_game_loop(game_objects)

#==================================================================

#PLATZHALTER

#==================================================================

def get_user_input():

pass
