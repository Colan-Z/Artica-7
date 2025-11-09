# Escena 4: Refugio en Ártica-7

label escena4_refugio:  
    narrador "Los estudiantes junto al tutor salen del helicóptero, dejando la mochila con los celulares en el asiento. La ventisca es cegadora. El viento azota sus rostros."
    scene fondo camino with fade
    stop music
    show tutor at left
    ## En el celtex tenemos un sonido de ventisca ensordecedora
    ## A partir de aca no escuche ningun sonido 1111111111111111
    tutor "2...4...6...8...9 ¡Todos bien! ¡Síganme!"

    scene fondo artica7_exterior with fade
    narrador "Uno de los estudiantes señala una estructura metálica medio enterrada en la nieve, aproximadamente a cincuenta metros de distancia. Es una construcción rectangular."
    narrador "Los estudiantes y el TUTOR corren hacia la instalación, luchando contra el viento, SARA tropieza con una piedra oculta bajo la nieve."

    chris "¡DAVID!¡SARA SE CAYÓ!"
    scene fondo sara_suelo with fade
   
    menu:                          
        "Ayudas a Sara":
            $ moral += 1
            scene fondo david_rescata_sara with fade
            david "¿Estas bien?"
            sara "Si, lo estoy, gracias..."
        "Ordenas a Chris que la ayude.":
            $ moral -= 1 
            scene fondo chris_rescata_sara with fade       
            chris "..."
            sara "Gracias..."
            

    scene fondo artica7_entrada with fade
    
    ### Deberiamos de borrar el "grabado en letras desgastadas"
    narrador "Llegan a la entrada principal. Es una instalación militar con el nombre 'ÁRTICA-7' grabado en letras desgastadas."
    
    narrador "El tutor ve la puerta entreabierta y logra abrirla para que puedan pasar."
    
    show tutor at left
    tutor "¡Adentro! ¡Rápido! Estaremos seguros hasta que pase la ventisca."
    ### Deberiamos ocultar el tutor?
    narrador "Los estudiantes entran apresuradamente en grupo. El tutor entra último, mirando atrás hacia el helicóptero, que apenas se ve entre la nieve."