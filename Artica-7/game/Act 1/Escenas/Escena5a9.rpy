label escena5a9:
    
    # ESCENA 6 - INT. ÁRTICA-7 - ENTRADA - DÍA
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
            # ESCENA 6-A - INT. ÁRTICA-7 - ENTRADA - DÍA
            show david at left
            david "¡Profesor, espere! ¡No creo que sea buena idea tocar esa puerta!"
            hide david
            narrador "El tutor ignoró a David, su desesperación lo habia ensordecido"  
        "No hacer nada.":
            # ESCENA 6-B - INT. ÁRTICA-7 - ENTRADA - DÍA
            tutor "NO, NO, NO, NO, ESPERA, ESPERA, ESPERA, ¡¿QUE ESTA PASANDO?!"

    play sound "descarga_electrica.mp3"
    show tutor at center with hpunch
    pause 0.5
    hide tutor

    play sound "caida_suelo.mp3"
    scene fondo tutor_electrocutado_quemado_radio with fade
    narrador "Al intentar forzar la puerta una descarga eléctrica recorre todo su cuerpo, dejándolo tirado en el suelo, convulsionando, hasta que deja de moverse."

    # ESCENA 7 - INT. ÁRTICA-7 - TUTOR ELECTROCUTADO - DÍA
    show estudiante_femenino at left
    estudiante_2 "¡SEÑOR!"
    hide estudiante_femenino
    

    menu:
        "Revisar si tiene pulso":
            # ESCENA 7-A - INT. ÁRTICA-7 - TUTOR ELECTROCUTADO SIN HUMO - DÍA
            show david at right
            david "No... no respira. No tiene pulso."
        "No tocarlo, podría ser peligroso":
            # ESCENA 7-B - INT. ÁRTICA-7 - TUTOR ELECTROCUTADO CON HUMO - DÍA
            narrador "No hacia falta verificar su pulso, el olor a carne quemada que desprendía, provocaba que algunos alumnos les dieran nauseas."

    hide david

    # ESCENA 7AB - INT. ÁRTICA-7 - TUTOR ELECTROCUTADO C/S HUMO - DÍA
    "PILOTO" "¿Ho... hola? ¿Se escu...(ESTÁTICA)...cha?"
    "PILOTO" "¿Es... están to...(ESTÁTICA)...dos bien?"
    scene fondo tutor_electrocutado_quemado with fade
    show sara at left
    sara "¡Necesitamos ayuda! ¡Nuestro tutor acaba de morir por una descarga eléctrica!"
    "PILOTO" "¡Tranquila, voy a intentar pedir ayuda!"
    hide sara

    # ESCENA 8 - EXT. ÁRTICA-7 - HELICOPTERO - DESPEGA - DÍA
    scene fondo helicoptero_despega with fade
    narrador "El piloto enciende el helicóptero y procede a despegar."
    scene fondo helicoptero_cae with fade
    narrador "Al elevarse, pierde el control, la ventisca era muy fuerte"
    scene fondo helicoptero_destrozado with fade
    narrador "El piloto se estrella dejando a los chicos a su suerte, dejando únicamente el ruido de la estática."
    
    # ESCENA 9 - INT. ÁRTICA - DÍA
    scene fondo tutor_electrocutado_quemado with fade
    show chris at left
    chris "¡No! ¡Esto no puede estar pasando!"
    hide chris
    show estudiante_masculino at right
    estudiante_3 "¡Tenemos que salir de aquí! ¡YA!"
    hide estudiante_masculino
    show estudiante_femenino at center
    estudiante_4 "¡Vamos a morir aquí!"
    hide estudiante_femenino
    show chris at left
    chris "¡Maldita sea! Se suponía que sería una excursión que me ayudaría con mis problemas, ¡PERO ESTO SOLO LO EMPEORA!"
    hide chris
    show estudiante_femenino at left
    estudiante_1 "¡Qué vamos a hacer!"
    hide estudiante_femenino
    show estudiante_masculino at right
    estudiante_3 "Quiero irme a casa."
    hide estudiante_masculino
    show david at center
    david "Escuchen... escúchenme todos. Sé que esto es horrible. Lo peor que nos ha pasado. Pero ahora mismo, en este momento, estamos vivos."
    hide david
    show estudiante_masculino at left
    estudiante_5 "¡Estamos atrapados con un cadáver!"
    hide estudiante_masculino
    show chris at right
    chris "¿Calmarnos? ¿Pensar? ¡Vamos a morir aquí!"
    hide chris
    show david at center
    david "Los entiendo, pero estando acá parados no vamos a solucionar nada. Deberíamos de investigar la instalación, puede que encontremos algo que nos mantenga con vida mientras esperamos a que nos rescaten."
    show sara at right
    sara "Tienes razón, tal vez logremos encontrar algo para contactarnos con los de afuera."
    david "¡Exacto!"
    show chris at left
    chris "Está bien. Espero que esto no sea una pérdida de tiempo... ¿Qué tienes en mente, héroe?"
    david "Primero, necesitamos un grupo que pueda explorar la instalación."
    hide chris
    hide sara
    hide david
    menu:
        "Ir con Chris a explorar la base.":
            # ESCENA 8-A - INT - ÁRTICA-7 - PASILLOS - DÍA
            scene fondo pasillo with fade
            show david at left
            david "Vamos por este pasillo, parece llevar hacia el centro de la base."
            hide david
            narrador "(Un estudiante intenta tocar una puerta)"
            show chris at right
            chris "¡No la toques! ¿¡Quieres terminar como nuestro tutor?! ¡¡¿FRITO?!!."
            show estudiante_femenino at left
            estudiante_5 "Lo siento, no volverá a pasar..."
            hide estudiante_femenino
            chris "Solamente vamos a entrar en habitaciones que tengan las puertas abiertas."
            hide chris
            show estudiante_masculino at right
            estudiante_6 "¡Aquí hay una puerta abierta! ¡Hay literas!"
            show david at left
            david "Contemos cuántas son."
            estudiante_6 "1... 2... 3... ¡Hay 6 literas, suficientes para todos!"
            hide estudiante_masculino
            show chris at right
            chris "Los colchones son viejos, tienen un poco de polvo. Bien, ya tenemos un lugar donde dormir, sigamos buscando."
            hide chris
            hide david
            narrador "(algunos minutos después)"
            show david at left
            david "Perfecto, encontramos un lugar donde dormir, baños, un invernadero y una radio, pero creo que no funciona... sigamos caminando tal vez encontremos algo de comida."
            hide david
            show estudiante_femenino at right
            estudiante_3 "Quisiera descansar un poco..."
            show chris at left
            chris "Cuando encontremos que comer, vas a descansar."
            estudiante_3 "Está bien..."
            hide estudiante_femenino
            hide chris
            narrador "Los chicos siguieron avanzando hasta encontrar un comedor y una cocina, donde había un poco de suministros para mantenerse unos días."
            show chris at left
            chris "Genial! Es hora de volver, tenemos que avisarle a los demás."
            hide chris
            scene fondo artica7_interior with fade
            narrador "Al llegar con los demás chicos, Chris cuenta con detalle los lugares encontrados."
            show david at left
            david "Bueno, vamos a movernos al comedor, necesitamos un plan que nos ayude a sobrevivir con lo que tengamos."
            hide david
        "Quedarse ayudando a los demás.":  
            # ESCENA 8-B - INT - ÁRTICA-7
            show sara at right
            sara "Yo... yo puedo acompañarte para cuidarlos."
            show david at left
            david "Me vendría bien un poco de ayuda..."
            hide sara 
            show chris at right
            chris "Que pasa héroe? pareces un tomate? hawdasgt"
            david "¡¿Qué?! No nada, nada, no me pasa nada... (tos nerviosa) ...Puedes ir a investigar?"
            chris "¡Obvio, ya tenía pensado hacerlo!"    
            hide david
            hide chris
            show estudiante_femenino at left
            estudiante_3 "Ya me encuentro mejor, puedo ir a investigar la zona."
            hide estudiante_femenino
            show estudiante_masculino at right
            estudiante_6 "Si, yo también lo estoy."
            hide estudiante_masculino
            show chris at right
            chris "Lo siento, pero no me gusta trabajar en equipo, me gusta estar solo."
            show david at left
            david "Vas a tener que trabajar con ellos Chris, no te queda de otra."
            chris "...Esta bien, vengan, vamos, no me hagan perder el tiempo."
            hide chris
            hide david
    
    # ESCENA 9 - INT. ÁRTICA-7 - COMEDOR COMÚN - TARDE (HORAS DESPUÉS)
    scene fondo comedor with fade
    narrador "En el comedor común encontraron un pizarra blanca, rayada con un mapa rudimentario de la instalación mostraba: dormitorios, cocina, invernadero, baños y comedor."
    show david at center
    david "Estos son los lugares accesibles que tenemos por ahora, si queremos que esto funcione, tendremos que dividirnos en grupos."
    hide david
    show chris at left
    chris "Yo puedo seguir explorando con mi grupo"
    hide chris
    show estudiante_femenino at right
    show estudiante_masculino at left
    "estudiante_3 y estudiante_4" "Oh no..."
    hide estudiante_femenino
    hide estudiante_masculino
    show estudiante_femenino at right
    estudiante_1 "Haremos nuestro mayor esfuerzo."
    hide estudiante_femenino
    show estudiante_masculino at right
    estudiante_4 "No soy bueno con las plantas, pero lo intentaré."
    hide estudiante_masculino
    show sara at left
    sara "Me gustaría dedicarle tiempo a la radio... tal vez pueda conseguir ayuda."
    show chris at right
    chris "Ese aparato viejo?(risas)... Suerte con eso... asdasd"
    hide chris
    hide sara 
    show david at center
    david "Bien, te encargo la radio. Los que quedan ¿Podrían encargarse de los suministros?"
    hide david
    show estudiante_femenino at left
    estudiante_2 "Claro, no hay problema."
    show estudiante_masculino at right
    estudiante_5 "Nosotros nos encargamos."
    hide estudiante_femenino
    hide estudiante_masculino