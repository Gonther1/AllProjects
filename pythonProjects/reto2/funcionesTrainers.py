import os
import core
def agregarTrainers():

    isTrue=True

    while isTrue:

        os.system("cls")

        info=core.CargarInfo('trainers.json')

        try:

            id=int(input('Ingrese el id del trainer: '))

            true=True

            while true:

                a=0

                for i in range(0,len(info['trainers'])):

                    if id==info['trainers'][i]['Id']:

                        a+=1

                if a>0:

                    os.system("cls")

                    id=int(input('Este id ya esta registrado\n\nIngrese un nuevo id para el trainer: '))

                else:

                    true=False   

            info['trainers'].append({

                'Id':id,

                'Nombre':input("Ingrese el nombre del trainer: "),

                'EmailPersonal':input("Ingrese el email personal: "),

                'EmailCorporativo':input("Ingrese el email corporativo: "),

                'TelefonoMovil':int(input("Ingrese el telefono movil: ")),

                'TelefonoResidencia':int(input("Ingrese el telefono de residencia: ")),

                'TelefonoEmpresa':int(input("Ingrese el telefono de empresa: ")),

                'TelefonoMovilEmpresarial':int(input("Ingrese el telefono movil empresarial: "))

            })

            core.SubirInfo(info,'trainers.json')

            isTrue=bool(input("Presione enter si desea abandonar: "))

        except:

            os.system("cls")

            isTrue=bool(input("No es posible ingresar texto en esta area\n\nPresione enter si desea abandonar..."))

def eliminarTrainers():

    isTrue=True

    while isTrue:

        os.system("cls")

        info=core.CargarInfo('trainers.json')

        try:

            if len(info['trainers'])>0:

                flag=False

                print('+','-'*74,'+')

                print("|{:^26}{}{:^26}|".format(' ','IDS TRAINERS DISPONIBLES',' '))

                print('+','-'*74,'+')

                for i in range(0,len(info['trainers'])):

                    print(f"--{info['trainers'][i]['Id']}--".center(72))

                IdBorrar=int(input("Ingrese el Id del trainer que quiere eliminar: "))

                for i in range(0,len(info['trainers'])):

                    if IdBorrar==info['trainers'][i]['Id']:

                        print(f"Se elimino el trainer {info['trainers'][i]['Nombre']} con exito")

                        info['trainers'].pop(i)

                        core.SubirInfo(info,'trainers.json')

                        os.system("cls")

                        flag=True

                        isTrue=bool(input("Presione enter si desea abandonar..."))

                if not(flag):

                    os.system("cls")

                    isTrue=bool(input(f"No se encotro el trainer con el id {IdBorrar}\n\nPresione enter si desea abandonar..."))

            else:

                os.system("cls")

                print(input("No hay trainers registrados\n\nPresione una tecla para continuar"))

                isTrue=False

        except:

            os.system("cls")

            print(input("No es posible agregar texto en esta area\n\nPresione una tecla para continuar..."))

