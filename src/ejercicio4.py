def imprime_pares_inverso(n):
    '''
    Imprime los números positivos pares menores o iguales a n
    '''
    
    if n%2 == 0:
        numero = n #podria poner 0, dependiendo de como lo consideremos
    else: 
        numero = n-1
    
    while numero >= 2:
        print(numero, end=" ")
        numero -= 2
    
    #for numero in range(2, n+1):
    #    print(numero, end = " ")

imprime_pares_inverso(9)