label escena1a2:
    # ESCENA 1 - EXT. HELICÓPTERO (CIELO ANTÁRTICO) - DÍA
    scene fondo helicoptero
    play music "helicoptero.mp3" fadein 2.0 volume 0.2
    scene fondo ventisca with fade
    play sound "ventisca.mp3" loop volume 0.5
    narrador "Un grupo de estudiantes había ganado un concurso académico."
    narrador "Su premio, un viaje científico a una base en la Antártida llamada Orcadas."
   
    # ESCENA 2 - INT. HELICÓPTERO - DÍA
    scene fondo interior_helicoptero with fade

    stop sound fadeout 1.0
    play sound "ventisca.mp3" loop volume 0.2
    show tutor at center
    tutor "En veinte minutos llegaremos."
    tutor "Allí pasaremos tres semanas estudiando ecosistemas polares, cambio climático y adaptación de especies."
    tutor "Debo pedirles que me entreguen sus celulares, me gustaría que se desconectaran del mundo digital y presten atención a su entorno."
    hide tutor
    show chris at left
    chris "Tres semanas. ¿Crees que sobrevivas sin videojuegos?"
    
    menu:
        "Responder de forma cortante.":
            # ESCENA 2-A INT. HELICÓPTERO - DÍA
            david "Sobreviviré."
            $ moral -= 1
            hide chris
            show chris_enojado at left
            chris "Está bien... supongo."
        "Bromear.":
            # ESCENA 2-B INT. HELICÓPTERO - DÍA
            david "Tú tampoco sobrevivirás mucho sin ellos."
            $ moral += 1        
            chris "¿Tú crees?"
        "Responder amistosamente.":
            # ESCENA 2-C INT. HELICÓPTERO - DÍA
            david "Al menos estaremos juntos."
            $ moral += 2       
            chris "Claro, héroe" 