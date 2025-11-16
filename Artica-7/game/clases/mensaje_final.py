from abc import ABC, abstractmethod
from typing import Dict

class MensajeFinal(ABC):
    def __init__(self, titulo: str, descripcion: str) -> None:
        self.__titulo = titulo
        self.__descripcion = descripcion
    
    @property
    def titulo(self) -> str:
        return self.__titulo
    
    @property
    def descripcion(self) -> str:
        return self.__descripcion
    
    @abstractmethod
    def obtener_mensaje(self) -> str:
        pass
    
    def mostrar_final(self) -> Dict[str, str]:
        return {
            'titulo': self.titulo,
            'descripcion': self.descripcion,
            'mensaje': self.obtener_mensaje()
        }