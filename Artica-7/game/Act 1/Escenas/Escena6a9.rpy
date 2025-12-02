init python:
    from clases import GestorFinales
    
    gestor = GestorFinales()

label escena6a9:
    
    #escena 10
    play sfx1 "ventisca.mp3" loop volume 0.2
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
    pause
    show estudiante_masculino at left
    estudiante_4 "¿Qué fue eso?"
    hide estudiante_masculino
    show chris at parpadear("chris"), right
    chris "Suena como un generador."
    chris "Pero no entiendo por qué se enciende solo... no tiene sentido."
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
    with fade
    tutor "¡No! ¡Puta madre! ¡La puerta se cerró!"
    stop sound
    scene fondo artica7_interior_tutor_corriendo with fade
    play sound "Corren.mp3" volume 0.3
    hide tutor

    menu:                    
        "Tratar de detenerlo.":
            # ESCENA 10A
            david "¡Profesor, espere! ¡No creo que sea buena idea tocar esa puerta!"
            stop sound
            scene fondo_tutor_toca_puerta_david
            play sound "descarga_electrica.mp3"
            pause 0.5
            scene black with fade   
            play sound "caida_suelo.mp3"

            stop music
            stop sfx3
            play sound "final_malo.mp3"
            python:
                final = gestor.activar_final("acto1_final_malo")   
                resultado = gestor.obtener_resultado()
            scene black with fade

            centered "{size=40}[resultado]{/size}"

            pause 3.0
            jump creditos

        "No hacer nada.":
            # ESCENA 10B
            tutor "MIERDA, MIERDA, MIERDA, ¡¿QUÉ ESTÁ PASANDO?!"
            stop sound
            scene fondo_tutor_toca_puerta_2

    play sound "descarga_electrica.mp3"
    pause 0.5
    play sound "caida_suelo.mp3"
    # ESCENA 11
    scene fondo tutor_electrocutado_radio with fade
    play movie "images/fondo-tutor_electrocutado_radio.webm"

    scene fondo tutor_electrocutado_radio
   
    
    show estudiante_femenino at left
    pause 1.5
    play sound "Estudiante femenino gritando.mp3" 
    play music "suspenso alumnos solos.mp3" loop volume 0.2
    estudiante_1 "¡SEÑOR!"
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
            narrador "No hacía falta verificar su pulso; el olor a carne quemada que desprendía provocaba que algunos alumnos les dieran náuseas."

    # ESCENA 11A/B
    play sound "radio interferencia.mp3" loop volume 0.2
    pause
    if renpy.showing("fondo tutor_electrocutado_radio"):
        scene fondo sara_walkie-talkie_sin_humo
    else:
        scene fondo sara_walkie-talkie
    piloto "¿Hola? ¿Me copia alguien?"
    piloto "Reporten estado. ¿Todos en condiciones?"
    if renpy.showing("fondo sara_walkie-talkie_sin_humo"):
        scene fondo tutor_electrocutado
    else:
        scene fondo tutor_electrocutado_quemado
    
    show sara gritando_walkie-talkie1 at parpadear("sara gritando_walkie-talkie1"),  right
    with fade
    sara "¡Necesitamos ayuda! ¡Nuestro tutor acaba de morir por una descarga eléctrica!"
    piloto "Mantengan la calma, solicitaré apoyo inmediato."
    hide sara gritando_walkie-talkie
    jump ESCENA_12

# Escena 12
label ESCENA_12:
    stop sfx3
    play sound "helicoptero despega.mp3" volume 0.3
    scene fondo helicoptero_despega with fade
    
    # Marcar que AFM temporal está activo
    # $ afm_temporal_activo = True
    # $ _preferences.afm_enable = True
    # $ _preferences.afm_time = 7
    
    piloto "No se muevan. Iré a buscar ayuda."
    
    scene fondo helicoptero_volando_ventisca with fade
    play sound "helicoptero pierde control.mp3" volume 0.3
    
    # $ _preferences.afm_time = 5
    piloto "¡Imposible! ¡La ventisca es demasiado intensa, no puedo estabilizarlo!"
    
    # window hide
    scene fondo helicoptero_cae with fade
    play sound "helicoptero cae.mp3" volume 0.3
    pause 2.0
    # invisible ""
    
    scene fondo helicoptero_destrozado with fade
    play sound "helicoptero destrozado.mp3" volume 0.3
    pause 2.0
    # invisible ""
    # pause 1.0
    
    # Desactivar y limpiar flag
    # $ del afm_temporal_activo
    # $ _preferences.afm_enable = False
    # $ renpy.restart_interaction()
    
    jump ESCENA_13
    
