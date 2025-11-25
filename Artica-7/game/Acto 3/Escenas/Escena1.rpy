init python:
    from clases import GestorFinales
    
    gestor = GestorFinales()

label act_3_escena1:
    # ESCENA 1 - INT. ÁRTICA-7 - COMEDOR DESORDENADO - NOCHE   
    scene fondo comedor_desorden with fade
    david "¡Qué hiciste!"
    show chris_enojado_ropa_rota_hacha
    chris "Lo que tenía que hacer."
    david "Chris, esa era nuestra única forma de pedir ayuda al exterior."
    chris "¿Ayuda? Nadie va a venir, David. Estamos completamente solos. Y tú sigues jugando al héroe perfecto."
    hide chris_enojado_ropa_rota_hacha
    while True:
        menu:
            'Calmar a Chris.' if moral >= 7:
                call calmar_a_chris from _call_calmar_a_chris
                return
            '{color=#FE0000}Calmar a Chris (Moral demasiado baja).{/color}' if moral < 8:
                pass   
            'Huir con Sara.':
                call huir_con_sara from _call_huir_con_sara
                return
    return


# Ramificación A: Calmar a Chris. (moral alta)
label calmar_a_chris:
    # ESCENA 1A - INT. ÁRTICA-7 - COMEDOR DESORDENADO - NOCHE
    scene fondo comedor_desorden with fade
    show sara_ropa_rota
    sara "David… tenemos que escapar de él o nos matará."
    david "No puedo. Es mi amigo… todo esto es culpa de la situación en la que estamos y de su pasado."
    sara "Pero eso ya no importa. ¡Él ya ni siquiera nos escucha!"
    hide sara_ropa_rota
    david "(¿Qué debo hacer…?)"
  
    menu:
        'IIntentar calmar a Chris.':
            # ESCENA FINAL BUENO - INT. ÁRTICA-7 - COMEDOR DESORDENADO - NOCHE
            jump intentar_calmar_a_chris
        'Huir con Sara.':
            # ESCENA 1B - INT. ÁRTICA-7 - COMEDOR DESORDENADO - NOCHE
            jump huir_con_sara
    
# ESCENA FINAL BUENO - INT. ÁRTICA-7 - COMEDOR DESORDENADO - NOCHE
label intentar_calmar_a_chris:
    scene fondo comedor_desorden with fade

    david "¡Chris, basta! ¡Suelta el hacha!"
    david "Lo siento... es mi culpa, te deje de lado y prioricé a los demás en vez de a mi mejor amigo. Todo se fue de mis manos, no pude mantenerlos calmados."
    show chris_ropa_rota at right
    chris "..."
    hide chris_ropa_rota
    show sara_ropa_rota at left
    sara "David, no intentes acercarte a él. Aún no sabemos cómo va a reaccionar."
    hide sara_ropa_rota

    david "Por favor, necesito que vuelvas a ser como eras antes de que todo esto pasara."
    david "Te necesito."
    show chris_ropa_rota_llorando at right
    chris "Yo... solo quería... protegerlos a todos. Como tú. Ser útil. Ser el héroe por una vez."
    show sara_ropa_rota at left
    sara "Me alegro que hayas entrado en razón y que recuperaran su amistad pero..."
    sara "¡Arruinaste mi trabajo! Faltaba tan poco..."
    hide chris_ropa_rota_llorando
    show chris_ropa_rota at right
    chris "Puedo compensarlo, durante la exploración encontramos otra radio, parecía estar en buen estado, pero no estoy seguro..."
    sara "Espero que funcione ¡Sino moriremos y esto será tú culpa!"
    chris "Lo siento..."
    hide sara_ropa_rota
    hide chris_ropa_rota

    scene fondo pasillo
    narrador "Chris los guía a la sala de herramientas mostrándoles la radio, Sara se acerca y comprueba que funcione."
    scene fondo_radio
    show sara_ropa_rota at left
    sara "¡Funciona! Voy a intentar contactarme."
    hide sara_ropa_rota
    narrador "Sara comenzó a calibrar la frecuencia, buscando una señal que pueda ayudarlos a salir de ese lugar."
    narrador "En ese momento una voz sale entre interferencias."
    'Operador' "¿…equipo… me reciben…? ¿hay alguien ahí?"
    show sara_ropa_rota at left
    sara "¡Sí, los recibo! ¡Estamos atrapados en una base llamada Ártica-7!"
    sara "¡Necesitamos su ayuda!"

    'Operador' "Recibido… Tranquilos… estamos preparando un equipo de rescate."

    sara "¡Y tenga cuidado al intentar abrir la puerta! ¡Nuestro tutor recibió una descarga y murió!"
    hide sara_ropa_rota
    
    scene black with fade
    play sound "final_bueno.mp3" volume 0.5
    narrador "Los rescatistas lograron llegar a la base Ártica-7, al pararse en frente, ven como la puerta principal se abre por sí sola."
    narrador "Frente a la puerta, estaba el cuerpo del tutor, emanaba un olor horrible, estaba muy descompuesto."
    narrador "Quitaron el cuerpo del camino y procedieron a entrar en busca de los estudiantes."
    narrador "Chris, David, Sara y el resto estaban felices, quedaron marcados, pero no perdieron a nadie. Con el pasar del tiempo, pudieron recuperarse mentalmente."
    narrador "Los chicos se volvieron a ver después de varios días, hablaron de los acontecimientos que habían vivido, nunca supieron qué pasó ahí dentro, si realmente veían y escuchaban cosas o si todo era por su falta de cordura."
    narrador "Su amistad se volvió mas fuerte."
    python:
        final = gestor.activar_final("bueno")   
        resultado = gestor.obtener_resultado()
    scene black with fade

    centered "{size=40}[resultado]{/size}"

    pause 3.0

    return

