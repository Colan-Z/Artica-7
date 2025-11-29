from .mensaje_final import MensajeFinal

class FinalAlternativo(MensajeFinal):
    def __init__(self):
        super().__init__("FINAL ALTERNATIVO")

    def obtener_mensaje(self): #Mensaje que se muestra si se hace el final bueno.
        return (
            "David muere al intentar detener al tutor. Ambos reciben una descarga eléctrica que recorre sus cuerpos, dejándolos tirados, convulsionando, hasta que dejan de moverse.\n"
            "Todos comienzan a perder el control, gritando y corriendo por todo el lugar en busca de ayuda. Algunos estudiantes mueren al intentar tocar otras puertas.\n"
            "Chris está de rodillas, llorando y desesperado, y Sara permanece en un rincón, completamente asustada.\n"
            "Al final nadie fue a rescatarlos."
        )

