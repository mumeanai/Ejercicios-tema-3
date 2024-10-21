def imprime_diccionario(diccionario):
    for clave in diccionario:
        valor = diccionario[clave]
        print(clave, "===>", valor)
    #otra forma:
    for clave, valor in diccionario.items():
        print(clave, "===>", valor)
        
        
#prueba
precios_productos = {
    "manzana": 0.5,
    "plátano": 0.3,
    "naranja": 0.6,
    "uva": 1.2,
    "fresa": 2.5
}
imprime_diccionario(precios_productos)