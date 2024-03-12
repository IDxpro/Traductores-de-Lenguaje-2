Importaciones y Definiciones:
Importamos las bibliotecas necesarias de Tkinter para crear la interfaz gráfica
(tk, filedialog, messagebox).
Importamos el namedtuple de la biblioteca collections para definir la estructura
de los tokens.
Definimos un namedtuple llamado Token para representar un token con un tipo
y un valor.
Clase Lexer:
Esta clase se encarga de analizar el texto del código fuente y producir tokens.
Tiene métodos para avanzar en el texto, saltar espacios en blanco, obtener
identificadores, números reales y cadenas, y obtener el siguiente token.
El método error() se utiliza para generar una excepción cuando se encuentra un
carácter no válido.
El método get_next_token() analiza el texto y devuelve el siguiente token
encontrado.
Función analyze_file:
Esta función toma una ruta de archivo como entrada, lee el contenido del
archivo y lo pasa al Lexer para analizarlo.
Captura excepciones como FileNotFoundError y Exception para manejar
posibles errores durante el análisis del archivo.
Función browse_file:
Esta función se llama cuando se hace clic en el botón "Browse".
Abre un cuadro de diálogo para que el usuario seleccione un archivo de código
fuente.
Llama a analyze_file para analizar el archivo seleccionado y mostrar los tokens
resultantes en la interfaz gráfica.
Muestra un mensaje de error si ocurre algún problema durante el análisis del
archivo.
Interfaz Gráfica (GUI):
Creamos una ventana principal de Tkinter llamada root.
Agregamos un marco (frame) para organizar los elementos de la interfaz.
Creamos un botón "Browse" que llama a la función browse_file cuando se hace
clic en él.
Creamos un widget de texto (token_list) para mostrar los tokens resultantes del
análisis del archivo.
Ejecutamos el bucle principal de Tkinter (root.mainloop()) para que la aplicación
se ejecute y responda a las interacciones del usuario.
La razón por la cual usamos Tkinter es para poder abrir cualquier archivo y sin
la dificultad de escribir la ruta o de tenerlo en una carpeta específica, así como
para poder mostrar los warnings desde una interfaz. Tenemos un problema con
la impresión de errores ya que muchas veces solo lo tomara como

identificadores y no lo marcará como error.
