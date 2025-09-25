# Define personajes

define i = Character("isaac")
define j = Character("Jordan")
define r = Character("Rowan") # Se agregaron 2 personajes nuevos a la historia
define m = Character("Mathias")

# Define imagenes personajes
image isaac = "images/personajes/Isaac.png"
image jordan_alegre = "images/personajes/personaje_alegre.png"
image jordan_triste = "images/personajes/porky_triste.png"
image Rowan = "images/personajes/Rowan.png" # Retrato de los nuevos personajes
image Mathias = "images/personajes/Mathias.png"

# Define imagenes fondos
image fondo = "images/fondos/fondo.png"
image escena_cuerno = "images/fondos/Escena_cuerno.png"
image inicio_nubes = "images/fondos/Inicio_nubes.png"
image toma_decision_lider = "images/fondos/Toma_de_decision_lider.png"

label start:

    show fondo

    show isaac at left
    i "¿Quien eres tu?"

    show jordan_alegre at right
    j "Me dicen Porky"

    call menu_reirse

    show jordan_triste at right

    jump mensaje_demo

label menu_reirse:
    menu:
        # "¿Te ries, reirse o no?"
        "Reirse":
            jump reirse
        "No reirse":
            jump no_reirse

label reirse:
    i "Jajaja, ¡Porky, Porky!."
    return

label no_reirse:
    i "JAJAJAJAJAJAJA."
    return

label mensaje_demo:
    "Esta fue la demo de The Forgotten Ones"
    return
