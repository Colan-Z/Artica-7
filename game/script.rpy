# Define personajes

define i = Character("???")
define p = Character("Muchacho")
define r = Character("Rowan") # Se agregaron 2 personajes nuevos a la historia
define m = Character("Mathias")

# Define imagenes personajes
image isaac = "images/personajes/Isaac.png"
image porky_alegre = "images/personajes/porky_alegre.png"
image porky_triste = "images/personajes/porky_triste.png"
image porky_neutro = "images/personajes/porky_neutro.png"
image Rowan = "images/personajes/Rowan.png" # Retrato de los nuevos personajes
image Mathias = "images/personajes/Mathias.png"

# Define imagenes fondos
image escena_cuerno = "images/fondos/Escena_cuerno.png"
image inicio_nubes = "images/fondos/Escena_Inicio_nubes.jpg"
image escena_playa = "images/fondos/Escena_Playa.jpg"
image aparicion_chicos = "images/fondos/Escena_Aparicion_Chicos_nueva.jpg"
image cima = "images/fondos/Escena_Cima_nueva.jpg"
image montana = "images/fondos/Escena_Montaña_nueva.jpg"
 
label start:

    "Antes de comenzar, dime tu nombre."

    $ nombre_personaje = renpy.input("Escribe tu nombre:")
    $ nombre_personaje = nombre_personaje.strip()

    if nombre_personaje == "":
        $ nombre_personaje = "Isaac"

    # ahora cambiamos el nombre del personaje
    $ i.name = nombre_personaje
    show inicio_nubes
    
    "Despiertas desorientado en un lugar que no conoces"
    i "Donde estoy?? Q... que paso??"
    
    show escena_playa


    "Observas a tu al rededor y no ves a nadie, solo arena, mar y palmeras.
    No recuerdas que paso, ni como terminaste en este lugar, solo que ibas en un avion.
    Decides caminar por la orilla en busca de respuestas."

    "Pasa el tiempo y de repente escuchas un grito en direccion al mar.
    Observas desde lejos y ves una silueta."

    show isaac at left

    i "Alguien se esta Ahogando!!"
    hide isaac
    "Saltas al agua sin dudar y vas a su rescate."

    "Logras traer al muchacho a la orilla con gran esfuerzo."
    
    show isaac at left

    show porky_triste at right
    "(Fatigado y sin aliento)"

    i "Estas ... bien??"

    "El muchacho responde entre toses."
    hide porky_triste
    show porky_alegre at right
    
    p "Uff muchas gracias (Coff cof)."
    
    call acto1_pregunta_estado_nombre
    "El Muchacho toma sus lentes que habia dejado en la arena."
    p "Gracias por haberme salvado."
    call preguntar_nombre
    call acto1_pregunta_reirse
    
    hide porky_triste
    show porky_neutro at right
    "Los muchachos deciden seguir caminando por la orilla."
    
    return









label acto1_pregunta_estado_nombre: 
    menu:
        "preguntarle como llego ahi":
            jump vio_algo  
        "preguntarle su nombre":
            jump preguntar_nombre  

label vio_algo:
    i "Por que te metiste al agua?"
    p "Crei haber visto algo, y decidi verlo mas de cerca."
    i "Estas aguas parecen engañar tu vision. Antes tambien me parecio haber visto algo. Pero desaparecio de repente."
    return

label preguntar_nombre:
    i "Me llamo Isaac, y vos como te llamas?"    
    p "Soy P... p... p... porky."
    $ p.name = "Porky"
    return

label acto1_pregunta_reirse: 
    menu:
        "Reirse":
            jump reise_de_su_nombre  
        "Viste a alguien mas?":
            jump vio_a_alguien
    
label reise_de_su_nombre:
    i "Que nombre curioso jajajaja."
    hide porky_alegre
    show porky_triste at right
    p "Todos me hacen burla..."
    return

label vio_a_alguien:
    i "Estuve caminando un largo rato pero no me he encontrado con nadie, y vos?"
    p "No he encontrado a nadie, solo a vos."
    return

#     show fondo

#     show isaac at left
#     i "¿Quien eres tu?"

#     show jordan_alegre at right
#     j "Me dicen Porky"

#     call menu_reirse

#     show jordan_triste at right

#     jump mensaje_demo

# label menu_reirse:
#     menu:
#         # "¿Te ries, reirse o no?"
#         "Reirse":
#             jump reirse
#         "No reirse":
#             jump no_reirse

# label reirse:
#     i "Jajaja, ¡Porky, Porky!."
#     return

# label no_reirse:
#     i "JAJAJAJAJAJAJA."
#     return

# label mensaje_demo:
#     "Esta fue la demo de The Forgotten Ones"
#     return
