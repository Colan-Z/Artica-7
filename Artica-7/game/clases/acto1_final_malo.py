from .mensaje_final import MensajeFinal

class Acto1FinalMalo(MensajeFinal):
    def __init__(self):
        super().__init__("FINAL MALO DEL ACTO 1")

    def obtener_mensaje(self): #Mensaje que se muestra si se hace el final bueno.
        return (
            "\nAmbos reciben una descarga eléctrica que recorre sus cuerpos, muriendo en el acto.\n"
            "Todos comienzan a perder el control, gritando y corriendo por todo el lugar en busca de ayuda.\n"
            "Chris está de rodillas, llorando inconsolablemente, y Sara permanece en un rincón, completamente traumada.\n"
            "Ninguno de los chicos fue rescatado. Nadie supo lo que pasó ahí dentro; simplemente desaparecieron."
        )