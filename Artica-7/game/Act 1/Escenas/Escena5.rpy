# Escena 5: El refugio misterioso

label escena5_refugio_misterioso:
    scene fondo artica7_interior with fade
    stop music
    ### Aca se vuelve a escuchar algo de nuevo 1111111111111111

    ### Deberia sonar cuando el estudiante habla? o despues de que habla?
    play sound "generador_enciende.mp3" volume 0.5

    show estudiante_femenino at left
    estudiante_1 "¿Qué es este lugar?"
    hide estudiante_femenino
    
    narrador "De repente se escucha el sonido de un generador funcionando, luces fluorescentes parpadean débilmente en el techo."
    
    narrador "Se encienden completamente, iluminando un pasillo largo con paredes metálicas oxidadas, piso de rejilla industrial y cables expuestos en el techo."

    narrador "El grupo mira alrededor. El lugar parece abandonado hace años. Hay polvo sobre consolas apagadas."
    
    play sound "puerta_cierra.mp3" volume 2.0
    narrador "La puerta se cierra detrás de ellos con un golpe metálico definitivo."

    narrador "El tutor corre hacia la puerta , se le cae el walkie-talkie en el suelo."

    menu:                          
        "Tratar de detener al tutor":
            show david at left
            david "¡Profesor, espere! ¡No creo que sea buena idea tocar esa puerta!"
            hide david
            narrador "El tutor ignoró a David, su desesperación lo habia ensordecido"  
        "No hacer nada.":
            tutor "NO, NO, NO, NO, ESPERA, ESPERA, ESPERA, ¡¿QUE ESTA PASANDO?!"
    show tutor at center

    "Al intentar forzar la puerta una descarga eléctrica recorre todo su cuerpo, dejándolo tirado en el suelo, convulsionando, hasta que deja de moverse."

    play sound "descarga_electrica.mp3"
    show tutor at center with hpunch
    pause 0.5
    hide tutor

    play sound "caida_suelo.mp3"
    scene fondo tutor_electrocutado_radio with fade
    narrador "Cayó al suelo. Sin vida."

    show estudiante_femenino at left
    estudiante_2 "¡SEÑOR!"
    hide estudiante_femenino

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

        sara "¡Necesitamos ayuda! ¡Nuestro tutor acaba de morir por una descarga eléctrica!"

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

        show david at left
        david "(Los chicos estan empezando a entrar en panico, tengo que tomar las riendas y calmarlos a todos.)"
        hide david

        narrador "David se pone frente a los demas."
        show david at center

        david "¡Nesito que me escuchen!"

        narrador "Los chicos se voltean y miran a David"

        david "vamos a calmarnos y tratemos de buscar algo con lo que podamos pedir ayuda"

        david "Escuchen... escúchenme todos. Sé que esto es horrible. Lo peor que nos ha pasado. Pero ahora mismo, en este momento, estamos vivos."

        jump explorar_instalación

    label explorar_instalación:

        show estudiante_femenino at left
        estudiante_5 "¡Estamos atrapados con un cadáver!"
        hide estudiante_femenino
        show chris at left
        chris "¿Calmarnos? ¿Pensar? ¡Vamos a morir aquí!"
        hide chris
        jump organizacion_grupos

    label organizacion_grupos:

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


    label asignacion_favorita:
        david "Chris, vos y los más fuertes exploran. Sara, vos y otros cuidan el invernadero."

        show chris at right
        show sara at left

        chris "Perfecto. Nosotros encontraremos lo que necesitamos."
        sara "¿Y los demás? ¿No es injusto?"
        david "Es lo más eficiente."

        narrador "Algunos chicos se sintieron excluidos."
        narrador "Las grietas comenzaron a formarse."