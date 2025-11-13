# ARTICA-7 - Script básico para Ren'Py
# Define los personajes
define david = Character("David", color="#4169E1")
define sara = Character("Sara", color="#ffb969")
define chris = Character("Chris", color="#14dc61")
define tutor = Character("Tutor", color="#dc6e14")
define estudiante_1 = Character("Estudiante 1", color="#5a14dc")
define estudiante_2 = Character("Estudiante 2", color="#c8dc14")
define estudiante_3 = Character("Estudiante 3", color="#dc2114")
define estudiante_4 = Character("Estudiante 4", color="#14d5dc")
define estudiante_5 = Character("Estudiante 5", color="#dc14b1")
define estudiante_6 = Character("Estudiante 6", color="#96dc14")
define narrador = Character(None)
image negro = "#000000"

# Variables del sistema de moral
default moral = 0
default moral_chris = 0
default radio_reparada = False
default confianza_chris = True
default invernadero_cuidado = False

# Inicio del juego
label start:
    $ moral = 0

    call escena1y2 from _call_escena1y2
    call escena3a5 from _call_escena3a5
    call escena5a9 from _call_escena5a9
    scene negro with fade
    centered  "{size= 65} FIN DEL ACTO 1 {/size}"

    # Resumen Acto 2
    centered  "{size= 45} Con el paso de las semanas, la esperanza inicial se desvanece. 
    El invernadero falla misteriosamente, como si alguien lo estuviera saboteando, y la comida comienza a escasear, obligando al grupo de exploración a adentrarse más en la base.
    Notan un fenómeno inquietante: puertas previamente cerradas se abren, revelando nuevos recursos que, sin embargo, son cada vez más escasos. 
    El miedo a sufrir la misma descarga eléctrica que mató a su tutor los paraliza, pero la desesperación por sobrevivir es más fuerte. {/size}"
    centered  "{size= 45} La cordura del grupo se deteriora rápidamente. Empiezan a ver cosas, a oír ruidos y el miedo los consume. 
    En un punto de quiebre, Chris y sus exploradores, ya sin temor, encuentran una sala con herramientas y una radio funcional. 
    Chris, en un acto egoísta, esconde el hallazgo con una frazada, toma un hacha y obliga a su grupo a guardar silencio, mintiendo a los demás sobre lo que encontraron. {/size}"
    centered  "{size= 45} Poseído por una creciente locura, Chris empieza a sentir que el hacha le habla, llenándolo de un sentimiento de superioridad y el deseo de ser el lider. 
    Esta locura culmina cuando confronta a Sara y, en un arranque de ira, destruye con el hacha la radio descompuesta que ella intentaba reparar, simbolizando la destrucción de su último hilo de esperanza y sumiendo al grupo en un caos total. {/size}"
    centered  "{size= 65} FIN DEL ACTO 2 {/size}"
    return








label semanas_pasan:
    scene fondo invernadero with fade
    play music "musica_tension.mp3" fadein 3.0

    narrador "Pasaron las semanas. Exploraron la base. Encontraron recursos limitados."
    narrador "Pero el invernadero empezó a fallar."
    scene fondo invernadero_plantas_muertas with fade
    show sara at center

    sara "Las plantas se están secando. No sé por qué."

    show chris at right

    chris "¿Alguien las está saboteando?"

    menu:
        "¿Cómo responder al fallo del invernadero?"

        "Trabajemos juntos para salvarlo.":
            $ moral += 1
            $ invernadero_cuidado = True
            jump salvar_invernadero

        "Alguien está saboteando. Hay que averiguar quién.":
            $ moral -= 1
            jump culpar_sabotaje

        "No perdamos tiempo. Busquemos otras fuentes de comida.":
            jump buscar_alternativas

label salvar_invernadero:
    david "Todos al invernadero. Vamos a revisar cada planta."

    narrador "Trabajaron juntos durante horas."
    narrador "Ajustaron la irrigación, la luz, la temperatura."
    narrador "El invernadero duró un poco más."

    show sara at left

    sara "Funcionó. Lo hicimos juntos."

    jump puertas_misteriosas

label culpar_sabotaje:
    chris "Tiene que ser alguien. Nadie es tan incompetente."

    narrador "Empezaron a acusarse entre ellos."
    narrador "La paranoia creció."
    narrador "El invernadero murió mientras discutían."

    jump puertas_misteriosas

