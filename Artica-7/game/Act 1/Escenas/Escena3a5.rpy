label escena3a5:
    # ESCENA 3 - EXT. HELICOPTERO - VENTISCA - DÍA
    transform shake:
        zoom 1.1
        linear 0.05 xoffset 10
        linear 0.05 xoffset -10
        repeat 
    scene fondo ventisca with fade
    play sfx1 "ventisca.mp3" loop volume 0.5
    
    # narrador "De repente, el helicóptero se sacude violentamente. Los estudiantes gritan, sus voces llenas de pánico. Por la ventana, una ventisca blanca lo envuelve todo en segundos."
    
    stop sfx1 fadeout 1.0
    play sfx1 "ventisca.mp3" loop volume 0.2
    play sfx2 "alarma_helicoptero.mp3" volume 0.5

    scene fondo interior_helicoptero with fade
    show fondo interior_helicoptero at shake

    # Agregar dialogo del piloto reaccionando a la fuerte ventisca
    piloto "¡Tenemos problemas! ¡Hay una fuerte ventisca!."

    pause
    piloto "¡Haremos un aterrizaje de emergencia! ¡¡Sosténganse fuerte!! ¡¡¡Sosténganse fuerte!!!"
    
    narrador "Los estudiantes se aferran a sus asientos. Sara cierra los ojos con fuerza, apretando su mochila contra el pecho."
    show sara_agarra_mochila at right:
        linear 0.03 xoffset -10
        linear 0.06 xoffset 10
        repeat

    pause
    hide sara_agarra_mochila
    stop sfx2
    scene fondo_aterrizaje with fade
    stop sfx1 fadeout 1.0
    play sfx1 "ventisca.mp3" loop volume 0.5

    narrador "Tras unos segundos de caos, el helicóptero logra estabilizarse y aterriza suavemente."

    stop sfx1 fadeout 1.0
    play sfx1 "ventisca.mp3" loop volume 0.5

    # ESCENA 4 - EXT. ANTÁRTIDA - DÍA (VENTISCA)
    stop sfx1 fadeout 1.5
    play sfx1 "ventisca.mp3" loop volume 0.2
    scene fondo interior_helicoptero with fade
    show tutor 
    tutor "¿Están todos.... bien...?"
    tutor "¿Qué es eso? creo que veo algo..."
    tutor "Chicos, aquí no estaremos seguros, necesito que vayan detrás de mí"
    hide tutor
    stop sfx1 fadeout 1.0
    play sfx1 "ventisca.mp3" loop volume 0.4
    scene fondo_tutor_deja_mochila with fade
    narrador "Los estudiantes junto al tutor salen del helicóptero, dejando la mochila con los celulares en el asiento."
    scene fondo_cerca_mochila_celulares with fade
    pause
    stop music #detiene el sonido del helicoptero
    scene fondo camino with fade
    show tutor at left
    tutor "2...4...6...8...9 ¡Estamos todos! ¡Síganme!"
    hide tutor
    # show estudiante_femenino at right
    # estudiante_2 "¡Señor! ¡Creo que veo algo!"
    # hide estudiante_femenino
   

    scene fondo artica7_exterior with fade

    # Reemplazar siguiente narrador por dialogo tutor, 'Alla hay algo, parece una instalacion de algun tipo. Aproximadamente ua unos 50 metros. Vamos chicos!
    tutor "Allá hay algo, parece una instalación de algún tipo. Aproximadamente a unos 50 metros. ¡Vamos chicos!"
    # narrador "Una estructura antigua oculta en la ventisca, aproximadamente a cincuenta metros de distancia."
    scene black
    play sound "pasos en la nieve.mp3"
    # narrador "Los estudiantes y el tutor se dirigen hacia la instalación, luchando contra el viento."
    pause 3.0
    stop sound
    scene fondo artica7_exterior with fade
    show chris_gritando_sara_cayo
    chris "¡SARA SE CAYÓ!"
    hide chris_gritando_sara_cayo
    
    scene fondo sara_suelo with fade
   
    menu:                        
        "Ayudar a Sara":
            # ESCENA 4-A - EXT. ANTÁRTIDA - DÍA (VENTISCA)  
            $ moral += 1
            # scene pov david_ayuda_sara with fade
            scene david_ayuda_sara with fade
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
    
    # Reemplazar el siguiente narrador por dialogo del tutor 'Llegamos... la puerta esta entreabierta. Esta un poco dura pero creo que puedo abrirla'. Sonido de puerta abriendose. '¡Entremos todos!'
    tutor "Llegamos... la puerta está entreabierta. Está un poco dura pero creo que puedo abrirla"
    play sound "puerta_abre.mp3"
    pause
    # narrador "Llegan a la entrada principal. Es una instalación militar con el nombre 'ÁRTICA-7' grabado en letras desgastadas."
    # narrador "El tutor ve la puerta entreabierta y logra abrirla."
    
    show tutor at left
    tutor "¡Adentro! ¡Rápido! Estaremos seguros hasta que pase la ventisca."
    hide tutor
    narrador "Los estudiantes entran apresuradamente en grupo. El tutor entra último, mirando atrás hacia el helicóptero, que apenas se ve entre la nieve."

    stop sound fadeout 2.0