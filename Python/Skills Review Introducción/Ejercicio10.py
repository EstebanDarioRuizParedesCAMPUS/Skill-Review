""" 10. En su casa le solicitan que realice un algoritmo en Python,
que permita calcular el valor a pagar por concepto de
energía eléctrica. Los datos que se conocen son los
siguientes:
- Mes de consumo - Valor kw
-Total kw consumido en el mes - estrato """

Meses = ["Null","Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
Estrato = ["null",1,2,3,4,5,6]
vkw = ["null",315.6,394.5,667.9,785.8,942.9,942.9]
numes = int(input(f"Ingrese en que mes estás (números): "))
numestratro = int(input(f"Ingresa tu estrato: "))
kwusado = int(input(f"¿Cúantos kw has usado en el mes? "))

print(f"En {Meses[numes]} debes pagar un total de COP${vkw[numestratro]*kwusado} al estar en estrato {Estrato[numestratro]}")