# ESCENA 1B - INT. ÁRTICA-7 - COMEDOR DESORDENADO - NOCHE
label huir_con_sara:
    narrador "David y Sara no ven una manera de tratar con Chris, que está casi fuera de sí. En un momento en que éste se distrae..."
    narrador "Sara toca a David en el brazo para llamar su atención y le habla en susurros."
    show sara_ropa_rota
    sara "David, huyamos. Busquemos algo para defendernos o un lugar donde escondernos."
    david "No tenemos otra opción. Este ya no es mi amigo, está totalmente consumido por la locura."
    hide sara_ropa_rota
    narrador "Sara le estira del brazo al ver que David no reacciona."
    show sara_ropa_rota
    sara "¡Vayámonos David! ¡Por favor!"
    david "Sí, vamos."
    hide sara_ropa_rota
    scene fondo pasillo with fade
    narrador "David y Sara recorren los pasillos, buscando algo que los ayude en su situación."
    david "No hay ninguna puerta abierta. Siento que estamos dando vueltas."
    show sara_ropa_rota
    sara "Hay que seguir avanzando, no queda de otra."
    david "Claro, sigamos adelante."
    hide sara_ropa_rota
    scene fondo pasillo_oscuro_puerta_abierta with fade
    narrador "Ambos siguieron corriendo por el pasillo, hasta llegar a una zona oscura de la instalación, en el que había una puerta abierta, con una luz parpadeando."
    show sara_ropa_rota
    sara "Entremos, tal vez haya algo que nos sirva."
    hide sara_ropa_rota
    scene fondo sala_herramientas_palanca with fade
    david "Nunca había visto este lugar antes. ¡Está lleno de cosas que nos pueden servir!"
    scene fondo_sala_herramientas_david_palanca with fade
    david "¡Encontré algo! Es una palanca... voy a quedármela por si acaso."
    scene fondo_radio_sabana with fade
    show sara_ropa_rota at left
    sara "¡Creo que encontré algo! ¡Necesito que me des una mano!"
    hide sara_ropa_rota
    scene fondo_radio with fade
    show sara sonrisa at left
    sara "¡ puedo creer! Es una radio, como la que estaba intentando reparar. ¡Todo este tiempo había otra! Espero que funcione."
    hide sara sonrisa
    narrador "Sara rápidamente empieza a buscar alguna señal que pueda ayudarlos."
    narrador "Unos minutos después..."
    play sound "radio interfencia.mp3"
    scene fondo sala_herramientas with fade
    stop sound
    show estudiante_masculino at right
    show estudiante_masculino_2 at left
    show chris_enojado_ropa_rota_hacha
    chris "¡¿QUÉ HACEN ACÁ?! ¿HUÍAN DE MÍ? ESTE LUGAR ES MÍO... ¡DEJEN ESA RADIO!"
    david "No estás bien Chris. Cálmate. Esta radio puede ser nuestra salvación."
    narrador "Chris mira la palanca."
    chris "¿Piensas atacarme, David?"
    chris "¿No? Entonces yo lo haré."
    hide chris_enojado_ropa_rota_hacha
    hide estudiante_masculino 
    hide estudiante_masculino_2
    menu:
        'Intentar desarmarlo.':
            # ESCENA 1BA - INT. ÁRTICA-7 - COMEDOR DESORDENADO - NOCHE
            jump transición_a_escena_1BA
        'Luchar contra él.':
            # ESCENA FINAL NORMAL - INT. ÁRTICA-7 -COMEDOR DESORDENADO - NOCHE
            jump transición_a_escena_final_malo

