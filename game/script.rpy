# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define i = Character("Isaac")
define j = Character("Jordan")


image Isaac = "images/personajes/Isaac.png"
image personaje_alegre = "images/personajes/personaje_alegre.png"

image fondo = "images/fondos/fondo.png"


# El juego comienza aquí.

# label start:

#     # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
#     # defecto. Es posible añadir un archivo en el directorio 'images' con el
#     # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

#     scene bg room

#     # Muestra un personaje: Se usa un marcador de posición. Es posible
#     # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
#     # 'images'.

#     show eileen happy

#     # Presenta las líneas del diálogo.

#     e "Has creado un nuevo juego Ren'Py."

#     e "Añade una historia, imágenes y música, ¡y puedes presentarlo al mundo!"

#     # Finaliza el juego:

#     return

label start:

    show fondo

    show Isaac at left
    i "¿Quien eres tu?"

    show personaje_alegre at right
    j "Me dicen Porky"

    call menu_reirse

    jump mensaje_demo

label menu_reirse:
    menu:
        # "¿Te ries, reirse o no?"
        "Reirse":
            jump reirse
        "No reirse":
            jump no_reirse

label reirse:
    i "Jajaja, Porky, Porky!."
    return

label no_reirse:
    i "JAJAJAJAJAJAJAJ."
    return

label mensaje_demo:
    "Esta fue la demo de The Forgotten Ones"
    return
