import json
import os

#data={"data":[]}



def SubirInfo(args:dict,fileName:str):
    texto=json.dumps(args)
    a=json.loads(texto)
    with open(f'data/{fileName}.json', "w") as f:
        json.dump(a,f,indent=4)
        f.close()
    print("Realizado con exito")

def razasMascotas(razas:list,tipo:str):
    while True:
        os.system("cls")
        print(f"Razas de {tipo}\n")
        for i,item in enumerate(razas):
            print (f"{i+1}-{item}", end=" ")
        print("\n")
        try:      
            raza=int(input("Ingrese el numero dependiendo de la raza: "))
            if raza==1:
                razaMascota=razas[0]
                break
            elif raza==2:
                razaMascota=razas[1]
                break
            elif raza==3:
                razaMascota=razas[2]
                break
            elif raza==4:
                razaMascota=razas[3]
                break
            else:
                print(input("El tipo de raza no existe"))
        except:
            print(input("El tipo de raza no existe"))
    return razaMascota
def TipoRazaMascota():
    IsTrue=True
    while True:
        try:
            os.system("cls")
            tipo=int(input("Tipos de mascotas disponibles\n\n1-Perro\n2-Gato\n3-Reptil\n4-Ave\n\nIngrese el numero dependiendo de la mascota: "))
            if tipo==1:
                tipoMascota="Perro"
                raza=razasMascotas(["Labrador","Bulldog","Beagle","Bullterrier"],"Perros")
                break
            elif tipo==2:
                tipoMascota="Gato"
                raza=razasMascotas(["Persa","Siames","Bengali","MaineCoon"],"Gatos")
                break
            elif tipo==3:
                tipoMascota="Reptil"
                raza=razasMascotas(["Boa","Iguana","Tortuga","Bullterrier"],"Cocodrilo")
                break
            elif tipo==4:
                tipoMascota="Ave"
                raza=razasMascotas(["Aguila","Buho","Loro","Pinguino"],"Aves")
                break 
            else:
                print(input("El tipo de mascota ingresado no existe"))     
        except:
            print(input("El tipo de mascota ingresado no existe"))
    return tipoMascota,raza   

#data["data"].append(a)
#print(input("Pausa"))
#SubirInfo(data)
# Output: {"name": "Bob", "age": 12, "children": null}