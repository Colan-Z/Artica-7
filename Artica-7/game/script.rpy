# ARTICA-7 - Script básico para Ren'Py
# Define los personajes
define david = Character("David", color="#4169E1")
define sara = Character("Sara", color="#ffb969")
define chris = Character("Chris", color="#14dc61")
define tutor = Character("Tutor", color="#dc6e14")
define estudiante_1 = Character("estudiante 1", color="#5a14dc")
define estudiante_2 = Character("estudiante 2", color="#c8dc14")
define estudiante_3 = Character("estudiante 3", color="#dc2114")
define estudiante_4 = Character("estudiante 4", color="#14d5dc")
define estudiante_5 = Character("estudiante 5", color="#dc14b1")
define estudiante_6 = Character("estudiante 6", color="#96dc14")
define narrador = Character(None)

# Variables del sistema de moral
default moral = 0
default moral_chris = 0
default radio_reparada = False
default confianza_chris = True
default invernadero_cuidado = False

# Inicio del juego
label start:
    $ moral = 0

    scene fondo helicoptero
    play music "helicoptero.mp3" fadein 2.0 volume 0.2

    narrador "Un grupo de estudiantes había ganado un concurso académico."
    narrador "Su premio: un viaje científico a una base en la Antártida."
   
   
    scene fondo interior_helicoptero with fade
   

    show tutor at center
    tutor "En veinte minutos llegaremos a Base Orcadas. "
    tutor "Allí pasaremos tres semanas estudiando ecosistemas polares, cambio climático y adaptación de especies."
    tutor "Debo pedirles que me entreguen sus celulares, me gustaría que se desconectaran del mundo digital y presten atención a su entorno."
    hide tutor
    show chris at left
    show david at right
    chris "Tres semanas. ¿Crees que sobrevivas sin videojuegos?"
    
    menu:

        "Sobreviviré.":
            $ moral -= 1
            chris "esta bien..."
        "Tú tampoco sobrevivirás mucho sin ellos.":
            $ moral += 1        
            chris "¿Tú crees? (risas)"
        "Al menos estaremos juntos.":
            $ moral += 2       
            chris "Claro, héroe" 


    scene fondo ventisca with fade
    play sound "ventisca.mp3" volume 0.2
    

    narrador "De repente, el helicóptero se sacude violentamente. Los estudiantes gritan. Por la ventana, una ventisca blanca lo envuelve todo en segundos."

    scene fondo interior_helicoptero with fade

    "piloto" "¡Haremos un aterrizaje de emergencia! Sosténganse fuerte! ¡Sosténganse fuerte!"

    narrador "Los estudiantes se aferran a sus asientos. Sara cierra los ojos con fuerza, apretando su mochila contra el pecho."
    scene fondo aterrizaje with fade
    narrador "Tras unos segundos de caos, el helicóptero logra estabilizarse y aterriza suavemente."
    
    jump entrada_artica7
    

label entrada_artica7:
    
    narrador "Los estudiantes junto al tutor salen del helicóptero, dejando la mochila con los celulares en el asiento. La ventisca es cegadora. El viento azota sus rostros."
    scene fondo camino with fade
    stop music
    show tutor at left
    tutor "2...4...6...8...9 ¡Todos bien! ¡Síganme!"

    scene fondo artica7_exterior with fade
    narrador "uno de los estudiantes señala una estructura metálica medio enterrada en la nieve, aproximadamente a cincuenta metros de distancia. Es una construcción rectangular."
    narrador "Los estudiantes y el TUTOR corren hacia la instalación, luchando contra el viento, SARA tropieza con una piedra oculta bajo la nieve."

    chris "¡DAVID!¡SARA SE CAYÓ!"
    scene fondo sara_suelo with fade
   
    menu:                          
        "Ayudas a Sara":
            $ moral += 1
            chris "¡Tú puedes héroe!"
            scene fondo david_rescata_sara with fade
            david "¿Estas bien?"
            sara "Si, lo estoy, gracias..."
        "Ordenas a Chris que la ayude.":
            $ moral -= 1 
            scene fondo chris_rescata_sara with fade       
            chris "..."
            sara "Gracias..."
            

    scene fondo artica7_entrada with fade
    
    narrador "Llegan a la entrada principal. Es una instalación militar con el nombre 'ÁRTICA-7' grabado en letras desgastadas."
    
    narrador "El tutor ve la puerta entreabierta y logra abrirla para que puedan pasar."
    
    show tutor at left
    tutor "¡Adentro! ¡Rápido! Estaremos seguros hasta que pase la ventisca."

    narrador "Los estudiantes entran apresuradamente en grupo. El tutor entra último, mirando atrás hacia el helicóptero, que apenas se ve entre la nieve."

    scene fondo artica7_interior with fade
    stop music
    play sound "generador_enciende.mp3" volume 0.5

    estudiante_1 "¿Qué es este lugar?"
    
    narrador "De repente se escucha el sonido de un generador funcionando, luces fluorescentes parpadean débilmente en el techo."
    
    narrador "Se encienden completamente, iluminando un pasillo largo con paredes metálicas oxidadas, piso de rejilla industrial y cables expuestos en el techo."

    narrador "El grupo mira alrededor. El lugar parece abandonado hace años. Hay polvo sobre consolas apagadas."
    
    play sound "puerta_cierra.mp3" volume 2.0
    narrador "La puerta se cierra detrás de ellos con un golpe metálico definitivo."

    narrador "El TUTOR corre hacia la puerta , se le cae el walkie-talkie en el suelo."

    menu:                          
        "Tratar de detener al tutor":
            david "¡Profesor, espere! ¡No creo que sea buena idea tocar esa puerta!"
            narrador "El tutor ignoró a David, su desesperación lo habia ensordecido"  
        "No hacer nada.":
            tutor "NO, NO, NO, NO, ESPERA, ESPERA, ESPERA, ¡¿QUE ESTA PASANDO?!"

    show tutor at center

    "Al intentar forzar la puerta una descarga eléctrica recorre todo su cuerpo, dejándolo tirado en el suelo, convulsionando, hasta que deja de moverse."

    play sound "descarga_electrica.mp3"
    show tutor at center with hpunch
    pause 0.5
    hide tutor

    narrador "El tutor intentó forzar las compuertas..."
    narrador "Una descarga eléctrica lo atravesó."
    play sound "caida_suelo.mp3"
    scene fondo tutor_electrocutado_radio with fade
    narrador "Cayó al suelo. Sin vida."

    show sara at left
    show david at right

    sara "¡No, no, no! ¡Despertá!"
    david "No tiene pulso... está muerto."

    hide david
    
    sara "Encontré su radio. Voy a intentar contactar al piloto."
    scene fondo tutor_electrocutado with fade

    menu: 
        
        "¿Sara debería intentar contactar al piloto?"

        "Sí, intentalo. Puede que nos ayude.":
            $ moral += 1
            jump contactar_piloto

        "No, es muy arriesgado con esta ventisca.":
            $ moral -= 1
            jump no_contactar_piloto

