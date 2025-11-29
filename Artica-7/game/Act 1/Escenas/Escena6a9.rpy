init python:
    from clases import GestorFinales
    
    gestor = GestorFinales()

label escena6a9:
    
    #escena 10
    scene fondo_sala_principal_puerta_abierta 
    stop music

    show estudiante_femenino at left
    with fade
    estudiante_1 "¿Qué es este lugar?"
    hide estudiante_femenino
    menu:
        "Parece ser una base militar.":
            show estudiante_femenino at left
            estudiante_1 "¿Por qué una base militar estaría abandonada?"
            hide estudiante_femenino
        "No logro ver nada.":
            pass

    play sfx3 "generador_enciende.mp3" volume 0.5
    queue sfx3 "generador_loop.ogg" loop
    show estudiante_masculino at left
    estudiante_4 "¿Qué fue eso?"
    hide estudiante_masculino
    pause
    show chris at parpadear("chris"), right
    chris "Suena como un generador."
    chris "Pero no entiendo por qué se enciende solo... eso no tiene sentido."
    hide chris
    show tutor
    tutor "Coincido. Los motores no 'despiertan' solos después de años congelados. Manténganse alerta. No toquen nada hasta que sepamos con qué estamos tratando."
    hide tutor

    show sara at parpadear("sara"), left
    sara "Hay polvo sobre las consolas... parece que lo abandonaron hace años."
    hide sara

    play sound "puerta_cierra.mp3" volume 2.0
    stop sfx1
    pause 1.0
    scene fondo artica7_interior 
    show tutor at left
    tutor "¡NOO! ¡Puta madre! ¡La puerta se cerró!"
    hide tutor
    with fade

    menu:                         
        "Tratar de detenerlo.":
            # ESCENA 10A
            david "¡Profesor, espere! ¡No creo que sea buena idea tocar esa puerta!"
            play sound "descarga_electrica.mp3"
            pause 0.5
            scene black with fade   
            play sound "caida_suelo.mp3"
            python:
                final = gestor.activar_final("final_alternativo")   
                resultado = gestor.obtener_resultado()
            scene black with fade

            centered "{size=40}[resultado]{/size}"

            pause 3.0
            jump creditos

        "No hacer nada.":
            # ESCENA 10B
            scene fondo_tutor_toca_puerta_2
            tutor "MIERDA, MIERDA, MIERDA, ¡¿QUÉ ESTÁ PASANDO?!"

    play sound "descarga_electrica.mp3"
    pause 0.5
    play sound "caida_suelo.mp3"
    # ESCENA 11
    scene fondo tutor_electrocutado_radio with fade
    play movie "images/fondo-tutor_electrocutado_radio.webm"

    scene fondo tutor_electrocutado_radio
   
    
    show estudiante_femenino at left
    pause 7
    play sound "Estudiante femenino gritando.mp3" 
    play music "suspenso alumnos solos.mp3" loop volume 0.2
    estudiante_2 "¡SEÑOR!"
    hide estudiante_femenino
    menu:
        "Tomar pulso del tutor.":
            #escena 11A
            scene fondo_tutor_pulso
            david "No... no respira. No tiene pulso."
            scene fondo tutor_electrocutado_radio with fade
        "No tocarlo, podría ser peligroso.":
            #escena 11B
            scene fondo tutor_electrocutado_quemado_radio with fade
            narrador "No hacía falta verificar su pulso, el olor a carne quemada que desprendía, provocaba que algunos alumnos les dieran nauseas."

    # ESCENA 11A/B
    play sound "radio interferencia.mp3"
    scene fondo sara_walkie-talkie with fade
    "Piloto" "¿Ho... hola? ¿Se escu... cha?"
    "Piloto" "¿Es... están to... dos bien?"
    if renpy.showing("fondo tutor_electrocutado_radio"):
        scene fondo tutor_electrocutado with fade
    else:
        scene fondo tutor_electrocutado_quemado with fade
    
    show sara gritando_walkie-talkie at left
    sara "¡Necesitamos ayuda! ¡Nuestro tutor acaba de morir por una descarga eléctrica!"
    "Piloto" "¡Tranquila, voy a intentar pedir ayuda!"
    hide sara gritando_walkie-talkie
    jump ESCENA_12

