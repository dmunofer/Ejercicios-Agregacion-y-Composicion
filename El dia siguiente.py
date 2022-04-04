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
New_York = Ciudad()
Los_Angeles = Ciudad()
A = Edificio(New_York)
B = Edificio(New_York)
C = Edificio(Los_Angeles)
Sres_Martin = Empleado(YooHoo)
Salim = Empleado(YooHoo)
Sra_Xing = Empleado(YooHoo)