def indica_primera_aparicion(lista, valor): 
    posicion = -1 #le pongo posicion -1, porque si valor nunca esta en la lista, 
    #no se entra ene el for, y me han dicho que si no esta, devuelva -1
    for i, elem in enumerate(lista):
        if elem == valor:
            posicion == i
            break
    #sin el break, el codigo devolveria la ultima posicion, pero piden la ultima 
    return posicion