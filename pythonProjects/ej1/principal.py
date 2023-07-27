# El centro de entrenamiento de software campus land desea realizar un programa que le permita llevar el control de los candidatos interesados a participar en su programa de entrenamiento.Campus desea realizar un registro previo de los participantes; 
# La informacion que se contempla por cada participante es la siguiente: 
# Nro Id
# ,Nombres
# ,Apellidos
# ,Edad,
# Correo
# Electronico,
# Ciudad de Origen
# ,Estado Civil
# ,Genero
# ,Nro Telefonico.
# Los campers que son menores de edad,deben registrar informacion de acudientes,con la siguiente informacion: 
# Identificacion del acudiente
# ,Nombre del acudiente y 
# parentezco.
# La informacion ingresada debe ser almacenada de forma local
import os
import campers
import core
dataCampers={'campers':[]}
dataAcudientes={'acudientes':[]}
if __name__=="__main__":
    isTrue=True
    if core.checkFile('campers.json')==False or core.checkFile('acudientes.json')==False:
        core.SubirInfo(dataCampers,'campers.json')
        core.SubirInfo(dataAcudientes,'acudientes.json')
    while isTrue:
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^20}{}{:^23}|".format(' ','Menu Principal',' '))
        print('+','-'*55,'+')
        print("1. Registrar campers")
        print("2. Salir")
        opcion=int(input("Opcion: "))
        if opcion==1:
            campers.MainMenu()
        elif opcion==2:
            menu=False