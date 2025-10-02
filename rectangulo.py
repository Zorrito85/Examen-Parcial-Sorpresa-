from punto import Punto

class Rectangulo:
    def __init__(self, p1=None, p2=None):
        """Constructor con dos puntos (si no, usa el origen)"""
        if p1 is None:
            p1 = Punto()
        if p2 is None:
            p2 = Punto()
        self.p1 = p1
        self.p2 = p2

    def base(self):
        """Devuelve la base (distancia en X)"""
        return abs(self.p2.x - self.p1.x)

    def altura(self):
        """Devuelve la altura (distancia en Y)"""
        return abs(self.p2.y - self.p1.y)

    def area(self):
        """Devuelve el área del rectángulo"""
        return self.base() * self.altura()

