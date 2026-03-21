class BancoCentral:
    _instancia = None

    # El método __new__ controla la creación del objeto
    def __new__(cls):
        if cls._instancia is None:
            # Si no existe, crea la única instancia
            cls._instancia = super(BancoCentral, cls).__new__(cls)
            cls._instancia.historial_transacciones = []
            print(">>> [LOG] Conexión única al núcleo bancario establecida.")
        return cls._instancia

    def registrar_evento(self, evento):
        """Registra cada acción en la instancia única"""
        self.historial_transacciones.append(evento)
        print(f"Bancore: {evento}")