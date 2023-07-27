import funcionesCitas as f
import os
import core
def MainMenu():
    
    isTrue=True
    while isTrue:
        os.system("cls")
        print('GESTION CITAS\n'.center(50))
        print('1-Agregar citas')
        print('2-Cancelar citas')
        print('3-Buscar citas')
        print('4-Editar citas')
        print('5-Volver')
        try:
            opcion=int(input(":)_"))
            if opcion==1:
                f.agregarCita() 
            elif opcion==2:
                f.cancelarCita()        
            elif opcion==3:
                f.buscarCitas()        
            elif opcion==4:
                f.editarCitas()        
            elif opcion==5:
                isTrue=False
        except:
            os.system("cls")
            print(input("No es posible agregar texto en esta area\n\nPresione enter para continuar"))