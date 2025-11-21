from .mensaje_final import MensajeFinal

class FinalBueno(MensajeFinal):
    def __init__(self):
        super().__init__("FINAL BUENO")

    def obtener_mensaje(self): #Mensaje que se muestra si se hace el final bueno.
        return (
            "A pesar del horror la amistad prevaleció.\n"
            "Chris, David y Sara salieron con vida.\n"
            "Su vínculo se fortaleció tras la pesadilla"
        )

