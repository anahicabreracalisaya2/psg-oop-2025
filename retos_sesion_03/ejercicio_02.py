class Cocinero:
    productividad_total = 0  # Métrica acumulada entre todos los cocineros

    recetas_sistema = {
        "pan": ["harina", "agua"],
        "pizza": ["harina", "agua", "sal", "tomate", "queso"],
        "galleta": ["harina", "agua", "sal", "chocolate"]
    }

    def __init__(self, nombre, ingredientes):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.intentos = 0
        self.logros = 0
        self.productividad = 0

    def _puede_cocinar(self, receta):
        if receta in Cocinero.recetas_sistema:
            requeridos = Cocinero.recetas_sistema[receta]
            i = 0
            while i < len(requeridos):
                if requeridos[i] not in self.ingredientes:
                    return False
                i += 1
            return True
        else:
            return False

    def _cocinar(self, receta):
        self.intentos += 1
        if self._puede_cocinar(receta):
            self.logros += 1
            self.productividad += 1
            Cocinero.productividad_total += 1
            print(f"{self.nombre} cocinó {receta} exitosamente 🎉")
        else:
            print(f"{self.nombre} no pudo cocinar {receta} 😢 (ingredientes faltantes)")

    def pan(self):
        self._cocinar("pan")

    def pizza(self):
        self._cocinar("pizza")

    def galleta(self):
        self._cocinar("galleta")

    def resumen(self):
        return {
            "nombre": self.nombre,
            "intentos": self.intentos,
            "logros": self.logros,
            "productividad individual": self.productividad
        }


# Cocineros con diferentes ingredientes
c1 = Cocinero("Anahi", ["harina", "agua", "sal", "chocolate"])
c2 = Cocinero("Luis", ["harina", "agua", "sal", "tomate", "queso"])
c3 = Cocinero("Marta", ["harina", "agua"])

# Pruebas de cocina
c1.galleta()
c1.pizza()
c2.pizza()
c2.pan()
c3.pan()
c3.galleta()

# Resúmenes individuales
print("\n📊 Resúmenes individuales:")
print(c1.resumen())
print(c2.resumen())
print(c3.resumen())

# Métrica agregada
print(f"\n🔥 Productividad total acumulada: {Cocinero.productividad_total}")