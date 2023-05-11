nombre = input("¿Nombre?: ")
ventas = float(input("¿n° de ventas?: "))
comision = round(ventas * 13 / 100, 2)


print(f"Ok, {nombre}. Este mes ganaste {comision} por tus ventas")


