init python:
    from clases import GestorFinales
    
    gestor = GestorFinales()

label act_3_escena1:
    # ESCENA 1 - INT. ÁRTICA-7 - COMEDOR DESORDENADO - NOCHE   
    scene fondo comedor_desorden with fade
    show david_ropa_rota at left
    david "¿Qué hiciste?"
    show chris_enojado_ropa_rota at right
    chris "Lo que tenía que hacer."
    david "Chris, esa era nuestra única forma de pedir ayuda al exterior."
    chris "¿Ayuda? Nadie va a venir, David. Estamos completamente solos. Y tú sigues jugando al héroe perfecto."
    hide david_ropa_rota
    hide chris_enojado_ropa_rota
    return

# Ramificación A: Calmar a Chris. (moral alta)
label calmar_a_chris:
    # ESCENA 1A - INT. ÁRTICA-7 - COMEDOR DESORDENADO - NOCHE
    scene fondo comedor_desorden with fade
    show sara_ropa_rota at left
    sara "David… tenemos que escapar de él o nos matará."
    show david_ropa_rota at right
    david "Tienes razón, Sara. No podemos dejar que esto continúe."
    sara "Pero eso ya no importa. ¡Él ya ni siquiera nos escucha!"
    hide sara_ropa_rota
    david "(¿Qué debo hacer…?)"
    hide david_ropa_rota
  
    menu:
        'Intentar razonar con Chris':
            # ESCENA FINAL BUENO - INT. ÁRTICA-7 - COMEDOR DESORDENADO - NOCHE
            jump intentar_calmar_a_chris
        'Huir con Sara':
            # ESCENA 1B - INT. ÁRTICA-7 - COMEDOR DESORDENADO - NOCHE
            jump huir_con_sara
    
# ESCENA FINAL BUENO - INT. ÁRTICA-7 - COMEDOR DESORDENADO - NOCHE
label intentar_calmar_a_chris:
    scene fondo comedor_desorden with fade

    show david_ropa_rota at left
    david "¡Chris, basta! ¡Suelta el hacha!"
    david "Lo siento... es mi culpa, te dejé de lado y prioricé a los demás en vez de a mi mejor amigo. Todo se fue de mis manos, no pude mantenerlos calmados."

    # Chris baja el hacha
    show chris_ropa_rota at right
    chris "..."
    hide chris_ropa_rota
    show sara_ropa_rota at right
    sara "David, no intentes acercarte a él. Aún no sabemos cómo va a reaccionar."
    hide sara_ropa_rota
    hide david_ropa_rota

    # David se acerca y abraza a Chris
    show david_ropa_rota at left
    david "Por favor, necesito que vuelvas a ser quien eras antes de que todo esto pasara."
    david "Te necesito."
    show chris_ropa_rota at right
    chris "Yo... solo quería... protegerlos a todos. Como tú. Ser útil. Ser el héroe por una vez."
    hide david_ropa_rota
    show sara_ropa_rota at left
    sara "Me alegro que hayas entrado en razón y que recuperaran su amistad pero..."
    sara "¡Arruinaste mi trabajo! Faltaba tan poco..."
    chris "Puedo compensarlo, durante la exploración encontramos otra radio, parecía estar en buen estado, pero no estoy seguro..."
    sara "¡Espero que funcione! ¡Si no, moriremos y esto será tu culpa!"
    chris "Lo siento..."
    hide sara_ropa_rota
    hide chris_ropa_rota

    narrador "Chris los guía a la sala de herramientas mostrándoles la radio. Sara se acercó a la radio para comprobar que funcione."
    show sara_ropa_rota at left
    sara "¡Funciona! Voy a intentar contactarme."
    hide sara_ropa_rota
    narrador "Sara comenzó a calibrar la frecuencia, buscando una señal que pueda ayudarlos a salir de ese lugar."
    narrador "En ese momento una voz sale entre interferencias."
    'Operador' "¿...equipo... me reciben...? ¿Hay alguien ahí?"
    show sara_ropa_rota at left
    sara "¡Sí, los recibo! ¡Estamos atrapados en una base llamada Artica-7!"
    sara "¡Necesitamos su ayuda!"

    'Operador' "Recibido... Tranquilos... estamos preparando un equipo de rescate."

    sara "¡Y tenga cuidado al intentar abrir la puerta! ¡Nuestro tutor recibió una descarga y murió!"
    hide sara_ropa_rota

    narrador "Los rescatistas lograron llegar a la base Ártica-7. Al pararse en frente, ven como la puerta principal se abre por sí sola."
    narrador "Frente a la puerta, estaba el cuerpo del tutor, emanaba un olor horrible, estaba muy descompuesto."
    narrador "Quitaron el cuerpo del camino y procedieron a entrar en busca de los estudiantes."
    narrador "Chris, David, Sara y el resto estaban felices. Quedaron marcados, pero no perdieron a nadie. Con el pasar del tiempo, pudieron recuperarse mentalmente."
    narrador "Los chicos se volvieron a ver después de varios días, hablaron de los acontecimientos que habían vivido. Nunca supieron qué pasó ahí dentro, si realmente veían y escuchaban cosas o si todo era por su falta de cordura."
    narrador "Su amistad se volvió más fuerte."
    python:
        final = gestor.activar_final('bueno')  # o 'normal' o 'malo'
        resultado = gestor.obtener_resultado()
    
    scene black with fade
    centered "{size=40}[resultado['titulo']]{/size}\n\n[resultado['mensaje']]\n\n"
    pause 3.0
    
    return

