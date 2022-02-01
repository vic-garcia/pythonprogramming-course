#web services. 
# Direccion url, conexion mediante protocolo http accedo a un servidor
#Request (client) >---<  Response(servidor)
#cada pagina tiene una URL con dominio o con IP (Puede accerderse por cualquiera de los dos)
#Cada maquina servidora tiene una direccion IP unica a nivel mundial
#JSON(FORMATO PARA INTERCAMBIO DE DATOS)
#AJAX (INTERCAMBIO ENTRE JS Y PYTHON EN TIEMPO REAL)

#Arquitectura RESTful. para interactuar con el servidor COMO CLIENTE.
#RECURSOS: LISTADOS
# http:// universidad.com/alumnos
# http:// universidad.com/profesores
# http:// universidad.com/administrativos

#COMO INTERACTUAMOS CON LOS RECURSOS: INDIVIDUAL
#--Enviando info o borrando o añadiendo info
#GET / profesor (Para leer info)
#POST/ alumno (para agregar y grabar nueva info)
#PUT / alumno/10(Para modificar info)
#DELETE (para eliminar info)

#....instalamos: pip install requests y pip install klein

#requests (para interactuar con http, web services, etc)
import requests

#ejemplo con servidor conocido
"""r= requests.get("https://google.com")
print(r.status_code)"""
#ejemplo servidor local
#OBTENER LISTADO DEL RECURSO
"""r= requests.get("http://localhost:7001/student")
print("Código:", r.status_code)
print("Contenido:",r.json())  #lee el archivo interpretando con json
"""
#GRABAR UN DATO EN EL SERVIDOR
r = requests.post("http://localhost:7001/student", 
                    json={"name":"Mateo", "courses":4})
print("Código:", r.status_code)
print("Contenido:", r.jason)

#GRABAR VARIOS DATOS
alumnos= (("Emily",2),("Juan",1),("Sofía", 5))
for nombre, cursos in alumnos:
    r = requests.post("http://localhost:7001/student", 
                    json={"name":"nombre", "courses":cursos})
    print("Código:", r.status_code)
    print("Código:", r.jason())  
#MODIFICAR ALUMNO
datos = {"name": "sofia","courses": 6}   #El id del student es 4
r= requests.put("http://localhost:7001/student/4", json=datos)
print(r.status_code)              

#Eliminar un alumno que tiene el id:1
r=requests.delete("http://localhost:7001/student/1")
print(r.status_code) #si me sale 204 el codigo salio bien
#PARA ELIMINAR O AGREGAR O ACTUAR SOBRE VARIOS RECURSOS A LA VEZ
recursos="ejemplo"
num_id= "ejemplo en numeros"

r=requests.delete("http://localhost:7001"+ recursos + "/" + num_id) #tengo que recorrer con un for y definir las variables primero.
print(r.status_code)


r = requests.get("http://localhost:7002/student/1")
if r.status_code== 200:
    respuesta = r.json()
    for alumno in respuesta["students"]:
        print("Id alumno:", alumno["id"])
        print("nombre:", alumno["name"])
        print("cant. de cursos", alumno["courses"])
else:
    print("Error del servidor")

#AHORA_____WEB FORMULARIO CON PYTHON

datos= {"name":"Ana", "email":"ana@algo.com", "message":"Hola"}
r = requests.post("http://localhost:8880/form", data= datos)
contenido = r.content.decode("utf-8")
if "mensaje enviado correctamente" in contenido:
    print("Formulario enviado")
else:
    print("Error al enviar datos")