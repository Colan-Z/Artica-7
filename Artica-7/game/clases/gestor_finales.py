from .final_bueno import FinalBueno
from .final_normal import FinalNormal
from .final_malo import FinalMalo
from .acto1_final_bueno import Acto1FinalBueno
from .final_alternativo import FinalAlternativo
from .final import Final
from .mensaje_final import MensajeFinal

class GestorFinales:

    def __init__(self):
        self._final_actual: MensajeFinal

    def activar_final(self, tipo: str):
        if tipo == "bueno":
            self._final_actual = FinalBueno()
        elif tipo == "normal":
            self._final_actual = FinalNormal()
        elif tipo == "malo":
            self._final_actual = FinalMalo()
        elif tipo == "final":
            self._final_actual = Final()
        elif tipo == "acto1_bueno":
            self._final_actual = Acto1FinalBueno()
        elif tipo == "final_alternativo":
            self._final_actual = FinalAlternativo()

        return self._final_actual

    def obtener_resultado(self):
        
        return self._final_actual.mostrar_final()

