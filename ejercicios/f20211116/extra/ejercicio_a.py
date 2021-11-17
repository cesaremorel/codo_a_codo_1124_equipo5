"""
Extra: a- Escribir una funcion que recibe un numero entero y imprima por salida estandar(usando print) un triangulo de numeros de altura igual al numero ingresado. Ej. Si se ingresa el numero 5, debe imprimir:

1
22
333
4444
55555
"""

def myfunction(number):

    aux = 0

    for i in range(1, number + 1):
        
        while aux < i:
            print(i, end="")
            aux += 1

        print()
        aux = 0