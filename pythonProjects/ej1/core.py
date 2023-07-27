import json
import os
def registroCampers():
    info=core.CargarInfo('campers.json')
    nombre=input("Ingrese el nombre del camper: ")
    while len(nombre)<1:
        nombre=input("Esta area no puede estar vacia\n\nIngrese el nombre del camper: ")
    apellido=input("Ingrese el apellido del camper: ")
    while len(apellido)<1:
        apellido=input("Esta area no puede estar vacia\n\nIngrese el apellido del camper: ")
    edad=int(input("Ingrese la edad del camper: "))
    while edad<1:
        edad=int(input("El dato ingresado no es valido\n\nIngrese la edad del camper: "))
    

# El centro de entrenamiento de software campus land desea realizar un programa que le permita llevar el control de los candidatos interesados a participar en su programa de entrenamiento.Campus desea realizar un registro previo de los participantes; La informacion que se contempla por cada participante es la siguiente: Nro Id
# ,Nombres
# ,Apellidos
# ,Edad
# ,Correo Electronico
# ,Ciudad de Origen
# ,Estado Civil
# ,Genero
# ,Nro Telefonico.

# Los campers que son menores de edad,deben registrar informacion de acudientes,con la siguiente informacion: 
# Identificacion del acudiente
# ,Nombre del acudiente
#  y parentezco.
# La informacion ingresada debe ser almacenada de forma local

def CargarInfo(fileName):
    if (checkFile(fileName)==True):
        with open('data/'+fileName,'r') as f:
            dicc=json.load(f)
            f.close()
        return dicc
    
def SubirInfo(args:dict, fileName:str):
    texto=json.dumps(args)
    dicc=json.loads(texto)
    with open(f'data/{fileName}','w') as f:
        json.dump(dicc,f,indent=4)
        
def checkFile(fileName):
    try:
        with open('data/'+fileName, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False