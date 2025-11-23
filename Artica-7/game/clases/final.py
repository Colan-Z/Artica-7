from .mensaje_final import MensajeFinal

class Final(MensajeFinal):
    def __init__(self):
        super().__init__("FINAL ALTERNATIVO")

    def obtener_mensaje(self): #Mensaje que se muestra si se hace el final normal.
        return (
            ""
        )