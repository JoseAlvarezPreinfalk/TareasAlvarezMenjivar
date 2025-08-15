# ERRORES IDENTIFICABLES POR FLAKE8

# 1) Indentación no es un múltiplo de 4 (cantidad de espacios)
if 1 < 2:
  print("Error E111 en Flake8")

# 2) Línea de código excede los 79 caracteres
print("La línea de código contiene más de 79 caracteres, causando un error E501")

# 3) Espacios en blanco luego del último caracter
print("Los espacio luego del print causan un error W291")   