# ESCENA 13
label ESCENA_13:
    # window hide
    play sfx3 "generador_loop.ogg" loop
    play sound "estatica estrella_helicoptero.mp3" fadein 1.5
    scene fondo sara_retrocede with fade
    pause 2.0
    
    # $ afm_temporal_activo = True
    # $ _preferences.afm_enable = True
    # $ _preferences.afm_time = 8
    # invisible ""
    # $ del afm_temporal_activo
    # $ _preferences.afm_enable = False
    # $ renpy.restart_interaction()
    
    play sound "golpe pared.mp3" volume 5.0
    scene fondo chris_golpea_pared with fade
    # invisible ""
    # window auto
    
    chris "¡No! ¡Esto no puede estar pasando!"
    scene fondo tutor_electrocutado 
    hide chris_enojado
    show estudiante_masculino_2 at right
    with fade
    estudiante_3 "¡Tenemos que salir de aquí! ¡YA!"
    hide estudiante_masculino_2
    show estudiante_masculino at left
    estudiante_4 "¡Vamos a morir aquí!"
    hide estudiante_masculino
    show chris_enojado at parpadear("chris_enojado"), center
    chris "¡Maldita sea! Se suponía que sería una excursión que me ayudaría con mis problemas."
    hide chris_enojado
    show chris_furioso at parpadear("chris_furioso"), center
    chris "¡PERO ESTO SOLO LO EMPEORA!"
    hide chris_furioso
    show estudiante_femenino at left
    estudiante_1 "¡Qué vamos a hacer!"
    hide estudiante_femenino
    show estudiante_masculino_2 at right
    estudiante_3 "Quiero irme a casa."
    hide estudiante_masculino_2

    $ salir_del_bucle = True
    while salir_del_bucle:
        menu:
            "Usar el celular" if tiene_celular:
                david "Cálmense todos. Antes al bajar del helicóptero tomé mi celular en caso de que algo pasara."
                david "Acá dentro hay algo de señal; voy a hacer una llamada de SOS para pedir ayuda. Espero que funcione..."
                scene fondo tutor_electrocutado_pov_celular
                play sound "sos.ogg" volume 0.5
                pause 1.0
                play sound "llamando celular.mp3" volume 0.5
                pause 2.0
                scene fondo tutor_electrocutado
                'Operador' "Aquí base Orcadas. ¿Cuál es su emergencia?"
                david "Hola, me llamo David. Somos los estudiantes que iban a una expedición en Orcadas. Tuvimos un problema con una ventisca, así que decidimos refugiarnos en una instalación llamada Ártica-7."
                'Operador' "¿Ártica-7? No conozco nada con ese nombre... Tal vez pueda localizar tu llamada."
                david "Puede que vean humo en el cielo, el helicóptero que nos llevaba se estrelló."
                'Operador' "Eso puede servirnos, estamos preparando el equipo de rescate. Manténganse ahí, llegaremos lo antes posible."
                stop music
                stop sfx3
                play sound "final_bueno.mp3" volume 0.5
                python:
                    final = gestor.activar_final("acto1_final_bueno")   
                    resultado = gestor.obtener_resultado()
                scene black with fade
                centered "{size=40}[resultado]{/size}"
                pause 3.0
                jump creditos

            '{color=#FE0000}Usar el celular.{/color}' if not tiene_celular:
                pass

            'Calmarlos':
                $ salir_del_bucle = False

    david "Escuchen... escúchenme todos. Sé que esto es horrible. Lo peor que nos pudo haber pasado. Pero ahora mismo, en este momento, estamos vivos."
    show estudiante_femenino_3 at left
    estudiante_5 "¡Estamos atrapados con un cadáver!"
    hide estudiante_femenino_3
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
            david "Chris, ¿Puedes ir a explorar? Yo puedo acompañarte."
            show estudiante_masculino_2 at left
            estudiante_3 "¿Yo también puedo ir? Ya me encuentro mejor."
            hide estudiante_masculino_2
            show estudiante_masculino_3 at right
            estudiante_6 "A mi también me gustaría ir con ustedes."
            hide estudiante_masculino_3
            show chris at parpadear("chris"), center
            chris "David y yo ya somos suficientes."
            david "Claro, pueden venir con nosotros."
            chris "..."
            hide chris
            $ir_con_chris = True    
            # ESCENA 9A - INT - ÁRTICA-7 - PASILLOS - DíA
            jump ESCENA_14
        "Quedarse con los demás.": 
            # Escena 9B - Interior - Ártica-7 - ENTRADA - DÍA
            jump ESCENA_13B

