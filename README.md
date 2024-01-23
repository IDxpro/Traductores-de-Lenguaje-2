# Traductores 2

Lexer README
Este código implementa un lexer simple en Python. Un lexer, o analizador léxico, es una parte esencial de un compilador o intérprete que divide el código fuente en tokens, unidades básicas de significado en un lenguaje de programación.

Clases
1. Token
La clase Token representa un token con dos propiedades: type (tipo de token) y value (valor del token).

2. Lexer
La clase Lexer es el analizador léxico principal. Al instanciarla con un texto, puede analizar y dividir ese texto en tokens.

Métodos Principales
error(): Lanza una excepción si encuentra un carácter no válido durante el análisis.

advance(): Avanza al siguiente carácter en el texto.

skip_whitespace(): Avanza a través de los espacios en blanco en el texto.

get_identifier(): Obtiene un identificador (secuencia de letras y dígitos) del texto.

get_real(): Obtiene un número real (con o sin parte decimal) del texto.

OPsuma(): Obtiene operadores de suma o resta del texto.

OPmultiplicacion(): Obtiene operadores de multiplicación o división del texto.

OPRelac(): Obtiene operadores de relación (<, <=) del texto.

OPNot(): Obtiene el operador de negación (!) del texto.

OPAnd(): Obtiene el operador lógico AND (&) del texto.

get_next_token(): Obtiene el próximo token del texto en función del carácter actual.

Ejemplo de Uso
python
Copy code
text = "abc123 45.67 x 33 + - 2 < / 3 ! &"
lexer = Lexer(text)

while True:
    token = lexer.get_next_token()
    if token.type == "EOF":
        break
    print(f"Token: {token.type}, Value: {token.value}")
Este ejemplo instancia un Lexer con un texto dado y luego imprime cada token obtenido a medida que se recorre el texto.

Es importante tener en cuenta que este lexer es un ejemplo básico y puede requerir ajustes según las necesidades específicas del lenguaje que estás analizando.






