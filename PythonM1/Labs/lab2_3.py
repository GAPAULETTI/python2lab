str = "Iker duerme como un bebe"
cont = len(str)
lista = []
palabra = ""
adic = []
ultimo = str[cont -1]
print(ultimo)
if(ultimo.isalpha()):
    str += " "
for word in str:
    if(word.isalpha()):
        palabra = palabra + word
    else:
        adic.append(palabra)
        palabra = ""
    
       
    
    lista = list(adic)
 
print(lista)
print(palabra)

#As function

"""
    def mysplit(strng):
    cont = len(strng)
    lista = []
    palabra = ""
    listaAd = []
    ultimo = strng[cont-1]
    if(ultimo.isalpha()):
        strng += " "
    for word in strng:
        if(word.isalpha()):
            palabra = palabra + word
        else:
            listaAd.append(palabra)
            palabra = ""
    
    lista = list(listaAd)
    return lista

print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("   "))
print(mysplit(" abc "))
#print(mysplit(""))
"""


