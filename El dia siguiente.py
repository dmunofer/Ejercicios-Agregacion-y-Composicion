class Empresa():
    def __init__(self, empresa):
        self.empresa = empresa




    class Ciudad(Empresa, Edificio):

        def __init__(self, ciudad):
            self.ciudad = ciudad



        class Edificio(Empresa, Ciudad):
            def __init__(self, edificio):
                self.edificio = edificio




            class Empleado(Empresa, Edificio):
                def __init__(self, empleado):
                    self.empleado = empleado