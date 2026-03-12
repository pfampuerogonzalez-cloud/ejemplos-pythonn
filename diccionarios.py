import os

## diccionarios
#una estructura de datos

#que guarda datos en formato clave , valor

#  clave  :    valor
# "nombre":"cristian"


persona = {
    "nombre" : "carlos",
    "edad" : 28,
    "direccion": "calle falsa 123",
    "ciudad" : "valparaiso"
}


# acceder a los valores de nuestro diccionario con ["keys"]
#print(persona["ciudad"])

#modificar valores

persona["edad"] = 35
persona["nombre"] = "carla"



#agregar un dato nuevo 

persona["pais"] = "chile"
persona["altura"] = 190

#print(persona)


#  recorrer el diccionario
# iterar keys
""" for k in persona:
    print(k)

##iterar values
for v in persona.values():
    print(v)

# iterar todo 
for k , v in persona.items():
    print(k,v) """


#lista de diccionarios de alumnos 
alumnos = []


while True:

    print("--------menu--------")
    print("1. agregar alumno")
    print("2. ver alumnos")
    print("3. salir")

    opcion = input("elige una opcion")
    os.system('cls' if os.name == 'nt' else 'clear')

    if opcion == "1":
        nombre = input("nombre de alumno")
        edad = input("edad del alumno")

        alumno = {
            "nombre":nombre,
            "edad": edad
        }
        alumnos.append(alumno)

        print("alumno agragado!!!!")

    elif opcion == "2":

        print("------lista de alumnos-----")

        for alumno in alumnos:
            print(alumno["nombre"], "--",alumno["edad"])
    
    elif opcion == "3":
        print("programa cerrado")
        break

    else:
        print("opcion no correcta solo se acepta 1,2 y 3 programa cerrado")
        break

    



















