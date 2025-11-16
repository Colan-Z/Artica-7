from .mensaje_final import MensajeFinal

class FinalBueno(MensajeFinal):
    def __init__(self) -> None:
        super().__init__(
            "FINAL BUENO",
            "David reconcilió a Chris y todos fueron rescatados"
        )

    def obtener_mensaje(self) -> str:
        return (
            "A pesar del horror la amistad prevaleció\n"
            "Chris David y Sara salieron con vida\n"
            "Su vínculo se fortaleció tras la pesadilla"
        )