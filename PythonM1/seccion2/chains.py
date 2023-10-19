#Operaciones con Cadenas

# Demonstración de min() max() - Ejemplo 1:
print(min("aAbByYzZ"))
print(max("aAbByYzZ"))


# Demonstración de min() - Ejemplos 2 y 3:
# Demostración de max() - Ejemplo 2 y 3:
t = 'Los Caballeros Que Dicen "Ni!"'
print('[' + min(t) + ']')
print('[' + max(t) + ']')

t = [0, 1, 2]
print(min(t))
print(max(t))

# Demonstración del método index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))

# Demostración de la función list():
print(list("abcabc"))

# Demostración del método count():
print("abcabc".count("b"))

str = 'programmer'
print(str.casefold())

#Ordenamiento
#Funcion sorted(): Devuelve una nueva lista
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)
print(first_greek_2)
print()

#Funcion sort(): no se crea una nueva lista
first_greek = ['omega', 'alpha', 'pi', 'gamma']
print(first_greek)

first_greek.sort()
print(first_greek)

#Convertir numeros a cadena
num = 10
num2 = 1.2
numStr = str(num)
num2Str = str(num2)

#Inversa a la anterior
si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)

print(itg + flt)