label contactar_piloto:
    show sara at center

    sara "¡Ayuda! ¡Ayuda! ¡El tutor está muerto!"

    play sound "estatica_radio.mp3"

    "Piloto" "*estática* ...los escucho... *estática* ...voy a pedir ayuda..."

    scene fondo helicoptero with fade
    play sound "helicoptero_crash.mp3"

    scene fondo helicoptero_despega with fade
    narrador "El piloto intentó despegar a pesar de la ventisca."
    scene fondo helicoptero_volando_ventisca with fade
    narrador "Perdió el control."
    scene fondo helicoptero_destrozado with fade
    narrador "Se estrelló."
    


    scene fondo tutor_electrocutado with fade
    show sara at left
    show david at right

    sara "Es mi culpa... yo le pedí que volara..."
    david "No. Él tomó la decisión. Hiciste lo que creíste correcto."

    jump eleccion_lider

label no_contactar_piloto:
    show sara at center

    sara "Tenés razón... con esta ventisca sería suicida."

    narrador "Dejaron que el piloto esperara."
    narrador "Horas después, el frío lo reclamó."
    narrador "Nunca supieron si podrían haberlo salvado."

    show david at right

    david "Tal vez deberíamos haber intentado..."

    jump eleccion_lider

label eleccion_lider:
    scene fondo tutor_electrocutado with fade

    show david at center

    david "(Los chicos estan empezando a entrar en panico, tengo que tomar las riendas y calmarlos a todos.)"

    narrador "David se pone frente a los demas."

    david "¡Nesito que me escuchen!"

    narrador "Los chicos se voltean y miran a David"

    david "vamos a calmarnos y tratemos de buscar algo con lo que podamos pedir ayuda"

    jump explorar_instalación

label explorar_instalación:

    scene fondo tutor_electrocutado with fade

    david "Escuchen... escúchenme todos. Sé que esto es horrible. Lo peor que nos ha pasado. Pero ahora mismo, en este momento, estamos vivos."

    show estudiante_femenino at left
    estudiante_5 "¡Estamos atrapados con un cadáver!"
    hide estudiante_femenino
    show chris at left
    chris "¿Calmarnos? ¿Pensar? ¡Vamos a morir aquí!"

    jump organizacion_grupos

label organizacion_grupos:
    scene fondo tutor_electrocutado with fade

    david "Necesitamos grupos de trabajo: exploración, agricultura, gestión de recursos."

    menu:
        "¿Cómo asignar las tareas?"

        "Rotación justa. Todos hacen de todo.":
            $ moral += 1
            jump asignacion_justa

        "Los mejores en cada tarea. Eficiencia primero.":
            $ moral -= 1
            jump asignacion_favorita

label asignacion_justa:
    david "Rotaremos. Así nadie se agota y todos aprenden."

    show chris at right
    show sara at left

    chris "Suena justo."
    sara "Todos participamos por igual."

    narrador "El grupo aceptó la organización."
    narrador "Se sentía como un equipo."

    jump semanas_pasan

label asignacion_favorita:
    david "Chris, vos y los más fuertes exploran. Sara, vos y otros cuidan el invernadero."

    show chris at right
    show sara at left

    chris "Perfecto. Nosotros encontraremos lo que necesitamos."
    sara "¿Y los demás? ¿No es injusto?"

    david "Es lo más eficiente."

    narrador "Algunos chicos se sintieron excluidos."
    narrador "Las grietas comenzaron a formarse."

    jump semanas_pasan

label semanas_pasan:
    scene fondo artica7_invernadero with fade
    play music "musica_tension.mp3" fadein 3.0

    narrador "Pasaron las semanas."
    narrador "Exploraron la base. Encontraron recursos limitados."
    narrador "Pero el invernadero empezó a fallar."

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
    david "No tenemos tiempo para esto. Exploremos más a fondo."

    narrador "Abandonaron el invernadero."
    narrador "Pragmático, pero frío."

    jump puertas_misteriosas

label puertas_misteriosas:
    scene fondo artica7_pasillo_oscuro with fade

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
    scene fondo artica7_pasillo_sucio with fade
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