def editarTrainers():

    isTrue=True

    while isTrue:

        os.system("cls")

        info=core.CargarInfo('trainers.json')

        try:

            if len(info['trainers'])>0:

                flag=False

                print('+','-'*74,'+')

                print("|{:^26}{}{:^26}|".format(' ','IDS TRAINERS DISPONIBLES',' '))

                print('+','-'*74,'+')

                for i in range(0,len(info['trainers'])):

                    print(f"--{info['trainers'][i]['Id']}--".center(72))

                IdEditar=int(input("Ingrese el Id del trainer que quiere editar: "))

                for i in range(0,len(info['trainers'])):

                    if IdEditar==info['trainers'][i]['Id']:

                        true=True

                        while true:

                            os.system("cls")

                            print('+','-'*74,'+')

                            print("|{:^30}{}{:^34}|".format(' ','MENU EDICION',' '))

                            print('+','-'*74,'+')

                            print("1. Editar nombre")

                            print("2. Editar email personal")

                            print("3. Editar email corporativo")

                            print("4. Editar telefono movil")

                            print("5. Editar telefono de residencia")

                            print("6. Editar telefono de empresa")

                            print("7. Editar telefono movil empresarial")

                            print("8. Volver")

                            print("9. Salir")

                            try:

                                opcion = int(input(":)_"))

                                if (opcion == 1):

                                    info['trainers'][i]['Nombre']=input(f"Ingrese el nuevo nombre para el trainer: ")

                                    while len(info['trainers'][i]['Nombre'])<1:

                                        info['trainers'][i]['Nombre']=input(f"Esta ranura no puede estar vacia\n\nIngrese el nuevo nombre para el trainer: ")

                                elif (opcion == 2):

                                    info['trainers'][i]['EmailPersonal']=input(f"Ingrese el nuevo email personal para el trainer: ")

                                    while len(info['trainers'][i]['EmailPersonal'])<1:

                                        info['trainers'][i]['EmailPersonal']=input(f"Esta ranura no puede estar vacia\n\nIngrese el nuevo email personal para el trainer: ")

                                elif (opcion == 3):

                                    info['trainers'][i]['EmailCorporativo']=input(f"Ingrese el nuevo email corporativo para el trainer: ")

                                    while len(info['trainers'][i]['EmailCorporativo'])<1:

                                        info['trainers'][i]['EmailCorporativo']=input(f"Esta ranura no puede estar vacia\n\nIngrese el nuevo email corporativo para el trainer: ")

                                elif (opcion == 4):

                                    info['trainers'][i]['TelefonoMovil']=int(input(f"Ingrese el nuevo telefono movil para el trainer: "))  

                                elif (opcion == 5):

                                    info['trainers'][i]['TelefonoResidencia']=int(input(f"Ingrese el nuevo telefono de residencia para el trainer: "))

                                elif (opcion == 6):

                                    info['trainers'][i]['TelefonoEmpresa']=int(input(f"Ingrese el nuevo telefono de empresa para el trainer: "))

                                elif (opcion == 7):

                                    info['trainers'][i]['TelefonoMovilEmpresarial']=int(input(f"Ingrese el nuevo telefono movil empresarial para el trainer: "))

                                elif (opcion == 8):

                                    true=False 

                                elif (opcion == 9):

                                    true=False

                                    isTrue=False  

                                else:

                                    os.system("cls")

                                    print(input("Esta opcion no esta disponible\n\nPresione una tecla para continuar..."))

                                core.SubirInfo(info,'trainers.json')

                            except:

                                os.system("cls")

                                print(input("No es posible ingresar texto en esta area\n\nPresione una tecla para continuar"))

                        flag=True

                if not(flag):

                    os.system("cls")

                    isTrue=bool(input(f"No se encotro el trainer con el id {IdEditar}\n\nPresione enter si desea abandonar..."))

            else:

                os.system("cls")

                print(input("No hay trainers registrados\n\nPresione una tecla para continuar"))

                isTrue=False

        except:

            os.system("cls")

            print(input("No es posible agregar texto en esta area\n\nPresione una tecla para continuar..."))

def buscarTrainers():

    isTrue=True

    while isTrue:

        os.system("cls")

        info=core.CargarInfo('trainers.json')

        #try:

        if len(info['trainers'])>0:

            flag=False

            print('+','-'*74,'+')

            print("|{:^26}{}{:^26}|".format(' ','IDS TRAINERS DISPONIBLES',' '))

            print('+','-'*74,'+')

            for i in range(0,len(info['trainers'])):

                print(f"--{info['trainers'][i]['Id']}--".center(72))

            IdBuscar=int(input("Ingrese el Id del trainer que quiere buscar: "))

            for i in range(0,len(info['trainers'])):

                if IdBuscar==info['trainers'][i]['Id']:

                    os.system("cls")

                    print('+','-'*74,'+')

                    print("|{:^32}{}{:^32}|".format(' ','INFO TRAINER',' '))

                    print('+','-'*74,'+')

                    for x,item in info['trainers'][i].items():

                        print(f"{x} : {item}")

                    isTrue=bool(input("Presione enter si desea abandonar..."))

                    flag=True

            if not(flag):

                os.system("cls")

                isTrue=bool(input(f"No se encotro el trainer con el id {IdBuscar}\n\nPresione enter si desea abandonar..."))

        else:

            os.system("cls")

            print(input("No hay trainers registrados\n\nPresione una tecla para continuar"))

            isTrue=False

        #except:

            #os.system("cls")

            #isTrue=bool(input("No es posible agregar texto en esta area\n\nPresione enter si desea abandora..."))