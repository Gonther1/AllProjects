import os
def MainMenu():
    isActivate = True
    opcion=0
    bandera=True
    while bandera:
        try:
            while isActivate:
                os.system("cls")
                print('+','-'*74,'+')
                print("|{:^27}{}{:^26}|".format(' ','GESTION DE VETERINARIOS',' '))
                print('+','-'*74,'+')
                print("1. Agregar veterinario")
                print("2. Buscar veterinario")
                print("3. Mostrar informacion de un veterinario")
                print("4. Volver al menu principal")
                opcion = int(input(":)_"))
                if (opcion == 1):
                    print(input(f"{opcion}"))
                elif (opcion == 2):
                    print(input(f"{opcion}"))
                elif (opcion == 3):
                    print(input(f"{opcion}"))
                elif (opcion == 4):
                    isActivate=False   
                    bandera=False
                else:
                    os.system("cls")
                    print(input("La opcion ingresada no es valida\n\nPresiona una tecla para continuar..."))
        except:
            os.system("cls")
            print(input("La opcion ingresada no es valida\n\nPresiona una tecla para continuar..."))