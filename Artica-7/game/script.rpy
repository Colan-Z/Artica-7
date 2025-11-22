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
define piloto = Character("Piloto", color="#dccf14")
define narrador = Character(None)
image negro = "#000000"

init python:
    renpy.music.register_channel("sfx1", mixer="music", loop=True)
    renpy.music.register_channel("sfx2",   mixer="music", loop=True)

label before_main_menu:
    $ renpy.music.set_volume(0.1, delay=0, channel="music")
    return

# Variables del sistema de moral
default moral = 5
default humo = 0

# Inicio del juego
label start:
    stop music
    $ renpy.music.set_volume(1.0, delay=1.0, channel="music")
    centered  "{size= 65} Se recomienda bajar un poco el volumen {/size}" with fade
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
    centered  "{size= 65} CREDITOS \n\n Productor/Guionista: Colantonio Franco\n Game Designer: Pelleritti Nicolás\n Programador: Gauto Carlos\n Arte: Bustelo Nicolás {/size}" with fade

    