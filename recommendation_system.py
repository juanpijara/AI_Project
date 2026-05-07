# recommendation_system.py
# Sistema de recomendación simple usando Python y GitHub Copilot

print("===================================")
print(" SISTEMA DE RECOMENDACIÓN DE IA ")
print("===================================")

# Base de datos de recomendaciones
recommendations = {
    "Accion": [
        "John Wick",
        "Mad Max: Fury Road",
        "Avengers Endgame"
    ],
    "Comedia": [
        "Son Como Niños",
        "Superbad",
        "Ted"
    ],
    "Terror": [
        "El Conjuro",
        "It",
        "Scream"
    ],
    "Ciencia Ficcion": [
        "Interstellar",
        "Matrix",
        "Blade Runner 2049"
    ],
    "Anime": [
        "Naruto",
        "Attack on Titan",
        "Demon Slayer"
    ]
}

# Solicitar género al usuario
genre = input(
    "Ingrese un género (Accion, Comedia, Terror, Ciencia Ficcion, Anime): "
).title()

# Mostrar recomendaciones
if genre in recommendations:
    print("\nRecomendaciones para ti:\n")

    for item in recommendations[genre]:
        print("-", item)

else:
    print("\nLo sentimos, no tenemos recomendaciones para ese género.")

print("\nGracias por usar el sistema de recomendación.")