# Escena 13B
label ESCENA_13B:
    show sara_timida at parpadear("sara_timida"), right
    sara "Yo... yo puedo acompañarte para cuidarlos."
    david "Me vendría bien un poco de ayuda..."
    hide sara_timida 
    show chris_sonrisa at parpadear("chris_sonrisa"), center
    chris "¿Qué pasa, héroe? Pareces un tomate. "
    menu:
        'Después te cuento.':
            show borde_verde at borde_top_simple
            $ moral += 1
            chris "Eso espero, amigo."
        'Cambiar de tema.':
            show borde_rojo at borde_top_simple
            $ moral -= 1
            hide chris_sonrisa
            show chris at parpadear("chris"), center
            david "¡¿Qué?! No, nada... no me pasa nada..."
    # Escena 9BA - Interior - Ártica-7 - ENTRADA - DÍA
    david "¿Puedes ir a investigar?"
    hide chris_sonrisa
    hide chris
    show chris_orgulloso at parpadear("chris_orgulloso"), center
    chris "¡Obvio, ya tenía pensado hacerlo!"
    hide chris_orgulloso
    hide chris
    show estudiante_masculino_2 at left
    estudiante_3 "Ya me encuentro mejor, puedo ir a investigar la zona."
    hide estudiante_masculino_2
    show estudiante_masculino_3 at right
    estudiante_6 "Sí, yo también lo estoy."
    hide estudiante_masculino_3
    show chris_enojado at parpadear("chris_enojado"), center
    chris "Lo siento, pero no me gusta trabajar en equipo, me gusta estar solo."
    david "Vas a tener que trabajar con ellos Chris, no te queda de otra."
    # Aca chris podria empezar a enojarse un poco con 
    # como le habla david pero aceptar igual (un gruñido o algo por el estilo)
    # agregar sprite de chris (un poco) enojado
    chris "...Está bien, vamos, no me hagan perder el tiempo."
    hide chris_enojado
    menu:
        'Verificar que los demás estén bien.':
            $ir_con_chris = True 
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
            david "No piensen en esas cosas, vamos a salir de esta."
            david "Hablaremos de esto cuando Chris encuentre un lugar donde podamos instalarnos."
            # narrador "Luego de un rato, Chris vuelve y cuenta con detalle los lugares encontrados en la instalación."
            scene black
            centered "{size=40}Chris regresa de la exploración y le cuenta a David lo que encontraron.{/size}"
            with fade
            scene fondo tutor_electrocutado
            # david "Gracias Chris por la información. Bueno, vamos a movernos al comedor, necesitamos un plan que nos ayude a sobrevivir con lo que tengamos."
            # david "Gracias Chris por la información. Vamos al comedor, necesitamos un plan que nos ayude a sobrevivir con lo que tengamos."
            jump ESCENA_15
        'Hablar con Sara.':
            $ir_con_chris = False 
            show sara_preocupada at parpadear("sara_preocupada"), center
            pause
            david "¿Estás bien, Sara? Te veo preocupada."
            hide sara_preocupada
            show sara_timida at parpadear("sara_timida"), center
            sara "¿Eh? ¡Sí, sí, estoy bien!"
            david "¿Estás segura? Puedes confiar en mí."
            sara "Bueno... no quería alarmar a nadie, pero hace un momento me pareció ver... algo por el pasillo."
            david "¿Algo? ¿A qué te refieres con algo?"
            sara "Me pareció ver una... sombra. Todos estábamos juntos, no pudo haber sido alguien de nosotros."
            david "¿Una sombra?"
            sara "Sí... no sé qué era, pero me asusté y retrocedí."
            hide sara_timida at parpadear("sara_timida")
            play sound "alumnos susurrando.mp3"
            david "(Los demás lo escucharon, no sé qué hacer.)"
            david "Hablaremos de eso más tarde, ahora esperemos a Chris y los demás para organizarnos."
            # david "(Puede que tenga razón, espero que no le pase nada a los chicos.)"
            hide sara
            stop sound fadeout 1.0
            pause
            # david "(Los demás lo escucharon, no sé qué hacer. ¿Trato de calmarlos o no le doy mucha importancia?)"
            
            # Poner este texto en pantalla con fondo negro
            # narrador "Luego de un rato, Chris vuelve y cuenta con detalle los lugares encontrados en la instalación."
            scene black
            centered "{size=40}Chris regresa de la exploración y le cuenta a David lo que encontraron.{/size}"
            with fade
            scene fondo tutor_electrocutado
            # david "Gracias Chris por la información. Bueno, vamos a movernos al comedor, necesitamos un plan que nos ayude a sobrevivir con lo que tengamos."
            # david "Vamos al comedor, necesitamos un plan que nos ayude a sobrevivir con lo que tengamos."
            jump ESCENA_15

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
    chris "¡No la toques! ¿¡Quieres terminar como nuestro tutor!? ¡¿FRITO?!"
    scene fondo pasillo 
    show chris_enojado at parpadear("chris_enojado"), left
    show estudiante_masculino_2 at right
    with fade
    estudiante_3 "Lo siento, no volverá a pasar..."
    hide estudiante_masculino_2
    hide chris_enojado
    menu:
        'Intervenir.':
            show borde_rojo at borde_top_simple
            $ moral -= 1
            david "No deberías de tratar así a las personas y menos en estos momentos."
            show chris_enojado at parpadear("chris_enojado"), center
            chris "No te metas donde no te incumbe."
        'Tranquilizar.':
            show borde_verde at borde_top_simple
            $ moral += 1
            david "Chris, tranquilo hermano, vamos a tomarnos esto con más calma, no sabemos cuánto tiempo vamos a estar acá."
            show chris at parpadear("chris"), center
            chris "Lo siento, no estoy en mi mejor momento..."
        'Ignorarlo.':
            pass
    chris "Solamente vamos a entrar en habitaciones que tengan las puertas abiertas."
    hide chris_enojado
    hide chris
    show fondo pasillo at yshake
    play sound "caminan.mp3"
    pause 2
    stop sound # para  caminan.mp3
    scene fondo_pasillo_puerta_abierta with fade
    pause 0.2
    show estudiante_masculino_3 at right
    estudiante_6 "¡Aquí hay una puerta abierta! ¡Hay literas!"
    scene fondo literas with fade
    david "Contemos cuántas son."
    show estudiante_masculino_3 at center
    estudiante_6 "¡Hay ocho literas, suficientes para todos!"
    hide estudiante_masculino_3
    show chris at parpadear("chris"), center
    chris "Los colchones son viejos y tienen polvo. Bueno... ya tenemos un lugar donde dormir, sigamos buscando."
    hide chris
    scene black 
    centered "{size=40}Algunos minutos después...{/size}"
    with fade
    scene fondo pasillo
    # david "Perfecto, encontramos un lugar donde..." 
    # scene fondo literas with fade
    # david "...dormir..." 
    # scene fondo banos with fade
    # david "...baños en casi buen estado..." 
    # scene fondo invernadero with fade
    # david "...un invernadero que podremos usar..." 
    show chris_radio at parpadear("chris_radio"), left
    chris "¡Miren! Encontré una {sc=4}{color=#008000}radio{/color}{/sc}... Tal vez podamos pedir ayuda."
    hide chris_radio
    scene fondo pasillo_radio
    david "Genial, déjame verla."
    david "Bien, después veremos si funciona..."
    scene fondo pasillo 
    show chris at parpadear("chris"), left
    chris "Sigamos caminando tal vez encontremos algo de comida."
    hide chris
    show estudiante_masculino_2 at right
    with fade
    estudiante_3 "Quisiera descansar un poco..."
    show chris at parpadear("chris"), left
    chris "Cuando encontremos qué comer, vas a descansar."
    estudiante_3 "Está bien..."
    hide estudiante_masculino_2
    hide chris
    scene fondo pasillo at yshake
    play sound "caminan.mp3"
    pause 2
    stop sound
    scene fondo comedor
    with fade
    show chris_enojado at parpadear("chris_enojado"), center
    chris "¡Genial! Tenemos camas sucias, algunas latas de comida están podridas y esta radio de porquería no parece que vaya a funcionar."
    hide chris_enojado
    david "Al menos tenemos comida y camas... eso nos compra tiempo. Es mejor que nada."
    # Agregar mas molestia creciente de chris con david
    david "Volvamos, los demás deben estar perdiendo la cabeza con el tutor a su lado, hay que darles las 'buenas' noticias."
    hide chris_enojado
    scene fondo comedor at yshake
    play sound "caminan.mp3"
    pause 2
    stop sound
    jump ESCENA_15
    
