import random


class DadosDeLaSuerte:
    """
    Representa el juego Dados de la Suerte.

    La clase gestiona el flujo completo del juego, incluyendo
    el lanzamiento de dados, la evaluación del resultado y
    la interacción con el jugador.
    """

    def __init__(self) -> None:
        """
        Inicializa el estado inicial del juego.

        Se establecen los valores iniciales de los dados,
        la suma y el estado del juego.
        """
        self.dado_1: int = 0
        self.dado_2: int = 0
        self.suma: int = 0
        self.juego_activo: bool = True

    def lanzar_dados(self) -> None:
        """
        Lanza dos dados de manera aleatoria y calcula su suma.

        Los valores generados están entre 1 y 6, simulando
        el comportamiento de dados reales.
        """
        self.dado_1 = random.randint(1, 6)
        self.dado_2 = random.randint(1, 6)
        self.suma = self.dado_1 + self.dado_2

        print(f"🎲 Dados: {self.dado_1} y {self.dado_2} | Suma: {self.suma}")

    def evaluar_resultado(self) -> str:
        """
        Evalúa el resultado del lanzamiento de los dados.

        Según la suma obtenida:
        - 7 u 11: el jugador gana.
        - 2, 3 o 12: el jugador pierde.
        - Cualquier otro valor: el juego continúa.

        Returns
        -------
        str
            El estado del juego. Puede ser:
            - 'gana'
            - 'pierde'
            - 'continua'

        Examples
        --------
        >>> juego = DadosDeLaSuerte()
        >>> juego.suma = 7
        >>> juego.evaluar_resultado()
        'gana'
        """
        if self.suma in (7, 11):
            return "gana"

        if self.suma in (2, 3, 12):
            return "pierde"

        return "continua"

    def jugar(self) -> None:
        """
        Ejecuta el flujo principal del juego.

        El método controla:
        - El inicio del juego.
        - Los lanzamientos de dados.
        - La evaluación del resultado.
        - La decisión del jugador de continuar o no.

        El juego finaliza cuando el jugador gana, pierde
        o decide no lanzar más.
        """
        print("🎮 Bienvenido a Dados de la Suerte")

        while self.juego_activo:
            self.lanzar_dados()
            resultado = self.evaluar_resultado()

            if resultado == "gana":
                print("🎉 ¡Felicidades! Has ganado.")
                self.juego_activo = False

            elif resultado == "pierde":
                print("💀 Lo siento, has perdido.")
                self.juego_activo = False

            else:
                respuesta = input("¿Deseas volver a lanzar? (SI/NO): ").strip().upper()
                if respuesta != "SI":
                    print("👋 Has decidido terminar el juego.")
                    self.juego_activo = False

        print("🏁 Juego terminado. ¡Gracias por jugar!")


# Ejecución del juego
juego = DadosDeLaSuerte()
juego.jugar()
