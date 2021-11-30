from unittest import TestCase

from ejercicios.f20211118.NumeroComplejo import NumeroComplejo
from ejercicios.f20211118.Matriz import Matrix3D

class Ejercicios20211118TestCase(TestCase):

    ## Pruebas Numero complejo

    def test_NumeroComplejo_igualdad(self):
        self.assertEqual( NumeroComplejo(2,7), NumeroComplejo(2,7))

    def test_NumeroComplejo_tipo(self):
        self.assertIsInstance((NumeroComplejo(2,7) + NumeroComplejo(3, -4)), NumeroComplejo)
        self.assertIsInstance((NumeroComplejo(2,7) - NumeroComplejo(3, -4)), NumeroComplejo)
        self.assertIsInstance((NumeroComplejo(2,7) * NumeroComplejo(3, -4)), NumeroComplejo)
        self.assertIsInstance((NumeroComplejo(2,7) / NumeroComplejo(3, -4)), NumeroComplejo)

    def test_NumeroComplejo_suma(self):
        self.assertEqual((NumeroComplejo(2,7) + NumeroComplejo(3, -4)), NumeroComplejo(5,3))
        self.assertEqual((NumeroComplejo(10,0) + NumeroComplejo(3, 0)), NumeroComplejo(13,0))
       
    def test_NumeroComplejo_resta(self):
        self.assertEqual((NumeroComplejo(9,5) - NumeroComplejo(4, 7)), NumeroComplejo(5, -2))
    
    def test_NumeroComplejo_producto(self):
        self.assertEqual((NumeroComplejo(3,2) * NumeroComplejo(5, 6)), NumeroComplejo(3,28))
    
    def test_NumeroComplejo_division(self):
        self.assertEqual((NumeroComplejo(1,5) / NumeroComplejo(1, 2)), NumeroComplejo(2.2,0.6))
        
   
   ## Pruebas Matriz

    def test_Matriz_suma(self):
       self.assertEqual((Matrix3D(1,2,3,4,5,6,7,8,9) + Matrix3D(1,2,3,4,5,6,7,8,9)), [[2, 4, 6], [8, 10, 12], [14, 16, 18]])

    def test_Matriz_resta(self):
       self.assertEqual((Matrix3D(1,2,3,4,5,6,7,8,9) - Matrix3D(1,2,3,4,5,6,7,8,9)), [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    def test_Matriz_producto(self):
       self.assertEqual((Matrix3D(1,2,3,4,5,6,7,8,9) * Matrix3D(1,2,3,4,5,6,7,8,9)), [[30, 36, 42], [66, 81, 96], [102, 126, 150]])