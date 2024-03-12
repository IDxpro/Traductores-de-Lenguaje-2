# Analizador Sintáctico

Este es un simple analizador sintáctico implementado en Python. El analizador toma una cadena de entrada y verifica si la sintaxis de la expresión es correcta según unas reglas predefinidas. El analizador utiliza un lexer para obtener los tokens de la cadena de entrada.

## Clase SyntaxAnalyzer

La clase `SyntaxAnalyzer` implementa las reglas de la gramática para analizar la sintaxis de la expresión. Contiene los siguientes métodos:

- **__init__(lexer)**: Inicializa el analizador sintáctico con un lexer proporcionado.
- **error(message="Syntax error")**: Lanza una excepción si se encuentra un error de sintaxis.
- **eat(expected_type)**: Avanza al siguiente token si el tipo esperado coincide con el tipo del token actual.
- **factor()**: Analiza un factor de la expresión (identificador, número real o expresión entre paréntesis).
- **term()**: Analiza un término de la expresión (producto o división de factores).
- **expression()**: Analiza la expresión completa.
- **parse()**: Inicia el análisis sintáctico de la expresión.

## Uso

Para usar el analizador sintáctico, primero debes instanciar un lexer con la cadena de entrada y luego crear una instancia de `SyntaxAnalyzer` pasando el lexer como argumento. Después, llama al método `parse()` para realizar el análisis sintáctico.

```python
text = "abc123 45.67 + 33 - 2 * 3 / 4"
lexer = Lexer(text)
syntax_analyzer = SyntaxAnalyzer(lexer)
success = syntax_analyzer.parse()

if not success:
    print("Maneja la entrada incorrecta aquí")