# ESCENA 1BA - INT. ÁRTICA-7 - COMEDOR DESORDENADO - NOCHE
label transición_a_escena_1BA:
    david "¡Detente Chris!"
    show chris_enojado_ropa_rota_hacha
    chris "Eres fuerte David. Pero yo voy a ganar."
    hide chris_enojado_ropa_rota_hacha
    narrador "Interferencia. Llega la respuesta de rescate."
    'Rescatistas' "Aquí base Orcadas... ¿Me reciben? Cambio."
    narrador "Por un momento hubo silencio."

    show sara_ropa_rota at center
    sara "¡Sí! ¡Aquí Sara Clarke, desde la base Ártica-7! Somos los estudiantes que íbamos a su base. Estamos atrapados desde hace semanas. ¡Necesitamos ayuda!"
    hide sara_ropa_rota
    'Operadores' "Está bien, Sara. Estábamos buscándolos. Escúchame bien, ya estamos saliendo para allá... llegamos en aproximadamente una hora."

    narrador "Todos miran la radio, todavía sin asimilar lo que acaban de escuchar."

    show chris_enojado_ropa_rota_hacha
    chris "¡Es esa voz otra vez! ¡No pueden engañarme!"
    david "(¿A qué voz se refiere?)"
    hide chris_enojado_ropa_rota_hacha
    david "Ya lo escucharon, el rescate viene en camino."
    narrador "Los estudiantes avanzan hacia Chris."
    narrador "Chris los mira. Ellos avanzan dubitativamente hacia él. Chris los amenaza con el hacha." #Hacerlo escena
    show chris_enojado_ropa_rota_hacha
    chris "¡No se metan!"
    hide chris_enojado_ropa_rota_hacha
    narrador "Los chicos retroceden por miedo a que Chris los ataque."

    narrador "Chris vuelve a lanzar un golpe con el hacha hacia David."
    david "¡YA BASTA!"
    narrador "David contraataca, enganchando la palanca al mango del hacha, tirando de él, logra quitarle el arma."
    narrador "Los estudiantes aprovechan el momento y retienen a Chris."

    # ESCENA FINAL NORMAL - INT. ÁRTICA-7 - COMEDOR DESORDENADO - NOCHE
    scene black with fade
    play sound "final_normal.mp3" volume 0.5
    narrador "Una hora después, la puerta principal de la base se abre. Los rescatistas irrumpen en el interior. Se dividen en equipos y recorren cada pasillo con linternas, llamando por los nombres de los desaparecidos."
    narrador "Finalmente, los encuentran en la sala de herramientas: el grupo está deshecho, agotado, con la mirada perdida. Sara reúne las pocas fuerzas que le quedan para explicar lo ocurrido, su voz quebrándose entre frases inconexas."
    narrador "David, aún con vida pero gravemente herido, es atendido de inmediato por los paramédicos. Chris, fuera de sí, es hallado apartado del resto, retenido por el grupo de exploración."
    narrador "Los rescatistas lo inmovilizan y lo ponen bajo custodia sin comprender del todo la magnitud de lo sucedido."
    narrador "Mientras evacuan la base, el silencio domina la escena. Los jóvenes son finalmente rescatados, pero en sus rostros queda grabado el horror de lo vivido."
    narrador "Ninguno de ellos volverá a ser el mismo: las cicatrices físicas sanarán, pero las psicológicas los acompañarán para siempre."
    python:
        final = gestor.activar_final("normal")
        resultado = gestor.obtener_resultado()

    scene black with fade

    centered "{size=40}[resultado]{/size}"

    pause 3.0

    return

