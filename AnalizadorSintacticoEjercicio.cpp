#include <iostream>
#include <list>
#include <string>

class Alumno {
public:
    virtual void muestra() = 0;
};

class Bachillerato : public Alumno {
protected:
    std::string codigo;
    std::string preparatoria;

public:
    Bachillerato(const std::string& codigo, const std::string& preparatoria) : codigo(codigo), preparatoria(preparatoria) {}

    void muestra() override {
        std::cout << "Alumno Bachillerato" << std::endl;
        std::cout << "Codigo: " << codigo << std::endl;
        std::cout << "Preparatoria: " << preparatoria << std::endl << std::endl;
    }
};

class Licenciatura : public Alumno {
protected:
    std::string codigo;
    std::string carrera;
    int creditos;

public:
    Licenciatura(const std::string& codigo, const std::string& carrera, int creditos) : codigo(codigo), carrera(carrera), creditos(creditos) {}

    void muestra() override {
        std::cout << "Alumno Licenciatura" << std::endl;
        std::cout << "Codigo: " << codigo << std::endl;
        std::cout << "Carrera: " << carrera << std::endl;
        std::cout << "Creditos: " << creditos << std::endl << std::endl;
    }
};

class Pila {
private:
    std::list<Alumno*> lista;

public:
    void push(Alumno* x) {
        lista.push_front(x);
    }

    Alumno* pop() {
        Alumno* x = *lista.begin();
        lista.erase(lista.begin());
        return x;
    }

    Alumno* top() {
        return *lista.begin();
    }

    void muestra() {
        std::list<Alumno*>::reverse_iterator it;
        std::cout << "Pila: ";

        for (it = lista.rbegin(); it != lista.rend(); it++) {
            Alumno* x = *it;
            x->muestra();
        }
        std::cout << std::endl;
    }
};

void ejemplo() {
    Pila pila;
    Alumno* alumno;
    alumno = new Licenciatura("345678", "Computacion", 200);
    pila.push(alumno);
    pila.push(new Bachillerato("456789", "Preparatoria 12"));
    pila.push(new Licenciatura("456789", "Informatica", 50));
    pila.muestra();
    std::cout << "*********************************" << std::endl;
    pila.pop();
    pila.muestra();
}

int main() {
    ejemplo();

    return 0;
}
