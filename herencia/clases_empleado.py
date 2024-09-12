'''
Clase empleado y nombrado, nombrado, parcial
Fecha 12/08/2024
'''
class Empleado:
    def __init__(self, nombre = "sin nombre"):
        self.nombre = nombre
    def calcular(self):
        pass
class Nombrado(Empleado):
    def __init__(self, nombre, sueldo):
        super().__init(nombre) #Asignar valores a la clase superior
        self.sueldo = sueldo
    def calcular(self, sueldo=None):
        if sueldo is None:
            return self.sueldo
        else:
            self.sueldo = sueldo
            return self.sueldo
class Parcial(Empleado):
    def __init__(self, nombre, horas_trabajadas, tarifa_hora = None):
        super().__init__(nombre)
        if horas_trabajadas is not None:
            self.horas_trabadas = horas_trabajadas
        if tarifa_hora is not None:
            self.tarifa_hora = tarifa_hora
    def calcular(self, horas_trabajadas = None, tarifa_hora = None):
        if horas_trabajadas is not None:
            self.horas_trabajadas = horas_trabajadas
        if tarifa_hora is not None:
            self.tarifa_hora = tarifa_hora
        return self.horas_trabajadas*self,tarifa_hora
    
    def__str__(self):
    return 'Parcial (nombre {}, horas_trabajadas: {}. tarifa_hora: {})'. format(self.nombre, self.horas_trabajadas, self.tarifa_hora)