label buscar_alternativas:
    show david at left
    david "No tenemos tiempo para esto. Exploremos más a fondo."
    hide david
    hide sara
    hide chris
    narrador "Abandonaron el invernadero."
    narrador "Pragmático, pero frío."

    jump puertas_misteriosas

label puertas_misteriosas:
    scene fondo pasillo_oscuro_puerta_abierta with fade

    show david at center

    david "¿Ven eso? Esa puerta estaba cerrada ayer."

    show chris at right

    chris "Hay recursos adentro. Comida enlatada."

    menu:
        "¿Qué hacer con los recursos encontrados?"

        "Compartir todo equitativamente con el grupo.":
            $ moral += 1
            jump compartir_recursos

        "Guardar un poco para nosotros. Por seguridad.":
            $ moral -= 1
            jump guardar_secreto

        "Racionamiento estricto pero justo.":
            jump racionamiento_justo

label compartir_recursos:
    david "Ponemos todo en común. Todos comen igual."

    show sara at left

    sara "Así debería ser."

    narrador "El grupo agradeció la transparencia."
    narrador "La confianza se fortaleció."

    jump sala_herramientas

label guardar_secreto:
    david "Guardemos algo. No sabemos cuánto durará esto."

    chris "Estoy de acuerdo. Nosotros somos los que arriesgamos."

    narrador "Algunos notaron las porciones desiguales."
    narrador "La desconfianza creció."

    jump sala_herramientas

label racionamiento_justo:
    david "Contamos todo. Calculamos cuánto necesitamos por día."

    narrador "Fue frío, pero nadie podía quejarse."
    narrador "Era matemáticamente justo."

    jump sala_herramientas

label sala_herramientas:
    scene fondo artica7_sala_oscura with fade

    show chris at center

    chris "Encontré algo... una sala llena de herramientas."

    narrador "Entre las herramientas, había un hacha."
    narrador "Chris la tomó. Se sentía... diferente."

    menu chris_decision:
        "¿Chris debería contar sobre las herramientas?"

        "(Chris) Contarles sobre todo lo que encontré.":
            $ moral += 1
            $ moral_chris += 1
            $ confianza_chris = True
            jump chris_honesto

        "(Chris) Ocultar el hacha. Es mía.":
            $ moral -= 1
            $ moral_chris -= 1
            $ confianza_chris = False
            jump chris_oculta

label chris_honesto:
    scene fondo artica7_salon with fade

    show chris at center

    chris "David, encontré una sala con herramientas. Hay martillos, destornilladores... y un hacha."

    show david at left

    menu:
        "¿Cómo reaccionar?"

        "Gracias por contarnos, Chris. Sos honesto.":
            $ moral += 1
            $ moral_chris += 1
            jump agradecer_chris

        "¿Por qué tenés vos el hacha?":
            $ moral -= 1
            $ moral_chris -= 1
            jump cuestionar_chris

label agradecer_chris:
    david "Gracias, Chris. Confiamos en vos."

    show chris at center

    chris "Somos un equipo. Siempre."

    jump reparacion_radio_temprana

label cuestionar_chris:
    david "¿Planeás quedártela? ¿Para qué?"

    show chris at center

    chris "Para protegernos. ¿No confiás en mí?"

    david "No dije eso..."

    chris "Pero lo pensaste."

    narrador "Chris se alejó, resentido."

    jump reparacion_radio

label chris_oculta:
    scene fondo artica7_salon with fade

    show chris at center

    chris "Encontré algunas herramientas. Nada importante."

    narrador "Chris ocultó el hacha bajo su chaqueta."
    narrador "La sostuvo cuando nadie miraba."
    narrador "Empezó a escuchar cosas... susurros."

    jump reparacion_radio

label reparacion_radio_temprana:
    scene fondo artica7_taller with fade

    show sara at center

    sara "Encontré una radio que podría funcionar. Necesito ayuda."

    menu:
        "¿Ayudar a Sara con la radio?"

        "Todos ayudamos. Es nuestra prioridad.":
            $ moral += 1
            $ radio_reparada = True
            jump radio_exitosa

        "Sara puede hacerlo sola. Sigamos explorando.":
            jump radio_lenta

