from pembeli_tunai import pembeli_tunai
from pembeli_nontunai import pembeli_nontunai

def pilihan1(key):  # method pilihan
    if (key == 1):  # pengkondisian untuk menampilkan list hape
        print(" Kode 1 -- XioMay May 8 Pro         - Rp 10.000.000\n"
              " Kode 2 -- XioMay May 7 Pro         - Rp 8.500.000\n"
              " Kode 3 -- XioMay Redmay Note 8 Pro - Rp 7.500.000")
        x_1 = float(input("Masukkan Kode Angka sesuai HP pilihan Anda: "))
        Pilihan_1 = {
            1: "XioMay May 8 Pro: RAM 8GB, SNAPDRAGON 1100, STORAGE 256GB - Total tagihan Anda Rp 10.000.000",
            2: "XioMay May 7 Pro: RAM 6GB, SNAPDRAGON 990, STORAGE 256GB - Total tagihan Anda Rp 8.500.000",
            3: "XioMay Redmay Note 8 Pro: RAM 6GB, SNAPDRAGON 900, STORAGE 256GB - Total tagihan Anda Rp 7.500.000"
        }
        if (x_1 == 1):
            total = 10000000
        elif (x_1 == 2):
            total = 8500000
        elif (x_1 == 3):
            total = 7500000
        print('Anda ingin membeli: %s' % Pilihan_1.setdefault(x_1, 'Inputan hanya 1 - 3'))
        return total

    elif (key == 2):
        print(" Kode 1 -- XioMay May 8             - Rp 7.499.000\n"
              " Kode 2 -- XioMay Redmay Note 7 Pro - Rp 6.499.000\n"
              " Kode 3 -- XioMay May 7             - Rp 5.899.000\n"
              " Kode 4 -- XioMay Redmay Note 7     - Rp 5.000.000")
        x_2 = float(input("Masukkan Kode Angka sesuai HP pilihan Anda: "))
        Pilihan_2 = {
            1: "XioMay May 8: RAM 8GB, SNAPDRAGON 880, STORAGE 256GB - Total tagihan Anda Rp 7.499.000",
            2: "XioMay Redmay Note 7 Pro: RAM 6GB, SNAPDRAGON 800, Total tagihan Anda STORAGE 128GB - Rp 6.499.000",
            3: "XioMay May 7: RAM 6GB, SNAPDRAGON 780, STORAGE 128GB - Total tagihan Anda Rp 5.899.000",
            4: "XioMay Redmay Note 7: RAM 4GB, SNAPDRAGON 700, STORAGE  - Total tagihan Anda Rp 5.000.000"
        }
        if (x_2) == 1:
            total = 7499000
        elif (x_2) == 2:
            total = 6499000
        elif (x_2) == 3:
            total = 5899000
        elif (x_2) == 4:
            total = 5000000
        print('Anda ingin membeli: %s' % Pilihan_2.setdefault(x_2, 'Inputan hanya 1 - 4'))
        return total

    elif (key == 3):
        print(" Kode 1 -- XioMay May 6             - Rp 4.990.000\n"
              " Kode 2 -- XioMay Redmay Note 6 Pro - Rp 4.499.000\n"
              " Kode 3 -- XioMay Redmay Note 6     - Rp 3.899.000\n"
              " Kode 4 -- XioMay May 5             - Rp 3.000.000\n"
              " Kode 5 -- XioMay Redmay Note 5 Pro - Rp 2.500.000\n"
              " Kode 6 -- XioMay Redmay Note 5     - Rp 1.999.000")
        x_3 = float(input("Masukkan Kode Angka sesuai HP pilihan Anda: "))
        Pilihan_3 = {
            1: "XioMay May 6: RAM 8GB, SNAPDRAGON 690, STORAGE 128GB - Total tagihan Anda Rp 4.990.000",
            2: "XioMay Redmay Note 6 Pro: RAM 6GB, SNAPDRAGON 670, Total tagihan Anda STORAGE 128GB - Rp Rp 4.499.000",
            3: "XioMay Redmay Note 6: RAM 6GB, SNAPDRAGON 600, STORAGE 64GB - Total tagihan Anda Rp 3.899.000",
            4: "XioMay May 5: RAM 4GB, SNAPDRAGON 590, STORAGE 64GB - Total tagihan Anda Rp 3.000.000",
            5: "XioMay Redmay Note 5 Pro: RAM 4GB, SNAPDRAGON 550, STORAGE 64GB - Total tagihan Anda Rp 2.500.000",
            6: "XioMay Redmay Note 5: RAM 3GB, SNAPDRAGON 500, STORAGE 32GB - Total tagihan Anda Rp 1.999.000"
        }
        if (x_3 == 1):
            total = 4990000
        elif (x_3 == 2):
            total = 4499000
        elif (x_3 == 3):
            total = 3899000
        elif (x_3 == 4):
            total = 3000000
        elif (x_3 == 5):
            total = 2500000
        elif (x_3 == 6):
            total = 1990000
        print('Anda ingin membeli: %s' % Pilihan_3.setdefault(x_3, '\nInputan hanya 1 - 6'))
        return total

    else:
        print("Inputan hanya 1, 2, dan 3 \nSilahkan masukkan inputan sesuai kode yang tersedia")


while True:  # looping do while
    print("\nSelamat Datang di HK Mobile Store (OFFICIAL STORE XIOMAY)")
    print("     Terpercaya dalam Memberikan Pelayanan Prima")
    print(" Menyediakan Solusi bagi Anda untuk Membeli Handphone")
    print("Pilihan Range Harga Handphone: \n1 = Rp 10.000.000 - 7.500.000")
    print("2 = Rp 7.499.000  - 5.000.000\n3 = Rp 4.999.000  - 1.999.000")
    lagi = ""
    key = (int(input("masukkan pilihan: ")))
    harga_hp = pilihan1(key)
    if harga_hp:
        bayar_mode = input("Apakah Anda ingin membayar secara tunai/nontunai? ")
        if bayar_mode.lower() == "tunai":
            nama = input("Nama pembeli: ")
            tanggal = input("Tanggal: ")
            waktu = input("Waktu: ")
            jumlah = harga_hp
            pembeli = pembeli_tunai(nama, tanggal, waktu, jumlah)
            pembeli.identitas_pembeli()
            uang = (int(input("Masukkan total uang yang akan anda bayarkan: ")))
            kembali = uang - harga_hp
            print("Uang kembalian anda: ", kembali, "\nTerima Kasih")

        elif bayar_mode.lower() == "nontunai":
            nama = input("Nama pembeli: ")
            tanggal = input("Tanggal: ")
            waktu = input("Waktu: ")
            rek_pembeli = input("Rekening pembeli: ")
            jumlah = harga_hp
            pembeli = pembeli_nontunai(nama, tanggal, waktu, rek_pembeli, jumlah)
            pembeli.identitas_pembeli()
            uang = (int(input("Masukkan total uang yang akan anda bayarkan: ")))
            kembali = uang - harga_hp
            print("Uang kembalian anda: ", kembali, "\nTerima Kasih")


    lagi = str(input("Apakah anda ingin membeli lainnya?(YA/TIDAK) "))
    if (lagi.upper() != "YA"):
        break
print("\n  Program ini dibuat oleh: ")
print("Hajime Yudha-21120119120017\nKarisa Zihni-21120119130077")
print("     Teknik Komputer\n  Universitas Diponegoro\n         2020")