import pila

def parsear(cadena_entrada):
    pila = Pila()
    pila.push("<programa>")  # Símbolo inicial
    cadena_entrada = cadena_entrada.split()
  
    while not pila.esta_vacia() and cadena_entrada:
        tope = pila.ver_tope()

        if tope.startswith("$"):  # Si el tope de la pila es una regla
            regla = tope
            pila.pop()

            if regla.startswith("$0"):  # Aplicar transformaciones de regla
                regla = regla[3:]  # Eliminar el prefijo "$0"
                if regla.endswith(";"):
                    regla = regla[:-1]  # Eliminar el punto y coma final
                pila.push(regla)
            elif regla.startswith("$"):
                num_regla = int(regla[1])
                for _ in range(num_regla):
                    pila.pop()

        elif tope == cadena_entrada[0]:  # Si el tope de la pila coincide con la entrada
            pila.pop()
            cadena_entrada.pop(0)

        else:
            print("¡Error de análisis!")
            return

    if pila.esta_vacia() and not cadena_entrada:
        print("¡Análisis exitoso!")
    else:
        print("¡Error de análisis!")


# Probar el analizador con una cadena de entrada
cadena_entrada = "int hola;"
parsear(cadena_entrada)
