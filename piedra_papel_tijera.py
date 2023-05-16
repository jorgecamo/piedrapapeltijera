import random
"""
En este fichero se implementa el juego de piedra papel o tijera mdificado, 
este juego es contra el ordenador, y se ha añadido una opcion mas que es lagarto,
tambien hemos añadido en la rama test el numero de intentos, y se juega tantas 
veces como numero de intentos hay y quien gane mas es el ganador.
Te va a devolver quien gana y cuantas veces ha ganado.
---
"""
Piedra = 'piedra'
Papel = 'papel'
Tijera = 'tijera'
Lagarto = 'lagarto'
Opciones = [Piedra, Papel, Tijera, Lagarto]
GanaUsuario = [[Papel, Piedra], [Tijera, Papel], [Piedra, Tijera],
               [Piedra, Lagarto], [Lagarto, Papel], [Tijera, Lagarto]]
GanaOrdenador = [[Piedra, Papel], [Papel, Tijera], [Tijera, Piedra],
                 [Lagarto, Piedra], [Papel, Lagarto], [Lagarto, Tijera]]


def EleccionAlAzar():
    """
    Este metodo elige una opcion para que juegue el ordenador
    :return: **Opcion aleatoria de las 4 disponibles**
    """
    OpcionAleatoria = random.choice(Opciones)
    return OpcionAleatoria


def Resultado(eleccionHumano, eleccionOrdenador):
    """
    Este metodo verifica quien gana, comparando los resultados con la lista que hay arriba que indica
    quien gana segun lo que toque.
    :param eleccionHumano: **String de las opciones que hay**
    :param eleccionOrdenador: **Opcion aleatoria de las 4 disponibles**
    :return: **Int segun quien gane o si quedan empate**
    """
    if [eleccionHumano, eleccionOrdenador] in GanaUsuario:
        return 1
    elif [eleccionHumano, eleccionOrdenador] in GanaOrdenador:
        return -1
    return 0


print("JUEGO : Piedra, papel , tijera y lagarto")
Nombre = input("Dime como te llamas: ")
Intentos = int(input("Cuantos intentos quieres ? "))
GanadasOrdenador = 0
GanadasUsuario = 0
while Intentos > 0:
    EleccionOrdenador = EleccionAlAzar()
    EleccionHumano = 0
    while True:
        Movimiento = input("Selecciona un movimiento ('p' para piedra / 'a' para papel /"
                           " 't' para tijeras / 'l' para lagarto /'TERMINAR' para acabar): ").lower()
        print(f"Elección del ordenador: {EleccionOrdenador}")
        if 'terminar' in Movimiento:
            print("Tienes miedo?")
            break
        if 'p' in Movimiento or 'a' in Movimiento or 't' in Movimiento or 'l' in Movimiento:
            if 'a' in Movimiento:
                EleccionHumano = Papel
            elif 'l' in Movimiento:
                EleccionHumano = Lagarto
            elif 't' in Movimiento:
                EleccionHumano = Tijera
            elif 'p' in Movimiento:
                EleccionHumano = Piedra
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
    print()
if GanadasOrdenador > GanadasUsuario:
    print("Ha ganado el ordenador, y ha ganado " + str(GanadasOrdenador) + " veces")
elif GanadasUsuario > GanadasOrdenador:
    print("Ha ganado " + Nombre + " , y ha ganado " + str(GanadasUsuario) + " veces")
else:
    print("Han quedado empate")
