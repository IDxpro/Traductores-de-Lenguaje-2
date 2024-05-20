import re
import ast


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


def creador_ast(codigo):
    # Parsear el código en un AST
    tree = ast.parse(codigo)

    # Función para imprimir el AST de manera estilizada
    def pprint_ast(node, indent=0, is_leaf=False):
        if isinstance(node, ast.AST):
            print(' ' * indent + f"Nodo: {type(node).__name__}")
            for child_node in ast.iter_child_nodes(node):
                pprint_ast(child_node, indent + 4)
        else:
            print(' ' * indent + f"Hoja: {node}")

    # Imprimir el AST estilizado
    pprint_ast(tree)


# Código de ejemplo
codigo_c = """
"""

"""
def main():
  a = 10
  b = 20
  c = a - b
  return 0
"""

analizador_semantico(codigo_c)
creador_ast(codigo_c)
