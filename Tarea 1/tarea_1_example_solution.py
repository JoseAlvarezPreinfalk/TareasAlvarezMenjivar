
"""
 Métodos Tarea 1 Microprocesadores y Microcontroladores
 José Pablo Álvarez Preinfalk y Marcela Menjívar Sánchez
 Ing. Rodolfo Piedra Camacho
 15 de agosto, 2025

"""


"""  Códigos de Errores Únicos

     -100 -> cadena no es string
     -200 -> cadena no es alfanumérico
     -300 -> caracter tiene más de un caracter o no es alfanumérico
     -400 -> parámetros no son enteros positivos
     -500 -> multiplo no es uno de los siguiente números: 1, 2, 4, 8, 16
       0  -> operación exitosa

"""


def count_char(cadena, caracter):  # Recibe parámetros cadena y caracter

    # A) Verifica que cadena sea string
    if not isinstance(cadena, str):  # Verifica si es string
        return -100, None  # Si no, código de error

    # B) Verifica que cadena solo sean letras y números
    if not cadena.isalnum():  # Librería verifica caracteres alfanuméricos
        return -200, None  # Si no, código de error

    # C) Verifica que carácter sea un único carácter del abecedario o número
    if not isinstance(caracter, str) or len(caracter) != 1 \
            or not caracter.isalnum():
        return -300, None  # Si no es carácter único y alfanumérico

    # D) Cuenta cuántas veces aparece el parámetro carácter en la cadena
    cantidad = cadena.count(caracter)  # count() cuenta cuántas veces aparece
    return 0, cantidad  # Retornar código de éxito y cantidad


def multiplo_2(base, multiplo):  # Recibe los parámetros: base y multiplo

    # A) Verifica que entradas sean enteros positivos
    # isinstance() ve si son enteros y luego < 0 si son positivos
    if not (isinstance(base, int) and isinstance(multiplo, int)) \
            or base <= 0 or multiplo <= 0:
        return -400, None  # Si verificación falla, retornar código de error

    # B) Verifica que "múltiplo" sea uno entre: 1, 2, 4, 8, 16
    if multiplo not in (1, 2, 4, 8, 16):
        return -500, None  # Si verificación falla, retornar código de error

    # C) Calcula operación muliplo*base (Sin +, * o ciclos for)
    # En binario, multiplicar por potencias de 2 se traduce en un
    # desplazamiento a la izquierda

    desplazar = multiplo.bit_length() - 1
    # Se cuentan bits de "multiplo" y se resta 1 para desplazarse lo
    # correspondiente a la multiplicación

    result = base << desplazar  # Se desplaza la base (binario) según desplazar
    return 0, result  # Retorna código de éxito y resultado de multiplicación
