print("Demostración del método capialize: ")
str = 'aBBsD'
print(str.capitalize())

print( "Demostración del método center():")
print('[' + 'alpha'.center(10) + ']')
print('[' + 'gamma'.center(20, '*') + ']')

print("Demostración del método endswith():")
if "epsilon".endswith("on"):
    print("si")
else:
    print("no")

print("Demostración del método startswith():") 
print("omega".startswith("meg"))
print("omega".startswith("om"))


print("Demostración del método find():")
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
print("Demostración del método isalnum():")
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

# Ejemplo: Demostración del método isalpha(): Solo alfabeticos
print(" Demostración del método isalpha():")
print("Moooo".isalpha())
print('Mu40'.isalpha())

# Ejemplo: Demostración del método isdigit(): solo numericos
print("Demostración del método isdigit():")
print('2018'.isdigit())
print("Year2019".isdigit())    

# Ejemplo: Demostración del método islower(): solo minúsculas
print("Demostración del método islower():")
print("Moooo".islower())
print('moooo'.islower())

# Ejemplo: Demostración del método isspace():
print("Demostración del método isspace():")
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

# Ejemplo: Demostración del método isupper():
print("Demostración del método isupper():")
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())

# Demostración del método join():
print("Demostración del método join():")
print(",".join(["omicron", "pi", "rho"]))
print("#".join(["omicron", "pi", "rho"]))

# Demostración del método lower():
print("Demostración del método lower():")
print("SiGmA=60".lower())

# Demostración del método lstrip(): elimina todos los espacios en blanco iniciales creando una nueva cadena
print("Demostración del método lstrip():")
print("[" + " tau ".lstrip() + "]")

print("www.cisco.com".lstrip("w."))

# Demostración del método rstrip():
print("Demostración del método rstrip():")
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))

# Demostración del método replace():
print("Demostración del método replace():")
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))

# Limitar los reemplazos con el 3er parámetro
print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))

# Demostración del método rfind(): Búsqueda reversa
print("Demostración del método rfind():")
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))

# Demostración del método split(): Divide en subcadenas por cada espacio 
print("Demostración del método split():")
print("phi       chi\npsi".split())

# Demostración del método strip(): Elimina espacios en blanco de ambos lados
print("Demostración del método strip():")
print("[" + "   aleph   ".strip() + "]")

# Demostración del método swapcase():
print("Demostración del método swapcase():")
print("Yo solo sé que no sé nada".swapcase())

# Demostración del método title():
print("Demostración del método title():")
print("Yo solo sé que no sé nada. Parte 1.".title())

# Demostración del método upper():hace una copia de la cadena de origen, reemplaza todas las letras minúsculas con sus equivalentes en mayúsculas
print("Demostración del método upper():")
print("Yo solo sé que no sé nada. Parte 2.".upper())

s1 = '¿Dónde están las nieves de antaño?'
s2 = s1.split()
print(s2[-3])

