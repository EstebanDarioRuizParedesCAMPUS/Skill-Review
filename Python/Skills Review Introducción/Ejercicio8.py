""" 8. Escriba un bloque cualquiera de código en Python en donde
utilice 2 condicionales (if) anidados. """

edad = int(input(f"¿Cuál es tu edad? "))
estatura = float(input(f"¿cuál es tu estatura en metros? "))

if edad > 18:
    if estatura < 1.60:
        print(f"No alcanzas la estatura mínima para entrar")
    else:
        print(f"Bienvenido, puedes pasar")
else:
    if estatura > 1.10:
        print(f"Ve a la sección de atracciones infantiles")
    else:
        print(f"No tenemos juegos para niños tan pequeños")