import random

frases = [
    "El éxito es la suma de pequeños esfuerzos repetidos día tras día.",
    "No esperes el momento perfecto, toma el momento y hazlo perfecto.",
    "La única forma de hacer un gran trabajo es amar lo que haces.",
    "Los sueños no tienen fecha de caducidad, nunca es tarde para perseguirlos.",
    "Cada día es una nueva oportunidad para cambiar tu vida.",
    "Pudrete, rie"
]

frase_elegida = random.choice(frases)

print("=" * 60)
print(f"  {frase_elegida}")
print("=" * 60)