class BeatBox:
    __instancia = None

    def __new__(cls):
        if cls.__instancia is None:
            cls.__instancia = super().__new__(cls)
            # Inicializamos atributos en la primera instancia
            cls.__instancia.pistas = []
            cls.__instancia.volumen = 0
            cls.__instancia.efecto = "ninguno"
        return cls.__instancia

    def seleccionar_pista(self, nombre):
        self.pistas.append(nombre)
        print(f"🎵 Pista agregada: {nombre}")

    def ajustar_volumen(self, cambio):
        if cambio <=100:
         self.volumen = cambio
         print(f"🔊 Volumen ajustado a {self.volumen}")
        else:
         print("💢 El volumen debe estar entre 0 y 100.")

    def aplicar_efecto(self, efecto):
        efectos_validos = ["eco", "reverb", "distorsión", "ninguno"]

        if efecto not in efectos_validos:
            print("💢 Efecto no válido")
            return

        self.efecto = efecto
        print(f"✨ Efecto aplicado: {self.efecto}")

    def mostrar_estado(self):
        print("🎚 Estado de la BeatBox")
        if self.pistas:
            print(f"- Pistas guardadas: {', '.join(self.pistas)}")
        else:
            print("- Pistas guardadas: Ninguna")
        print(f"- Volumen: {self.volumen}")
        print(f"- Efecto: {self.efecto}")

while True:
    print("=" * 30)
    print("🎛 Consola BeatBox")
    print("1. Seleccionar pista de audio")
    print("2. Ajustar volumen")
    print("3. Aplicar efecto")
    print("4. Mostrar estado")
    print("5. Salir")
    print("=" * 30)
    opcion = input("Selecciona una opción: ")

    beatbox = BeatBox()  # Usamos siempre la misma instancia

    if opcion == "1":
        nombre = input("🎵 Nombre de la pista: ")
        beatbox.seleccionar_pista(nombre)

    elif opcion == "2":
        try:
            valor = int(input("🔊 Ajuste de volumen (+/-): "))
            beatbox.ajustar_volumen(valor)
        except ValueError:
            print("💢 Debes ingresar un número.")

    elif opcion == "3":
        efecto = input("✨ Efecto (eco / reverb / distorsión / ninguno): ").lower()
        beatbox.aplicar_efecto(efecto)

    elif opcion == "4":
        beatbox.mostrar_estado()

    elif opcion == "5":
        print("👋 chau chau")
        break

    else:
        print("💢 Opción no válida.")