cad="Curso de Python"
"""
#Mostrar cadenas de distinitas maneras
print(cad[-1])
for caracter in cad:
    print(caracter)
#Slicing
print(cad[3:10])
print(cad[-6:])
print(cad[3:])
#funciones
print(cad.startswith("Curso"))
print(cad.endswith("Python"))

#Strip
nombre= "Juan\n"
nombre = nombre.strip()  #remueve espacios y saltos de lineas y reasigna
print(nombre.strip() =="juan")
#Replace
print(cad.replace("Python","Javascript"))
#===============================
letras= "A B C A B C A B C"
print(letras.replace(" ", "")) #El cambio no se aplica a la cadena, si no al print nada mas

#Split - genera una lista partiendo la cadena separando con un delimitador(esoacios o comas).
nombres= "Juan, Sofia, Ana" 
print(nombres.split(",")) 
#Find
cad = "Curso de Python"
print(cad.find("w"))  #si la w no existe devuelve -1
print(cad.find("o")) #solo devuelve la primera ocurrencia

#UPPER LOWER - Llevamos lo que ingrese el usuario todo a mayuscula  
print(cad.upper())
print(cad.lower()) """



