label escena1a2:
    # ESCENA 1
    scene fondo helicoptero with fade
    play music "helicoptero.mp3" loop volume 0.2 #SFX Rotor del helicoptero. Utilizamos music para evitar que se quite el sonido mientras suena la ventisca.
    pause 3
    # ESCENA 2
    $ renpy.music.set_volume(0.45, delay=0.5, channel="music")
    scene fondo interior_helicoptero at shake_leve, with fade
    play sound "estudiantes hablando.mp3" volume 0.3 loop
    pause
    scene fondo interior_helicoptero_sin_tutor at shake_leve
    show tutor at shake_leve, center, with fade
    tutor "¡Chicos, presten atención!"
    
    stop sound fadeout 1.0
    tutor "Miren dónde están. No cualquiera llega a la Antártida. Ustedes están acá porque se lo ganaron, porque demostraron ser los mejores en el concurso académico."
    tutor "¡Son la élite!"
    tutor "En veinte minutos tocamos suelo en Orcadas."
    tutor "Esto no es un paseo turístico, es una misión científica real. Ecosistemas polares, cambio climático, adaptación de especies... Van a ver con sus propios ojos lo que solo conocen de los libros."
    tutor "Ahora, necesito que presten atención. Los celulares a la bolsa. Allá afuera no hay tiempo para distraerse."
    tutor "Quiero sus ojos en el horizonte, no en una pantalla."
    hide tutor
    scene fondo interior_helicoptero at shake_leve
    show expression Image("chris_sonrisa.png") at parpadear_shake("chris_sonrisa"), shake_leve, center, with fade

    chris "Tres semanas. ¿Crees que sobrevivirás sin videojuegos?"
    
    menu:
        "Responder de forma cortante.":
            # ESCENA 2-A INT. HELICÓPTERO - DÍA
            show borde_rojo at borde_top_simple
            $ moral -= 1
            david "Sobreviviré."
            hide chris_sonrisa
            scene fondo interior_helicoptero at shake_leve
            show expression Image("chris.png") at parpadear_shake("chris"), shake_leve, center
            chris "Está bien... supongo."
        "Bromear.":
            # ESCENA 2-B INT. HELICÓPTERO - DÍA
            show borde_verde at borde_top_simple
            $ moral += 1
            david "Tú tampoco sobrevivirás mucho sin ellos."
            # show expression Image("chris_sonrisa.png") at shake_leve, center
            chris "¿Tú crees?"
        "Responder amistosamente.":
            # ESCENA 2-C INT. HELICÓPTERO - DÍA
            show borde_verde at borde_top_simple
            $ moral += 2   
            # show expression Image("chris_sonrisa.png") at shake_leve, center
            david "Al menos estaremos juntos."
            chris "Claro, héroe." 
            