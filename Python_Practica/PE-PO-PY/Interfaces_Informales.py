class Mando:
    def siguiente_canal(self):
        pass
    def canal_anterior(self):
        pass
    def subir_volumen(self):
        pass
    def bajar_volumen(self):
        pass
    
#Herencia
class MandoSamsung(Mando):
    def siguiente_canal(self):
        print("Samsung->Siguiente")
    def canal_anterior(self):
        print("Samsung->Anterior")
    def subir_volumen(self):
        print("Samsung->Subir Volumen")
    def bajar_volumen(self):
        print("Samsung->Bajar Volumen")


class MandoLG(Mando):
    def siguiente_canal(self):
        print("LG->Siguiente")
    def canal_anterior(self):
        print("LG->Anterior")
    def subir_volumen(self):
        print("LG->Subir Volumen")
    def bajar_volumen(self):
        print("LG->Bajar Volumen")
    
mando_samsung = MandoSamsung()
mando_lg = MandoLG()
mando_samsung.siguiente_canal()
mando_lg.bajar_volumen()