label ESCENA_15:
    # Reemplazar esto por texto en pantalla
    # narrador "Al llegar con los demás chicos, Chris cuenta con detalle los lugares encontrados."
    # poner sprites de algunos estudiantes escuchando a chris
    scene fondo tutor_electrocutado 
    show sara at right
    show chris at left
    show estudiante_femenino_2:
        xpos -300
        ypos -400
    show estudiante_masculino_2:
        xpos 1200
        ypos -400  
    with fade
    david "Gracias Chris. Bueno, vamos a movernos al comedor, necesitamos un plan que nos ayude a sobrevivir con lo que tengamos."
    hide sara
    hide chris
    hide estudiante_femenino_2
    hide estudiante_masculino_2
    scene fondo pasillo at yshake with fade
    play sound "caminan.mp3"
    pause 2
    jump ESCENA_16

# ESCENA 16
label ESCENA_16:
    stop sound
    scene fondo comedor_estudiantes_sentados with fade
    play sound "estudiantes hablando.mp3" volume 0.3 loop
    # Poner estudiantes en las sillas (chris y sara pueden 
    # estar parados a su lado aunque no se vean)
    david "Chicos, hagan silencio y escuchen."
    stop sound fadeout 2.0
    menu:
        # "Dividirse en grupos de trabajo.":
        #     jump ESCENA_17A
        # "Quedarse todos juntos.":
        #     jump ESCENA_17B
        "Contar lo que encontraron.":
            show borde_rojo at borde_top_simple
            $ moral -= 1
            david "Perfecto, encontramos un lugar donde..." 
            scene fondo literas with fade
            david "...dormir..." 
            scene fondo banos with fade
            david "...baños en casi buen estado..." 
            scene fondo invernadero with fade
            david "...un invernadero que podremos usar..."
        "Dejar que Chris hable.":
            show borde_verde at borde_top_simple
            $ moral += 1
            show chris_orgulloso at parpadear("chris_orgulloso"), right
            chris "Bueno lo que encontramos fue..."
            hide chris_orgulloso
            scene fondo literas with fade
            chris "...literas sucias, llenas de polvo, que lo más probable nos dé contracturas..." 
            scene fondo banos with fade
            chris "...baños, en buen estado, quitando el olor horrible que emana..." 
            scene fondo invernadero with fade
            chris "...un invernadero, que siendo sincero ¿Alguna vez plantaron algo, o tocaron pasto?"

    scene fondo comedor_estudiantes_sentados with fade
    show Chris at parpadear("chris"), left
    chris "Y una radio, que no me sorprendería que no funcione..."
    hide Chris
    show pov_radio at center
    david "Bueno, al menos tenemos una radio."
    hide pov_radio
    show sara at parpadear("sara"), right
    sara "Me gustaría dedicarle tiempo a la radio... tengo algunas herramientas en mi mochila. Tal vez si la reparo, consigamos pedir ayuda."
    show chris_sarcastico at parpadear("chris_sarcastico"), left
    chris "¿Ese aparato viejo? Suerte con eso..."
    hide chris_sarcastico
    hide sara
    pause
    scene fondo comedor_estudiantes_sentados
    david "Me parece bien, Sara. Por mi parte, me aseguraré de que todo esté bajo control. Ahora, sobre los cuatro que quedan: Daiana y Juan, ustedes dos gestionarán los recursos."
    show estudiante_femenino at right
    estudiante_1 "Haré mi mayor esfuerzo."
    hide estudiante_femenino
    scene fondo comedor_estudiantes_sentados_sin_otro_masculino
    show estudiante_masculino at left
    estudiante_4 "No soy bueno con las plantas, pero lo intentaré."
    hide estudiante_masculino
    david "Ana y Ariana, encárguense del invernadero."
    scene fondo comedor_estudiantes_sentados
    scene fondo comedor_estudiantes_sentados_sin_beige
    show estudiante_femenino_2 at left
    estudiante_2 "Claro, no hay problema."
    hide estudiante_femenino_2
    scene fondo comedor_estudiantes_sentados_sin_violeta
    show estudiante_femenino_3 at right
    estudiante_5 "Nosotros nos encargaremos."
    hide estudiante_femenino_3
    
    if ir_con_chris:
        show sara_preocupada at parpadear("sara_preocupada"), right
        pause
        david "¿Estás bien, Sara? Te veo preocupada."
        hide sara_preocupada
        show sara_timida at parpadear("sara_timida"), right
        sara "¿Eh? ¡Sí, sí, estoy bien!"
        david "¿Estás segura? Puedes confiar en mí."
        sara "Bueno... no quería alarmar a nadie, pero hace un momento me pareció ver... algo por el pasillo."
        david "¿Algo? ¿A qué te refieres con algo?"
        hide sara_timida at parpadear("sara_timida")
        show sara at parpadear("sara"), right
        sara "Me pareció ver una... sombra. Todos estábamos juntos, no pudo haber sido alguien de nosotros."
        play sound "alumnos susurrando.mp3"
        david "¿Una sombra?"
        sara "Sí... era como una silueta, no llegué a verlo del todo bien... tenía mucho miedo."
        david "¿Dónde la viste?"
        sara "En el pasillo, despues de la muerte del... piloto."
        hide sara
        stop sound fadeout 1.0
    else:
        david "Chicos, tengo algo de qué hablar con ustedes... hace un rato Sara me contó que vio una sombra en uno de los pasillos."
    
    show estudiante_masculino at right
    estudiante_3 "¿Una sombra? ¡Estás loca! No hay nadie más aquí."
    hide estudiante_masculino
    show estudiante_femenino_2 at left
    estudiante_2 "Tengo miedo... ¿Y si entró algún tipo de {sc=4}{color=#FF0000}bestia{/color}{/sc}? La puerta estaba abierta..."
    hide estudiante_femenino_2
    show chris_sarcastico at parpadear("chris_sarcastico"), center
    chris "¿Una sombra? Ja, seguro que fue tu imaginación, Sara."
    hide chris_sarcastico

    menu:
        'Hablar de Síndrome ártico.':
            david "Tranquilos, lo que Sara creyó haber visto es algo normal en lugares aislados, lo vi en una película, algo como... \n{sc=4}{color=#ADD8E6}Síndrome ártico{/color}{/sc}... Cuanto más le demos importancia será peor."
            david "Si ven o escuchan cosas, no lo oculten a los demás. Estamos juntos en esto."
        'No darle importancia.':
            david "(No puedo permitir que entren en pánico.)"
            david "Seguramente fue alguno de nosotros, Sara. Éstas luces y sombras engañan fácilmente… No vale la pena preocuparse por eso."
            show chris at parpadear("chris"), center
            chris "Nosotros cuando fuimos a explorar no vimos nada raro."
            hide chris
    pause
    david "De todas formas, debemos estar atentos. Cualquier cosa rara que vean, me la cuentan de inmediato."

    hide sara_preocupada

    david "Sigamos con la asignación de grupos."
    david "Chris... Tú sigue explorando con Diego y Pedro."

    # En base a la moral obtenida por el jugador, chris puede aceptar ir acompañado o no y cerramos el acto 1 
    # mostrando que de cualquier manera chris es el más afectado por la situación.
    if moral >= 8:
        show chris at parpadear("chris"), center
        chris "Yo puedo seguir explorando, pero voy sólo."
        david "No podemos permitir que vayas solo, Chris. Es demasiado peligroso."
        david "Pedro y Diego te acompañarán."
        hide chris
        scene fondo comedor_estudiantes_sentados_sin_dos_masculinos
        show estudiante_masculino_3 at right
        show estudiante_masculino_2 at left
        f"{estudiante_3} y {estudiante_6}" "Cuenta con nosotros..."
        hide estudiante_masculino_3
        hide estudiante_masculino_2
        show chris at parpadear("chris"), center
        chris "Está bien, pero no seré su niñera."
        hide chris
    else:
        show chris_enojado at parpadear("chris_enojado"), center
        chris "Estoy cansado de que me des órdenes, héroe."
        chris "Y no soporto ese maldito ruido del generador, ni siquiera sabemos dónde está."
        chris "Iré solo."
        hide chris_enojado


    # while salir_del_bucle:
    #     menu:
    #         'Exigirle que vaya acompañado.' if moral < 3:

    #             chris "Nos vemos, chicos."
    #         'Convencerlo de que no vaya sólo.' if moral < 5:
    #             show chris at parpadear("chris"), center
    #             chris "Yo puedo seguir explorando, pero voy sólo."
    #             david "No podemos permitir que vayas solo, Chris. Es demasiado peligroso."
    #             david "Pedro y Diego te acompañarán."
    #             hide chris
    #             scene fondo comedor_estudiantes_sentados_sin_dos_masculinos
    #             show estudiante_masculino_3 at right
    #             show estudiante_masculino_2 at left
    #             f"{estudiante_3} y {estudiante_6}" "Cuenta con nosotros..."
    #             hide estudiante_masculino_3
    #             hide estudiante_masculino_2
    #             show chris at parpadear("chris"), center
    #             chris "Está bien, pero no seré su niñera."
    #             hide chris
    #         'Pedirle que traiga repuestos para la radio.' if moral < 9:

    
    # if moral >= 8:
    #     show chris at parpadear("chris"), center
    #     chris "Yo puedo seguir explorando, pero voy sólo."
    #     david ""
    #     david "Está bien, lo siento."
    #     hide chris
    #     scene fondo comedor_estudiantes_sentados_sin_dos_masculinos
    #     show estudiante_masculino_3 at right
    #     show estudiante_masculino_2 at left
    #     f"{estudiante_3} y {estudiante_6}" "Cuenta con nosotros..."
    #     hide estudiante_masculino_3
    #     hide estudiante_masculino_2
    #     chris ""
    # else:
    #     show Chris_enojado at parpadear("Chris_enojado"), center
        
    #     hide Chris_enojado

    # menu:
    #     'Hacerlo entrar en razón.':
    #         david "Chris, cálmate. No estamos en condiciones de pelear entre nosotros."
    #     'Responder con firmeza.':
    #         david "¡Basta, Chris! No voy a permitir que pongas en riesgo a los demás por tu egoísmo."
            

    stop music
    stop sfx3
    play sound "final_normal.mp3" volume 0.2
    python:
        final = gestor.activar_final("acto1_final_normal")   
        resultado = gestor.obtener_resultado()
    scene black with fade
    centered "{size=40}[resultado]{/size}"
    pause 3.0
    jump creditos
    # Agregar final normal ()