label radio_exitosa:
    show sara at center
    show david at left
    show chris at right

    sara "¡Lo logramos! ¡Funciona!"

    play sound "radio_señal.mp3"

    sara "Base científica, ¿me escuchan? Estamos atrapados en Artica-7."

    "Base Científica" "Los escuchamos. Enviaremos rescate. Mantengan la calma."

    jump espera_rescate_bueno

label espera_rescate_bueno:
    scene fondo artica7_salon with fade

    david "El rescate viene en camino. Solo tenemos que esperar."

    menu:
        "¿Cómo manejar la espera?"

        "Mantengamos la esperanza y el orden.":
            $ moral += 2
            jump preparacion_rescate

        "Estoy nervioso... ¿y si no llegan?":
            jump ansiedad_rescate

label preparacion_rescate:
    narrador "Se organizaron para el rescate."
    narrador "Prepararon un área de aterrizaje."
    narrador "Juntaron sus pertenencias."
    narrador "Se mantuvieron unidos."

    jump final_bueno

label ansiedad_rescate:
    narrador "La ansiedad causó algunas peleas."
    narrador "Pero se mantuvieron juntos lo suficiente."

    if moral >= 8:
        jump final_bueno
    else:
        jump final_normal_anticipado

label radio_lenta:
    $ radio_reparada = False

    sara "Está bien... lo intentaré sola."

    narrador "Sara trabajó durante días."
    narrador "Progresaba lentamente."

    jump deterioro_mental

label reparacion_radio:
    scene fondo artica7_taller with fade

    show sara at center

    sara "Voy a intentar reparar esta radio. Puede ser nuestra salvación."

    narrador "Sara trabajó incansablemente."

    if confianza_chris:
        jump radio_progreso
    else:
        jump chris_destruye_radio

label chris_destruye_radio:
    scene fondo artica7_taller with fade

    show sara at center
    show chris at right

    narrador "Chris entró al taller."
    narrador "El hacha en su mano."
    narrador "Sus ojos vacíos."

    chris "No necesitamos rescate. Podemos quedarnos aquí."

    sara "¿Chris? ¿Qué te pasa?"

    play sound "hacha_golpe.mp3"

    narrador "Chris golpeó la radio con el hacha."
    narrador "Una vez. Dos veces. Tres."
    narrador "La radio quedó hecha pedazos."

    show sara at center

    sara "¡¿QUÉ HICISTE?!"

    jump confrontacion_final

label radio_progreso:
    narrador "Sara seguía trabajando."
    narrador "Pero el tiempo se agotaba."

    jump deterioro_mental

label deterioro_mental:
    scene fondo pasillo_oscuro_puerta_abierta with fade
    play music "musica_horror.mp3" fadein 2.0

    narrador "Pasaron más días."
    narrador "Los recursos seguían escaseando."
    narrador "Las paredes ya no estaban limpias."
    narrador "Mesas y sillas tiradas por todos lados."
    narrador "Las miradas... vacías."

    show david at left
    show chris at right

    david "Chris... tenemos que mantener la calma."

    chris "La calma... ¿para qué? Vamos a morir aquí."

    jump busqueda_desesperada

label busqueda_desesperada:
    scene fondo artica7_pasillo_oscuro with fade

    show chris at center

    chris "Nadie me respeta. Con esto... con el hacha... puedo ser el líder."

    narrador "Chris buscó a David."
    narrador "El hacha hablaba."
    narrador "O eso creía."

    jump confrontacion_final

label confrontacion_final:
    scene fondo artica7_salon_caos with fade

    show david at left
    show chris at right
    show sara at center

    chris "Debería ser yo el líder. ¡YO!"

    david "Chris, por favor. Calmáte."

    play sound "hacha_aire.mp3"

    narrador "Chris lanzó un hachazo al aire."
    narrador "David retrocedió."

    menu decision_final:
        "Esta es la decisión final."

        "Abrazar a Chris.":
            $ moral += 2
            jump abrazo_final

        "Huir con Sara.":
            jump huida_final

        "Enfrentar a Chris con violencia.":
            $ moral -= 2
            jump pelea_final

label abrazo_final:
    show david at center
    hide sara

    david "Chris... hermano..."

    narrador "David caminó hacia Chris."
    narrador "Abrió los brazos."

    show chris at right

    chris "¿Qué...?"

    david "Sé que estás asustado. Yo también lo estoy."

    narrador "David abrazó a Chris."
    narrador "El hacha cayó al suelo."


    chris "Lo siento... lo siento tanto..."

    if moral_chris >= 0:
        jump chris_redimido
    else:
        jump abrazo_fallido

