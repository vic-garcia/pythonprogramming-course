#sistema de archivos
import os
import shutil
import subprocess
import sys  #para el laboratorio
#LISTDIR
print(os.listdir("C:\window"))  #usar \ da error, usamos/ o \\ 
print(os.listdir("C:\\window"))  #lista las direcciones en el la ruta puesta
print(os.listdir("C:/window"))

#DIRECTORIO ACTUAL
print(os.getcwd())   #current window directory cwd

#VERIFICAR SI EXISTE UNA RUTA
print(os.path.exists("C:/webmedata"))

#CREAR UNA NUEVA CARPETA
os.mkdir("C:/webmedata/educacionIT/data.txt")

#Eliminar un archivo
os.remove("C:/webmedara/educacionIT/data.txt")
#RENOMBRAR UN ARCHIVO
os.rename("C:/webmedata/educacionIT/resumen.txt","C:/webmedata/educacionIT/dataresumen.txt")
#SHUTIL
#COPIAR ARCHIVO A OTRA CARPETA
print(shutil.copy("C:/webdata/educacionIT/data.txt", "C:/webmedat/eduacionIT/clase5/"))

#Mover un archivo
print(shutil.move("C:/webmedata/educacionIT/nota.txt", "C:/webmedata/educacionIT/clase5/"))
#ELIMINAR CARPETA
shutil.rmtree("C:/webmedata/educacionIT/clase5")


#SUBPROCESS
#RUN
#EJECUTAR PROGRAMA O UN COMANDO desde  python

#comando
subprocess.run(["mkdir","CarpetaPython"],shell=True)
print("Se ha creado la carpeta con exito")

#Programa - Capturamos la salida con una variable. hostname me da el nombre de mi equipo o computadora
p= subprocess.run("hostname", capture_output= True, encoding= "cp850")
print(p.stdout)  #standar output

#Laboratorio
try:
    ruta = sys.argv[1]
    extension = sys.argv[2]
except IndexError:
    print("Faltan arguementos")
    sys.exit()