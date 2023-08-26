def ejecucion1():
    print("Ejercicio celecionado 1 ")
    mi_tupla = ("Hola", "mundo", "Python")
    mi_lista = list(mi_tupla)
    mi_lista.pop(1)
    mi_tupla = tuple(mi_lista)
    print(mi_tupla)
def ejecucion2():
    print("Ejercicio celecionado 2 ")
def ejecucion3():
    print("Ejercicio celecionado 3 ")
def ejecucion4():
    print("Ejercicio celecionado 4 ")
def ejecucion5():
    print("Ejercicio celecionado 5 ")

print("Menu")
print('1. ejecucion1')
print('2. ejecucion1')
print('3. ejecucion1')
print('4. ejecucion1')
print('5. ejecucion1')

opcion=int(input("selecione un numero"))

if opcion == 1:
    ejecucion1()
elif opcion == 2:
    ejecucion2()
elif opcion == 3:
    ejecucion3()
elif opcion == 4:
    ejecucion4()
elif opcion == 5:
    ejecucion5()
    

