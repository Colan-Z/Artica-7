label escena3a5:
    # ESCENA 3
    scene fondo ventisca with fade
    play sfx1 "ventisca.mp3" loop volume 0.5
    pause
    
    # ESCENA 4
    stop sfx1 fadeout 1.0
    play sfx1 "ventisca.mp3" loop volume 0.2
    play sfx2 "alarma_helicoptero.mp3" volume 0.5

    scene fondo interior_helicoptero at shake_fuerte, with fade

    piloto "¡Ventisca pesada, perdemos estabilidad!"
    piloto "¡Prepararse para aterrizaje de emergencia! ¡Aseguren posiciones!"
    play sound "chicos gritando.mp3"  volume 0.5 loop
    show sara_agarra_mochila at shake_fuerte, right
    pause
    stop sfx2
    stop sound
    stop music
    # ESCENA 5
    play sfx2 "aterrizaje forzoso.mp3" noloop
    scene fondo interior_helicoptero_aterrizaje with fade
    hide sara_agarra_mochila
    pause
    stop sfx2

    stop sfx1 fadeout 1.0
    play sfx1 "ventisca.mp3" loop volume 0.5

    # ESCENA 6
    stop sfx1 fadeout 1.5
    play sfx1 "ventisca.mp3" loop volume 0.2
    play sfx2 "helicoptero_aterriza.mp3" noloop
    scene fondo aterrizaje with fade
    pause 1.0
    scene fondo interior_helicoptero_aterrizado_sin_tutor
    show tutor
    tutor "¡Chicos! ¡Reaccionen! ¿Están todos enteros? ¿Alguien se golpeó fuerte?"
    menu:
        "Responder al tutor.":
            #Opcion A
            david "Sí, estoy bien. ¿Y ustedes?"
            # show sara at right
            # show chris at left
            # show estudiante_femenino_2:
            #     xpos -300
            #     ypos -400
            # show estudiante_masculino_2:
            #     xpos 1200
            #     ypos -400           
            "Estudiantes" "Estamos bien."
            # hide sara
            # hide chris
            # hide estudiante_femenino_2
            # hide estudiante_masculino_2
            show tutor 

            tutor "Menos mal..."
            tutor "Mantengan la calma. Estamos vivos, eso es lo principal."
            tutor "Nadie se desabrocha el cinturón hasta que yo revise la salida."
        "Mirar por la ventana.":
            #Opcion B
            pass

    scene fondo helicoptero_vista_artica 
    david "¿Qué es eso?" 
    david "Señor, creo que veo algo afuera."
    scene fondo interior_helicoptero_aterrizado_sin_tutor
    show tutor
    with fade
    tutor "Tienes razón... Buen ojo, David. Aquí dentro nos vamos a congelar."
    tutor "¡Muy bien, cambio de planes! ¡Todos afuera, ahora! ¡No se separen y síganme los pasos! ¡Vamos, muévanse!"
    stop sfx1 fadeout 1.0
    play sfx1 "ventisca.mp3" loop volume 0.4
    scene fondo_tutor_deja_mochila with fade
    hide tutor
    pause
    scene fondo_cerca_mochila_celulares with fade
    # escena 7
    menu:
        "Tomar el {sc=4}{color=#9c416e}celular{/color}{/sc}.":
            david "Voy a llevarlo, tal vez sirva de algo."
            $ tiene_celular = True
        "Dejar el {sc=4}{color=#9c416e}celular{/color}{/sc}.":
            david "Espero no arrepentirme..."
            $ tiene_celular = False
    stop music # detiene el sonido del helicoptero
    # escena 8
    scene fondo camino
    show tutor at left
    with fade
    tutor "¡Dos... cuatro... seis... ocho... nueve! ¡Están todos! ¡Manténganse juntos, no quiero a nadie solo!"
    hide tutor
    window hide
    show fondo camino at yshake
    play sound "pasos en la nieve.mp3"
    pause 3.0
    stop sound
    scene fondo artica7_exterior 
    show tutor at right
    with fade
    tutor "¡Ahí está! ¡Bien visto, David! ¡Es un refugio! ¡Vamos hacia la estructura! ¡Muévanse, muévanse!"
    scene fondo artica7_exterior at yshake, with fade 
    play sound "pasos en la nieve.mp3"
    pause 3.0
    stop sound
    scene fondo artica7_exterior
    show chris_gritando_sara_cayo at parpadear("chris_gritando_sara_cayo"), center
    play sound "chris_hey.ogg"
    chris "¡SARA SE CAYÓ!"
    stop sound
    hide chris_gritando_sara_cayo
    
    scene fondo sara_suelo with fade
   
    
    menu:                        
        "Ayudar a Sara":
            #Opción A:
            show borde_verde at borde_top_simple
            $ moral += 1
            scene david_ayuda_sara with fade
            david "¿Estás bien?"
            sara "Sí, lo estoy, gracias..."
        "Ordenar a Chris que la ayude.":
            #Opción B:
            show borde_rojo at borde_top_simple
            $ moral -= 1 
            scene fondo chris_rescata_sara with fade       
            chris "..."
            sara "Gracias..."
            
    #escena 9
    scene fondo artica7_entrada 
    show tutor at center
    with fade
    tutor "¡Llegamos! ¡La puerta está entreabierta!"
    hide tutor
    scene fondo artica7_entrada_tutor_abriendo
    tutor "¡Mierda... el óxido la trabó!"
    play sound "puerta_abre.mp3"
    pause 2.0
    scene fondo artica7_entrada_abierta
    show tutor at center
    tutor "¡Ahí está!"
    show tutor at left
    tutor "¡Adentro! ¡Rápido! ¡No se detengan en la entrada! ¡Pasen todos, vamos a estar seguros aquí! ¡Vamos, entren!"
    hide tutor
   
    stop sound fadeout 2.0