import random

Piedra = 'piedra'
Papel = 'papel'
Tijera = 'tijera'
Opciones = [Piedra, Papel, Tijera]
GanaUsuario = [[Papel, Piedra], [Tijera, Papel], [Piedra, Tijera]]
GanaOrdenador = [[Piedra, Papel], [Papel, Tijera], [Tijera, Piedra]]


def EleccionAlAzar():
    OpcionAleatoria = random.choice(Opciones)
    return OpcionAleatoria


def Resultado(eleccionHumano, eleccionOrdenador):
    if [eleccionHumano, eleccionOrdenador] in GanaUsuario:
        return 1
    elif [eleccionHumano, eleccionOrdenador] in GanaOrdenador:
        return -1
    return 0


print("JUEGO : Piedra, papel y tijera")
Nombre = input("Dime como te llamas: ")
Intentos = int(input("Cuantos intentos quieres ? "))
GanadasOrdenador = 0
GanadasUsuario = 0
while Intentos > 0:
    EleccionOrdenador = EleccionAlAzar()
    EleccionHumano = 1
    while True:
        Movimiento = input("Selecciona un movimiento ('p' para piedra / 'a' para papel /"
                           " 't' para tijeras): ").lower()
        print(f"Elección del ordenador: {EleccionOrdenador}")
        if 'p' in Movimiento or 'a' in Movimiento or 't' in Movimiento:
            if 'p' in Movimiento:
                EleccionHumano = Piedra
            elif 'a' in Movimiento:
                EleccionHumano = Papel
            elif 't' in Movimiento:
                EleccionHumano = Tijera
            print(f"Elección del usuario: {EleccionHumano}")
            if Resultado(EleccionHumano, EleccionOrdenador) == 1:
                GanadasUsuario += 1
            elif Resultado(EleccionHumano, EleccionOrdenador) == -1:
                GanadasOrdenador += 1
            elif Resultado(EleccionHumano, EleccionOrdenador) == 0:
                print("Empate !!!")
            break
        else:
            print("Entrada incorrecta. Vuelve a intentar.")
    Intentos -= 1
if GanadasOrdenador > GanadasUsuario:
    print("Ha ganado el ordenador, y ha ganado " + str(GanadasOrdenador) + " veces")
elif GanadasUsuario > GanadasOrdenador:
    print("Ha ganado " + Nombre + " , y ha ganado " + str(GanadasUsuario) + " veces")
else:
    print("Han quedado empate")
