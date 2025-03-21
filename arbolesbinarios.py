using
System;


class Nodo
    {
        public
    int
    Valor;
    public
    Nodo
    Izquierdo, Derecho;

    public
    Nodo(int
    valor)
    {
        Valor = valor;
    Izquierdo = Derecho = null;
    }
    }

    class ArbolBinario
        {
            private
        Nodo
        raiz;

        public
        void
        Insertar(int
        valor)
        {
            raiz = InsertarRec(raiz, valor);
        }

        private
        Nodo
        InsertarRec(Nodo
        nodo, int
        valor)
        {
        if (nodo == null)

    return new
    Nodo(valor);

    if (valor < nodo.Valor)
        nodo.Izquierdo = InsertarRec(nodo.Izquierdo, valor);
    else if (valor > nodo.Valor)
    nodo.Derecho = InsertarRec(nodo.Derecho, valor);

    return nodo;
    }

    public
    void
    InOrden()
    {
    InOrdenRec(raiz);
    Console.WriteLine();
    }

    private
    void
    InOrdenRec(Nodo
    nodo)
    {
    if (nodo != null)
        {
            InOrdenRec(nodo.Izquierdo);
        Console.Write(nodo.Valor + " ");
        InOrdenRec(nodo.Derecho);
        }
        }

        public
        bool
        Buscar(int
        valor)
        {
        return BuscarRec(raiz, valor);
        }

        private
        bool
        BuscarRec(Nodo
        nodo, int
        valor)
        {
        if (nodo == null)
            return false;
        if (nodo.Valor == valor)
            return true;

        return valor < nodo.Valor ? BuscarRec(nodo.Izquierdo, valor): BuscarRec(nodo.Derecho, valor);
        }
        }

        class Program
            {
                static
            void
            Main()
            {
                ArbolBinario
            arbol = new
            ArbolBinario();
            int
            opcion;

            do
            {
                Console.WriteLine("\nMenú de Operaciones:");
            Console.WriteLine("1. Insertar elemento");
            Console.WriteLine("2. Mostrar InOrden");
            Console.WriteLine("3. Buscar elemento");
            Console.WriteLine("4. Salir");
            Console.Write("Seleccione una opción: ");
            opcion = int.Parse(Console.ReadLine());

            switch(opcion)
            {
                case
            1: \
                Console.Write("Ingrese un número: ");
            int
            num = int.Parse(Console.ReadLine());
            arbol.Insertar(num);

        break;
        case
        2:
        Console.WriteLine("Recorrido InOrden: ");
        arbol.InOrden();
        break;
        case
        3:
        Console.Write("Número a buscar: ");
        int
        buscar = int.Parse(Console.ReadLine());
        Console.WriteLine(arbol.Buscar(buscar) ? "Elemento encontrado": "Elemento no encontrado");
        break;
        case
        4:
        Console.WriteLine("Saliendo...");
        break;
        default:
        Console.WriteLine("Opción no válida");
        break;
        }
        } while (opcion != 4);
        }
        }
