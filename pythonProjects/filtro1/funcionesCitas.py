import core
import os
import pprint
def agregarCita():
    info=core.CargarInfo('citas.json')
    isTrue=True
    while isTrue:
        os.system("cls")
        true=True    
        try:
            os.system("cls")
            id=int(input("Ingrese el id de la cita: "))
            while true:
                b=0
                for i in range(0,len(info['citas'])):
                    if id==info['citas'][i]['Id']:
                        os.system('cls')
                        id=int(input("El id esta repetido\n\nIngrese un id nuevo para esta cita: "))
                        b=1
                if b<1:
                    true=False
            os.system("cls")
            nombre=input("Ingrese el nombre del paciente: ")
            while (len(nombre)<1):
                os.system("cls")
                nombre=input("El nombre del paciente no puede estar vacio\nIngrese el nombre del paciente: ")
            os.system("cls")   
            fecha=modificarFecha()
            os.system("cls")
            hora=modificarHora()
            os.system("cls")
            motivo=input("Ingrese el motivo de la consulta: ")
            while (len(motivo)<1):
                os.system("cls")
                motivo=input("El motivo de la consulta no puede estar vacio\nIngrese el motivo de la consulta: ")
            info['citas'].append({
                'Id':id,
                'NombrePaciente':nombre,
                'FechaCita':fecha,
                'HoraCita':hora,
                'MotivoCita':motivo
            })
            core.SubirInfo(info,'citas.json')
            isTrue=bool(input("Presione enter si desea abandonar..."))
        except:
            os.system("cls")
            isTrue=bool(input("No es posible agregar texto en esta area\n\nPresione enter si desea abandonar..."))

def cancelarCita():
    info=core.CargarInfo('citas.json')
    isTrue=True
    while isTrue:
        if (len(info['citas'])>0):
            try:
                os.system('cls')
                print('IDS CITAS DISPONIBLES'.center(50))
                for i in range(0,len(info['citas'])):
                    print(f'{info["citas"][i]["Id"]}'.center(50))
                a=0
                id=int(input("Ingrese el id de la cita que quiere cancelar: "))
                for i in range(0,len(info['citas'])):
                    if id==info['citas'][i]['Id']:
                        os.system('cls')
                        print(f'Se cancelo la cita con id {id} correctamente')
                        info['citas'].pop(i)
                        core.SubirInfo(info,'citas.json')
                        a=1
                        isTrue=bool(input("Presione enter si desea abandonar..."))
                if a<1:
                    os.system("cls")
                    isTrue=bool(input(f'No se encontro la cita con el id {id}\n\nPresione enter si desea abandonar...'))
            except:
                os.system("cls")
                isTrue=bool(input("No es posible agregar texto en esta area\n\nPresione enter para continuar"))
        else:
            os.system("cls")
            print(input("No hay citas registradas\n\nPresione enter si desea abandonar..."))
            isTrue=False

def editarCitas():
    info=core.CargarInfo('citas.json')
    isTrue=True
    while isTrue:
        if (len(info['citas'])>0):
            try:
                os.system('cls')
                print('IDS CITAS DISPONIBLES'.center(50))
                for i in range(0,len(info['citas'])):
                    print(f'{info["citas"][i]["Id"]}'.center(50))
                a=0
                id=int(input("Ingrese el id de la cita que quiere editar: "))
                for i in range(0,len(info['citas'])):
                    if id==info['citas'][i]['Id']:
                        os.system('cls')
                        isFlag=True
                        while isFlag:
                            os.system("cls")
                            print('Informacion a editar\n'.center(50))
                            print('1-Nombre del paciente')
                            print('2-Fecha de la cita')
                            print('3-Hora de la cita')
                            print('4-Motivo de la cita')
                            print('5-Volver')
                            print('6-Salir al menu principal')
                            dato=int(input(":)_"))
                            if dato==1:
                                os.system("cls")
                                nombre=input("Ingrese el nombre del paciente: ")
                                while (len(nombre)<1):
                                    os.system("cls")
                                    nombre=input("El nombre del paciente no puede estar vacio\nIngrese el nombre del paciente: ")
                                info['citas'][i]['NombrePaciente']=nombre
                                core.SubirInfo(info,'citas.json')
                            elif dato==2:
                                os.system("cls")
                                fecha=modificarFecha() 
                                info['citas'][i]['FechaCita']=fecha
                                core.SubirInfo(info,'citas.json')
                            elif dato==3:
                                os.system("cls")
                                hora=modificarHora()
                                info['citas'][i]['HoraCita']=hora
                                core.SubirInfo(info,'citas.json')
                            elif dato==4:
                                os.system("cls")
                                motivo=input("Ingrese el motivo de la consulta: ")
                                while (len(motivo)<1):
                                    os.system("cls")
                                    motivo=input("El motivo de la consulta no puede estar vacio\nIngrese el motivo de la consulta: ")
                                info['citas'][i]['MotivoCita']=motivo
                                core.SubirInfo(info,'citas.json')
                            elif dato==5:
                                isFlag=False
                            elif dato==6:
                                isFlag=False
                                isTrue=False  
                        a=1
                if a<1:
                    os.system("cls")
                    isTrue=bool(input(f'No se encontro la cita con el id {id}\n\nPresione enter si desea abandonar...'))
            except:
                os.system("cls")
                isTrue=bool(input("No es posible agregar texto en esta area\n\nPresione enter si desea abandonar"))
        else:
            os.system("cls")
            print(input("No hay citas registradas\n\nPresione enter para continuar..."))
            isTrue=False
