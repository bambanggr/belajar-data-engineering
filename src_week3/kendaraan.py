class Kendaraan:
    # eng_name = "Transportation" #class attribute
    bahan_bakar = "Bensin" #class attribute

    def __init__(self,nama, warna, jml_roda):
        self.nama=nama #instance attribute
        self.warna=warna #instance attribute
        self.jml_roda=jml_roda #instance attribute
    
    def maju(self): #instance method
        # self.gerak=gerak
        print(self.nama, "Sedang Maju")
    
    def mundur(self): #instance method
        # self.gerak=gerak
        print(self.nama, "Sedang Mundur")

    def gerakan(self, gerak): #instance method
        print(self.nama, "Sedang",gerak)

    @staticmethod
    def isi_bahan_bakar():
        print(Kendaraan.bahan_bakar, "Sedang Diisi, Static Method")

    @classmethod
    def isi_bahan_bakar2(cls,param2=None):
        if(param2 != None):
            print(cls.bahan_bakar, param2,"Sedang diisi, Class Method")
        else:
            print("Tidak Ada Kendaraan Yang di Isi")


class Pesawat(Kendaraan):
    bahan_bakar = "Avtur"

    def __init__(self, nama):
        self.nama=nama
    
    @staticmethod #contoh overriding
    def isi_bahan_bakar():
        print(Pesawat.bahan_bakar, "Sedang diisi")

class Mobil(Kendaraan):
    bahan_bakar = "Solar"

    def __init__(self, nama):
        self.nama=nama
    
    @staticmethod
    def isi_bahan_bakar():
        print(Mobil.bahan_bakar, "Sedang diisi")
    
    @classmethod #contoh overloading
    def belok(cls, belok=None):
        if(belok != None):
            print("Mobil sedang belok ", belok)
        else:
            print("Lurus, Tidak Belok-Belok")


obj_kendaraan = Kendaraan("Truck","Merah",12)
# obj_kendaraan.isi_bahan_bakar2()

obj_pesawat = Pesawat("Boeing 999")
# obj_pesawat.isi_bahan_bakar()

obj_mobil = Mobil("Mobil2an")
obj_mobil.belok("Kanan")
obj_mobil.maju()