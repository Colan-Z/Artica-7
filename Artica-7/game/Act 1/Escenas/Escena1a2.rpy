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
    tutor "¡Presten atención!"
    stop sound fadeout 1.0
    tutor "Miren dónde están. No cualquiera llega a la Antártida. Ustedes no están acá por suerte, están acá porque ganaron el concurso académico."
    tutor "¡Son la élite!"
    tutor "En veinte minutos tocamos suelo en Orcadas."
    tutor "Esto no es un paseo turístico, es una misión científica. Ecosistemas polares, cambio climático y adaptación de especies... Vamos a ver la realidad a la cara."
    tutor "Ahora, necesito enfoque total. Los celulares a la bolsa. ¡Ya! Allá afuera no hay señal ni tiempo para distraerse."
    tutor "Quiero sus ojos en el horizonte, no en una pantalla."
    hide tutor
    scene fondo interior_helicoptero at shake_leve
    #show chris_sonrisa
    show expression Image("chris_sonrisa.png") at parpadear_shake("chris_sonrisa"), shake_leve, center, with fade

    chris "Tres semanas. ¿Crees que sobrevivirás sin videojuegos?"
    
    menu:
        "Responder de forma cortante.":
            # ESCENA 2-A INT. HELICÓPTERO - DÍA
            david "Sobreviviré."
            $ moral -= 1
            hide chris_sonrisa
            show expression Image("chris_sonrisa.png") at parpadear_shake("chris_sonrisa"), shake_leve, center
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
            chris "Claro, héroe." 