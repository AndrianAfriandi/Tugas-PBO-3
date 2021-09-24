class Laptop:
    def __init__(self, Warna, RAM, Merk):
        self.Warna = Warna
        self.RAM = RAM
        self.Merk = Merk

    def printname(self):
        print(self.Warna)
        print(self.RAM)
        print(self.Merk)

class IOS(Laptop):
     def __init__(self, Warna, RAM, Merk):
         Laptop.__init__(self, Warna, RAM, Merk)
         self.KapasistasBaterai = "10000mAH"

     def IOS(Self):
        print("Warna             : ", Self.Warna)
        print("RAM               : ", Self.RAM)
        print("Merk              : ", Self.Merk)
        print("Kapasitas Baterai : ", Self.KapasistasBaterai)
        print("******************************")


class Windows(Laptop):
    def __init__(self, Warna, RAM, Merk):
          Laptop.__init__(self, Warna, RAM, Merk)
          self.KapasistasBaterai = "8000mAH"

    def Windows(Self):
        print("Warna             : ", Self.Warna)
        print("RAM               : ", Self.RAM)
        print("Merk              : ", Self.Merk)
        print("Kapasitas Baterai : ", Self.KapasistasBaterai)
        print("******************************")
        

class Linux(Laptop):
    def __init__(self, Warna, RAM, Merk):
          Laptop.__init__(self, Warna, RAM, Merk)
          self.KapasistasBaterai = "5000mAH"

    def Linux(Self):
        print("Warna             : ", Self.Warna)
        print("RAM               : ", Self.RAM)
        print("Merk              : ", Self.Merk)
        print("Kapasitas Baterai : ", Self.KapasistasBaterai)
        print("******************************")

x = IOS("Merah", "12 GB", "Apple")
y = Windows("Hitam", "8 Gb", "Lenovo")
z = Linux("Biru", "4 GB", "Acer")

x.IOS()
y.Windows()
z.Linux()