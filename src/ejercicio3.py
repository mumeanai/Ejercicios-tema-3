def imprime_pares(n):
    '''
    Imprime los números positivos pares menores o iguales a n
    '''
    
    numero = 2 #podria poner 0, dependiendo de como lo consideremos
    
    #while numero <= n:
    #    print(numero, end=" ")
    #    numero += 2
    
    for numero in range(2, n+1, 2):
        print(numero, end = " ")

imprime_pares(10)