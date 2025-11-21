from abc import ABC, abstractmethod

class MensajeFinal(ABC):
    def __init__(self, titulo: str):
        self._titulo = titulo

    @property
    def titulo(self):
        return self._titulo

    @abstractmethod
    def obtener_mensaje(self):
        pass

    def mostrar_final(self):
        return f"{self.titulo}\n{self.obtener_mensaje()}"
    