label chris_redimido:
    show chris at center

    chris "Yo... yo tenía una radio. Escondida en la sala de herramientas."

    show sara at left

    sara "¿Qué? ¿Por qué no lo dijiste?"

    chris "Tenía miedo... de perder control. Pero David tiene razón."

    jump contacto_final_bueno

label contacto_final_bueno:
    scene fondo artica7_taller with fade

    show sara at center

    sara "La radio funciona. Contactando..."

    play sound "radio_señal.mp3"

    sara "Base científica, estamos en Artica-7. Necesitamos rescate urgente."

    "Base Científica" "Recibido. En camino."

    if moral >= 10:
        jump final_bueno
    else:
        jump final_normal

label abrazo_fallido:
    hide david
    show chris at center

    chris "¡NO! ¡Es una trampa!"

    narrador "Chris empujó a David."
    narrador "Tomó el hacha de nuevo."

    jump pelea_final

label huida_final:
    scene fondo artica7_pasillo with fade

    show david at left
    show sara at right

    david "¡Corré, Sara!"

    narrador "Corrieron por los pasillos."
    narrador "Buscando una salida."
    narrador "Buscando esperanza."

    scene fondo artica7_habitacion_luces with fade

    narrador "Encontraron una habitación con luces parpadeantes."
    narrador "Se encerraron dentro."

    show sara at center

    sara "¡Hay una radio! ¡En buen estado!"

    show david at right

    david "¡Rápido, contactá!"

    play sound "radio_señal.mp3"

    sara "Base científica, estamos atrapados. Necesitamos ayuda."

    "Base Científica" "Recibido. Enviando equipo de rescate."

    play sound "puerta_golpes.mp3"

    chris "¡ABRAN LA PUERTA!"

    menu:
        "Chris está afuera golpeando la puerta."

        "Esperar al rescate. No abrir.":
            jump esperar_rescate

        "Intentar razonar con Chris.":
            jump razonar_chris

label esperar_rescate:
    narrador "Esperaron en silencio."
    narrador "Los golpes continuaron."
    narrador "Luego... silencio."

    if moral >= 5:
        jump rescate_a_tiempo
    else:
        jump chris_irrumpe

label rescate_a_tiempo:
    play sound "helicoptero.mp3"

    narrador "El sonido de un helicóptero."
    narrador "Voces afuera."
    narrador "El rescate había llegado."

    jump final_normal

label chris_irrumpe:
    play sound "puerta_rompe.mp3"

    narrador "Chris forzó la puerta."
    narrador "Entró con el hacha en alto."

    jump pelea_final

label razonar_chris:
    hide sara
    show david at center

    david "¡Chris! ¡El rescate viene! ¡Vamos a salir de aquí!"

    if moral_chris >= -1:
        show chris at right
        chris "¿De verdad...?"
        jump rescate_a_tiempo
    else:
        show chris at right
        chris "¡MENTÍRA!"
        jump pelea_final

label pelea_final:
    scene fondo artica7_salon_caos with fade
    play music "musica_accion.mp3"

    show david at left
    show chris at right

    narrador "La pelea comenzó."
    narrador "David encontró una palanca."
    narrador "Chris blandía el hacha."

    if moral >= 3:
        jump david_gana
    elif moral <= -3:
        jump chris_mata
    else:
        jump pelea_empate

label david_gana:
    narrador "David esquivó un hachazo."
    narrador "Usó la palanca para desarmar a Chris."
    narrador "El hacha voló por el aire."

    show david at center
    show chris

    david "Se acabó, Chris."

    narrador "Los otros exploradores entraron."
    narrador "Retuvieron a Chris."

    play sound "helicoptero.mp3"

    narrador "El rescate llegó."

    jump compuerta_final

label chris_mata:
    narrador "Chris fue más rápido."
    narrador "El hacha cortó profundo."
    narrador "David cayó."

    show chris at center
    show sara at Position(xpos=0.35)

    sara "¡NOOOOO!"

    show chris

    chris "¿Qué... qué hice?"

    narrador "Chris soltó el hacha."
    narrador "Se arrodilló junto a David."
    narrador "Las lágrimas caían."

    chris "David... perdóname... yo no quería..."

    narrador "Pero era demasiado tarde."
    narrador "David cerró los ojos."

    play sound "helicoptero.mp3"

    narrador "El rescate llegó."
    narrador "Pero llegaron a una escena de horror."

    jump puerta_maldita

