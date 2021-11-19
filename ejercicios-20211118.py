from ejercicios.f20211118.NumeroComplejo import NumeroComplejo

print('\n################### EJERCICIOS 18-11-2021 ###################\n')

print('\n################### Numeros Complejos ###################\n')

complejo1 = NumeroComplejo(2, 7)
complejo2 = NumeroComplejo(3, -4)
complejo3 = complejo1.sumar(complejo2)
print(str(complejo1)  + ' + ' + str(complejo2) + ' = ' + str(complejo3))

complejo1 = NumeroComplejo(9, 5)
complejo2 = NumeroComplejo(4, 7)
complejo3 = complejo1.restar(complejo2)
print(str(complejo1)  + ' - ' + str(complejo2) + ' = ' + str(complejo3))

complejo1 = NumeroComplejo(3, 2)
complejo2 = NumeroComplejo(5, 6)
complejo3 = complejo1.multiplicar(complejo2)
print(str(complejo1)  + ' * ' + str(complejo2) + ' = ' + str(complejo3))

complejo1 = NumeroComplejo(1, 5)
complejo2 = NumeroComplejo(1, 2)
complejo3 = complejo1.dividir(complejo2)
print(str(complejo1)  + ' / ' + str(complejo2) + ' = ' + str(complejo3))
