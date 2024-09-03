#Crear la clase persona y comparar datos para 2 objetos persona
class Persona:
    #Atributos o propiedades declarados
    nombre = " "
    apellido = ""
    peso = 0
    # Métodos u operaciones
    def comer(self):
        self.peso += 1
        pass #pass significa que ahi debe ir codigo pero este momento no tengo la logica
    def caminar(self):
        pass
        self.peso -= 0.5
#Realizar operaciones con clases y objetos
#Crear loss objetos
per1 = Persona()
per2 = Persona()
print(per1.nombre + " , " + per1.apellido + ", peso: " + str(per1.peso))
#Asignar valores a las propiedades
per1.nombre = "María"
per1.apellido = "Ramos"
per1.peso = 55

per2.nombre = "Juan"
per2.apellido = "Perez"
per2.peso = 70

print(per1.nombre + " , " + per1.apellido + " ,peso: " + str/(per1.peso)