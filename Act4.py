#Actividad 4 - Seminario de solucion de problemas de sistemas operativos
#Brizuela Arias Ulises Israel

from os import system 
from sys import exit
from collections import deque

#----------- LECTURA DE ARCHIVO ----------------------------------
def LeerArchivo():
    procesos = []
    with open("./procesos.txt", 'r') as f:
        lineas = f.readlines()
        for linea in lineas:
            proceso, ciclos, prioridad = linea.strip().split(',')
            procesos.append((proceso, int(ciclos), int(prioridad)))
    return procesos



#------------------- INSERTAR NUEVOS PROCESOS -----------------------
def AgregarProcesos(procesos):
    system('cls')
    nuevos_procesos = procesos
    try:
        n = str(input("Deseas agregar un nuevo Proceso? Y/N "))
        if n == 'Y' or n == 'y':
            system('cls')
            try:
                nombre = str(input("Ingresa Nombre: "))
                ciclos = int(input("Ingresa Ciclos/Quantum: "))
                prioridad = int(input("Ingresar Prioridad: "))
                try:
                    l = str(input("Quieres agregar el proceso al Inicio o al Final? I/F "))
                    if l == 'I' or l == 'i':
                        nuevos_procesos.insert(0, (nombre, ciclos, prioridad))
                        return AgregarProcesos(nuevos_procesos)
                    elif l == 'F' or l == 'f':
                        nuevos_procesos.append((nombre, ciclos, prioridad))
                        return AgregarProcesos(nuevos_procesos)
                    else:
                        print("Opcion Invalida.")
                        input("\npresiona Enter para continuar...")
                        AgregarProcesos(nuevos_procesos)

                except ValueError:
                    print("Dato invalido.")
                    input("\npresiona Enter para continuar...")
                    AgregarProcesos(nuevos_procesos)

            except ValueError:
                print("Dato invalido.")
                input("\npresiona Enter para continuar...")
                AgregarProcesos(nuevos_procesos)

        elif n == 'N' or n == 'n':
            return nuevos_procesos
        else:
            print("Opcion Invalida.")
            input("\npresiona Enter para continuar...")
            AgregarProcesos(nuevos_procesos)

    except ValueError: 
        print("Dato invalido.")
        input("\npresiona Enter para continuar...")
        AgregarProcesos(nuevos_procesos)  



#------------- ALGORITMO ROUND ROBIN --------------------------------
def RoundRobin(procesos, Q):
    system('cls')
    cola = deque(procesos)
    while cola:
        proceso_actual = cola.popleft()
        nombre, quantum, p = proceso_actual
        print(f"Ejecuntando: {nombre}, con {quantum} quantum.")
        quantum -= Q
        if quantum > 0:
            cola.append((nombre, quantum, p))
            print(f"El proceso: {nombre} volvio a la cola con {quantum} quantum restantes.\n")
        else:
            print(f"Proceso {nombre} terminado.\n")

    input("\npresiona Enter para continuar...")
    Menu()



#------------------------- ALGORITMO SFJ ---------------------------------
def SFJ(procesos):
    system('cls')
    cola = deque(sorted(procesos, key = lambda x: x[1]))
    while cola:
        proceso_actual = cola.popleft()
        nombre, tamaño, p = proceso_actual
        print(f"Proceso ejecutado: {nombre} con {tamaño} ciclos.\n")

    input("\npresiona Enter para continuar...")
    Menu()



#-------------------- ALGORITMO FIFO ----------------------------------
def FIFO(procesos):
    system('cls')
    cola = deque(procesos)
    while cola:
        proceso_actual = cola.popleft()
        nombre, q, p = proceso_actual
        print(f"Proceso ejecutado: {nombre}.\n")

    input("\npresiona Enter para continuar...")
    Menu()



#--------------------- ALGORITMO DE PRIORIDADES ------------------------------
def Prioridades(procesos):
    system('cls')
    cola = deque(sorted(procesos, key = lambda x: x[2]))
    while cola:
        proceso_actual = cola.popleft()
        nombre, q, prioridad = proceso_actual
        print(f"Proceso Ejecutado: {nombre}, con prioridad {prioridad}.\n")

    input("\npresiona Enter para continuar...")
    Menu()    



#---------------------MENU PRINCIPAL --------------------------------------
def Menu(): 
    system('cls')
    archivo = LeerArchivo()
    procesos = AgregarProcesos(archivo)
   
#   impresion solo para comprobacion de la lista de procesos final
    for proceso in procesos:
        print(proceso)

    try:
        m = int(input("""
        SELECCIONA UNA OPCION.

        1.- ROUND ROBIN
        2.- SJF
        3.- FIFO
        4.- PRIORIDADES
        0.- SALIR
        
        # """))

        if m == 1:
            Quantum = 3
            RoundRobin(procesos, Quantum)
        elif m == 2: 
            SFJ(procesos)
        elif m == 3: 
            FIFO(procesos)
        elif m == 4: 
            Prioridades(procesos)
        elif m == 0:
            system('cls')
            exit();
        else:
            print("Opcion Invalida.")
            input("\npresiona Enter para continuar...")
            Menu()

    except ValueError: 
        print("Dato invalido.")
        input("\npresiona Enter para continuar...")
        Menu()


if __name__ == "__main__":
    Menu()