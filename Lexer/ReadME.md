Analizador de Gramática en Python
Este proyecto implementa un analizador básico de gramática en Python. Utiliza una pila para aplicar reglas de producción a una cadena de entrada y determinar si la cadena es válida según la gramática especificada.

Funcionalidades
Análisis de Gramática: El analizador puede procesar cadenas de entrada y verificar si cumplen con las reglas gramaticales definidas.
Reglas de Producción: Se pueden definir reglas de producción para especificar la gramática del lenguaje a analizar.
Cómo usar
Clonar el Repositorio:

bash
Copy code
git clone https://github.com/tu_usuario/analizador-gramatica-python.git
Ejecutar el Código:

bash
Copy code
cd analizador-gramatica-python
python main.py
Probar con Diferentes Entradas:

Modifica el archivo main.py para proporcionar diferentes cadenas de entrada y observar cómo el analizador las procesa.

Ejemplo
Supongamos que tenemos la siguiente gramática:

php
Copy code
<programa> ::= <Definiciones>
<Definiciones> ::= <Definicion> <Definiciones> | \e
<Definicion> ::= <DefVar>
<DefVar> ::= tipo identificador <ListaVar> ;
<ListaVar> ::= identificador , <ListaVar> | identificador
Y queremos analizar la cadena de entrada "int x, y;". El analizador verificará si esta cadena es válida según la gramática definida.

Contribuciones
Las contribuciones son bienvenidas. Si encuentras algún error, tienes ideas para mejoras o deseas añadir nuevas funcionalidades, no dudes en abrir un issue o enviar un pull request.

Licencia
Este proyecto está bajo la Licencia MIT.

