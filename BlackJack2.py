import random

cartas = { 
    chr(0x1f0a1): 11, 
    chr(0x1f0a2): 2, 
    chr(0x1f0a3): 3, 
    chr(0x1f0a4): 4, 
    chr(0x1f0a5): 5, 
    chr(0x1f0a6): 6, 
    chr(0x1f0a7): 7, 
    chr(0x1f0a8): 8, 
    chr(0x1f0a9): 9, 
    chr(0x1f0aa): 10, 
    chr(0x1f0ab): 10, 
    chr(0x1f0ad): 10, 
    chr(0x1f0ae): 10, 
} 

def obtener_valor_carta(carta):
    return cartas[carta]

def barajar_cartas():
    return list(cartas.keys())

def jugar_blackjack():
    mazo = barajar_cartas()

    
    jugador_carta1 = random.choice(mazo)
    mazo.remove(jugador_carta1)
    jugador_carta2 = random.choice(mazo)
    mazo.remove(jugador_carta2)

    jugador_puntuacion = obtener_valor_carta(jugador_carta1) + obtener_valor_carta(jugador_carta2)

    print(f"Jugador: Cartas [{jugador_carta1}, {jugador_carta2}], Puntuación: {jugador_puntuacion}")


    banca_carta1 = random.choice(mazo)
    mazo.remove(banca_carta1)
    banca_carta2 = random.choice(mazo)

    banca_puntuacion = obtener_valor_carta(banca_carta1) + obtener_valor_carta(banca_carta2)

    print(f"Banca: Cartas [{banca_carta1}, {banca_carta2}], Puntuación: {banca_puntuacion}")

    
    while True:
        tomar_carta = input("¿Quieres tomar otra carta? (s/n): ").lower()
        if tomar_carta == 's':
            nueva_carta = random.choice(mazo)
            nueva_carta_banca = random.choice(mazo)
            mazo.remove(nueva_carta)
            mazo.remove(nueva_carta_banca)
            jugador_puntuacion += obtener_valor_carta(nueva_carta)
            banca_puntuacion += obtener_valor_carta(nueva_carta_banca)
            print(f"Jugador: Nueva carta [{nueva_carta}], Puntuación: {jugador_puntuacion}")

            if banca_puntuacion > 21 and jugador_puntuacion > 21:
                print("La banca y tú habéis perdido")
                break
            elif jugador_puntuacion == 21:
                print ("¡¡Has ganado!!")
                break
            elif banca_puntuacion > 21:
                print("La bacanca ha perdido. ¡Tú ganas!")
                break
            elif jugador_puntuacion > 21:
                print("¡Te has pasado de 21! Has perdido.")
                break
        elif tomar_carta == 'n':
            
            if jugador_puntuacion == banca_puntuacion:
                print("Has empatado con la banca.")
                break
            elif jugador_puntuacion > banca_puntuacion:
                print("¡Has ganado a la banca!")
                break
            elif jugador_puntuacion < banca_puntuacion:
                print("¡Te ha ganado la banca!")
            break
        else:
            print("Respuesta no válida. Por favor, ingresa 's' para sí o 'n' para no.")


if __name__ == "__main__":
    jugar_blackjack()