# ESCENA 1B - INT. ÁRTICA-7 - COMEDOR DESORDENADO - NOCHE
label huir_con_sara:
    narrador "David y Sara no ven una manera de tratar con Chris, que está casi fuera de sí. En un momento en que éste se distrae..."
    narrador "(Sara toca a David en el brazo para llamar su atención y le habla en susurros.)"
    show sara_ropa_rota at right
    sara "David, huyamos. Busquemos algo para defendernos o un lugar donde escondernos."
    show david_ropa_rota at left
    david "No tenemos otra opción. Este ya no es mi amigo, está totalmente consumido por la locura."
    hide david_ropa_rota
    hide sara_ropa_rota
    narrador "Sara le estira del brazo al ver que David no reacciona."
    show sara_ropa_rota at right
    sara "¡Vayámonos David! ¡Por favor!"
    show david_ropa_rota at left
    david "Sí, vamos."
    hide david_ropa_rota
    hide sara_ropa_rota
    scene fondo pasillo with fade
    narrador "David y Sara recorren los pasillos, buscando algo que los ayude en su situación."
    show david_ropa_rota at left
    david "No hay ninguna puerta abierta. Siento que estamos dando vueltas."
    show sara_ropa_rota at right
    sara "Hay que seguir avanzando, no queda de otra."
    david "Claro, sigamos adelante."
    hide david_ropa_rota
    hide sara_ropa_rota
    scene fondo pasillo_oscuro_puerta_abierta with fade
    narrador "Ambos siguieron corriendo por el pasillo, hasta llegar a una zona oscura de la instalación, en el que había una puerta abierta, con una luz parpadeando."
    show sara_ropa_rota at left
    sara "Entremos, tal vez haya algo que nos sirva."
    hide sara_ropa_rota
    scene fondo sala_herramientas_palanca with fade # falta imagen
    show david_ropa_rota at left
    david "Nunca había visto este lugar antes. ¡Está lleno de cosas que nos pueden servir!"
    hide david_ropa_rota
    narrador "David y Sara buscan algo útil entre las herramientas."
    show david_ropa_rota at left
    david "¡Encontré algo! Es una palanca... voy a quedármela por si acaso."
    scene fondo sala_herramientas with fade
    hide david_ropa_rota
    scene fondo_radio_sabana with fade
    narrador "Sara, buscando, encuentra algo tapado con una sábana encima de una mesa."
    show sara_ropa_rota at left
    sara "¡Creo que encontré algo! ¡Necesito que me des una mano!"
    hide sara_ropa_rota
    narrador "David llega junto a Sara, ambos agarran cada punta de la sábana y la quitan de un tirón." 
    scene fondo_radio with fade
    narrador "Debajo se encontraba una radio."
    show sara sonrisa at left
    sara "¡No lo puedo creer! Es una radio, como la que estaba intentando reparar. ¡Todo este tiempo había otra! Espero que funcione."
    hide sara sonrisa
    narrador "Sara rápidamente empieza a buscar alguna señal que pueda ayudarlos y sean rescatados."
    # Poner efecto de sonido
    narrador "Señales de radio, interferencia."
    narrador "Unos minutos después..."
    # Sonido puerta abriéndose
    scene fondo sala_herramientas with fade
    narrador "Chris entra violentamente"
    show chris_enojado_ropa_rota at right
    chris "¡¿QUÉ ESTÁN HACIENDO ACÁ?! ¿HUÍAN DE MÍ? ESTE LUGAR ES MÍO... ¡DEJEN ESA RADIO!"
    # David se adelanta con la palanca
    show david_ropa_rota at left
    david "No estás bien Chris. Cálmate. Esta radio puede ser nuestra salvación."
    narrador "Chris mira la palanca"
    chris "¿Piensas atacarme, David? Veremos quién gana, mi hacha o tu palanca."
    hide david_ropa_rota
    hide chris_enojado_ropa_rota
    narrador "Chris levanta el hacha sobre su cabeza, su expresión convierte sus facciones en alguien que David no conoce. Se abalanza y con un movimiento diagonal y descendente del hacha, apunta directo al costado de David."
    menu:
        'Intentar desarmarlo':
            # ESCENA 1BA - INT. ÁRTICA-7 - COMEDOR DESORDENADO - NOCHE
            jump transición_a_escena_1BA
        'Luchar contra él':
            # ESCENA FINAL NORMAL - INT. ÁRTICA-7 -COMEDOR DESORDENADO - NOCHE
            jump transición_a_escena_final_malo

