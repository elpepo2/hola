'''
Módulo de pruebas unitarias para programa.py
'''
import unittest
from prueba.test.programa import suma, es_mayor

class TestPrograma(unittest.TestCase):
    # Métodos de prueba
    def test_suma_positivos(self):
        self.assertEqual(suma(1, 4), 5)
    def test_suma_negativos(self):
        self.assertEqual(suma(-2, -4), -6)
    def test_suma_detro_de_un_rango(self):
        self.assertIn(suma(2,9), [1, 2, 4, 6,7])
    #Desarrollar pruebas para la función "es_mayor"
    #Desarrollar pruebas para la división de 2 números

if __name__ =='__main__':
    unittest.main()