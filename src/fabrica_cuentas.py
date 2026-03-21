from .modelos import CuentaAhorros, CuentaCorriente

class FabricaFinanciera:
    @staticmethod
    def crear_cuenta(tipo_cuenta):
        """Lógica para instanciar el objeto correcto según la necesidad"""
        if tipo_cuenta.lower() == "ahorros":
            return CuentaAhorros()
        elif tipo_cuenta.lower() == "corriente":
            return CuentaCorriente()
        else:
            raise ValueError(f"El tipo de cuenta '{tipo_cuenta}' no existe.")