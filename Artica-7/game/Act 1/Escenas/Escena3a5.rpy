label escena3a5:
    # ESCENA 3 - EXT. HELICOPTERO - VENTISCA - DÍA
    transform shake:
        zoom 1.1
        linear 0.05 xoffset 10
        linear 0.05 xoffset -10
        repeat 
    
    scene fondo ventisca with fade
    play sfx1 "ventisca.mp3" loop volume 0.5
    pause
     
    stop sfx1 fadeout 1.0
    play sfx1 "ventisca.mp3" loop volume 0.2
    play sfx2 "alarma_helicoptero.mp3" volume 0.5

    scene fondo interior_helicoptero with fade
    show fondo interior_helicoptero at shake

    piloto "¡Tenemos problemas! ¡Hay una fuerte ventisca!."
    piloto "¡Haremos un aterrizaje de emergencia! ¡¡Sosténganse fuerte!! ¡¡¡Sosténganse fuerte!!!"
    
    show sara_agarra_mochila at right:
        linear 0.03 xoffset -10
        linear 0.06 xoffset 10
        repeat
    
    pause
    hide sara_agarra_mochila
    stop sfx2
    pause 0.01
    stop music
    play sfx2 "helicoptero_aterriza.mp3" noloop
    scene fondo aterrizaje with fade
    pause
    stop sfx2

    stop sfx1 fadeout 1.0
    play sfx1 "ventisca.mp3" loop volume 0.5

    # ESCENA 4 - EXT. ANTÁRTIDA - DÍA (VENTISCA)
    stop sfx1 fadeout 1.5
    play sfx1 "ventisca.mp3" loop volume 0.2
    scene fondo interior_helicoptero with fade
    show tutor 
    tutor "¿Están todos... bien...?"
    menu:
        "Responder al tutor.":
            #Opcion A
            david "Si, estamos bien. ¿Y ustedes?"
            tutor "Estamos bien, gracias por preguntar."
        "Mirar por la ventana.":
            #Opcion B
            scene fondo helicoptero_vista_artica   
            david "¿Qué es eso?" 
            david "Señor, Creo que veo algo afuera... Parece una estructura."

    scene fondo interior_helicoptero with fade
    show tutor
    tutor "Es cierto... chicos, aquí no estaremos seguros, necesito que vayan detrás de mí."
    hide tutor
    stop sfx1 fadeout 1.0
    play sfx1 "ventisca.mp3" loop volume 0.4
    scene fondo_tutor_deja_mochila with fade
    pause
    scene fondo_cerca_mochila_celulares with fade
    # escena 7
    menu:
        "Tomar el celular.":
            david "Voy a llevarlo, tal vez nos sirva de algo."
            $ tiene_celular = True
        "Dejar el celular.":
            david "Espero no arrepentirme..."
            $ tiene_celular = False
    stop music # detiene el sonido del helicoptero
    scene fondo camino with fade
    show tutor at left
    tutor "2... 4... 6... 8... 9 ¡Estamos todos! ¡Síganme!"
    hide tutor

    scene fondo artica7_exterior with fade
    show tutor at left
    tutor "Allá esta lo que decías David. ¡Vamos chicos!"
    scene fondo artica7_exterior with fade
    #scene black
    play sound "pasos en la nieve.mp3"
    pause 3.0
    stop sound
    scene fondo artica7_exterior
    show chris_gritando_sara_cayo
    chris "¡SARA SE CAYÓ!"
    hide chris_gritando_sara_cayo
    
    scene fondo sara_suelo with fade
   
    menu:                        
        "Ayudar a Sara":
            # ESCENA 4-A - EXT. ANTÁRTIDA - DÍA (VENTISCA)  
            $ moral += 1
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
    show tutor at center
    tutor "Llegamos... la puerta está entreabierta. Está un poco dura pero creo que puedo abrirla."
    play sound "puerta_abre.mp3"
    pause 2.0
    
    show tutor at left
    tutor "¡Adentro! ¡Rápido! Estaremos seguros hasta que pase la ventisca."
    hide tutor
   
    stop sound fadeout 2.0