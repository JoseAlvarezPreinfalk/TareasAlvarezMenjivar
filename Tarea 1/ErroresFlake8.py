# ERRORES IDENTIFICABLES POR FLAKE8

# 1) Indentación no es un múltiplo de 4 (cantidad de espacios)
if 1 < 2:
    print("Se corrige el error E111 en Flake8")

# 2) Línea de código excede los 79 caracteres
print("La línea de código ya no excede 79 caracteres, evitando un error E501")

# 3) Espacios en blanco luego del último caracter
print("Ya no hay espacios luego del print, no causan un error W291")