# Escena 12
label ESCENA_12:
    play sound "helicoptero despega.mp3" fadein 0.5
    scene fondo helicoptero_despega with fade
    piloto "No se preocupen. ¡Voy a buscar ayuda!"
    scene fondo helicoptero_volando_ventisca with fade
    play sound "helicoptero pierde control.mp3"
    piloto "¡NO! ¡La ventisca es muy fuerte! ¡¡Estoy perdiendo el control!!"
    scene fondo helicoptero_cae with fade
    play sound "helicoptero cae.mp3"
    pause
    scene fondo helicoptero_destrozado with fade
    play sound "helicoptero destrozado.mp3"
    pause
    jump ESCENA_13
    
# ESCENA 13
label ESCENA_13:
    play sound "estatica estrella_helicoptero.mp3" fadein 1.5
    scene fondo sara_retrocede with fade
    pause 1.5
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
    show chris_furioso at parpadear("chris_furioso"), center
    chris "¡Maldita sea! Se suponía que sería una excursión que me ayudaría con mis problemas, ¡PERO ESTO SOLO LO EMPEORA!"
    hide chris_furioso
    show estudiante_femenino at left
    estudiante_1 "¡Qué vamos a hacer!"
    hide estudiante_femenino
    show estudiante_masculino at right
    estudiante_3 "Quiero irme a casa."
    hide estudiante_masculino

    if tiene_celular:
        menu:
            "Usar el celular":
                david "Tranquilícense, por favor. Tomé mi celular al bajar del helicóptero y tiene señal. Podemos usar la función SOS para contactar al servicio de emergencias y pedir ayuda."
                scene fondo interior_artica_sos
                'Operador' "Puesto de comunicaciones de la Base Polar Orcadas, ¿Cuál es su emergencia?"
                david "Habla David… estamos en la base Ártica-7. ¡Necesitamos ayuda urgente!"
                david "Somos un grupo de estudiantes. Éramos nueve en total… y nos quedamos solos. Nuestro tutor y el piloto del helicóptero murieron."
                'Operador' "Entendido. ¿Hay heridos entre ustedes?"
                david "No hay heridos graves, pero estamos sin adultos atrapados aquí."
                'Operador' "Copiado. Quédense dentro de la base y aseguren puertas y suministros. El equipo más cercano está en ruta; intentaré establecer contacto regular con ustedes cada diez minutos."
                david "Gracias. Vamos a esperar las instrucciones."
                python:
                    final = gestor.activar_final("acto1_bueno")   
                    resultado = gestor.obtener_resultado()
                scene black with fade

                centered "{size=40}[resultado]{/size}"

                pause 3.0

                jump creditos
            'Calmarlos':
                pass

    david "Escuchen... escúchenme todos. Sé que esto es horrible. Lo peor que nos pudo haber pasado. Pero ahora mismo, en este momento, estamos vivos."
    show estudiante_femenino at left
    estudiante_5 "¡Estamos atrapados con un cadáver!"
    hide estudiante_femenino
    show chris_furioso at parpadear("chris_furioso"), center
    chris "¿Calmarnos? ¿Pensar? ¡Vamos a morir aquí!"
    hide chris_furioso
    
    david "Los entiendo, pero estando acá parados no vamos a solucionar nada. Deberíamos investigar la instalación, puede que encontremos algo que nos mantenga con vida mientras esperamos a que nos rescaten."
    show sara at right
    show sara at parpadear("sara"), right
    sara "Tienes razón, tal vez logremos encontrar algo para contactarnos con los de afuera."
    david "¡Exacto!"
    show chris at parpadear("chris"), left
    chris "Está bien. Espero que esto no sea una pérdida de tiempo... ¿Qué tienes en mente, héroe?"
    david "Primero, necesitamos un grupo que pueda explorar la instalación."
    hide chris
    hide sara
    menu:
        "Ir con Chris a explorar la base.":
            # ESCENA 9A - INT - ÁRTICA-7 - PASILLOS - DíA
            jump ESCENA_14
        "Quedarse ayudando a los demás.":  
            # Escena 9B - Interior - Ártica-7 - ENTRADA - DÍA
            jump ESCENA_13B

