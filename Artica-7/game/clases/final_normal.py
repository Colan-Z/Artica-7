from .mensaje_final import MensajeFinal

class FinalNormal(MensajeFinal):
    def __init__(self) -> None:
        super().__init__("FINAL NORMAL")

    def obtener_mensaje(self) -> str: #Mensaje que se muestra si se hace el final normal.
        return (
            "El rescate llegó.\n"
            "Todos los estudiantes sobrevivieron.\n"
            "Las cicatrices psicológicas permanecerán para siempre."
        )