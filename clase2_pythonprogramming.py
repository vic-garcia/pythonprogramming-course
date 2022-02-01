"""alumnos= ["maria","Juan","Jose"]
for i in range (len(alumnos)):
    nombre = alumnos [i]
    print(i,nombre)"""

#Ejercicio: Crear un bucle que almacene en una variable la suma de todos los elementos numericos de una lista, con excepcion del ultimo.
"""lista1=[1,5,"cuatro",False,5,4]
sumatoria=0
for i in range (0,len(lista1)-1):
    if type(lista1[i])==int:
      sumatoria += lista1[i]
print(sumatoria)"""
#Utilizando un bucle "while", elaborar un codigo que imprima en pantalla cada uno de los elementos de una lista y simultaneamente los elimine, hasta quedar vacía.
"""lista2= [1,2,3,4]
while len(lista2)!=0:
    print(lista2[len(lista2)-1])
    del lista2[len(lista2)-1]
    print(lista2)"""
#Laboratorio extra
tam=int(input("Ingrese el tamaño de la colección de datos:"))
lista=[]
while len(lista)!=tam:
    elem=float(input("ingrese un valor"))
    lista.append(elem)
print(lista)
for i in range(len(lista)):
    if lista[i]%5== 0 and lista[i]%3== 0:
        print("FizzBuzz")
    elif lista[i]%5== 0:
        print("Buzz")
    elif lista[i] % 3 == 0: 
        print("Fizz")
    else:
        print(lista[i])

