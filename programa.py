"""
Programa que usa las clases declaradas en el archivo clase.py
Fecha 02/09/2024
"""
import clases as cl
#Crear objetos de clase persona
per1 = cl.Persona("Juan", 70)
per2 = cl.Persona("Maria", 55)
#Asignar valor a las propiedades
per1.peso = 75
per2.peso = 57
per2.nombre += "Elena"
#Usar los métodos
per1.caminar()
per2.comer()
per2.comer()
print("Nombre: {} y Peso {}", format(per1.nombre,per1.peso))

per1.caminar(16)
print("Nombre: {} y Peso: {}" ,format( per1.nombre,per1.peso))

per1.caminar()
print("Nombre: {} y Peso {}" ,format(per1.nombre,per1.peso))

