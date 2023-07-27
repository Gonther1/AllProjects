import os
import core
def MainMenu():
    data={"Pacientes":[]}
    id=0
    isActivate = True
    opcion=0
    bandera=True
    while bandera:
        try:
            while isActivate:
                os.system("cls")
                print('+','-'*74,'+')
                print("|{:^27}{}{:^29}|".format(' ','GESTION DE PACIENTES',' '))
                print('+','-'*74,'+')
                print("1. Agregar paciente")
                print("2. Buscar paciente")
                print("3. Mostrar informacion de un paciente")
                print("4. Volver al menu principal")
                opcion = int(input(":)_"))
                if (opcion == 1):
                    while True:
                        dueño=input("Ingrese el nombre del dueño: ")
                        nombre=input("Ingrese el nombre de la mascota: ")
                        edad=int(input("Ingrese la edad de la mascota: "))
                        resultado=core.TipoRazaMascota()
                        tipoMascota,razaMascota=resultado
                        data["Pacientes"][id]={
                            "Id":id,
                            "Dueño":dueño,
                            "Mascota":nombre,
                            "EdadMascota":edad,
                            "Tipo": tipoMascota,
                            "Raza": razaMascota
                        }
                        core.SubirInfo(data,"pacientes")
                        break
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