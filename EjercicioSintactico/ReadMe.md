# Sistema de Gestión de Alumnos

Este es un simple sistema de gestión de alumnos implementado en C++. El sistema consta de clases para representar diferentes tipos de alumnos (Bachillerato y Licenciatura) y una clase Pila para almacenar instancias de estos alumnos.

## Clases

1. **Alumno**: Una clase abstracta que define una interfaz común para todos los tipos de alumnos. Contiene un método virtual puro `muestra()` que debe ser implementado por las clases derivadas.

2. **Bachillerato**: Una clase que representa a un alumno de bachillerato. Almacena el código del alumno y el nombre de la preparatoria a la que asiste.

3. **Licenciatura**: Una clase que representa a un alumno de licenciatura. Almacena el código del alumno, el nombre de la carrera y el número de créditos completados.

4. **Pila**: Una clase que implementa una estructura de datos de pila utilizando una lista enlazada. Permite agregar, eliminar y mostrar elementos de la pila.

## Métodos Principales

- **push(Alumno* x)**: Agrega un nuevo alumno a la pila.
- **pop()**: Elimina y devuelve el alumno en la cima de la pila.
- **top()**: Devuelve el alumno en la cima de la pila sin eliminarlo.
- **muestra()**: Muestra todos los alumnos almacenados en la pila.

## Uso

El código proporcionado incluye una función `ejemplo()` que demuestra cómo usar la clase Pila y las clases de alumno. Se instancia una pila, se agregan diferentes tipos de alumnos y se muestra el contenido de la pila.

```cpp
int main() {
    ejemplo();

    return 0;
}