label pelea_empate:
    narrador "Ambos pelearon con desesperación."
    narrador "Ambos recibieron heridas profundas."
    narrador "Ambos cayeron."

    show sara at center

    sara "¡David! ¡Chris! ¡Despierten!"

    narrador "Sara intentó ayudar."
    narrador "Pero las heridas eran graves."

    if moral >= 0:
        narrador "David abrió los ojos débilmente."
        jump rescate_herido
    else:
        narrador "Ninguno se movió."
        jump ambos_muertos

label rescate_herido:
    play sound "helicoptero.mp3"

    narrador "El rescate llegó justo a tiempo."
    narrador "Paramédicos entraron corriendo."

    jump compuerta_final

label ambos_muertos:
    narrador "El silencio llenó Artica-7."
    narrador "Sara quedó sola."
    narrador "Rodeada de muerte."

    play sound "helicoptero_distante.mp3"

    narrador "Cuando el rescate llegó..."
    narrador "Era demasiado tarde."

    jump puerta_maldita

label compuerta_final:
    scene fondo artica7_puerta_principal with fade

    "Rescatista" "¡Estamos aquí! ¡Vamos a sacarlos!"

    narrador "Los rescatistas intentaron abrir la puerta principal."

    if moral >= 5:
        play sound "puerta_abre.mp3"
        narrador "La puerta se abrió misteriosamente."
        narrador "Como si Artica-7 los dejara ir."
        jump final_normal
    else:
        play sound "descarga_electrica.mp3"
        narrador "Una descarga eléctrica."
        narrador "Los rescatistas cayeron."
        jump puerta_maldita

label puerta_maldita:
    scene fondo artica7_interior_oscuro with fade
    play music "musica_horror_final.mp3"

    show sara at center

    sara "¡No! ¡NO! ¡La puerta mató a los rescatistas!"

    narrador "Intentaron comunicarse con la base."
    narrador "Pero nadie más vendría."
    narrador "Artica-7 había ganado."

    jump final_malo

# FINALES

label final_bueno:
    scene fondo final_bueno with fade
    play music "musica_esperanza.mp3" fadein 3.0

    narrador "El rescate llegó sin complicaciones."
    narrador "La puerta se abrió como si nunca hubiera estado cerrada."

    show david at left
    show sara at center
    show chris  at right

    narrador "Salieron juntos de Artica-7."
    narrador "Traumatizados, pero vivos."
    narrador "Su amistad, aunque dañada, permanecía."

    narrador "Semanas después, se reencontraron."
    narrador "Hablaron sobre lo que pasó."
    narrador "Procesaron el trauma juntos."

    narrador "Chris buscó ayuda profesional."
    narrador "David lo apoyó en cada paso."
    narrador "Sara escribió sobre la experiencia."

    narrador "No olvidarían Artica-7."
    narrador "Pero tampoco los definiría."
    narrador "Sobrevivieron."
    narrador "Y seguirían adelante."

    centered "{size=+10}{color=#32CD32}FINAL BUENO{/color}{/size}\n\nTRAUMA MÍNIMO\nAMISTAD PRESERVADA\nTODOS SOBREVIVEN"

    return

label final_normal_anticipado:
    jump final_normal