# Escena 13B
label ESCENA_13B:
    show sara at parpadear("sara"), right
    sara "Yo... yo puedo acompañarte para cuidarlos."
    david "Me vendría bien un poco de ayuda..."
    hide sara 
    show chris at parpadear("chris"), center
    chris "¿Qué pasa, héroe? pareces un tomate. "
    menu:
        'Cambiar de tema':
            # Escena 9BA - Interior - Ártica-7 - ENTRADA - DÍA
            david "¡¿Qué?! No nada, nada, no me pasa nada... ¿Puedes ir a investigar?"
            chris "¡Obvio, ya tenía pensado hacerlo!"    
            hide chris
            show estudiante_masculino at left
            estudiante_3 "Ya me encuentro mejor, puedo ir a investigar la zona."
            hide estudiante_masculino
            show estudiante_masculino at right
            estudiante_6 "Sí, yo también lo estoy."
            hide estudiante_masculino
            show chris at parpadear("chris"), center
            chris "Lo siento, pero no me gusta trabajar en equipo, me gusta estar solo."
            david "Vas a tener que trabajar con ellos Chris, no te queda de otra."
            chris "...Está bien, vamos, no me hagan perder el tiempo."
            hide chris
            menu:
                'Verificar los demás estén bien.':
                    david "¿Cómo se encuentran?"
                    show estudiante_femenino at center
                    estudiante_1 "No sé como sentirme... todo pasó tan rápido."
                    hide estudiante_femenino
                    show estudiante_masculino at center
                    estudiante_4 "Tengo miedo. ¿Y si no salimos de esta? ¿Y si hay alguien más dentro?"
                    hide estudiante_masculino
                    show estudiante_femenino_2 at center
                    estudiante_2 "No digas esas estupideces ¿Cómo puede haber alguien dentro de este lugar de mierda?"
                    hide estudiante_femenino_2
                    david "Hablaremos de esto cuando Chris encuentre un lugar donde podamos instalarnos."
                    david "No piensen en esas cosas, vamos a salir de esta."
                    narrador "Luego de un rato, Chris vuelve y cuenta con detalle los lugares encontrados en la instalación."
                    david "Gracias Chris por la información. Bueno, vamos a movernos al comedor, necesitamos un plan que nos ayude a sobrevivir con lo que tengamos."
                    jump ESCENA_16
                'Hablar con Sara.':
                    david "¿Estás bien, Sara? Te veo preocupada."
                    show sara at parpadear("sara"), center
                    sara "¿Eh? ¡Sí, sí, estoy bien!"
                    david "¿Estás segura? Puedes confiar en mí."
                    sara "Bueno... no quería alarmar a nadie, pero hace un momento me pareció ver... algo por el pasillo."
                    david "¿Algo? ¿A qué te refieres con algo?"
                    sara "Me pareció ver una... sombra. Todos estábamos juntos, no pudo haber sido alguien de nosotros."
                    david "(Puede que tenga razón, espero que no le pase nada a los chicos.)"
                    hide sara
                    play sound "alumnos susurrando.mp3"
                    david "(Los demás lo escucharon, no sé qué hacer. ¿Trato de calmarlos o no le doy mucha importancia?)"
                    menu:
                        'Hablar con los demás.':
                            stop sound fadeout 1.0
                            david "Tranquilos, lo que Sara creyó haber visto es algo normal en lugares aislados, lo vi en una película, algo como... síndrome ártico... Cuanto más le demos importancia será peor."
                            david "Si ven o escuchan cosas, no lo oculten a los demás. Estamos juntos en esto."
                            narrador "Ante estas palabras los estudiantes parecieron tranquilizarse un poco."
                        'No darle importancia.':
                            david "Seguro fue tú imaginación, Sara. Estas luces y sombras engañan fácil… No vale la pena preocuparse por eso."
                    narrador "Luego de un rato, Chris vuelve y cuenta con detalle los lugares encontrados en la instalación."
                    stop sound fadeout 1.0
                    david "Gracias Chris por la información. Bueno, vamos a movernos al comedor, necesitamos un plan que nos ayude a sobrevivir con lo que tengamos."
                    jump ESCENA_16

