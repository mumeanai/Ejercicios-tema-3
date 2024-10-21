def fecha_en_intervalo(fecha, fecha_min, fecha_max):
    #return fecha_min <= fecha <= fecha_max
    #podria escribirse asi, pero al meter el tema de los none, resulta mas complicado
    #se recomienda que cuando haya varios parametros de filtrado, se traten de froma separado
    return (fecha_min == None or fecha_min <= fecha) and (fecha_max == None or fecha <= fecha_max)