# ESCENA 1BA - INT. ÁRTICA-7 - COMEDOR DESORDENADO - NOCHE
label transición_a_escena_1BA:
    show david_ropa_rota at left
    david "¡Detente Chris!"
    hide david_ropa_rota
    narrador "David bloquea el hacha con la palanca"
    narrador "David levanta la palanca que choca en el aire con el hacha. Saltan chispas."

    show chris_ropa_rota at right
    chris "Eres fuerte David. Pero yo voy a ganar."
    hide chris_ropa_rota
    # Efecto de sonido de interferencia
    narrador "Interferencia. Llega la respuesta de rescate"
    'Rescatistas' "Aquí base Orcadas... me reciben? Cambio."
    narrador "Por un momento hubo silencio."

    show sara_ropa_rota at center
    sara "¡Sí! ¡Aquí Sara Clarke, desde la base Ártica-7! Somos los estudiantes que íbamos a su base. Estamos atrapados desde hace semanas. ¡Necesitamos ayuda!"
    hide sara_ropa_rota
    'Rescatistas' "Está bien, Sara. Estábamos buscándolos. Escúchame bien, ya estamos saliendo para allá... llegamos en aproximadamente una hora."

    narrador "Todos miran la radio, todavía sin asimilar lo que acaban de escuchar."
    narrador "El primero en hablar es Chris."

    show chris_enojado_ropa_rota at right with hpunch
    chris "¡Es esa voz otra vez! ¡No pueden engañarme!"
    hide chris_enojado_ropa_rota
    show david_ropa_rota at left
    david "Ya lo escucharon, el rescate viene en camino."
    hide david_ropa_rota
    narrador "Los estudiantes avanzan hacia Chris"
    narrador "Chris los mira. Ellos avanzan dubitativamente hacia él. Chris los amenaza con el hacha."
    show chris_furioso_ropa_rota at right
    chris "¡No se metan!"
    hide chris_furioso_ropa_rota
    narrador "Los chicos retroceden por miedo a que Chris los ataque"

    narrador "Chris ataca de nuevo"
    narrador "Intenta darle con el hacha a David."
    show david_ropa_rota at left
    david "¡YA BASTA!"
    hide david_ropa_rota
    narrador "David contrataca, enganchando la palanca al mango del hacha, haciendo palanca, logra quitarle el arma"
    narrador "Los estudiantes aprovechan el momento y retienen a Chris."

    # ESCENA FINAL NORMAL - INT. ÁRTICA-7 - COMEDOR DESORDENADO - NOCHE
    narrador "Una hora después, la puerta principal de la base se abre. Los rescatistas irrumpen en el interior. Se dividen en equipos y recorren cada pasillo con linternas, llamando por los nombres de los desaparecidos."
    narrador "Finalmente, los encuentran en la sala de herramientas: el grupo está deshecho, agotado, con la mirada perdida. Sara reúne las pocas fuerzas que le quedan para explicar lo ocurrido, su voz quebrándose entre frases inconexas."
    narrador "David, aún con vida pero gravemente herido, es atendido de inmediato por los paramédicos. Chris, fuera de sí, es hallado apartado del resto, retenido por el grupo de exploración."
    narrador "Los rescatistas lo inmovilizan y lo ponen bajo custodia sin comprender del todo la magnitud de lo sucedido."
    narrador "Mientras evacuan la base, el silencio domina la escena. Los jóvenes son finalmente rescatados, pero en sus rostros queda grabado el horror de lo vivido."
    narrador "Ninguno de ellos volverá a ser el mismo: las cicatrices físicas sanarán, pero las psicológicas los acompañarán para siempre."
    python:
        final = gestor.activar_final('normal')
        resultado = gestor.obtener_resultado()
        titulo_final = resultado['titulo']
        mensaje_final = resultado['mensaje']
    
    scene black with fade
    centered "{size=40}[resultado['titulo']]{/size}\n\n[resultado['mensaje']]\n\n"
    pause 3.0
    
    return

