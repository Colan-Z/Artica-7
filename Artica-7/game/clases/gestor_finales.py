from typing import Dict, Optional
from .mensaje_final import MensajeFinal
from .final_bueno import FinalBueno
from .final_normal import FinalNormal
from .final_malo import FinalMalo

class GestorFinales:
    
    def __init__(self) -> None:
        self.__finales: Dict[str, MensajeFinal] = {
            'bueno': FinalBueno(),
            'normal': FinalNormal(),
            'malo': FinalMalo()
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