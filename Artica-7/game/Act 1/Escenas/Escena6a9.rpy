label escena6a9:
    
    # ESCENA 6 - INT. ÁRTICA-7 - ENTRADA - DÍA
    scene fondo_sala_principal_puerta_abierta with fade
    stop music

    show estudiante_femenino at left
    estudiante_1 "¿Qué es este lugar?"
    hide estudiante_femenino

    play sfx1 "generador_enciende.mp3" volume 0.5
    queue sfx1 "generador_loop.ogg" loop
    # Agregar dialogo de los personajes reaccionando al sonido del generador 
    # e1 '¿Qué es eso?' 
    #e2 'Suena como un generador. Pero no entiendo por qué se enciende solo.' 
    #chris 'Si... es raro.'
    pause
    show estudiante_masculino
    estudiante_4 "¿Qué es eso?"
    hide estudiante_masculino
    show chris at right
    chris "Suena como un generador. Pero no entiendo por qué se enciende solo."
    hide chris
    show tutor
    tutor "Si... es raro."
    hide tutor
    # narrador "De repente se escucha el sonido de un generador encendiéndose."
    
    show sara at left
    sara "Parece que lo abandonaron hace años."
    hide sara
    scene fondo artica7_interior_2

    play sound "puerta_cierra.mp3" volume 2.0
    narrador "La puerta se cierra detrás de ellos con un golpe metálico definitivo."
    narrador "Mientras el tutor corría desesperado hacia la puerta, un walkie-talkie cae de su bolsillo."
    scene fondo_tutor_toca_puerta_2
    menu:                         
        "Tratar de detenerlo":
            # ESCENA 6-A - INT. ÁRTICA-7 - ENTRADA - DÍA
            david "¡Profesor, espere! ¡No creo que sea buena idea tocar esa puerta!"
            narrador "El tutor ignoró a David, su desesperación lo habia ensordecido"  
        "No hacer nada.":
            # ESCENA 6-B - INT. ÁRTICA-7 - ENTRADA - DÍA
            # show tutor at center with hpunch
            tutor "NO, NO, NO, NO, ESPERA, ESPERA, ESPERA, ¡¿QUE ESTA PASANDO?!"

    play sound "descarga_electrica.mp3"
    # show tutor at center with hpunch
    pause 0.5
    # hide tutor
    play sound "caida_suelo.mp3"
    scene fondo tutor_electrocutado_radio with fade
    play movie "images/fondo-tutor_electrocutado_radio.webm"

    scene fondo tutor_electrocutado_radio
   
    # ESCENA 7 - INT. ÁRTICA-7 - TUTOR ELECTROCUTADO - DÍA
    show estudiante_femenino at left
    pause 7
    play sound "Estudiante femenino gritando.mp3" 
    estudiante_2 "¡SEÑOR!"
    hide estudiante_femenino
    menu:
        "Tomar pulso del tutor.":
            # ESCENA 7-A - INT. ÁRTICA-7 - TUTOR ELECTROCUTADO SIN HUMO - DÍA
            scene fondo_tutor_pulso
            david "No... no respira. No tiene pulso."
            $ humo = 0
        "No tocarlo, podría ser peligroso.":
            # ESCENA 7-B - INT. ÁRTICA-7 - TUTOR ELECTROCUTADO CON HUMO - DÍA
            scene fondo tutor_electrocutado_quemado_radio with fade
            narrador "No hacia falta verificar su pulso, el olor a carne quemada que desprendía, provocaba que algunos alumnos les dieran nauseas."
            $ humo = 1

    # ESCENA 7AB - INT. ÁRTICA-7 - TUTOR ELECTROCUTADO - DÍA
    if humo == 0:
        scene fondo tutor_electrocutado_radio with fade
    else:
        scene fondo tutor_electrocutado_quemado_radio with fade
    play sound "radio interferencia.mp3"
    "Piloto" "¿Ho... hola? ¿Se escu... cha?"
    "Piloto" "¿Es... están to... dos bien?"
    if humo == 0:
        scene fondo tutor_electrocutado with fade
    else:
        scene fondo tutor_electrocutado_quemado with fade
    
    show sara at left
    sara "¡Necesitamos ayuda! ¡Nuestro tutor acaba de morir por una descarga eléctrica!"
    "Piloto" "¡Tranquila, voy a intentar pedir ayuda!"
    hide sara
    jump ESCENA_8

