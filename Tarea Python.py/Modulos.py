class Estudiante:
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera

    def presentarse(self):
        return f"Hola, mi nombre es {self.nombre} y estudio {self.carrera}."
    