# Escena 14
label ESCENA_14:
    play sound "caminan.mp3"
    pause 2
    stop sound
    scene fondo pasillo with fade
    david "Vamos por este pasillo, parece llevar hacia el centro de la base."
    scene fondo_pasillo_estudiante_toca_puerta
    pause
    show chris_enojado at parpadear("chris_enojado"), left
    chris "¡No la toques! ¿¡Quieres terminar como nuestro tutor?! ¡¡¿FRITO?!!."
    scene fondo pasillo with fade
    show chris_enojado at parpadear("chris_enojado"), left
    show estudiante_masculino at right
    estudiante_3 "Lo siento, no volverá a pasar..."
    hide estudiante_masculino
    hide chris_enojado
    menu:
        'Intervenir.':
            $ moral -= 1
            david "No deberías de tratar así a las personas y menos en estos momentos."
            show chris_enojado at parpadear("chris_enojado"), center
            chris "No te metas donde no te incumbe."
        'Tranquilizar.':
            $ moral += 1
            david "Chris, tranquilo hermano, vamos a tomarnos esto con más calma, no sabemos cuánto tiempo vamos a estar acá."
            show chris at parpadear("chris"), center
            chris "Lo siento, no estoy en mi mejor momento..."
        'Ignorarlo.':
            pass
    chris "Solamente vamos a entrar en habitaciones que tengan las puertas abiertas."
    hide chris_enojado
    hide chris
    play sound "caminan.mp3"
    pause 2
    stop sound # para  caminan.mp3
    scene fondo_pasillo_puerta_abierta with fade
    pause 0.2
    show estudiante_masculino at right
    estudiante_6 "¡Aquí hay una puerta abierta! ¡Hay literas!"
    scene fondo literas with fade
    david "Contemos cuántas son."
    show estudiante_masculino at center
    estudiante_6 "¡Hay 8 literas, suficientes para todos!"
    hide estudiante_masculino
    show chris at parpadear("chris"), center
    chris "Los colchones son viejos, tienen un poco de polvo. Bien, ya tenemos un lugar donde dormir, sigamos buscando."
    hide chris
    narrador "(algunos minutos después)"
    scene fondo pasillo with fade
    david "Perfecto, encontramos un lugar donde..." 
    scene fondo literas with fade
    david "...dormir..." 
    scene fondo banos with fade
    david "...baños en casi buen estado..." 
    scene fondo invernadero with fade
    david "...un invernadero que podremos usar..." 
    scene fondo pasillo_radio with fade
    david "...y una radio, pero creo que no funciona... sigamos caminando tal vez encontremos algo de comida."
    scene fondo pasillo 
    show estudiante_masculino at right
    estudiante_3 "Quisiera descansar un poco..."
    show chris at parpadear("chris"), left
    chris "Cuando encontremos qué comer, vas a descansar."
    estudiante_3 "Está bien..."
    hide estudiante_masculino
    hide chris
    play sound "caminan.mp3"
    pause 2
    stop sound
    scene fondo comedor with fade
    show chris_enojado at parpadear("chris_enojado"), center
    chris "¡Genial! Tenemos camas sucias, algunas latas de comida están podridas y esta radio de porquería no parece que vaya a funcionar."
    hide chris_enojado
    david "Al menos tenemos comida y camas... eso nos compra tiempo. Es mejor que nada."
    david "Volvamos, los demás deben estar perdiendo la cabeza con el tutor a su lado, hay que darles las 'buenas' noticias."
    play sound "caminan.mp3"
    pause 2
    stop sound
    scene fondo tutor_electrocutado with fade
    jump ESCENA_15
    
label ESCENA_15:
    narrador "Al llegar con los demás chicos, Chris cuenta con detalle los lugares encontrados."
    david "Bueno, vamos a movernos al comedor, necesitamos un plan que nos ayude a sobrevivir con lo que tengamos."
    play sound "caminan.mp3"
    pause 2
    stop sound # para  caminan.mp3
    jump ESCENA_16

# ESCENA 16
label ESCENA_16:
    stop sound
    scene fondo comedor with fade
    play sound "estudiantes hablando.mp3" volume 0.3 loop
    david "Chicos hagan silencio y escúchenme."
    stop sound fadeout 2.0
    david "Estos son los lugares accesibles que tenemos por ahora, si queremos que esto funcione, tendremos que dividirnos en grupos."
    show chris at parpadear("chris"), center
    chris "Yo puedo seguir explorando con mi grupo."
    hide chris
    show estudiante_masculino at right
    show estudiante_masculino_2 at left
    f"{estudiante_3} y {estudiante_6}" "Oh, no..."
    hide estudiante_masculino
    hide estudiante_masculino_2
    david "Me parece bien, entonces los 6 que quedamos. Por mi parte, me encargaré de que todo esté bajo control, ustedes dos se encargarán del invernadero."
    show estudiante_femenino at right
    estudiante_1 "Haremos nuestro mayor esfuerzo."
    hide estudiante_femenino
    show estudiante_masculino at left
    estudiante_4 "No soy bueno con las plantas, pero lo intentaré."
    hide estudiante_masculino
    show sara at parpadear("sara"), right
    sara "Me gustaría dedicarle tiempo a la radio... tengo algunas herramientas en mi mochila, tal vez pueda conseguir ayuda."
    show chris at parpadear("chris"), left
    chris "¿Ese aparato viejo? Suerte con eso..."
    david "Bien, te encargo la radio. Los que quedan ¿Podrían encargarse de los suministros?"
    hide chris
    hide sara
    show estudiante_femenino at left
    estudiante_2 "Claro, no hay problema."
    hide estudiante_femenino
    show estudiante_femenino_2 at right
    estudiante_5 "Nosotros nos encargaremos."
    hide estudiante_femenino_2