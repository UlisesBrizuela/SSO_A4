from os import system


def LeerArchivo():
    procesos = []
    with open("./procesos.txt", 'r') as f:
        lineas = f.readlines()
        for linea in lineas:
            proceso, ciclos, prioridad = linea.strip().split(',')
            procesos.append((proceso, int(ciclos), int(prioridad)))
        #print(procesos)
    return procesos

 
def AgregarProcesos(procesos):
   # system('cls')
    nuevos_procesos = procesos
    print(f"copia {nuevos_procesos}")
    try:
        n = str(input("Deseas agregar un nuevo Proceso? Y/N "))
        if n == 'Y' or n == 'y':
            #system('cls')
            try:
                nombre = str(input("Ingresa Nombre: "))
                ciclos = int(input("Ingresa Ciclos/Quantum: "))
                prioridad = int(input("Ingresar Prioridad: "))
                try:
                    l = str(input("Quieres agregar el proceso al Inicio o al Final? I/F "))
                    if l == 'I' or l == 'i':
                        nuevos_procesos.insert(0, (nombre, int(ciclos), int(prioridad)))
                        return AgregarProcesos(nuevos_procesos)
                    elif l == 'F' or l == 'f':
                        nuevos_procesos.append((nombre, int(ciclos), int(prioridad)))
                        return AgregarProcesos(nuevos_procesos)
                    else:
                        print("Opcion Invalida.")
                        input("\npresiona Enter para continuar...")
                        #AgregarProcesos(nuevos_procesos)

                except ValueError:
                    print("Dato invalido.")
                    input("\npresiona Enter para continuar...")
                    #AgregarProcesos(nuevos_procesos)

            except ValueError:
                print("Dato invalido.")
                input("\npresiona Enter para continuar...")
                #AgregarProcesos(nuevos_procesos)

        elif n == 'N' or n == 'n':
            print(f"return {nuevos_procesos}")
            l = nuevos_procesos
            print(f"l {l}")
            return l
        else:
            print("Opcion Invalida.")
            input("\npresiona Enter para continuar...")
            #AgregarProcesos(nuevos_procesos)

    except ValueError: 
        print("Dato invalido.")
        input("\npresiona Enter para continuar...")
        #AgregarProcesos(nuevos_procesos) 


l= LeerArchivo()
print(f"\n\nleer {l}")
n= AgregarProcesos(l)
print(f"\n\nnuevo {n}")
