# Define los personajes
define david = Character("David", color="#4169E1")
define sara = Character("Sara", color="#ffb969")
define chris = Character("Chris", color="#14dc61")
define tutor = Character("Tutor", color="#dc6e14")
define estudiante_1 = Character("Estudiante 1", color="#5a14dc")
define estudiante_2 = Character("Estudiante 2", color="#c8dc14")
define estudiante_3 = Character("Estudiante 3", color="#dc2114")
define estudiante_4 = Character("Estudiante 4", color="#14d5dc")
define estudiante_5 = Character("Estudiante 5", color="#dc14b1")
define estudiante_6 = Character("Estudiante 6", color="#96dc14")
define narrador = Character(None)
image negro = "#000000"

# Variables del sistema de moral
default moral = 0
default humo = 0

# Inicio del juego
label start:
    call escena1a2 from _call_escena1a2
    call escena3a5 from _call_escena3a5
    call escena6a9 from _call_escena6a9
    scene negro with fade
    centered  "{size= 65} FIN DEL ACTO 1 {/size}"
    call resumen_acto2
    centered  "{size= 65} FIN DEL ACTO 2 {/size}"
    call act_3_escena1
    menu:
        'Calmar a Chris (Necesita moral alta).':
            call calmar_a_chris
        'Huir con Sara (Necesita moral media/baja).':
            call huir_con_sara 
    scene negro with fade
    centered  "{size= 65} FIN DEL ACTO 3 {/size}"

    