label transición_a_escena_final_malo:
    david "Lo siento amigo, no puedo dejar que te acerques a esa radio."
    show chris_enojado_ropa_rota
    chris "Si no puedo cruzar por las buenas..." 
    hide chris_enojado_ropa_rota
    show chris_furioso_ropa_rota
    chris "¡SERÁ POR LAS MALAS!"
    hide chris_furioso_ropa_rota
    scene fondo_sala_herramientas_chris_hacha
    pause 1.0
    scene fondo_sala_herramientas_chris_ataca_hacha
    play sound "hacha_palanca.mp3"
    pause 1.8
    scene fondo_sala_herramientas_palanca_suelo
    play sound "palanca_cae.mp3"
    pause
    play sound "hacha_hiere_david.mp3"
    pause
    scene david_sala_herramientas_herida_mortal2
    play sound "caida_suelo.mp3"
    narrador "El hacha atraviesa el pecho de David, que cae lentamente al suelo."
    show fondo sala_herramientas
    show sara_gritando_que_hiciste at right
    sara "¡QUÉ HICISTE!"
    hide sara_gritando_que_hiciste
    play sound "quiebre.mp3"
    show chris_arrepentido 
    pause
    chris "Qué acabo de hacer..."
    hide chris_arrepentido
    scene david_sala_herramientas_herida_mortal2
    david "No es tu culpa, hermano... traté de hacer todo el tiempo posible para que Sara pu... pudiera contactarse con alguien que pueda salvarnos."
    chris "Necesito que aguantes, todo va a salir bien."
    david "Si... todo va a salir bien..."
    hide chris_arrepentido
    narrador "Sus ojos se cierran, su corazón se detiene."
    show fondo sala_herramientas
    show chris_ropa_rota_llorando
    chris "¿Héroe...? ¿¡David!? ¡No responde! ¡Ayúdenlo! ¡Por favor!"
    hide chris_ropa_rota_llorando
    show fondo sala_herramientas_rojo
    pause 0.2
    show fondo sala_herramientas
    pause 0.2
    show fondo sala_herramientas_rojo
    play sound "generador_apagado.mp3" fadeout 0.3
    narrador "El generador hace un ruido extraño, como si no le hubiera gustado lo que acababa de pasar."
    show estudiante_masculino_rojo at left
    estudiante_6 "¿Qué esta pasando? Siento frío..."
    hide estudiante_masculino_rojo
    show estudiante_masculino_rojo at right
    estudiante_3 "Yo también siento frío."
    hide estudiante_masculino_rojo
    show sara_ropa_rota_rojo
    sara "¡El generador se apagó!"
    hide sara_ropa_rota_rojo
    show chris_ropa_rota_llorando_rojo
    chris "¡Por favor, no me dejes solo!"
    hide chris_ropa_rota_llorando_rojo
    show sara_ropa_rota_rojo at left
    play sound "estatica_radio.ogg" loop
    pause 
    sara "¿¡HOLA!? ¿¡ALGUIEN ME ESCUCHA!? ¡TENEMOS UN HERIDO!"
    hide sara_ropa_rota_rojo
    stop sound
    scene black with fade
    play sound "final_malo.mp3"
    narrador "La señal de la radio dejó de funcionar, el frío llegó a sus cuerpos, las luces cada vez tenían menos fuerza."
    narrador "Chris no solo había matado a su amigo, mató a su única salvación, la única persona que mantuvo el orden. Chris se había convertido en una {sc=4}{color=#FF0000}bestia{/color}{/sc}."
    narrador "Todos murieron de frío, nadie supo nada de lo ocurrido, los chicos habían 'desaparecido'."
    python:
        final = gestor.activar_final("malo")
        resultado = gestor.obtener_resultado()

    scene black with fade

    centered "{size=40}[resultado]{/size}"

    pause 3.0

    return


label final_alternativo:
    scene black with fade   
    play sound "caida_suelo.mp3"
    narrador "David muere al intentar detener al tutor. Ambos reciben una descarga eléctrica que recorre sus cuerpos, dejándolos tirados, convulsionando, hasta que dejan de moverse."
    narrador "Todos comienzan a perder el control, gritando y corriendo por todo el lugar en busca de ayuda. Algunos estudiantes mueren al intentar tocar otras puertas."
    narrador "Chris está de rodillas, llorando y desesperado, y Sara permanece en un rincón, completamente asustada."
    narrador "Al final nadie fue a rescatarlos."
    python:
        final = gestor.activar_final("final")
        resultado = gestor.obtener_resultado()
    scene black with fade
    centered "{size=40}[resultado]{/size}"
    pause 3.0