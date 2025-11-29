import random

class PiedraPapelTijera:
    __instancia = None
    iniciado = False
    puntaje_jugador = 0
    puntaje_computadora = 0
    opciones = ["piedra", "papel", "tijera"]

    def __new__(cls):
        if cls.__instancia is None:
            cls.__instancia = super().__new__(cls)
        return cls.__instancia

    def iniciar(self):
        if self.iniciado:
            print("💢 El juego ya está en curso.")
            return
        print("🎮 Iniciando partida de Piedra, Papel o Tijera")
        self.iniciado = True

    def finalizar(self):
        print("❗ Partida finalizada.")
        self.iniciado = False

    def competir(self, eleccion_jugador, jugador):
        if not self.iniciado:
            print("💢 El juego no ha iniciado.")
            return

        eleccion_pc = random.choice(self.opciones)
        print(f"🤖 La computadora eligió: {eleccion_pc}")

        if eleccion_jugador == eleccion_pc:
            print("⚖️ Empate.")
        elif (eleccion_jugador == "piedra" and eleccion_pc == "tijera") or \
             (eleccion_jugador == "papel" and eleccion_pc == "piedra") or \
             (eleccion_jugador == "tijera" and eleccion_pc == "papel"):
            print("🎉 ¡Ganaste la ronda!")
            self.puntaje_jugador += 1
        else:
            print("💀 La computadora gana la ronda.")
            self.puntaje_computadora += 1

    def mostrarPuntaje(self):
        print("\n🏆 PUNTAJES ACUMULADOS")
        print(f"👤 Jugador: {self.puntaje_jugador}")
        print(f"🤖 Computadora: {self.puntaje_computadora}\n")

    def reiniciarJuego(self):
        print("🔄 Reiniciando puntajes...")
        self.puntaje_jugador = 0
        self.puntaje_computadora = 0

    def estado(self):
        return self.iniciado


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.eleccion = None

    def __str__(self):
        return f"🕹️ {self.nombre}"

    def jugar(self):
        PiedraPapelTijera().iniciar()

    def competir(self, eleccion):
        self.eleccion = eleccion
        PiedraPapelTijera().competir(eleccion, self)

    def reiniciar(self):
        PiedraPapelTijera().reiniciarJuego()

    def finalizar(self):
        PiedraPapelTijera().finalizar()

    def jugando(self):
        return PiedraPapelTijera().estado()


print("🎮 Bienvenido a Piedra, Papel o Tijera, que comience el juego!!!")

nombre = input("💬 Ingresa tu nombre para jugar : ")
jugador = Jugador(nombre)

while True:
    print("="*10)
    print("📌 MENÚ")
    print("""
          
1️. Iniciar nueva partida
2️. Mostrar puntajes
3️. Reiniciar juego
4️. Salir
""")
    print("="*10)

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        jugador.jugar()
        while jugador.jugando():
            eleccion = input(" Elige piedra, papel, tijera 🪨📄✂️ o 'salir': ").lower()
            
            if eleccion == "salir":
                jugador.finalizar()
                break
            elif eleccion in PiedraPapelTijera().opciones:
                jugador.competir(eleccion)
            else:
                print("❌ Opción no válida. Intenta nuevamente.")

    elif opcion == "2":
        PiedraPapelTijera().mostrarPuntaje()

    elif opcion == "3":
        jugador.reiniciar()

    elif opcion == "4":
        print("👋 Gracias por jugar. ¡Hasta lueguito!")
        break

    else:
        print("❌ Opción no válida.")
