from .mensaje_final import MensajeFinal

class Acto1FinalBueno(MensajeFinal):
    def __init__(self):
        super().__init__("FINAL BUENO DEL ACTO 1")

    def obtener_mensaje(self): #Mensaje que se muestra si se hace el final bueno.
        return (
            "\nEl equipo de rescate logra encontrar la base.\n"
            "Todos los estudiantes fueron rescatados."
        )

