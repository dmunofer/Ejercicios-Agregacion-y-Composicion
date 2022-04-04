class Empresa():
    def __init__(self, empresa):
        self.empresa = empresa

class Ciudad(Empresa):

    def __init__(self, ciudad):
        self.ciudad = ciudad

class Edificio(Ciudad):
    def __init__(self, edificio):
        self.edificio = edificio

class Empleado(Empresa):
    def __init__(self, empleado):
        self.empleado = empleado



YooHoo = Empresa('YooHoo!')
New_York = Ciudad('New York')
Los_Angeles = Ciudad('Los Angeles')
A = Edificio('A')
B = Edificio('B')
C = Edificio('C')
Sres_Martin = Empleado('Sres. Martin')
Salim = Empleado('Salim')
Sra_Xing = Empleado('Sra Xing')