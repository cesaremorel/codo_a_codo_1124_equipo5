from unittest import TestCase

from ejercicios.f20211118.NumeroComplejo import NumeroComplejo

class Ejercicios20211118TestCase(TestCase):

    def test_NumeroComplejo_suma(self):
        self.assertEqual((NumeroComplejo(2,7) + NumeroComplejo(3, -4)), NumeroComplejo(5,3))
        self.assertEqual((NumeroComplejo(10,0) + NumeroComplejo(3, 0)), NumeroComplejo(13,0))
       
    def test_NumeroComplejo_resta(self):
        self.assertEqual((NumeroComplejo(9,5) - NumeroComplejo(4, 7)), NumeroComplejo(5, -2))
    
    def test_NumeroComplejo_producto(self):
        self.assertEqual((NumeroComplejo(3,2) * NumeroComplejo(5, 6)), NumeroComplejo(3,28))
    
    def test_NumeroComplejo_division(self):
        self.assertEqual((NumeroComplejo(1,5) / NumeroComplejo(1, 2)), NumeroComplejo(2.2,0.6))
    