# ESCENA 8 - EXT. ÁRTICA-7 - HELICOPTERO - DESPEGA - DÍA
label ESCENA_8:
    play sound "helicoptero despega.mp3" fadein 0.5
    scene fondo helicoptero_despega with fade
    piloto "No se preocupen. ¡Voy a buscar ayuda!"
    # narrador "El piloto enciende el helicóptero y procede a despegar."
    scene fondo helicoptero_volando_ventisca with fade
    play sound "helicoptero pierde control.mp3"
    piloto "¡NO! ¡La ventisca es muy fuerte! ¡¡Estoy perdiendo el control!!"
    # narrador "Al elevarse, pierde el control." 
    scene fondo helicoptero_cae with fade
    play sound "helicoptero cae.mp3"
    pause
    # narrador "La ventisca era muy fuerte."
    scene fondo helicoptero_destrozado with fade
    play sound "helicoptero destrozado.mp3"
    pause
    # narrador "Por lo que termina estrellándose, dejando a los chicos a su suerte, dejando únicamente el ruido de la estática."
    jump ESCENA_9
    
# ESCENA 9 - INt. ÁRTICA - ENTRADA
label ESCENA_9:
    play sound "estatica estrella_helicoptero.mp3" fadein 1.5
    scene fondo sara_retrocede with fade
    pause 1.5
    play music "suspenso alumnos solos.mp3" loop volume 0.1
    scene fondo chris_golpea_pared with fade
    play sound "golpe pared.mp3" volume 5.0
    chris "¡No! ¡Esto no puede estar pasando!"  
    scene fondo tutor_electrocutado with fade
    hide chris_enojado
    show estudiante_masculino at right
    estudiante_3 "¡Tenemos que salir de aquí! ¡YA!"
    hide estudiante_masculino
    show estudiante_masculino at left
    estudiante_4 "¡Vamos a morir aquí!"
    hide estudiante_masculino
    show chris_furioso 
    chris "¡Maldita sea! Se suponía que sería una excursión que me ayudaría con mis problemas, ¡PERO ESTO SOLO LO EMPEORA!"
    hide chris_furioso
    show estudiante_femenino at left
    estudiante_1 "¡Qué vamos a hacer!"
    hide estudiante_femenino
    show estudiante_masculino at right
    estudiante_3 "Quiero irme a casa."
    hide estudiante_masculino
    david "Escuchen... escúchenme todos. Sé que esto es horrible. Lo peor que nos pudo haber pasado. Pero ahora mismo, en este momento, estamos vivos."
    show estudiante_femenino at left
    estudiante_5 "¡Estamos atrapados con un cadáver!"
    hide estudiante_femenino
    show chris_enojado
    chris "¿Calmarnos? ¿Pensar? ¡Vamos a morir aquí!"
    hide chris_enojado
    
    david "Los entiendo, pero estando acá parados no vamos a solucionar nada. Deberíamos investigar la instalación, puede que encontremos algo que nos mantenga con vida mientras esperamos a que nos rescaten."
    show sara at right
    sara "Tienes razón, tal vez logremos encontrar algo para contactarnos con los de afuera."
    david "¡Exacto!"
    show chris at left
    chris "Está bien. Espero que esto no sea una pérdida de tiempo... ¿Qué tienes en mente, héroe?"
    david "Primero, necesitamos un grupo que pueda explorar la instalación."
    hide chris
    hide sara
    menu:
        "Ir con Chris a explorar la base.":
            # ESCENA 9A - INT - ÁRTICA-7 - PASILLOS - DíA
            jump ESCENA_9A
        "Quedarse ayudando a los demás.":  
            # Escena 9B - Interior - Ártica-7 - ENTRADA - DÍA
            jump ESCENA_9B

