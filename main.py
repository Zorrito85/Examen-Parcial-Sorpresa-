from punto import Punto, Rectangulo

# Crear los puntos
A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto(0, 0)

# Imprimir los puntos
print("Punto A:", A)
print("Punto B:", B)
print("Punto C:", C)
print("Punto D:", D)

# Consultar cuadrantes
print("Cuadrante de A:", A.cuadrante())
print("Cuadrante de C:", C.cuadrante())
print("Cuadrante de D:", D.cuadrante())

# Consultar vectores AB y BA
print("Vector AB:", A.vector(B))
print("Vector BA:", B.vector(A))

# Consultar distancia entre A y B y entre B y A
print("Distancia A-B:", A.distancia(B))
print("Distancia B-A:", B.distancia(A))

# Determinar cuál está más lejos del origen
origen = Punto(0, 0)
distancias = {
    'A': A.distancia(origen),
    'B': B.distancia(origen),
    'C': C.distancia(origen)
}
mas_lejos = max(distancias, key=distancias.get)
print(f"El punto más lejos del origen es: {mas_lejos} con distancia {distancias[mas_lejos]}")

# Crear un rectángulo con A y B
rect = Rectangulo(A, B)
print("Base del rectángulo:", rect.base())
print("Altura del rectángulo:", rect.altura())
print("Área del rectángulo:", rect.area())
