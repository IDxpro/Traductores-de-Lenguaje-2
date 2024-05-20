
import re

def analizador_semantico(codigo):
    # Expresión regular para detectar declaraciones de variables y asignaciones
    patron_declaracion = r'(\w+)\s+(\w+)\s*;'
    patron_asignacion = r'(\w+)\s*=\s*(\w+)\s*([+\-*/])\s*(\w+)\s*;'

    # Buscar coincidencias de declaraciones y asignaciones
    coincidencias_declaracion = re.findall(patron_declaracion, codigo)
    coincidencias_asignacion = re.findall(patron_asignacion, codigo)

    # Analizar las declaraciones
    for tipo, variable in coincidencias_declaracion:
        print(f"Se encontró una declaración de variable: Tipo: {tipo}, Variable: {variable}")

    # Analizar las asignaciones
    for var_destino, var1, operador, var2 in coincidencias_asignacion:
        print(f"Se encontró una asignación: {var_destino} = {var1} {operador} {var2}")

# Código de ejemplo
codigo_c = """
int main(){
float a;
int b;
int c;
c = a+b;
c = suma(8,9);
}
"""

analizador_semantico(codigo_c)