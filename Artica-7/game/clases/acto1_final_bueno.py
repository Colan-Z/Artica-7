from .mensaje_final import MensajeFinal

class Acto1FinalBueno(MensajeFinal):
    def __init__(self):
        super().__init__("FINAL BUENO")

    def obtener_mensaje(self): #Mensaje que se muestra si se hace el final bueno.
        return (
            "David tomó el celular antes de entrar a la base y pudo usarlo para llamar a emergencias.\n"
            "Todos fueron rescatados."
        )

