""""
Clases a usar en nuestros proyectos 02/09/24
"""
class Persona:
    def __init__(self,nombre,peso):
        self.nombre = nombre
        self.peso = peso
    def caminar(self, *args):
        if len(args) > 0:
            self.peso -= args[0] /8.0
        else:
            self.peso -= 0.5
        self.peso -= 0.5
    def comer(self):
        self.peso += 1
