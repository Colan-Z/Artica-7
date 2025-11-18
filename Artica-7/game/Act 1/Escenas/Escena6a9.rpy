label escena6a9:
    
    # ESCENA 6 - INT. ÁRTICA-7 - ENTRADA - DÍA
    scene fondo artica7_interior with fade
    stop music

    play sound "generador_enciende.mp3" volume 0.5

    show estudiante_femenino at left
    estudiante_1 "¿Qué es este lugar?"
    hide estudiante_femenino
    
    narrador "De repente se escucha el sonido de un generador funcionando, luces fluorescentes parpadean débilmente en el techo."
    narrador "Se encienden completamente, iluminando un pasillo largo con paredes de concreto y cables expuestos en el techo."
    narrador "El grupo mira alrededor. El lugar parece abandonado hace años. Hay polvo sobre las consolas."
    
    play sound "puerta_cierra.mp3" volume 2.0
    narrador "La puerta se cierra detrás de ellos con un golpe metálico definitivo."

    narrador "Mientras el tutor corría desesperado hacia la puerta, un walkie-talkie cae de su bolsillo."

    menu:                         
        "Tratar de detenerlo":
            # ESCENA 6-A - INT. ÁRTICA-7 - ENTRADA - DÍA
            david "¡Profesor, espere! ¡No creo que sea buena idea tocar esa puerta!"
            narrador "El tutor ignoró a David, su desesperación lo habia ensordecido"  
        "No hacer nada.":
            # ESCENA 6-B - INT. ÁRTICA-7 - ENTRADA - DÍA
            show tutor at center with hpunch
            tutor "NO, NO, NO, NO, ESPERA, ESPERA, ESPERA, ¡¿QUE ESTA PASANDO?!"

    play sound "descarga_electrica.mp3"
    show tutor at center with hpunch
    pause 0.5
    hide tutor

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
            david "No... no respira. No tiene pulso."
            $ humo = 0
        "No tocarlo, podría ser peligroso.":
            # ESCENA 7-B - INT. ÁRTICA-7 - TUTOR ELECTROCUTADO CON HUMO - DÍA
            scene fondo tutor_electrocutado_quemado_radio with fade
            narrador "No hacia falta verificar su pulso, el olor a carne quemada que desprendía, provocaba que algunos alumnos les dieran nauseas."
            $ humo = 1

    # ESCENA 7AB - INT. ÁRTICA-7 - TUTOR ELECTROCUTADO - DÍA
    if humo == 0:
        scene fondo tutor_electrocutado with fade
    else:
        scene fondo tutor_electrocutado_quemado with fade
    play sound "radio interferencia.mp3"
    "Piloto" "¿Ho... hola? ¿Se escu... cha?"
    "Piloto" "¿Es... están to... dos bien?"
    show sara at left
    sara "¡Necesitamos ayuda! ¡Nuestro tutor acaba de morir por una descarga eléctrica!"
    "Piloto" "¡Tranquila, voy a intentar pedir ayuda!"
    hide sara
    jump ESCENA_8

# ESCENA 8 - EXT. ÁRTICA-7 - HELICOPTERO - DESPEGA - DÍA
label ESCENA_8:
    play sound "helicoptero despega.mp3" fadein 0.5
    scene fondo helicoptero_despega with fade
    narrador "El piloto enciende el helicóptero y procede a despegar."
    scene fondo helicoptero_volando_ventisca with fade
    play sound "helicoptero pierde control.mp3"
    narrador "Al elevarse, pierde el control." 
    scene fondo helicoptero_cae with fade
    play sound "helicoptero cae.mp3"
    narrador "La ventisca era muy fuerte."
    scene fondo helicoptero_destrozado with fade
    play sound "helicoptero destrozado.mp3"
    narrador "Por lo que termina estrellándose, dejando a los chicos a su suerte, dejando únicamente el ruido de la estática."
    jump ESCENA_9
    
# ESCENA 9 - INt. ÁRTICA - ENTRADA
label ESCENA_9:
    play sound "estatica estrella_helicoptero.mp3"
    scene fondo tutor_electrocutado with fade
    play music "suspenso alumnos solos.mp3" loop volume 0.1
    show chris_enojado at left
    chris "¡No! ¡Esto no puede estar pasando!"  
    hide chris_enojado
    show estudiante_masculino at right
    estudiante_3 "¡Tenemos que salir de aquí! ¡YA!"
    hide estudiante_masculino
    show estudiante_femenino at center
    estudiante_4 "¡Vamos a morir aquí!"
    hide estudiante_femenino
    show chris_furioso at left
    chris "¡Maldita sea! Se suponía que sería una excursión que me ayudaría con mis problemas, ¡PERO ESTO SOLO LO EMPEORA!"
    hide chris_furioso
    show estudiante_femenino at left
    estudiante_1 "¡Qué vamos a hacer!"
    hide estudiante_femenino
    show estudiante_masculino at right
    estudiante_3 "Quiero irme a casa."
    hide estudiante_masculino
    david "Escuchen... escúchenme todos. Sé que esto es horrible. Lo peor que nos pudo haber pasado. Pero ahora mismo, en este momento, estamos vivos."
    show estudiante_masculino at left
    estudiante_5 "¡Estamos atrapados con un cadáver!"
    hide estudiante_masculino
    show chris_enojado at right
    chris "¿Calmarnos? ¿Pensar? ¡Vamos a morir aquí!"
    hide chris_enojado
    
    david "Los entiendo, pero estando acá parados no vamos a solucionar nada. Deberíamos de investigar la instalación, puede que encontremos algo que nos mantenga con vida mientras esperamos a que nos rescaten."
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
    narrador "(Un estudiante intenta tocar una puerta)"
    show chris_enojado at right
    chris "¡No la toques! ¿¡Quieres terminar como nuestro tutor?! ¡¡¿FRITO?!!."
    show estudiante_femenino at left
    estudiante_5 "Lo siento, no volverá a pasar..."
    hide estudiante_femenino
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
    show chris at right
    chris "Que pasa héroe? pareces un tomate? jajaj"
    menu:
        'Cambiar de tema':
            # Escena 9BA - Interior - Ártica-7 - ENTRADA - DÍA
            jump ESCENA_9BA


