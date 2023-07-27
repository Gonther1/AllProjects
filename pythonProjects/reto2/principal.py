import os
import trainers
import hardware
import incidencias
import core
dataTrainers={"trainers":[]}
dataHardware={'hardware':[]}
dataIncidencias={"incidencias":[]}
if __name__=="__main__":

    if core.checkFile('trainers.json')==False and core.checkFile('hardware.json')==False and core.checkFile('incidencias.json')==False:

        core.SubirInfo(dataTrainers,'trainers.json')
        core.SubirInfo(dataHardware,'hardware.json')
        core.SubirInfo(dataIncidencias,'incidencias.json')

    isTrue=True

    while isTrue:

        os.system("cls")

        print('+','-'*74,'+')

        print("|{:^30}{}{:^32}|".format(' ','MENU PRINCIPAL',' '))

        print('+','-'*74,'+')

        print("1. Gestion trainers")

        print("2. Gestion incidencias")

        print("3. Gestion equipos")

        print("4. Salir")

        #try:

        opcion = int(input(":)_"))

        if (opcion == 1):
            trainers.MainMenu()

        elif (opcion == 2):
            incidencias.MainMenu()

        elif (opcion == 3):
            hardware.MainMenu()

        elif (opcion == 4):

            isTrue=False  
        else:
            os.system("cls")
            print(input("Esta opcion no esta disponible\n\nPresione una tecla para continuar..."))
"""
        except:

            os.system("cls")

            print(input("No es posible ingresar texto en esta area\n\nPresione una tecla para continuar"))"""


