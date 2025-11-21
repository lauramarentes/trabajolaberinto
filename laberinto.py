import random
def encontrar_posiciones(lab):
    pos_p = None
    monstruos = []

    filas = len(lab)
    columnas = len(lab[0])

    for i in range(filas):
        for j in range(columnas):
            if lab[i][j] == "P":
                pos_p = (i, j)
            elif lab[i][j] == "M":
                monstruos.append((i, j))

    return pos_p, monstruos



def imprimir_laberinto(lab):
    for fila in lab:
        linea = ""
        for elemento in fila:
            if elemento == 1:
                linea += "1 " 
            elif elemento == "P":
                linea += "P " 
            elif elemento == "M":
                linea += "M " 
            elif elemento == "S":
                linea += "S " 
            else:
                linea += str(elemento) + " " 
        print(linea)
    print()


# -----------------------------
# LABERINTO NIVEL ÚNICO 20x20
# -----------------------------
lab = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,"P",0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,0,1,0,1,"M",0,0,0,0,0,1,0,0,1,0,0,1],
    [1,"M",1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,1],
    [1,0,0,0,1,1,0,1,0,1,0,0,0,0,1,1,0,0,1,1],
    [1,1,1,0,1,0,0,1,0,1,0,0,0,0,1,0,0,1,0,1],
    [1,0,"M",0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,1,0,1,1,0,0,0,0,0,0,0,1,1],
    [1,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1,0,1],
    [1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,0,1],
    [1,0,0,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,1,1],
    [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,0,1,0,1,"M",0,0,0,0,0,1,0,0,1,0,0,1],
    [1,"M",1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,1],
    [1,0,0,0,1,1,0,1,0,1,0,0,0,0,1,1,0,0,1,1],
    [1,1,1,0,1,0,0,1,0,1,0,0,0,0,1,0,0,1,0,1],
    [1,0,"M",0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,1,0,1,1,0,0,0,0,0,0,0,1,1],
    [1,0,0,0,1,0,0,0,1,1,0,0,1,"S",0,0,0,1,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]   

(pos_i, pos_j), monstruos = encontrar_posiciones(lab)
vidas = 5
turno = 0  

movs = {
    "w": (-1, 0),
    "s": (1, 0),
    "a": (0, -1),
    "d": (0, 1)
}

jugando = True

print("Juego del Laberinto con Monstruo y Colores ANSI")
print("Cada 2 turnos el Monstruo se moverá aleatoriamente.\n")
imprimir_laberinto(lab)

while jugando:
    print("Vidas:", vidas)
    mov = input("Mover (w/a/s/d) o 'q' para salir: ")

    if mov == "q":
        print("Fin del juego.")
        jugando = False
    else:
        # Validación del movimiento sin usar "in"
        try:
            di, dj = movs[mov]
            movimiento_valido = True
        except KeyError:
            movimiento_valido = False

        if movimiento_valido:
            ni = pos_i + di
            nj = pos_j + dj
            casilla = lab[ni][nj]

            # 1) Chocar contra pared
            if casilla == 1:
                vidas -= 1
                print("Has chocado contra una pared. Pierdes una vida.")
                if vidas == 0:
                    print("Te quedaste sin vidas.")
                    jugando = False

            # 2) Llegar a salida
            elif casilla == "S":
                lab[pos_i][pos_j] = 0
                lab[ni][nj] = "P"
                #imprimir_laberinto(lab)
                print("¡Has ganado!")
                jugando = False

            # 3) Encontrar al monstruo
            elif casilla == "M":
                print("El monstruo te ha atrapado. Teletransporte aleatorio...")
                lab[pos_i][pos_j] = 0

                encontrada = False
                while encontrada == False:
                    filas = len(lab)
                    columnas = len(lab[0])
                    '''
                    random.randint(a, b):
                    - Genera un número entero aleatorio entre a y b.
                    - Incluye tanto a como b.
                    - Lo usamos para elegir una posición aleatoria dentro del laberinto.
                    '''
                    tele_i = random.randint(1, filas - 2)
                    tele_j = random.randint(1, columnas - 2)
                    if lab[tele_i][tele_j] == 0:
                        encontrada = True
                '''
                pos_i = tele_i
                pos_j = tele_j
                '''
                pos_i, pos_j = tele_i, tele_j
                lab[pos_i][pos_j] = "P"
                #imprimir_laberinto(lab)

            # 4) Casilla normal
            else:
                lab[pos_i][pos_j] = 0
                lab[ni][nj] = "P"
                '''
                pos_i = ni
                pos_j = nj
                '''
                pos_i, pos_j = ni, nj
                #imprimir_laberinto(lab)

            # ----------------------------
            # MOVIMIENTO DE TODOS LOS MONSTRUOS
        if turno % 2 == 0:  # Cada 2 turnos

            nuevos_monstruos = []

            for (mon_i, mon_j) in monstruos:
                '''
                list(movs.values()):
                - Obtiene todos los valores del diccionario 'movs'.
                - Cada valor es un desplazamiento (di, dj) para moverse.
                - Lo convertimos a lista para poder recorrerlo o elegir un movimiento aleatorio.
                '''
                # 4 direcciones
                direcciones = list(movs.values())
                posibles = []

                for d in direcciones:
                    mi = mon_i + d[0]
                    mj = mon_j + d[1]

                    # Solo mover si es un camino vacío
                    if lab[mi][mj] == 0:
                        posibles.append((mi, mj))

                # Elegir movimiento aleatorio si existe
                if len(posibles) > 0:
                    '''
                    random.choice(posibles):
                    - 'posibles' es una lista con todas las casillas a las que el monstruo puede moverse.
                    - random.choice() selecciona una de esas casillas al azar.
                    - Guardamos esa casilla en 'elegido' para mover el monstruo allí.
                    '''
                    elegido = random.choice(posibles)
                    nuevo_i, nuevo_j = elegido

                    lab[mon_i][mon_j] = 0
                    lab[nuevo_i][nuevo_j] = "M"

                    nuevos_monstruos.append((nuevo_i, nuevo_j))
                else:
                    # Monstruo sin movimiento
                    nuevos_monstruos.append((mon_i, mon_j))

            monstruos = nuevos_monstruos
            imprimir_laberinto(lab)



        else:
            print("Movimiento no válido.")