def buscarCitas():
    info=core.CargarInfo('citas.json')
    isTrue=True
    while isTrue:
        if (len(info['citas'])>0):
            try:
                os.system("cls")
                print("METODOS DE BUSQUEDA".center(50))
                print("1-Nombre")
                print("2-Fecha")
                print("3-Volver")
                opcion=int(input(":)_"))
                if opcion==1:
                    flag=True
                    a=0
                    while flag:
                        os.system("cls")
                        nombre=input("Ingrese el nombre que quiere buscar: ")
                        for i in range(0,len(info['citas'])):
                            if nombre==info['citas'][i]['NombrePaciente']:
                                print(info['citas'][i])
                                a=1
                        if a<1:
                            os.system("cls")
                            print("No existe ninguna cita con este paciente")
                        flag=bool(input("Presione enter si quiere volver..."))
                elif opcion==2:
                    flag=True
                    while flag:
                        os.system("cls")
                        fecha=modificarFecha()
                        for i in range(0,len(info['citas'])):
                            if fecha==info['citas'][i]['FechaCita']:
                                print(json.dumps(info['citas'][i],sort_keys=False,ident=4))
                                a=1
                        if a<1:
                            os.system("cls")
                            print("No existe ninguna cita con esta fecha")
                        flag=bool(input("Presione enter si quiere volver..."))
                elif opcion==3:
                    isTrue=False
            except:
                os.system("cls")
                print(input("No es posible agregar texto en esta area\n\nPresione enter para continuar"))               
        else:
            os.system("cls")
            print(input("No hay citas registradas\n\nPresione enter para continuar..."))
            isTrue=False
def modificarFecha():
    try:
        dia=int(input("Ingrese el numero del dia: "))
        while (dia>31 or dia<1):
            dia=int(input("Recuerda que solo hay 31 dias\n\nIngrese un numero de dia valido: "))
        if dia<10 and dia>0:
            diaConcreto=f'0{dia}'
        else:
            diaConcreto=dia
        mes=int(input("Ingrese el numero del mes "))
        while (mes<1 or mes>12):
            mes=int(input("Recuerda que solo hay 12 meses\n\nIngrese el numero del mes "))
        if mes<10 and mes>0:
            mesConcreto=f'0{mes}'
        else:
            mesConcreto=mes
        año=int(input("Ingrese el año "))
        while (año<1990 or año>2024):
            año=int(input("Años validos desde 1990 hasta 2024\n\nIngrese un año valido "))
        fecha=f'{diaConcreto}/{mesConcreto}/{año}'
        return fecha
    except:
        print(input("No es posible agregar texto en esta area\n\nPresione enter para continuar"))

def modificarHora():
    try:
        horas=int(input("Ingrese la hora en la que se realizara la cita: "))
        while (horas<0 or horas>23):
            os.system("cls")
            horas=int(input("La hora de la cita medica no puede ser negativa ni mas que 23\nIngrese el hora de la cita medica: "))
        if horas<10 and horas>0:
            horaConcreta=f'0{horas}'
        else:
            horaConcreta=horas
        minutos=int(input("Ingrese los minutos en los que tendra la cita: "))
        while (minutos<0 or minutos>59):
            minutos=int(input("Ingrese los minutos en los que tendra la cita: "))
        if minutos<10 and minutos>=0:
            minutoConcreto=f'0{minutos}'
        else:
            horaConcreta=horas
        hora=f'{horaConcreta}:{minutoConcreto}'
        return hora
    except:
        print(input("No es posible agregar texto en esta area\n\nPresione enter para continuar"))