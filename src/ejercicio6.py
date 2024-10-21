def calcula_precios(precio_normal, edades):
    
    precio_reducido = precio_normal/2
    precios = []
    for edad in edades:
        if edad <= 18 or edad >= 65:
            precios.append(precio_reducido)
        else: 
            precios.append(precio_normal)
    return precios

precios = calcula_precios(6, [8,48, 90])
print(precios)
    