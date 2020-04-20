class pembeli_nontunai:
    def __init__(self, nama, tanggal, waktu, rek_pembeli, jumlah):
        self.nama = nama
        self.waktu = waktu
        self.tanggal = tanggal
        self.rek_pembeli = rek_pembeli
        self.jumlah = jumlah

    def identitas_pembeli(self):
        print(f"\nPENJUALAN\t {self.tanggal}")
        print(f"         \t {self.waktu}")
        print(f"NAMA      : {self.nama}")
        print(f"DARI REK. : {self.rek_pembeli}")
        print(f"KE REK.   : 418801000524507")
        print(f"JUMLAH    : RP.      {self.jumlah}")