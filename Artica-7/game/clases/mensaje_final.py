from abc import ABC, abstractmethod

class MensajeFinal(ABC):
    def __init__(self, titulo: str) -> None:
        self._titulo = titulo

    @property
    def titulo(self) -> str:
        return self._titulo

    @abstractmethod
    def obtener_mensaje(self) -> str:
        pass

    def mostrar_final(self) -> str:
        return f"{self.titulo}\n{self.obtener_mensaje()}"