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
while 1:
    Jugar = input("Quieres jugar? (s/n): ")
    if 's' in Jugar.lower():
        EleccionOrdenador = EleccionAlAzar()
        EleccionHumano = 1
        while True and 1 == 1:
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
                    print("Has ganado " + Nombre)
                elif Resultado(EleccionHumano, EleccionOrdenador) == -1:
                    print("Gana el ordenador !!!")
                elif Resultado(EleccionHumano, EleccionOrdenador) == 0:
                    print("Empate !!!")
                break
            else:
                print("Entrada incorrecta. Vuelve a intentar.")
    elif 'n' in Jugar.lower():
        break
    else:
        print('Entrada incorrecta. Vuelve a intentar.')
    print()
