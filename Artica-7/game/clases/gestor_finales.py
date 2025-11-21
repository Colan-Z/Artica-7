from .final_bueno import FinalBueno
from .final_normal import FinalNormal
from .final_malo import FinalMalo
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

        return self._final_actual

    def obtener_resultado(self):
        
        return self._final_actual.mostrar_final()

