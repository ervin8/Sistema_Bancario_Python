from src.banco_singleton import BancoCentral
from src.fabrica_cuentas import FabricaFinanciera

def ejecutar_sistema():
    # 1. Accedemos al Singleton
    core_bancario = BancoCentral()
    core_bancario.registrar_evento("Sistema Iniciado correctamente.")

    # 2. Usamos la Factory para crear productos sin conocer sus clases internas
    try:
        # Ejemplo: El usuario pide una cuenta de ahorros
        mi_cuenta = FabricaFinanciera.crear_cuenta("ahorros")
        
        print("\n--- DATOS DE TU CUENTA ---")
        print(mi_cuenta.obtener_detalles())
        
        core_bancario.registrar_evento("Nueva Cuenta de Ahorros generada.")
        
    except Exception as e:
        core_bancario.registrar_evento(f"Error: {e}")

if __name__ == "__main__":
    ejecutar_sistema()