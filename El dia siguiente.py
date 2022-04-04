class Empresa():
    def __init__(self, empresa):
        self.empresa = empresa

class Ciudad(Empresa):

    def __init__(self, ciudad):
        self.ciudad = ciudad

class Edificio(Ciudad):
    def __init__(self, edificio):
        self.edificio = edificio

class Empleado(Edificio):
    def __init__(self, empleado):
        self.empleado = empleado