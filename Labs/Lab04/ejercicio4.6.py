def calcularpago(horas, tarifa):
    MAX_HORAS= 40
    if (horas > MAX_HORAS):
        horas_extras = horas - MAX_HORAS
    else:
        horas_extras = 0
        calculo = (horas*tarifa) + (horas_extras * (tarifa/2))
        return calculo

try:
            horas = float(input("Ingrese número de horas: "))
            tarifa = float(input("Ingrese tarifa: "))
            pago = calcularpago(horas, tarifa)
            print(pago)
except: 
    print("Error, valor ingresado no válido")
