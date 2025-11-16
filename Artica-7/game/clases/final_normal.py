from .mensaje_final import MensajeFinal

class FinalNormal(MensajeFinal):
    def __init__(self) -> None:
        super().__init__(
            "FINAL NORMAL",
            "Sobrevivieron pero a un costo muy alto"
        )

    def obtener_mensaje(self) -> str:
        return (
            "El rescate llegó pero no todos ilesos\n"
            "David sobrevivió de milagro Chris fue detenido\n"
            "Las cicatrices psicológicas permanecerán para siempre"
        )