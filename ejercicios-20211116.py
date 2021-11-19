from ejercicios.f20211116.ejercicio_01 import myfunction as ejercicio_01
from ejercicios.f20211116.ejercicio_02 import myfunction as ejercicio_02
from ejercicios.f20211116.ejercicio_03 import myfunction as ejercicio_03
from ejercicios.f20211116.ejercicio_04 import myfunction as ejercicio_04
from ejercicios.f20211116.ejercicio_05 import myfunction as ejercicio_05
from ejercicios.f20211116.extra.ejercicio_a import myfunction as ejercicio_a
from ejercicios.f20211116.extra.ejercicio_b import myfunction as ejercicio_b

print('\n################### EJERCICIOS 16-11-2021 ###################\n')

def reporte(ejercicio, invocacion, resultado = False) :
    print('Ejercicio: ' + '\033[1;32;40m' + ejercicio + '\033[0m')
    print('\033[1;30;20m' + 'Probando con: ' + invocacion + '\033[0m' )
    if resultado:
        print('Resultado: ' + '\033[1;37;20m' + repr(resultado) + '\033[0m')
    print('-----------')


reporte('1', 'ejercicio_01(\'hola mundo\')', ejercicio_01('hola mundo'))
reporte('2', 'ejercicio_02(\'Hola Mundo\')', ejercicio_02('Hola Mundo'))
reporte('3', 'ejercicio_03(\'mesa\', 2, \'t\')', ejercicio_03('mesa', 2, 't'))
reporte('4', 'ejercicio_04(\'alejandro medici\')', ejercicio_04('alejandro medici'))
reporte('5', 'ejercicio_05([2,6,10,10,7,8,5,6])', ejercicio_05([2,6,10,10,7,8,5,6]))

print('\n################### EXTRAS ###################\n')
# Son procedimientos (imprimen en pantalla pero no retornan data)
reporte('extra A', 'ejercicio_a(6)')
print('\033[1;37;20m')
ejercicio_a(6),
print('\033[0m')

reporte('extra B', 'ejercicio_b(\'Telefunken\')')
print('\033[1;37;20m')
ejercicio_b('Telefunken')
print('\033[0m')