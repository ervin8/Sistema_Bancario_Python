from abc import ABC, abstractmethod

# Interfaz abstracta para cumplir con la arquitectura de alto nivel
class Cuenta(ABC):
    @abstractmethod
    def obtener_detalles(self):
        """Define el comportamiento que todas las cuentas deben tener"""
        pass

# Producto Concreto 1
class CuentaAhorros(Cuenta):
    def obtener_detalles(self):
        return "Beneficios: Interés del 2% anual, ideal para ahorros a largo plazo."

# Producto Concreto 2
class CuentaCorriente(Cuenta):
    def obtener_detalles(self):
        return "Beneficios: Sobregiro disponible y chequera personalizada."