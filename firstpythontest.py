import logging 

logging.basicConfig(filename = "henris_log.txt", filemode = "w", level = logging.INFO, \
	format = "%(asctime)s-%(process)d-%(levelname)s-%(message)s")

user_name = input("Wie heißt du ?: ")
user_age = input("Wie alt bist du ?: ") 
user_hobby = input("Was ist dein liebstes Hobby?: ") 


list_1 = ["Thorsten", "Caro", "Silke"] 
for i in list_1: 
	print(i)
stefan_vorhanden = False 
for i in list_1: 
	if i == "Stefan": 
		stefan_vorhanden = True 
if stefan_vorhanden == False: 
	list_1.append("Stefan")

for i in list_1: 
	print(i)

list_1.sort()

for i in list_1: 
	print(i)

if "Dieter" not in list_1: 
	list_1.append("Dieter") 
	list_1.sort()

for i in list_1: 
	print(i)

def myfirstpythonfunction (a, b, c): 
	"""
	inserts value a at index b of mutable container c 	
	""" 
	
	if isinstance(c, list) == True: 
		c.insert(b, a) 
		print("myfunction erfolgreich") 
		return 	
	else:
		("myfunction nicht erfolgreich") 
		return 

myfirstpythonfunction(user_name, 0, list_1)

for i in list_1: 
	print(i)

file = "user_daten.txt"

try:
	myfile = open(file, "x") 
except FileExistsError: 
	myfile = open(file, "w")

myfile.write("Name: {}\nAlter: {}\nHobby: {}".format(user_name, user_age, user_hobby))
myfile.close()
logging.info("User Daten in File geschrieben")

dict_1 = {}
with open(file, "r") as f: 	
	for line in f: 
		print(line)
		dict_1[line.split(":")[0]] = line.split(":")[1]  
logging.info("dict befüllt")

print(dict_1.values())
print(dict_1.keys())
