# Tendencias e Innovación en Tecnología Agrícola (TEA)
minutos = input("minutos jugados?")
valorPorMinuto = input("valor por minuto?")

# se utiliza la conversion de tipo a int
# sino se hace la conversion existira error porque trata de multiplicar strings
# calculando el valor total de laas minutos jugadas
total = int(minutos) * int(valorPorMinuto)
