MAX_BLOQUES = 0
TAM_BlOQUE = 0
BLOQUES_USADOS = 0

def menu():
    print("1.-Insertar archivo")
    print("2.-Eliminar archivo")
    print("3.-Visualizar bLoques")
    print("4.-Salir ", end="")
    opcion = int(input())
    return opcion

def insertarC(bloques):
    nombre = input("Da el nombre del archivo: ")
    for i in bloques:
        if i == nombre:
            print("\tError, ya hay un archivo con ese nombre")
            return 0
    tam = int(input("Da el numero de bytes del archivo: "))
    if tam < 1 or tam > MAX_BLOQUES * TAM_BlOQUE:
        print("\tError, tamaño de bloque incorrecto")
        return 0
    noBloques = 0
    if tam < TAM_BlOQUE:
        noBloques = 1
    else:
        if tam % TAM_BlOQUE == 0:
            noBloques = tam/TAM_BlOQUE
        else:
            noBloques = tam//TAM_BlOQUE + 1
    # noBloques = round(tam / TAM_BlOQUE)
    if noBloques > MAX_BLOQUES - BLOQUES_USADOS:
        print("\tError, No hay suficiente memoria")
        return 0
    for i in range(len(bloques)):
        if bloques[i] == "@":
            k = i
            j = 0
            while bloques[k] == "@":
                j += 1
                k += 1
                if j == noBloques:
                    break
                if k > len(bloques)-1:
                    break
            if j == noBloques:
                for k in range(j):
                    bloques[i] = nombre
                    i += 1
                print("\tSe agrego el archivo ",nombre)
                return noBloques
    j = i = 0
    while i < len(bloques):
        if bloques[i] == "@":
            j += 1
            bloques.pop(i)
        else: 
            i += 1
    for i in range(noBloques):
        bloques.append(nombre)
        j -= 1
    for i in range(j):
        bloques.append("@")
    print("\tSe agrego el archivo ",nombre)
    return noBloques

def eliminarC(bloques):
    nombre = input("Da el nombre del archivo a eliminar: ")
    tam = 0
    for i in range(len(bloques)):
        if bloques[i] == nombre:
            while bloques[i] == nombre:
                bloques[i] = "@"
                i += 1
                tam += 1
                if i == MAX_BLOQUES:
                    break
            return tam
    if tam == 0:
        print("No se encontro ese nombre")
    return 0

def insertarNC(bloques):
    nombre = input("Da el nombre del archivo: ")
    for i in bloques:
        if i == nombre:
            print("\tError, ya hay un archivo con ese nombre")
            return 0
    tam = int(input("Da el numero de bytes del archivo: "))
    if tam < 1 or tam > MAX_BLOQUES * TAM_BlOQUE:
        print("\tError, tamaño de bloque incorrecto")
        return 0
    noBloques = 0
    if tam < TAM_BlOQUE:
        noBloques = 1
    else:
        if tam % TAM_BlOQUE == 0:
            noBloques = tam/TAM_BlOQUE
        else:
            noBloques = tam//TAM_BlOQUE + 1
    if noBloques > MAX_BLOQUES - BLOQUES_USADOS:
        print("\tError, No hay suficiente memoria")
        return 0
    j = 0
    for i in range(len(bloques)):
        if bloques[i] == "@":
            bloques[i] = nombre
            j += 1
        if j == noBloques:
            print("\tSe agrego el archivo ",nombre)
            return noBloques
    return 0

def eliminarNC(bloques):
    nombre = input("Da el nombre del archivo a eliminar: ")
    tam = 0
    for i in range(len(bloques)):
        if bloques[i] == nombre:
            bloques[i] = "@"
            tam += 1
    if tam == 0:
        print("No se encontro ese nombre") 
    return tam

if __name__ == '__main__':
    bloques = []
    while True:
        tam = int(input("Da el max de memoria en bytes: "))
        TAM_BlOQUE = int(input("Da el tamaño en bytes del bloque: "))
        if tam % TAM_BlOQUE != 0:
            print("\tTamaño de bloque incorrecto,de otro")
        else:
            MAX_BLOQUES = tam // TAM_BlOQUE
            break
    for i in range(MAX_BLOQUES):
        bloques.append('@')
    while True:
        print("De el tipo de almacenamiento")
        print("1.-Contigua\n2.-No contigua ", end = "")
        tipo = int(input())
        if tipo != 1 and tipo != 2:
            print("\tOpcion incorrecta, de otra")
        else:
            break
    # Forma Contigua
    print("------------------")
    if tipo == 1:
        while True:
            print("Numero de bloques ocupados ",BLOQUES_USADOS)
            opcion = menu()
            if opcion == 1:
                BLOQUES_USADOS +=  insertarC(bloques)
            elif opcion == 2:
                BLOQUES_USADOS -= eliminarC(bloques)
            elif opcion == 3:
                for i in bloques:
                    print("[ ",i," ]")
            elif opcion == 4:
                print("Gracias por usar este programa")
                break
            else:
                print("Opcion incorrecta, de otra")
    # Forma No continua
    else:
        while True:
            print("Numero de bloques ocupados ",BLOQUES_USADOS)
            opcion = menu()
            if opcion == 1:
                BLOQUES_USADOS +=  insertarNC(bloques)
            elif opcion == 2:
                BLOQUES_USADOS -= eliminarNC(bloques)
            elif opcion == 3:
                for i in bloques:
                    print("[ ",i," ]")
            elif opcion == 4:
                print("Gracias por usar este programa")
                break
            else:
                print("Opcion incorrecta, de otra")

