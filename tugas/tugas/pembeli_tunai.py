class pembeli_tunai:
    def __init__(self, nama, tanggal, waktu, jumlah):
        self.nama = nama
        self.tanggal = tanggal
        self.waktu = waktu
        self.jumlah = jumlah

    def identitas_pembeli(self):
        print(f"\nPENJUALAN\t {self.tanggal}")
        print(f"         \t {self.waktu}")
        print(f"NAMA: {self.nama}")
        print(f"JUMLAH    : RP.   {self.jumlah}")
