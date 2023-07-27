import os
import core
import acudientes
def MainMenu():
    os.system("clear")
    mainMenu = True
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^16}{}{:^16}|".format(' ','ADMINISTRACION DE CAMPERS',' '))
    print('+','-'*55,'+')
    print("1. Registrar camper")
    print("2. Buscar camper")
    print("3. Eliminar camper")
    print("4. Editar camper")
    print("5. Regresar menu principal")
    opcion =int(input("Opcion: "))
    if (opcion == 1):
        core.registroCampers()
    elif (opcion == 2):
        pass
    elif (opcion == 3):
        pass
    elif (opcion == 4):
        pass
    elif (opcion == 5):
        mainMenu = False
    if mainMenu:
        MainMenu()