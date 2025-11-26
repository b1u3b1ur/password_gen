import random 

def guardar(data):
    pass

def cargar():
    pass

password = 0

list = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[',
    ']', '{', '}', '|', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?',
    '`', '~'
]

per = int(input("1:Para generar contrasena 2:Para ver anteriores: "))
if per == 1:
    while per == 1:
        password += 1
        qu = int(input('De que longitud desea su clave: '))

        gn = [random.choice(list) for i in range(qu)]
        generator = str(gn)
        result = generator.replace('[', "")
        result = result.replace(']',"")
        result = result.replace(",","")
        result = result.replace("'","")
        result = result.replace(" ","")
        
        guardar(result)
    
        print(f'{result}:{password}')
    
        per = int(input("0:para salir 1:cambiar de clave: "))

elif per == 2:
    pass