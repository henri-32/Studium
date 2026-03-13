from enum import Enum
class PROPULSION(Enum):
	SAIL = 1
	MOTOR = 2
	RUDDER = 3

class Boat():
	def __init__(self, length = 0.0, width = 0.0, displacement = 0.0, propulsion = None, waterCapacity = 0.0, currentWaterFill = 0.0):
		self.length = length
		self.width = width
		self.displacement = displacement
		self.propulsion = propulsion
		self.waterCapacity = waterCapacity
		self.currentWaterFill = currentWaterFill

	def bunkerWater (self, liters = None):
		if liters == None:
			liters = self.waterCapacity
			self.currentWaterFill += liters

		if self.currentWaterFill > self.waterCapacity:
			self.currentWaterFill = self.waterCapacity

invicta = Boat(8.06, 2.25, 2350, PROPULSION.SAIL, 100)
contessa = Boat(7.77, 2.30, 2450, PROPULSION.SAIL, 90)

filename = "Bootsbibliothek.txt"

def main ():
	with open(filename, "w") as f:
		f.write("Bootstyp Invicta \n")
		f.write("Länge: " + str(invicta.length) + "\n" + "Füllstand Wasser: " + str(invicta.currentWaterFill))
		f.write("Bootstyp Contessa \n")

	def startBunkering():
		boot = input("Welches Boot möchten sie mit Wasser bebunkern?: ")
		waterFill = input("Wie viel Wasser möchten sie bunkern?: ")

		if boot == "invicta" or boot == "Invicta":
			invicta.bunkerWater(int(waterFill))
		elif boot == "contessa" or boot == "Contessa":
			contessa.bunkerWater(int(waterFill))
		else:
			print("Die Eingabe {} entspricht keinem gültigen Bootstypen. Achten sie auf Gross- und Kleinschreibung".format(boot))

	startBunkering()
	if input("Möchten sie ein weiteres Boot betanken?: || Y/N") == "Y":
		startBunkering()

	with open(filename, "a") as f:
		f.write("Füllstände nach Wasser Bunkern: \n" + "Invicta: " + str(invicta.currentWaterFill) +"\n" \
		+ "Contessa: " + str(contessa.currentWaterFill) + "\n")





main()