# Escena 9AA - Int. Ártica-7 - Pasillos - Día
label ESCENA_9AA:
    david "No deberías de tratar así a las personas y menos en estos momentos."
    show chris_enojado at right
    chris "No te metas donde no te incumbe."
    jump ESCENA_10

# Escena 9AB - INT. ÁRTICA-7 (PASILLOS) - DÍA
label ESCENA_9AB:
    david "Chris, tranquilo hermano, vamos a tomarnos esto con mas calma, no sabemos cuanto tiempo vamos a estar acá."
    show chris at right
    chris "Lo siento, no estoy en mi mejor momento..."
    jump ESCENA_10

label ESCENA_9BA:
    david "¡¿Qué?! No nada, nada, no me pasa nada... puedes ir a investigar?"
    chris "¡Obvio, ya tenía pensado hacerlo!"    
    hide chris
    show estudiante_femenino at left
    estudiante_3 "Ya me encuentro mejor, puedo ir a investigar la zona."
    hide estudiante_femenino
    show estudiante_masculino at right
    estudiante_6 "Si, yo también lo estoy."
    hide estudiante_masculino
    show chris at right
    chris "Lo siento, pero no me gusta trabajar en equipo, me gusta estar solo."
    david "Vas a tener que trabajar con ellos Chris, no te queda de otra."
    chris "...Está bien, vamos, no me hagan perder el tiempo."
    hide chris
    narrador "David ve a Sara preocupada. Se acerca a preguntarle qué le pasa."
    david "¿Estás bien, Sara? Te veo preocupada."
    show sara at right
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
    show estudiante_masculino at right
    estudiante_6 "¡Aquí hay una puerta abierta! ¡Hay literas!"
    david "Contemos cuántas son."
    estudiante_6 "¡Hay 8 literas, suficientes para todos!"
    hide estudiante_masculino
    show chris at right
    chris "Los colchones son viejos, tienen un poco de polvo. Bien, ya tenemos un lugar donde dormir, sigamos buscando."
    hide chris
    narrador "(algunos minutos después)"
    david "Perfecto, encontramos un lugar donde dormir, baños, un invernadero y una radio, pero creo que no funciona... sigamos caminando tal vez encontremos algo de comida."
    show estudiante_femenino at right
    estudiante_3 "Quisiera descansar un poco..."
    show chris at left
    chris "Cuando encontremos que comer, vas a descansar."
    estudiante_3 "Está bien..."
    hide estudiante_femenino
    hide chris
    narrador "Los chicos siguieron avanzando hasta encontrar un comedor y una cocina, donde había un poco de suministros para mantenerse unos días."
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
    show chris at left
    chris "Yo puedo seguir explorando con mi grupo."
    hide chris
    show estudiante_femenino at right
    show estudiante_masculino at left
    f"{estudiante_3} y {estudiante_4}" "Oh no..."
    hide estudiante_femenino
    hide estudiante_masculino
    david "Me parece bien, entonces los 6 que quedamos. Por mi parte, me encargaré de que todo esté bajo control, ustedes dos se encargarán del invernadero."
    show estudiante_masculino at right
    estudiante_1 "Haremos nuestro mayor esfuerzo."
    hide estudiante_masculino
    show estudiante_femenino at left
    estudiante_4 "No soy bueno con las plantas, pero lo intentaré."
    hide estudiante_femenino
    show sara at left
    sara "Me gustaría dedicarle tiempo a la radio... tengo algunas herramientas en mi mochila, tal vez pueda conseguir ayuda."
    hide sara
    show chris at right
    chris "Ese aparato viejo? jaja... Suerte con eso... jaja."
    hide chris

    david "Bien, te encargo la radio. Los que quedan ¿Podrían encargarse de los suministros?."
    show estudiante_femenino at left
    estudiante_2 "Claro, no hay problema."
    show estudiante_masculino at right
    estudiante_5 "Nosotros nos encargamos."
    hide estudiante_femenino
    hide estudiante_masculino