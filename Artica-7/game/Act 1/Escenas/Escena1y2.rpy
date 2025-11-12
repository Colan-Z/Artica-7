label escena1y2:
    # ESCENA 1 - EXT. HELICÓPTERO (CIELO ANTÁRTICO) - DÍA
    scene fondo helicoptero
    play music "helicoptero.mp3" fadein 2.0 volume 0.2

    narrador "Un grupo de estudiantes había ganado un concurso académico."
    narrador "Su premio: un viaje científico a una base en la Antártida."
   
    # ESCENA 2 - INT. HELICÓPTERO - DÍA
    scene fondo interior_helicoptero with fade
   
    show tutor at center
    tutor "En veinte minutos llegaremos a Base Orcadas. "
    tutor "Allí pasaremos tres semanas estudiando ecosistemas polares, cambio climático y adaptación de especies."
    tutor "Debo pedirles que me entreguen sus celulares, me gustaría que se desconectaran del mundo digital y presten atención a su entorno."
    hide tutor
    show chris at left
    show david at right
    chris "Tres semanas. ¿Crees que sobrevivas sin videojuegos?"
    
    menu:
        "Sobreviviré.":
            # ESCENA 2-A INT. HELICÓPTERO - DÍA
            $ moral -= 1
            chris "Esta bien..."
        "Tú tampoco sobrevivirás mucho sin ellos.":
            # ESCENA 2-B INT. HELICÓPTERO - DÍA
            $ moral += 1        
            chris "¿Tú crees? (risas)"
        "Al menos estaremos juntos.":
            # ESCENA 2-C INT. HELICÓPTERO - DÍA
            $ moral += 2       
            chris "Claro, héroe" 