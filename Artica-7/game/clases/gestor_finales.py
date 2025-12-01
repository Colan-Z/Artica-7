from .final_bueno import FinalBueno
from .final_normal import FinalNormal
from .final_malo import FinalMalo
from .acto1_final_bueno import Acto1FinalBueno
from .acto1_final_malo import Acto1FinalMalo
from .acto1_final_normal import Acto1FinalNormal
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
        elif tipo == "acto1_final_bueno":
            self._final_actual = Acto1FinalBueno()
        elif tipo == "acto1_final_malo":
            self._final_actual = Acto1FinalMalo()
        elif tipo == "acto1_final_normal":
            self._final_actual = Acto1FinalNormal()

        return self._final_actual

    def obtener_resultado(self):
        
        return self._final_actual.mostrar_final()