label transición_a_escena_final_malo:
    narrador "David decide enfrentar a Chris, listo para acabar con todo."
    show david_ropa_rota at left
    david "Lo siento amigo, no puedo dejar que te acerques a esa radio."
    show chris_furioso_ropa_rota at right
    chris "Si no puedo cruzar por las buenas... \n¡SERA POR LAS MALAS!"
    hide david_ropa_rota
    hide chris_furioso_ropa_rota
    narrador "David y Chris se enfrentan, chispas salen con el choque de la palanca y el hacha."
    narrador "Chris logra hacerle un corte en el brazo a David. La palanca cae al suelo."
    narrador "Aprovechando ese momento, Chris decide dar un golpe final. El hacha atraviesa el pecho de David, que cae lentamente al suelo."
    show sara_ropa_rota at left
    sara "¡QUÉ HICISTE!"
    hide sara_ropa_rota
    show chris_ropa_rota at right
    chris "Qué acabo de hacer..."
    show david_ropa_rota at left
    david "No es tu culpa hermano... trate de hacer todo el tiempo posible para que Sara pu... pudiera contactarse con alguien que pueda salvarnos."
    chris "Necesito que aguantes, todo va a salir bien."
    david "Si... todo va a salir bien..."
    hide chris_ropa_rota
    hide david_ropa_rota
    narrador "Sus ojos se cierran, su corazón se detienen."
    show chris_ropa_rota at right
    chris "¿Héroe...? ¿¡David!? ¡No responde! ¡Ayúdenlo! ¡Por favor!"
    hide chris_ropa_rota
    narrador "Las luces empiezan a parpadear, luego de un rato se tornan de color rojo."
    narrador "El generador hace un ruido extraño, como si no le hubiera gustado lo que acababa de pasar."
    show sara_ropa_rota at left
    sara "¿¡HOLA!? ¿¡Alguien me escucha!?"
    hide sara_ropa_rota
    # sfx(ruido blanco de la radio)
    show estudiante_femenino at left
    estudiante_6 "¿Qué esta pasando? Siento frio..."
    hide estudiante_femenino
    show estudiante_masculino at left
    estudiante_3 "Yo también siento frio."
    hide estudiante_masculino
    show chris_ropa_rota at right
    chris "¡Por favor, no me dejes solo!"
    hide chris_ropa_rota
    narrador "La señal de la radio dejó de funcionar, el frío llegó a sus cuerpos, las luces cada vez tenían menos fuerza."
    narrador "Chris no solo había matado a su amigo, mató a su única salvación, la única persona que mantuvo el orden. Chris se había convertido en una bestia."
    narrador "Todos murieron de frío, nadie supo nada de lo ocurrido, los chicos habían 'desaparecido'."
    python:
        final = gestor.activar_final('malo')
        resultado = gestor.obtener_resultado()
    
    scene black with fade
    centered "{size=40}[resultado['titulo']]{/size}\n\n[resultado['mensaje']]\n\n"
    pause 3.0
    
    return