import os
import pacientes
import veterinarios
import citas
if __name__ == "__main__":
    isActivate = True
    opcion=0
    bandera=True
    while bandera:
        try:
            while isActivate:
                os.system("cls")
                print('+','-'*74,'+')
                print("|{:^20}{}{:^19}|".format(' ','ADMINISTRACION DEL CENTRO VETERINARIO',' '))
                print('+','-'*74,'+')
                print("1. Gestion de pacientes")
                print("2. Gestion de veterinarios")
                print("3. Gestion de citas medicas")
                print("4. Salir")
                opcion = int(input(":)_"))
                if (opcion == 1):
                    pacientes.MainMenu()
                elif (opcion == 2):
                    veterinarios.MainMenu()
                elif (opcion == 3):
                    citas.MainMenu()
                elif (opcion == 4):
                    isActivate=False  
                    bandera=False
                    print(input("Prueba"))
                else:
                    os.system("cls")
                    print(input("La opcion ingresada no es valida\n\nPresiona una tecla para continuar..."))        
        except:
            os.system("cls")
            print(input("La opcion ingresada no es valida\n\nPresiona una tecla para continuar..."))
      
    
