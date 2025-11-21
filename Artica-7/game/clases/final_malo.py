from .mensaje_final import MensajeFinal

class FinalMalo(MensajeFinal):
    def __init__(self) -> None:
        super().__init__("FINAL MALO")

    def obtener_mensaje(self) -> str: #Mensaje que se muestra si se hace el final malo.
        return (
            "La locura y el frío consumieron a todos.\n"
            "Chris asesinó a David sellando su destino.\n"
            "Nadie supo qué ocurrió en Ártica-7."
        )