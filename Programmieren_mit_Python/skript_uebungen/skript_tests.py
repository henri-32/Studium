from enum import Enum


class Chapter(Enum):
    Datenstrukturen = 1
    Konditionaler_Code = 2
    Funktionen = 3
    Schleifen = 4
    IO = 5
    Protokollierung = 6
    OOP_Einfuerung = 7
    Iteratoren = 8

activeChapters = {Chapter.OOP_Einfuerung}

# Chapter Datenstrukturen
# =============================================================================
if Chapter.Datenstrukturen in activeChapters:
    # Einen String erzeugen
    string_1 = "Hallo mein Name ist Henri"
    # Einzelne Zeichen ansprechen
    print(string_1[11])

    # Einen Slice ausgeben
    print(string_1[0:5])

    # Einen Slice bis zum Ende Ausgeben
    print(string_1[10:])

    # Alles bis auf die letzten x Zeichen ausgeben
    print(string_1[:-10])

    # Strings mit + erweitern
    string_1 += " und ich bin 28 Jahre alt"
    print(string_1)

    # .join() Funktion
    string_2 = "-".join(["test1", "test2"])
    print(string_2)

    # Länge ausgeben lassen
    string_3 = " - ".join(
        [string_1, "Länge des Strings {}".format(len(string_1))]
    )
    print(string_3)

    # Substring finden
    indexBegin_Jahre = string_1.find("Jahre")
    print(indexBegin_Jahre)

    # upper() für case-insensitive nutzen
    indexBegin_Jahre = string_1.upper().find("jahre".upper())
    print(indexBegin_Jahre)

    # .format (wie C++ snprintf())
    anzahlAutos = 10
    string_4 = "Wir haben hier insgesamt {} Autos stehen".format(anzahlAutos)
    print(string_4)

    # Listen
    list_1 = ["Henri", "Luca", "Lennart"]
    print(list_1[1])

    # alphanumerisch sortieren
    list_2 = sorted(list_1)
    print(list_2)

    # Index abfragen
    interesse = "Lennart"
    liste = list_2
    listname = "list_2"
    print(
        "Der Index von {} in {} ist ".format(interesse, listname)
        + str(liste.index(interesse))
    )

    # Liste erweitern
    list_1.append("Jenny")

    del list_1[0]

    # Listen verknüpfen
    list_3 = list_1.extend(list_2)
    # extend gibt none zurück !! das geht so nicht

    # Tupel (immutable)
    tuple_1 = ("Torben", "Silke", "Bernd")

    # Lists in Tupel sind mutable
    tuple_2 = (list_1, list_2)
    tuple_2[1].append("Stefan")

    # Sets (jedes Element kommt nur einmal vor)
    set_1 = {"Schraube", "Mutter", "Dübel"}
    print(set_1)
    set_1.add("Mutter")
    print(set_1)

    # Sets können schnittmengen ausgeben
    set_2 = {"x", "y", "z", "Mutter"}
    # Dafür kann & | ^ als operatoren genutzt werden
    print(set_1 & set_2)

    # Frozensets (frieren mutable objects ein)
    frozenset_1 = frozenset(list_1)

    # Dictionaries sind veränderbare key:value Paare
    dict_1 = {"Alter": 28, "Name": "Henri", "Größe": 1.82}

    # wird getrennt nach key:value oder nach Paar abgefragt
    dict_1.keys()
    dict_1.values()
    dict_1.items()

# ============================================================================
# Chapter Konditionaler Code
# ============================================================================
if Chapter.Konditionaler_Code in activeChapters:
    x = 100
    y = 200
    if x < y:
        print("x ist kleiner als y")

    # gültige Operatoren für if-statements sind:
    # == oder <>
    # !=
    # <
    # >
    # >=
    # a in b
    # a not in b

# =============================================================================
# Chapter Funktionen
# =============================================================================
if Chapter.Funktionen in activeChapters:

    def myFunctionAdds(x, y):
        returnvalue = x + y
        return returnvalue

    print(myFunctionAdds(100, 200))
    import customlibs as libs

    # fremde Funktionen nutzen
    print(libs.myFunctionMultiplies(100, 200))

    # Controlle über Ausführung eines Moduls mit __name__
    def main():
        if myFunctionAdds(100, 200) == 300:
            return True

    # __name__ ist eine Systemvariable, die den Aufrufer beinhaltet.
    # Wird dieses Modul
    # nur importiert, ist __name__ ungleich __main__main und das skript wird
    # nicht ausgeführ#t es wird also nur ausgeführt, wenn es direkt gerufen
    # wird.
    if __name__ == "__main__":
        main()

    # Standardparameter, wie bekannt aus C++
    # Funktionen mit unbestimmter Anzahl von Argumenten
    def some_of_unknown(*args):
        out = sum(args)
        print(out)

    some_of_unknown(1, 5, 7, 9)

    # Das geht auch mit dictionaries
    def some_of_unknown_dic(**args):
        out = sum(args.values())
        print(out)

    some_of_unknown_dic(first=3, second=6, third=9)

    # lambda Funktionen sind vereinfachte Funktionsdefinitionen mit
    # folgender syntax
    # lambda <Funktionsargumente>:<return>
    # Vergleich

    def sum_of_product(x, y):
        return sum(x * y)


