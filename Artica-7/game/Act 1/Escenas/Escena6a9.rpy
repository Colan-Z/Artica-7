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
    with fade
    tutor "¡NOO! ¡Puta madre! ¡La puerta se cerró!"
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
            python:
                final = gestor.activar_final("final_alternativo")   
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
            scene fondo tutor_electrocutado_quemado_radio with fade
        "No tocarlo, podría ser peligroso.":
            #escena 11B
            scene fondo tutor_electrocutado_quemado_radio with fade
            narrador "No hacía falta verificar su pulso, el olor a carne quemada que desprendía, provocaba que algunos alumnos les dieran nauseas."

    # ESCENA 11A/B
    play sound "radio interferencia.mp3" loop volume 0.2
    pause
    scene fondo sara_walkie-talkie
    piloto "¿Ho... hola? ¿Se escu... cha?"
    piloto "¿Es... están to... dos bien?"
    if renpy.showing("fondo tutor_electrocutado_radio"):
        scene fondo tutor_electrocutado
    else:
        scene fondo tutor_electrocutado_quemado
    
    show sara gritando_walkie-talkie at parpadear("sara gritando_walkie-talkie"),  right
    with fade
    sara "¡Necesitamos ayuda! ¡Nuestro tutor acaba de morir por una descarga eléctrica!"
    piloto "¡Tranquila, voy a intentar pedir ayuda!"
    hide sara gritando_walkie-talkie
    jump ESCENA_12

# Escena 12
label ESCENA_12:
    play sound "helicoptero despega.mp3" volume 0.3
    scene fondo helicoptero_despega with fade
    
    # Marcar que AFM temporal está activo
    # $ afm_temporal_activo = True
    # $ _preferences.afm_enable = True
    # $ _preferences.afm_time = 7
    
    piloto "No se preocupen. ¡Voy a buscar ayuda!"
    
    scene fondo helicoptero_volando_ventisca with fade
    play sound "helicoptero pierde control.mp3" volume 0.3
    
    # $ _preferences.afm_time = 5
    piloto "¡NO! ¡La ventisca es muy fuerte! ¡¡Estoy perdiendo el control!!"
    
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
    window hide
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
    show chris_furioso at parpadear("chris_furioso"), center
    chris "¡Maldita sea! Se suponía que sería una excursión que me ayudaría con mis problemas, ¡PERO ESTO SOLO LO EMPEORA!"
    hide chris_furioso
    show estudiante_femenino at left
    estudiante_1 "¡Qué vamos a hacer!"
    hide estudiante_femenino
    show estudiante_masculino_2 at right
    estudiante_3 "Quiero irme a casa."
    hide estudiante_masculino_2

    $ salir_del_bucle = True
    while salir:
        menu:
            "Usar el celular" if tiene_celular:
                david "Cálmense todos. Antes al bajar del helicóptero tome mi celular en caso de que algo pasara."
                david "Acá dentro hay algo de señal, voy a hacer una llamada de SOS para pedir ayuda. Espero que funcione..."
                scene fondo interior_artica_sos
                'Operador' "Aquí base orcadas. ¿Cuál es su emergencia?"
                david "Hola, me llamo David, somos los estudiantes que iban a una expedición en orcadas, tuvimos un problema por una ventisca por lo que decidimos refugiarnos en una instalación llamada Artcia-7"
                'Operador' "¿Artica-7? No conozco nada con ese nombre... Tal vez pueda localizar tu llamada."
                david "Puede que vean humo en el cielo, el helicóptero que nos llevaba se estrello."
                'Operador' "Eso puede servirnos, estamos preparando el equipo de rescate, manténganse ahí, llegaremos lo antes posible."
                david "Gracias. Vamos a esperar las instrucciones."
                python:
                    final = gestor.activar_final("acto1_bueno")   
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
            show estudiante_masculino_2 at left
            estudiante_3 "Ya me encuentro mejor, puedo ir a investigar la zona."
            hide estudiante_masculino_2
            show estudiante_masculino_3 at right
            estudiante_6 "Sí, yo también lo estoy."
            hide estudiante_masculino_3
            show chris at parpadear("chris"), center
            chris "Lo siento, pero no me gusta trabajar en equipo, me gusta estar solo."
            david "Vas a tener que trabajar con ellos Chris, no te queda de otra."
            # Aca chris podria empezar a enojarse un poco con 
            # como le habla david pero aceptar igual (un gruñido o algo por el estilo)
            # agregar sprite de chris (un poco) enojado
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
                    # Agregar sara preocupada (sprite y en celtex)
                    show sara at parpadear("sara"), center
                    sara "¿Eh? ¡Sí, sí, estoy bien!"
                    david "¿Estás segura? Puedes confiar en mí."
                    sara "Bueno... no quería alarmar a nadie, pero hace un momento me pareció ver... algo por el pasillo."
                    david "¿Algo? ¿A qué te refieres con algo?"
                    sara "Me pareció ver una... sombra. Todos estábamos juntos, no pudo haber sido alguien de nosotros."
                    david "(Puede que tenga razón, espero que no le pase nada a los chicos.)"
                    hide sara
                    play sound "alumnos susurrando.mp3"
                    pause
                    david "(Los demás lo escucharon, no sé qué hacer. ¿Trato de calmarlos o no le doy mucha importancia?)"
                    menu:
                        'Hablar con los demás.':
                            # Hacer una rama o algo que no quede como cosmetico
                            # aca se puede poner el final normal, que se note como les esta afectando todo
                            stop sound fadeout 1.0
                            david "Tranquilos, lo que Sara creyó haber visto es algo normal en lugares aislados, lo vi en una película, algo como... síndrome ártico... Cuanto más le demos importancia será peor."
                            david "Si ven o escuchan cosas, no lo oculten a los demás. Estamos juntos en esto."
                            # Agregar dialogo de los estudiantes, mostrando que creen a david (por el momento)
                            narrador "Ante estas palabras los estudiantes parecieron tranquilizarse un poco."
                        'No darle importancia.':
                            david "Seguramente fue tu imaginación, Sara. Éstas luces y sombras engañan fácilmente… No vale la pena preocuparse por eso."
                    # Poner este texto en pantalla con fondo negro
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
    scene fondo pasillo 
    show chris_enojado at parpadear("chris_enojado"), left
    show estudiante_masculino_2 at right
    with fade
    estudiante_3 "Lo siento, no volverá a pasar..."
    hide estudiante_masculino_2
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
    estudiante_6 "¡Hay 8 literas, suficientes para todos!"
    hide estudiante_masculino_3
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
    show estudiante_masculino_2 at right
    estudiante_3 "Quisiera descansar un poco..."
    show chris at parpadear("chris"), left
    chris "Cuando encontremos qué comer, vas a descansar."
    estudiante_3 "Está bien..."
    hide estudiante_masculino_2
    hide chris
    play sound "caminan.mp3"
    pause 2
    stop sound
    scene fondo comedor 
    show chris_enojado at parpadear("chris_enojado"), center
    with fade
    # Dialogo inconsistente con el dialogo cuando ve las camas por primera vez
    chris "¡Genial! Tenemos camas sucias, algunas latas de comida están podridas y esta radio de porquería no parece que vaya a funcionar."
    
    david "Al menos tenemos comida y camas... eso nos compra tiempo. Es mejor que nada."
    # Agregar mas molestia creciente de chris con david
    david "Volvamos, los demás deben estar perdiendo la cabeza con el tutor a su lado, hay que darles las 'buenas' noticias."
    hide chris_enojado
    play sound "caminan.mp3"
    pause 2
    stop sound
    scene fondo tutor_electrocutado with fade
    jump ESCENA_15
    
