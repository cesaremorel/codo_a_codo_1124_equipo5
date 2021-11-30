from unittest import TestCase
import io
from contextlib import redirect_stdout

from ejercicios.f20211116.ejercicio_01 import myfunction as ejercicio_01
from ejercicios.f20211116.ejercicio_02 import myfunction as ejercicio_02
from ejercicios.f20211116.ejercicio_03 import myfunction as ejercicio_03
from ejercicios.f20211116.ejercicio_04 import myfunction as ejercicio_04
from ejercicios.f20211116.ejercicio_05 import myfunction as ejercicio_05
from ejercicios.f20211116.extra.ejercicio_a import myfunction as ejercicio_a
from ejercicios.f20211116.extra.ejercicio_b import myfunction as ejercicio_b

class Ejercicios20211116TestCase(TestCase):
    def test_ejercicio1(self):
        self.assertEqual(ejercicio_01('hola mundo'), 'hola-mundo' )
        self.assertEqual(ejercicio_01('hola mundo Cruel'), 'hola-mundo-Cruel' )
        self.assertEqual(ejercicio_01('hola  mundo Cruel'), 'hola--mundo-Cruel' )

    def test_ejercicio2(self):
        self.assertEqual(ejercicio_02('hola mundo'), 'HOLA MUNDO' )
        self.assertEqual(ejercicio_02('Hola Mundo Cruel'), 'hOLA mUNDO cRUEL')
        self.assertEqual(ejercicio_02('HolaMundo'), 'hOLAmUNDO')
        self.assertEqual(ejercicio_02('No Seas niÑato'), 'nO sEAS NIñATO')

    def test_ejercicio3(self):
        self.assertEqual(ejercicio_03('mesa',2,'t'), 'meta' )
        self.assertEqual(ejercicio_03('mesa',1,'t'), 'mtsa' ) 
        self.assertEqual(ejercicio_03('mesa',0,'t'), 'tesa' )

    def test_ejercicio4(self):
        self.assertEqual(ejercicio_04('alejandro medici'), 'Alejandro Medici' )
    
    def test_ejercicio5(self):
        self.assertEqual(ejercicio_05([2,6,10,10,7,8,5,6]), 8 )
        self.assertEqual(ejercicio_05([2,6,10]), 6 )
    

    def test_ejercicio_a(self):
        f = io.StringIO()
        with redirect_stdout(f):
            ejercicio_a(2)
        self.assertEqual(f.getvalue(), '1\n22\n')
        f.close()
        f = io.StringIO()
        with redirect_stdout(f):
            ejercicio_a(6)
        self.assertEqual(f.getvalue(), '1\n22\n333\n4444\n55555\n666666\n')
        f.close()

    def test_ejercicio_b(self):
        f = io.StringIO()
        with redirect_stdout(f):
            ejercicio_b('Telefunken')
        self.assertEqual(f.getvalue(), 'e 3\nn 2\nt 1\n')
        f.close()
        f = io.StringIO()
        with redirect_stdout(f):
            ejercicio_b('La Serenisima')
        self.assertEqual(f.getvalue(), 'a 2\ns 2\ne 2\n')
        f.close()