# ============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
if Chapter.Schleifen in activeChapters:
    list_1 = [1, 2, 3, 4, 5, 6, 7, 8]

    # break beendet den Schleifendurchlauf
    for i in list_1:
        if i % 2 == 0:
            print("{}".format(i) + "ist eine gerade Zahl")
            break
    # continue überspringt den konditionalen code und geht in die nächste iteration
    for i in list_1:
        if i % 2 == 0:
            continue
        list_1.remove(i)
    print("list_1 enthält nur noch gerade Zahlen")
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
if Chapter.IO in activeChapters:
    user_name = input("Wie heißt du?: ")

    # Einlesen von TEXTBASIERTEN DATEIEN
    myFile = open("textzumeinlesen.txt", "r")
    myFileContent = myFile.read()
    myFile.close()
    print(myFileContent)

    # Datei sicher öffnen
    with open("textzumeinlsen.txt", "r") as f:
        my_File_Content = myFile.read()
# =============================================================================
# Protokollierung
# =============================================================================
if Chapter.Protokollierung in activeChapters:
    import logging
    # die config muss vor beginn des loggings feststehen

    logging.basicConfig(filename="my_log_1.log", filemode="w")
    # normalerweise werden nur error und critical geloggt
    logging.debug("Nachricht")
    logging.info("Info")
    logging.warning("Warunung")
    logging.error("Error")
    logging.critical("CriticalError")
    # das Loglevel kann in der config angepasst werden, dann werden alle
    # Ebenen hierarchisch bis zum angegebenen
    # level geloggt

    logging.debug("Nachricht")
    logging.info("Info")
    logging.warning("Warunung")
    logging.error("Error")
    logging.critical("CriticalError")

    # das logging kann auch in Dateien passieren
    logging.warning("Achtung")
    logging.critical("CriticalError")

# =============================================================================
# OOP/Einführung
# =============================================================================
if Chapter.OOP_Einfuerung in activeChapters:

    class Vehicle:
        def __init__(self, wheels, speed, product_number, known_accidents):
            self.wheels = wheels
            # Privates Attribut semantischer Hinweis, dass es nicht 
            # verändert werden sollte 
            self._speed = speed 
            # Geschützte Attribut darf nicht gelesen / verändert werden 
            self.__product_number = product_number
            # Geschützte Attribute mit Setter 
            self.__known_accidents = known_accidents

        def increase_speed(self, increment=5.0):
            self.current_speed += increment
        
        # Setter Methode für geschützte Attribute 
        def setType (self, accidents):
            self.__known_accidents = accidents
        
        def getAccidents (self, accidents):
            return self.__known_accidents

    class Ford(Vehicle):
        def __init__(self, model, color):
            self.model = model
            self.color = color

        @property 
        def description(self):
            return self.model + " " + self.color
        
        def increase_speed(self, increment=7.5):
            self.current_speed += increment

    car = Vehicle(4, 5.0, 453687, 25)
    car.increase_speed()
    print(car.current_speed)
    values = []
    myCar = Ford("F150", "blue")
    values = []
	# mit dir können alle Attribute eines Objekts ausgegeben werden 
    for name in dir(myCar):
        values.append(getattr(myCar, name))
    with open("aktuelleKlassenAttribute", "w") as f:
        f.write(str(values))
	# description ist wie oben definiert eine methode und benötigt ()
    print(myCar.description())
	# mit @property werden Methoden wie Atrribute behandelt
    print(myCar.description)
    print("test")
	# help() gibt die Informationen zur Klassenvererbung aus 
    help(myCar)
    print(isinstance(car, Vehicle))
    print(issubclass(Ford, Vehicle))
    # Methodenüberschreibung ist, wenn eine Subklasse die Methoden der Basiskl
    # asse überschreibt


#============================================================================
# Iteratoren 
#=============================================================================

if Chapter.Iteratoren in activeChapters: 
    # Range funktioniert von bis Schritte
    my_range = list(range(0, 20, 3)) 
    # Den Iterator gezielt aufrufen 
    my_iter = iter(my_range)
    # Den Iterator gezielt einen weiter schieben 
    next(my_iter)
    # Prüfen ob ein Objekt ein Iterator ist. Ein Iterator ist nicht gleich 
    # einem iterierbaren Objekt. Man kann auch über Listen etc. iterieren. 
    # die haben aber nicht die __next__ Funktion 
    hasattr(my_iter, "__next__")
