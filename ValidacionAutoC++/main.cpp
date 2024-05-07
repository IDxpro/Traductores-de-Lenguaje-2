// Clase Nodo
class Nodo {
public:
    char tipoDato;
    static TablaSimbolos *tablaSimbolos;
    static string ambito;

    virtual void validaTipos() {
        tipoDato= 'v';
        if (sig != NULL) sig->validaTipos();
    }
};

// Clase Semantico
class Semantico {
private:
    TablaSimbolos *tablaSimbolos;

public:
    Semantico() {
        Nodo::tablaSimbolos= tablaSimbolos= new TablaSimbolos(&listaErrores);
    }

    void analiza(Nodo *arbol) {
        this->arbol= arbol;
        arbol->validaTipos();
        tablaSimbolos->muestra();
        muestraErrores();
    }
};

// Clase Tipo
class Tipo {
public:
    char dimeTipo() {
        if (simbolo.compare("int") == 0) return 'i';
        if (simbolo.compare("float") == 0) return 'f';
        if (simbolo.compare("string") == 0) return 's';
        if (simbolo.compare("void") == 0) return 'v';
    }
};

// Archivo principal.cpp
TablaSimbolos * Nodo::tablaSimbolos= NULL;
string Nodo::ambito= "";

int main() {
    Semantico semantico;
    semantico.analiza(arbol);
    return 0;
}
