orientaciones = ["NORTE","SUR", "ESTE","OESTE"]

class Pared():
    def __init__(self,orientacion):
        if orientacion == orientaciones[0]:
            self.orientacion = "NORTE"
        elif orientacion == orientaciones[1]:
            self.orientacion = "SUR"
        elif orientacion == orientaciones[2]:
            self.orientacion= "ESTE"
        elif orientacion == orientaciones[3]:
            self.orientacion = "OESTE"
class Cristal(Pared):
    def __init__(self,orientacion,superficie):
        self.orientacion = orientacion
        self.superficie = superficie

class Ventana(Cristal):
    def __init__(self,num):
        self.ventana= (Pared(),num)

class Casa(Pared(),Ventana()):
    def __init__(self,pared,ventana):
        self.pared = pared
        self.ventana = ventana
    def __str__(self):
        return str(self.pared)+str(self.ventana)
    def superficie_acristalada(self):
        suma=0
        for e in self.ventana:
            suma=suma+e
        return suma

class ParedCortina(Cristal):
    def __init__(self,orientacion,superficie):
        self.orientacion = orientacion
        self.superficie = superficie

