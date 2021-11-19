from fractions import Fraction

class NumeroComplejo():
    def __init__(self, real = 0, imaginario = 0) -> None:
        self.real = real
        self.imaginario = imaginario

    def sumar(self, complejo):
        real = self.real + complejo.real
        imaginario = self.imaginario + complejo.imaginario
        return NumeroComplejo(real, imaginario)

    def restar(self, complejo):
        real = self.real - complejo.real
        imaginario = self.imaginario - complejo.imaginario
        return NumeroComplejo(real, imaginario)

    def multiplicar(self, complejo):
        real = (self.real * complejo.real) - ( self.imaginario * complejo.imaginario ) 
        imaginario = (self.real * complejo.imaginario) + ( self.imaginario * complejo.real )
        return NumeroComplejo(real, imaginario)

    def dividir(self, complejo):
        real = ( self.real * complejo.real + self.imaginario * complejo.imaginario ) / ( complejo.real ** 2 + complejo.imaginario ** 2)
        imaginario = (self.imaginario * complejo.real - self.real * complejo.imaginario ) / ( complejo.real ** 2 + complejo.imaginario ** 2)
        return NumeroComplejo(real, imaginario)
        

    def __str__(self):
        return '(' + repr(self.real) + ' + ' + repr(self.imaginario) + 'i)' 