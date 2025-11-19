label escena3a5:
    # ESCENA 3 - EXT. HELICOPTERO - VENTISCA - DÍA
    transform shake:
        zoom 1.1
        linear 0.05 xoffset 10
        linear 0.05 xoffset -10
        repeat 
    scene fondo ventisca with fade
    play sound "ventisca.mp3" loop volume 0.5
    narrador "De repente, el helicóptero se sacude violentamente. Los estudiantes gritan, sus voces llenas de pánico. Por la ventana, una ventisca blanca lo envuelve todo en segundos."

    scene fondo interior_helicoptero with fade
    show fondo interior_helicoptero at shake

    stop sound fadeout 1.0
    play sound "ventisca.mp3" loop volume 0.2

    "Piloto" "¡Haremos un aterrizaje de emergencia! ¡¡Sosténganse fuerte!! ¡¡¡Sosténganse fuerte!!!"
    
    narrador "Los estudiantes se aferran a sus asientos. Sara cierra los ojos con fuerza, apretando su mochila contra el pecho."
    scene fondo_aterrizaje with fade
    stop sound fadeout 1.0
    play sound "ventisca.mp3" loop volume 0.5

    narrador "Tras unos segundos de caos, el helicóptero logra estabilizarse y aterriza suavemente."

    stop sound fadeout 1.0
    play sound "ventisca.mp3" loop volume 0.6

    # ESCENA 4 - EXT. ANTÁRTIDA - DÍA (VENTISCA)
    stop sound fadeout 1.5
    play sound "ventisca.mp3" loop volume 0.2
    scene fondo interior_helicoptero with fade
    show tutor 
    tutor "¿Están todos.... bien...?"
    tutor "¿Qué es eso? creo que veo algo..."
    tutor "Chicos, aquí no estaremos seguros, necesito que vayan detrás de mí"
    hide tutor
    narrador "Los estudiantes junto al tutor salen del helicóptero, dejando la mochila con los celulares en el asiento."

    stop sound fadeout 1.0
    play sound "ventisca.mp3" loop volume 0.5
    
    stop music #detiene el sonido del helicoptero
    scene fondo camino with fade
    show tutor at left
    tutor "2...4...6...8...9 ¡Estamos todos! ¡Síganme!"
    hide tutor
    show estudiante_femenino at right
    estudiante_2 "¡Señor! ¡Creo que veo algo!"
    hide estudiante_femenino
    tutor "(Bien... parece una base abandonada, espero que podamos refugiarnos dentro.)"

    scene fondo artica7_exterior with fade

    narrador "Una estructura metálica medio enterrada en la nieve, aproximadamente a cincuenta metros de distancia."
    narrador "Los estudiantes y el tutor se dirigen hacia la instalación, luchando contra el viento, Sara tropieza con una piedra oculta bajo la nieve."
    show chris
    chris "¡SARA SE CAYÓ!"
    hide chris
    
    scene fondo sara_suelo with fade
   
    menu:                        
        "Ayudar a Sara":
            # ESCENA 4-A - EXT. ANTÁRTIDA - DÍA (VENTISCA)  
            $ moral += 1
            scene pov david_ayuda_sara with fade
            david "¿Estás bien?"
            sara "Si, lo estoy, gracias..."
        "Ordenar a Chris que la ayude.":
            # ESCENA 4-B - EXT. ANTÁRTIDA - DÍA (VENTISCA)
            $ moral -= 1 
            scene fondo chris_rescata_sara with fade       
            chris "..."
            sara "Gracias..."
            
    # ESCENA 5 - EXT. ÁRTICA-7 - ENTRADA - DÍA
    scene fondo artica7_entrada with fade
    
    narrador "Llegan a la entrada principal. Es una instalación militar con el nombre 'ÁRTICA-7' grabado en letras desgastadas."
    
    narrador "El tutor ve la puerta entreabierta y logra abrirla."
    
    show tutor at left
    tutor "¡Adentro! ¡Rápido! Estaremos seguros hasta que pase la ventisca."
    hide tutor
    narrador "Los estudiantes entran apresuradamente en grupo. El tutor entra último, mirando atrás hacia el helicóptero, que apenas se ve entre la nieve."

    stop sound fadeout 2.0