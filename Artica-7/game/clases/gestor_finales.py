from typing import Dict, Optional
from .mensaje_final import MensajeFinal


class GestorFinales:
    
    def __init__(self) -> None:
        self.__finales: Dict[str, MensajeFinal] = {
            
        }
        self.__final_actual: Optional[MensajeFinal] = None
    
    def activar_final(self, tipo: str) -> Optional[MensajeFinal]:
        if tipo in self.__finales:
            self.__final_actual = self.__finales[tipo]
            return self.__final_actual
        return None
    
    def obtener_resultado(self) -> Optional[Dict[str, str]]:
        if self.__final_actual:
            return self.__final_actual.mostrar_final()
        return None