# Escena 9A - Int - Ártica-7 - pasillos - día
label ESCENA_9A:
    scene fondo pasillo with fade
    david "Vamos por este pasillo, parece llevar hacia el centro de la base."
    scene fondo_pasillo_estudiante_toca_puerta
    pause
    # narrador "Un estudiante intenta tocar una puerta"
    show chris_enojado at left
    chris "¡No la toques! ¿¡Quieres terminar como nuestro tutor?! ¡¡¿FRITO?!!."
    scene fondo pasillo with fade
    show chris_enojado at left
    show estudiante_masculino at right
    estudiante_3 "Lo siento, no volverá a pasar..."
    hide estudiante_masculino
    hide chris_enojado
    menu:
        'Intervenir.':
            $ moral -= 1
            jump ESCENA_9AA
        'Tranquilizar.':
            $ moral += 1
            jump ESCENA_9AB
        'Ignorarlo.':
            jump ESCENA_10

label ESCENA_9B:
    show sara at right
    sara "Yo... yo puedo acompañarte para cuidarlos."
    david "Me vendría bien un poco de ayuda..."
    hide sara 
    show chris
    chris "Que pasa héroe? pareces un tomate? jajaj"
    menu:
        'Cambiar de tema':
            # Escena 9BA - Interior - Ártica-7 - ENTRADA - DÍA
            jump ESCENA_9BA


# Escena 9AA - Int. Ártica-7 - Pasillos - Día
label ESCENA_9AA:
    david "No deberías de tratar así a las personas y menos en estos momentos."
    show chris_enojado
    chris "No te metas donde no te incumbe."
    jump ESCENA_10

# Escena 9AB - INT. ÁRTICA-7 (PASILLOS) - DÍA
label ESCENA_9AB:
    david "Chris, tranquilo hermano, vamos a tomarnos esto con mas calma, no sabemos cuanto tiempo vamos a estar acá."
    show chris
    chris "Lo siento, no estoy en mi mejor momento..."
    jump ESCENA_10

label ESCENA_9BA:
    david "¡¿Qué?! No nada, nada, no me pasa nada... puedes ir a investigar?"
    chris "¡Obvio, ya tenía pensado hacerlo!"    
    hide chris
    show estudiante_masculino at left
    estudiante_3 "Ya me encuentro mejor, puedo ir a investigar la zona."
    hide estudiante_masculino
    show estudiante_masculino at right
    estudiante_6 "Si, yo también lo estoy."
    hide estudiante_masculino
    show chris
    chris "Lo siento, pero no me gusta trabajar en equipo, me gusta estar solo."
    david "Vas a tener que trabajar con ellos Chris, no te queda de otra."
    chris "...Está bien, vamos, no me hagan perder el tiempo."
    hide chris
    narrador "David ve a Sara preocupada. Se acerca a preguntarle qué le pasa."
    david "¿Estás bien, Sara? Te veo preocupada."
    show sara
    sara "¿Eh? ¡Sí, sí, estoy bien!"
    david "¿Estás segura? Puedes confiar en mí."
    sara "Bueno... no quería alarmar a nadie, pero hace un momento me pareció ver... algo por el pasillo."
    david "¿Algo? ¿A qué te refieres con algo?"
    sara "Me pareció ver una... sombra. Todos estábamos juntos, no pudo haber sido alguien de nosotros."
    david "(Puede que tenga razón, espero que no le pase nada a los chicos.)"
    hide sara
    narrador "Algunos estudiantes escucharon esta conversación y empezaron a hablar en susurros entre ellos."
    david "(Los demás lo escucharon, no sé qué hacer. ¿Trato de calmarlos o no le doy mucha importancia?)"
    menu:
        'Hablar con los demás.':
            david "Tranquilos chicos, lo que Sara creyó haber visto es algo normal en lugares aislados, lo vi en una película, algo como... síndrome ártico... Cuanto más le demos importancia será peor."
            david "Si ven o escuchan cosas es por eso, no lo oculten a los demás. Estamos juntos en esto."
        'No darle importancia.':
            david "Seguro fue tu imaginación, Sara. Estas luces y sombras engañan fácil… No vale la pena preocuparse por eso."
            narrador "(los estudiantes siguieron hablando en susurros, su preocupación pareció aumentar.)"
    narrador "Luego de un rato, Chris vuelve y cuenta con detalle los lugares encontrados en la instalación."
    david "Gracias Chris por la información. Bueno, vamos a movernos al comedor, necesitamos un plan que nos ayude a sobrevivir con lo que tengamos." 
    jump ESCENA_11


