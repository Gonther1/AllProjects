import json

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