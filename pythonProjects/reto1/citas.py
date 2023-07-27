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
                print("|{:^27}{}{:^25}|".format(' ','GESTION DE CITAS MEDICAS',' '))
                print('+','-'*74,'+')
                print("1. Crear cita")
                print("2. Cancelar cita")
                print("3. Consultar citas por fecha")
                print("4. Consultar citas por veterinario")
                print("5. Volver al menu principal")
                opcion = int(input(":)_"))
                if (opcion == 1):
                    print(input(f"{opcion}"))
                elif (opcion == 2):
                    print(input(f"{opcion}"))
                elif (opcion == 3):
                    print(input(f"{opcion}"))
                elif (opcion == 4):
                    pass
                elif (opcion == 5):
                    isActivate=False        
                    bandera=False
                else:
                    os.system("cls")
                    print(input("La opcion ingresada no es valida\n\nPresiona una tecla para continuar..."))
        except:
            os.system("cls")
            print(input("La opcion ingresada no es valida\n\nPresiona una tecla para continuar..."))