label final_normal:
    scene fondo final_normal with fade
    play music "musica_melancolia.mp3" fadein 3.0

    narrador "El rescate llegó después de la violencia."
    narrador "Vieron la base destrozada."
    narrador "Paredes manchadas. Muebles rotos."
    narrador "Miradas vacías en los rostros de los chicos."

    show david at left
    show sara at center
    show chris at right

    narrador "Los paramédicos atendieron a David."
    narrador "Sus heridas eran profundas, pero sobreviviría."

    narrador "Chris tuvo que ser contenido."
    narrador "Forcejeó, gritó, lloró."
    narrador "La cordura apenas sostenida por un hilo."

    narrador "Sara contó todo lo sucedido."
    narrador "Su voz era un susurro quebrado."

    scene fondo hospital with fade

    narrador "Semanas después, en diferentes hospitales:"

    narrador "David enfrentaba pesadillas cada noche."
    narrador "El sonido del hacha cortando el aire."
    narrador "Los gritos de Chris."
    narrador "La sangre."

    narrador "Sara no podía entrar a cuartos cerrados."
    narrador "El pánico la paralizaba."
    narrador "Veía puertas cerrándose solas."
    narrador "Escuchaba el generador en su mente."

    narrador "Chris fue internado en psiquiatría."
    narrador "No hablaba con nadie."
    narrador "Solo sostenía sus manos."
    narrador "Mirando la sangre que ya no estaba ahí."

    scene fondo final_normal_texto with fade

    narrador "Todos sobrevivieron."
    narrador "Pero dejaron parte de sí mismos en Artica-7."

    narrador "Las cicatrices físicas sanarían."
    narrador "Las psicológicas... esas permanecerían."

    narrador "Nunca volverían a ser los mismos chicos."
    narrador "Los ganadores del concurso académico."
    narrador "Los estudiantes brillantes con futuro prometedor."

    narrador "Artica-7 se los había llevado."
    narrador "Y les devolvió solo sombras."

    centered "{size=+10}{color=#FFD700}FINAL NORMAL{/color}{/size}\n\nSALVADOS CON TRAUMA SEVERO\nCICATRICES PSICOLÓGICAS PROFUNDAS\nNUNCA SERÁN LOS MISMOS"

    return

label final_malo:
    scene fondo final_malo with fade
    play music "musica_tragedia.mp3" fadein 3.0

    narrador "La puerta no abrió."
    narrador "Los rescatistas cayeron electrocutados."
    narrador "Sus cuerpos inmóviles frente a la entrada."

    scene fondo artica7_interior_final with fade

    if "david" in globals():
        show sara at center

    narrador "Dentro de Artica-7, los sobrevivientes comprendieron."
    narrador "No habría más rescates."
    narrador "Nadie más vendría."
    narrador "La instalación había reclamado demasiadas vidas."

    narrador "Intentaron abrir la puerta desde dentro."
    narrador "Pero cada intento terminaba en descargas."
    narrador "En dolor."
    narrador "En desesperación."

    scene fondo artica7_semanas_despues with fade

    narrador "Pasaron los días."
    narrador "Luego semanas."

    narrador "Los recursos finales se agotaron."
    narrador "El hambre se volvió insoportable."
    narrador "El frío se filtraba por todas partes."

    narrador "Las luces parpadeaban cada vez menos."
    narrador "El generador gemía como una bestia moribunda."

    scene fondo artica7_oscuridad with fade

    narrador "En la oscuridad completa."
    narrador "En el silencio absoluto."
    narrador "Artica-7 finalmente se quedó quieta."

    narrador "Los cuerpos nunca fueron recuperados."
    narrador "La instalación fue declarada zona restringida."
    narrador "Los archivos, clasificados."

    scene fondo reporte_oficial with fade

    narrador "El reporte oficial:"
    narrador "'Accidente trágico durante expedición educativa.'"
    narrador "'Fallo estructural en instalación abandonada.'"
    narrador "'Múltiples bajas. Sin sobrevivientes.'"

    narrador "Pero no mencionaba las puertas que se abrían solas."
    narrador "Ni el hacha que susurraba."
    narrador "Ni cómo Artica-7 parecía... viva."

    scene fondo artica7_exterior_abandonado with fade
    play sound "viento_final.mp3"

    narrador "Años después, la instalación sigue ahí."
    narrador "Cubierta de nieve."
    narrador "Olvidada."
    narrador "Esperando."

    narrador "Las luces a veces parpadean en la oscuridad polar."
    narrador "El generador ocasionalmente zumba."
    narrador "Como si algo dentro todavía viviera."

    narrador "Como si Artica-7 nunca durmiera."
    narrador "Solo esperara."
    narrador "Paciente."
    narrador "Hambrienta."

    centered "{size=+10}{color=#8B0000}FINAL MALO{/color}{/size}\n\nMUERTE EN ARTICA-7\nNADIE ESCAPA\nTRAGEDIA TOTAL\n\n{size=-2}Los nombres fueron añadidos\na la lista de desaparecidos\nen la Antártida.{/size}"

    return

# Créditos finales
label creditos:
    scene fondo negro with fade

    centered "{size=+5}ARTICA - 7{/size}\n\nUna historia de supervivencia\ny pérdida de humanidad\n\nBasada en 'El Señor de las Moscas'\nde William Golding\n\nDesarrollado en Ren'Py"

    return