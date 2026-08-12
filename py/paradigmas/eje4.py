# Alumnos: Cohen Tiago, De la Cruz Alfredo y Meo Nielsen Tiago
def convertir_binario_a_decimal(binario):
    # La variable 'decimal' acumulará el resultado
    decimal = 0
    # El exponente para un número de 8 bits empieza en 7 (2^7 = 128)
    exponente = 7
    
    for bit in binario:
        if bit == '1':
            # Si hay un 1, sumamos la potencia de 2 correspondiente
            decimal = decimal + (2 ** exponente)
        
        # Bajamos el exponente para la siguiente posición (6, 5, 4...)
        exponente = exponente - 1
        
    return decimal

# --- Bloque Principal ---
# Pedimos al usuario que ingrese el número (Consigna Ejercicio 4)
numero_binario = input("Ingrese un número binario de 8 bits: ")

# Verificamos que tenga 8 caracteres
if len(numero_binario) == 8:
    resultado = convertir_binario_a_decimal(numero_binario)
    print(f"El equivalente decimal es: {resultado}") 
else:
    print("Error: El número debe tener exactamente 8 bits.")