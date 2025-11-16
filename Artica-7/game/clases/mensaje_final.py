from abc import ABC, abstractmethod
from typing import Dict

class MensajeFinal(ABC):
    def __init__(self, titulo: str) -> None:
        self.__titulo = titulo
    
    @property
    def titulo(self) -> str:
        return self.__titulo
    
    @abstractmethod
    def obtener_mensaje(self) -> str:
        pass
    
    def mostrar_final(self) -> Dict[str, str]:
        return {
            'titulo': self.titulo,
            'mensaje': self.obtener_mensaje()
        }