# ESCENA 10 - INT. ÁRTICA-7 - MÚLTIPLES LOCACIONES - DÍA
label ESCENA_10:
    chris "Solamente vamos a entrar en habitaciones que tengan las puertas abiertas."
    hide chris_enojado
    hide chris
    scene fondo_pasillo_puerta_abierta
    pause
    show estudiante_masculino at right
    estudiante_6 "¡Aquí hay una puerta abierta! ¡Hay literas!"
    scene fondo literas with fade
    david "Contemos cuántas son."
    show estudiante_masculino at center
    estudiante_6 "¡Hay 8 literas, suficientes para todos!"
    hide estudiante_masculino
    show chris
    chris "Los colchones son viejos, tienen un poco de polvo. Bien, ya tenemos un lugar donde dormir, sigamos buscando."
    hide chris
    narrador "(algunos minutos después)"
    scene fondo pasillo with fade
    david "Perfecto, encontramos un lugar donde..." 
    scene fondo literas with fade
    david "dormir..." 
    scene fondo banos with fade
    david "baños..." 
    scene fondo invernadero with fade
    david "un invernadero..." 
    scene fondo pasillo_radio with fade
    david "y una radio, pero creo que no funciona... sigamos caminando tal vez encontremos algo de comida."
    scene fondo pasillo 
    show estudiante_masculino at right
    estudiante_3 "Quisiera descansar un poco..."
    show chris at left
    chris "Cuando encontremos que comer, vas a descansar."
    estudiante_3 "Está bien..."
    hide estudiante_masculino
    hide chris
    narrador "Los chicos siguieron avanzando hasta encontrar un comedor y una cocina, donde había un poco de suministros para mantenerse unos días."
    scene fondo comedor
    show chris at left
    chris "¡Genial! Es hora de volver, tenemos que avisarle a los demás."
    hide chris
    scene fondo artica7_interior with fade
    narrador "Al llegar con los demás chicos, Chris cuenta con detalle los lugares encontrados."
    david "Bueno, vamos a movernos al comedor, necesitamos un plan que nos ayude a sobrevivir con lo que tengamos."

# ESCENA 11 - INT. ÁRTICA-7 - COMEDOR COMÚN - tarde (HORAS DESPUÉS)
label ESCENA_11:
    scene fondo comedor with fade
    david "Esto son los lugares accesibles que tenemos por ahora, si queremos que esto funcione, tendremos que dividirnos en grupos."
    show chris
    chris "Yo puedo seguir explorando con mi grupo."
    hide chris
    show estudiante_masculino at right
    show estudiante_masculino_2 at left
    f"{estudiante_3} y {estudiante_6}" "Oh no..."
    hide estudiante_masculino
    hide estudiante_masculino_2
    david "Me parece bien, entonces los 6 que quedamos. Por mi parte, me encargaré de que todo esté bajo control, ustedes dos se encargarán del invernadero."
    show estudiante_femenino at right
    estudiante_1 "Haremos nuestro mayor esfuerzo."
    hide estudiante_femenino
    show estudiante_masculino at left
    estudiante_4 "No soy bueno con las plantas, pero lo intentaré."
    hide estudiante_masculino
    show sara at right
    sara "Me gustaría dedicarle tiempo a la radio... tengo algunas herramientas en mi mochila, tal vez pueda conseguir ayuda."
    show chris at left
    chris "Ese aparato viejo? jaja... Suerte con eso... jaja."
    david "Bien, te encargo la radio."
    hide chris
    hide sara
    david "Los que quedan ¿Podrían encargarse de los suministros?."
    show estudiante_femenino at left
    estudiante_2 "Claro, no hay problema."
    show estudiante_femenino_2 at right
    estudiante_5 "Nosotros nos encargamos."
    hide estudiante_femenino
    hide estudiante_femenino_2