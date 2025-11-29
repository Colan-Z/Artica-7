# Define los personajes
define david = Character("David", color="#4169E1")
define sara = Character("Sara", color="#ffb969")
define chris = Character("Chris", color="#14dc61")
define tutor = Character("Tutor", color="#dc6e14")
define estudiante_1 = Character("Daiana", color="#5a14dc")
define estudiante_2 = Character("Ana", color="#c8dc14")
define estudiante_3 = Character("Diego", color="#dc2114")
define estudiante_4 = Character("Juan", color="#14d5dc")
define estudiante_5 = Character("Ariana", color="#dc14b1")
define estudiante_6 = Character("Pedro", color="#96dc14")
define piloto = Character("Piloto", color="#6b4909")
define narrador = Character(None)
image negro = "#000000"

label before_main_menu:
    $ renpy.music.set_volume(0.1, delay=0, channel="music")
    return

# Variables del sistema de moral
default moral = 5

#Tiempo de pestañeo
transform parpadear(personaje):
    "{}".format(personaje)
    choice: 
        1.0
    choice: 
        2.0
    choice: 
        0.5
    "{}_blink".format(personaje)
    choice: 
        0.25
    repeat

transform parpadear_shake(p):
    Image(p + ".png")
    choice:
        1.0
    choice:
        2.0
    choice:
        0.5
    Image(p + "_blink.png")
    choice:
        0.25
    repeat

transform shake_fuerte:
    zoom 1.01
    xalign 0.5
    yalign 0.5
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    repeat 

transform shake_leve:
    zoom 1.009
    xalign 0.5
    yalign 0.5
    linear 0.05 xoffset 2
    linear 0.05 xoffset -2
    repeat

transform shake_medio:
    zoom 1.009
    xalign 0.5
    yalign 0.5
    linear 0.05 xoffset 5
    linear 0.05 xoffset -5
    repeat

transform yshake:
    zoom 1.2
    xalign 0.5
    yalign 0.5
    linear 0.14 yoffset -8
    linear 0.14 yoffset 8
    repeat

# Inicio del juego
label start:
    stop music
    $ renpy.music.set_volume(1.0, delay=1.0, channel="music")
    call escena1a2 from _call_escena1a2
    call escena3a5 from _call_escena3a5
    call escena6a9 from _call_escena6a9
    scene negro with fade
    play sound "final actos.mp3"
    centered  "{size= 65} FIN DEL ACTO 1 {/size}" with fade
    call resumen_acto2 from _call_resumen_acto2
    play sound "final actos.mp3"
    centered  "{size= 65} FIN DEL ACTO 2 {/size}" with fade
    call act_3_escena1 from _call_act_3_escena1

    label creditos:
        scene black
        show text "{size=65}CREDITOS\n\nProductor/Guionista: Colantonio Franco\nGame Designer: Pelleritti Nicolás\nProgramador: Gauto Carlos\nArte: Bustelo Nicolás{/size}" as creditos_text
        with Dissolve(1.0)

        pause 2.0
        
        hide creditos_text
        with Dissolve(1.0)

        pause 0.2

        $ renpy.full_restart()


    