label ESCENA_15:
    # Reemplazar esto por texto en pantalla
    narrador "Al llegar con los demás chicos, Chris cuenta con detalle los lugares encontrados."
    # poner sprites de algunos estudiantes escuchando a chris
    david "Bueno, vamos a movernos al comedor, necesitamos un plan que nos ayude a sobrevivir con lo que tengamos."
    play sound "caminan.mp3"
    pause 2
    stop sound # para  caminan.mp3
    jump ESCENA_16

# ESCENA 16
label ESCENA_16:
    stop sound
    scene fondo comedor_estudiantes_sentados with fade
    play sound "estudiantes hablando.mp3" volume 0.3 loop
    # Poner estudiantes en las sillas (chris y sara pueden 
    # estar parados a su lado aunque no se vean)
    david "Chicos hagan silencio y escúchenme."
    stop sound fadeout 2.0
    david "Estos son los lugares accesibles que tenemos por ahora, si queremos que esto funcione, tendremos que dividirnos en grupos."
    show chris at parpadear("chris"), center
    chris "Yo puedo seguir explorando con mi grupo."
    hide chris
    scene fondo comedor_estudiantes_sentados_sin_dos_masculinos
    show estudiante_masculino_3 at right
    show estudiante_masculino_2 at left
    f"{estudiante_3} y {estudiante_6}" "Oh, no..."
    hide estudiante_masculino_3
    hide estudiante_masculino_2
    scene fondo comedor_estudiantes_sentados
    david "Me parece bien, entonces los 6 que quedamos. Por mi parte, me encargaré de que todo esté bajo control, ustedes dos se encargarán del invernadero."
    scene fondo comedor_estudiantes_sentados_sin_beige
    show estudiante_femenino at right
    estudiante_1 "Haremos nuestro mayor esfuerzo."
    hide estudiante_femenino
    scene fondo comedor_estudiantes_sentados_sin_otro_masculino
    show estudiante_masculino at left
    estudiante_4 "No soy bueno con las plantas, pero lo intentaré."
    hide estudiante_masculino
    scene fondo comedor_estudiantes_sentados
    show sara at parpadear("sara"), right
    sara "Me gustaría dedicarle tiempo a la radio... tengo algunas herramientas en mi mochila, tal vez pueda conseguir ayuda."
    show chris at parpadear("chris"), left
    chris "¿Ese aparato viejo? Suerte con eso..."
    david "Bien, te encargo la radio. Los que quedan ¿Podrían encargarse de los suministros?"
    hide chris
    hide sara
    scene fondo comedor_estudiantes_sentados_sin_beige
    show estudiante_femenino_2 at left
    estudiante_2 "Claro, no hay problema."
    hide estudiante_femenino_2
    scene fondo comedor_estudiantes_sentados_sin_violeta
    show estudiante_femenino_3 at right
    estudiante_5 "Nosotros nos encargaremos."
    hide estudiante_femenino_3
    # Agregar final normal ()