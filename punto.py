import math

class Punto:
    def __init__(self, x=0, y=0):
        """Constructor con valores por defecto"""
        self.x = x
        self.y = y

    def __str__(self):
        """Mostrar el punto en formato (X,Y)"""
        return f"({self.x}, {self.y})"

    def cuadrante(self):
        """Indica en qué cuadrante o eje está el punto"""
        if self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "Cuarto cuadrante"
        elif self.x == 0 and self.y != 0:
            return "Está sobre el eje Y"
        elif self.x != 0 and self.y == 0:
            return "Está sobre el eje X"
        else:
            return "Está en el origen"

    def vector(self, otro):
        """Devuelve el vector entre dos puntos"""
        return (otro.x - self.x, otro.y - self.y)

    def distancia(self, otro):
        """Calcula la distancia entre dos puntos"""
        return math.sqrt((otro.x - self.x)**2 + (otro.y - self.y)**2)




