""" 9. Construya un algoritmo en Python, que permita ingresar la
información de un empleado e imprima el nombre, los
apellidos y la antigüedad. Los datos que se deben solicitar
son los siguientes:
*Nombre * Teléfono *Año de ingreso a la empresa
*Apellidos *Edad. """

print(f"Por favor ingrese los siguientes datos")
print(f"Nombre: ")
nombre = input()
print(f"Apellido: ")
apellido = input()
print(f"Edad: ")
edad = int(input())
print(f"Teléfono: ")
telefono = int(input())
print(f"Año de ingreso a la empresa")
añoEmpleo = int(input())

print(f"{nombre} {apellido} lleva trabajando en esta empresa {2023-añoEmpleo} años")