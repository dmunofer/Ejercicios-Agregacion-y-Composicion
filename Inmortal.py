class Yin: pass
class Yang:
    def __del__(self):
        print("Yang destruido")

yin = Yin()
yang = Yang()
yin.yang = yang


# El mensaje Yang destruido no llega a mostrarsi ni siquiera después del '?' ya que no hay un método __str__ definido en nuestra clase Yang