import os
import core
import funcionesHardware as f
def MainMenu():
    isTrue=True
    while isTrue:
        os.system("cls")
        print('+','-'*74,'+')
        print("|{:^30}{}{:^30}|".format(' ','GESTION HARDWARE',' '))
        print('+','-'*74,'+')
        print("1. Registrar trainers")
        print("2. Eliminar trainers")
        print("3. Editar trainers")
        print("4. Buscar trainers")
        print("5. Volver")
        try:
            opcion = int(input(":)_"))
            if (opcion == 1):
                f.agregarTrainers()
            elif (opcion == 2):
                f.eliminarTrainers()
            elif (opcion == 3):
                f.editarTrainers()
            elif (opcion == 4):
                f.buscarTrainers()
            elif (opcion == 5):
                isTrue=False  
            else:
                os.system("cls")
                print(input("Esta opcion no esta disponible\n\nPresione una tecla para continuar..."))
        except:
            print(input("No es posible ingresar textos en esta area\n\nPresione una tecla para continuar..."))