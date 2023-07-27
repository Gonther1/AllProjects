import os
import core
import citas
data={'citas':[]}
if __name__=='__main__':
    if core.checkFile('citas.json')==False:
        core.SubirInfo(data,'citas.json')
    isTrue=True
    while isTrue:
        os.system("cls")
        print('Menu principal'.center(50))
        print('1-Gestion citas')
        print('2-Salir')
        try:
            opcion=int(input(":)_"))
            if opcion==1:
                citas.MainMenu()
            elif opcion==2:
                print("Hasta la proxima :)")
                isTrue=False
        except:
            os.system("cls")
            print(input("No es posible agregar texto en esta area\n\nPresione enter para continuar"))
        
    
    