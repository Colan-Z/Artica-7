#Escena 2: Viaje en helicóptero a la Antártida

label escena2_helicoptero:
    scene fondo helicoptero
    play music "helicoptero.mp3" fadein 2.0 volume 0.2

    narrador "Un grupo de estudiantes había ganado un concurso académico."
    narrador "Su premio: un viaje científico a una base en la Antártida."
   
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
            $ moral -= 1
            chris "Esta bien..."
        "Tú tampoco sobrevivirás mucho sin ellos.":
            $ moral += 1        
            chris "¿Tú crees? (risas)"
        "Al menos estaremos juntos.":
            $ moral += 2       
            chris "Claro, héroe" 