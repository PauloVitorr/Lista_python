class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5
    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1


televisao = Televisao()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)
print('canal: {}'.format(televisao.canal))
televisao.aumenta_canal()
televisao.power()
print(televisao.ligada)
televisao.aumenta_canal()
print('Canal: {}'.format(televisao.canal))
televisao.diminui_canal()
televisao.diminui_canal()
print('Canal: {}'.format(televisao.canal))