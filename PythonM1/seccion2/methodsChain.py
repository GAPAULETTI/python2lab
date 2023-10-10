str = 'aBBsD'
print(str.capitalize())

# Demostración del método center():
print('[' + 'alpha'.center(10) + ']')
print('[' + 'gamma'.center(20, '*') + ']')

# Demostración del método endswith():
if "epsilon".endswith("on"):
    print("si")
else:
    print("no")

# Demostración del método find():
print("Eta".find("ta"))
print("Eta".find("mma"))

print("Ocurrency with find")

the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)

# Demostración del método isalnum(): Comprueba si tiene char alfabeticos o numeros solamente
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

# Ejemplo: Demostración del método isalpha(): Solo alfabeticos
print("Moooo".isalpha())
print('Mu40'.isalpha())

# Ejemplo: Demostración del método isdigit(): solo numericos
print('2018'.isdigit())
print("Year2019".isdigit())    

# Ejemplo: Demostración del método islower(): solo minúsculas
print("Moooo".islower())
print('moooo'.islower())

# Ejemplo: Demostración del método isspace():
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

# Ejemplo: Demostración del método isupper():
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())

# Demostración del método join():
print(",".join(["omicron", "pi", "rho"]))
print("#".join(["omicron", "pi", "rho"]))

# Demostración del método lower():
print("SiGmA=60".lower())

# Demostración del método lstrip(): elimina todos los espacios en blanco iniciales creando una nueva cadena
print("[" + " tau ".lstrip() + "]")

print("www.cisco.com".lstrip("w."))