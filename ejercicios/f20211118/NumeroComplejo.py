from fractions import Fraction

class NumeroComplejo():
    def __init__(self, real = 0, imaginario = 0) -> None:
        self.real = real
        self.imaginario = imaginario

    def __add__(self, complejo):
        real = self.real + complejo.real
        imaginario = self.imaginario + complejo.imaginario
        return NumeroComplejo(real, imaginario)

    def __sub__(self, complejo):
        real = self.real - complejo.real
        imaginario = self.imaginario - complejo.imaginario
        return NumeroComplejo(real, imaginario)

    def __mul__(self, complejo):
        real = (self.real * complejo.real) - ( self.imaginario * complejo.imaginario ) 
        imaginario = (self.real * complejo.imaginario) + ( self.imaginario * complejo.real )
        return NumeroComplejo(real, imaginario)

    def __truediv__(self, complejo):
        real = ( self.real * complejo.real + self.imaginario * complejo.imaginario ) / ( complejo.real ** 2 + complejo.imaginario ** 2)
        imaginario = (self.imaginario * complejo.real - self.real * complejo.imaginario ) / ( complejo.real ** 2 + complejo.imaginario ** 2)
        return NumeroComplejo(real, imaginario)
        

    def __str__(self):
        parte_real = repr(self.real)
        parte_imaginaria = ' + ' + repr(self.imaginario) if self.imaginario > 0  else ' - ' + repr(self.imaginario * -1)
        return '(' + parte_real + parte_imaginaria + 'i)' 

    def __eq__(self, complejo):
        return self.real == complejo.real and self.imaginario == complejo.imaginario