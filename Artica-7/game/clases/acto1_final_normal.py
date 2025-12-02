from .mensaje_final import MensajeFinal

class Acto1FinalNormal(MensajeFinal):
    def __init__(self):
        super().__init__("FIN DEL ACTO 1")

    def obtener_mensaje(self): #Mensaje que se muestra si se hace el final bueno.
        return (
            "\nSara cuenta que vio una sombra misteriosa.\n"
            "Algunos estudiantes empiezan a preocuparse y una histeria colectiva se asoma.\n"
            "Chris está cada vez más irritable, mientras que Sara mantiene la esperanza de un rescate al haber conseguido una radio que puede intentar reparar.\n"
            "David intenta mantener el control y ánimo de los estudiantes en este rol de líder no buscado.\n\n"
            "Continuará..."
        )

