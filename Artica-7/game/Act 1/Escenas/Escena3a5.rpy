label escena3a5:
    # ESCENA 3 - EXT. HELICOPTERO - VENTISCA - DÍA
    scene fondo ventisca with fade
    play sound "ventisca.mp3" volume 0.2
    
    narrador "De repente, el helicóptero se sacude violentamente. \nLos estudiantes gritan. Por la ventana, una ventisca blanca lo envuelve todo en segundos."

    scene fondo interior_helicoptero with fade
    ## Falta sonido de alarma del helicoptero

    "Piloto" "¡Haremos un aterrizaje de emergencia! ¡¡Sosténganse fuerte!! ¡¡¡Sosténganse fuerte!!!"

    narrador "Los estudiantes se aferran a sus asientos. Sara cierra los ojos con fuerza, apretando su mochila contra el pecho."
    scene fondo_aterrizaje with fade
    ## Falta sonido de aterrizaje del helicoptero
    narrador "Tras unos segundos de caos, el helicóptero logra estabilizarse y aterriza suavemente."

    # ESCENA 4 - EXT. ANTÁRTIDA - DÍA (VENTISCA)
    tutor "¿¡Están todos.... bien!? ¿Qué es eso? creo que veo algo..."
    tutor "Chicos, aquí no estaremos seguros, necesito que vayan detrás de mí"
    narrador "Los estudiantes junto al tutor salen del helicóptero, dejando la mochila con los celulares en el asiento. La ventisca es cegadora. El viento azota sus rostros."

    scene fondo camino with fade
    stop music
    show tutor at left
    ## En el celtex tenemos un sonido de ventisca ensordecedora
    ## A partir de aca no escuche ningun sonido 1111111111111111
    tutor "2...4...6...8...9 ¡Estamos todos! ¡Síganme!"

    scene fondo artica7_exterior with fade
    ## Deberiamos buscar un imagen que se ve artica 7 mas de lejos
    narrador "Una estructura metálica medio enterrada en la nieve, aproximadamente a cincuenta metros de distancia."
    narrador "Los estudiantes y el tutor se dirigen hacia la instalación, luchando contra el viento, Sara tropieza con una piedra oculta bajo la nieve."
    show chris at left
    chris "¡SARA SE CAYÓ!"
    hide chris
    
    scene fondo sara_suelo with fade
   
    menu:                        
        "Ayudas a Sara":
            # ESCENA 4-A - EXT. ANTÁRTIDA - DÍA (VENTISCA)  
            $ moral += 1
            scene fondo david_rescata_sara with fade
            david "¿Estas bien?"
            sara "Si, lo estoy, gracias..."
        "Ordenas a Chris que la ayude.":
            # ESCENA 4-B - EXT. ANTÁRTIDA - DÍA (VENTISCA)
            $ moral -= 1 
            scene fondo chris_rescata_sara with fade       
            chris "..."
            sara "Gracias..."
            
    # ESCENA 5 - EXT. ÁRTICA-7 - ENTRADA - DÍA
    scene fondo artica7_entrada with fade
    
    ### Deberiamos de borrar el "grabado en letras desgastadas"
    narrador "Llegan a la entrada principal. Es una instalación militar con el nombre 'ÁRTICA-7' grabado en letras desgastadas."
    
    narrador "El tutor ve la puerta entreabierta y logra abrirla para que puedan pasar."
    
    show tutor at left
    tutor "¡Adentro! ¡Rápido! Estaremos seguros hasta que pase la ventisca."
    hide tutor
    narrador "Los estudiantes entran apresuradamente en grupo. El tutor entra último, mirando atrás hacia el helicóptero, que apenas se ve entre la nieve."