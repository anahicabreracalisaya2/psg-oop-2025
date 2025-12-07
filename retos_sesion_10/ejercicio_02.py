class Monstruo:
    tipo = "Monstruo"

    def luchar(self):
        print(f"{self.tipo} 🧟‍♂️ listo para luchar")


class Dragon(Monstruo):
    tipo = "Dragón"

    def luchar(self):
        print("🐉 El Dragón ruge y se prepara para la batalla")


class Zombi(Monstruo):
    tipo = "Zombi"

    def luchar(self):
        print("🧟‍♂️ El Zombi avanza lentamente hacia el combate")


class Vampiro(Monstruo):
    tipo = "Vampiro"

    def luchar(self):
        print("🧛‍♂️ El Vampiro se transforma y se lanza al ataque")


class Spawner:
    def crear(self):
        pass


class SpawnerDragon(Spawner):
    def crear(self):
        return Dragon()


class SpawnerZombi(Spawner):
    def crear(self):
        return Zombi()


class SpawnerVampiro(Spawner):
    def crear(self):
        return Vampiro()


def crear_monstruo(tipo):
    tipo = tipo.lower()

    if tipo in ("dragon", "dragón"):
        return SpawnerDragon().crear()
    if tipo == "zombi":
        return SpawnerZombi().crear()
    if tipo == "vampiro":
        return SpawnerVampiro().crear()

    else: print("❌ Monstruo no disponible. Intente de nuevo")


class Jugador:
    nombre = "Jugador"

    def elegir_monstruo(self, eleccion):
        return crear_monstruo(eleccion)


def resolver_batalla(m1, m2):
    reglas = {
        "Dragón": {"fuerte": "Zombi", "debil": "Vampiro"},
        "Zombi": {"fuerte": "Vampiro", "debil": "Dragón"},
        "Vampiro": {"fuerte": "Dragón", "debil": "Zombi"},
    }

    t1 = m1.tipo
    t2 = m2.tipo

    if t1 == t2:
        return "🤝 ¡Empate! Ambos monstruos son iguales."

    if reglas[t1]["fuerte"] == t2:
        return f"🏆 El {t1} gana — es fuerte contra {t2}"

    if reglas[t1]["debil"] == t2:
        return f"❌ El {t1} pierde — es débil contra {t2}"

    return "Resultado inesperado."


while True:
    print("\n🧩 Selección de Monstruos 🧩")

    p1 = input("Jugador 1: Elige tu monstruo (dragon/zombi/vampiro/salir): ").strip().lower()
    if p1 == "salir":
        print("👋 Saliendo del simulador.")
        break

    p2 = input("Jugador 2: Elige tu monstruo (dragon/zombi/vampiro/salir): ").strip().lower()
    if p2 == "salir":
        print("👋 Saliendo del simulador.")
        break

    try:
        j1 = Jugador()
        j2 = Jugador()

        m1 = j1.elegir_monstruo(p1)
        m2 = j2.elegir_monstruo(p2)

        m1.luchar()
        m2.luchar()

        print("\n⚔️ RESULTADO DE LA BATALLA ⚔️")
        print(resolver_batalla(m1, m2))

    except ValueError as e:
        print(e)
