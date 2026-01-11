import math

print("=== BangunDatar.py ===")

# Input nama
nama = input("Masukkan nama Anda: ")
print(f"Halo, {nama}")

# Array / list bangun datar
bangun_datar = [
    "Persegi",
    "Persegi Panjang",
    "Segitiga",
    "Lingkaran"
]

# ===== PERULANGAN UTAMA PROGRAM =====
while True:
    print("\nDaftar Bangun Datar:")

    # ===== PERULANGAN MENAMPILKAN MENU =====
    for i in range(len(bangun_datar)):
        print(f"{i + 1}. {bangun_datar[i]}")

    print("0. Keluar")

    pilihan = input("Pilih bangun datar (0-4): ")

    if pilihan == "0":
        print("\nTerima kasih telah menggunakan aplikasi ini 🙏")
        break

    elif pilihan == "1":
        sisi = float(input("Masukkan sisi: "))
        luas = sisi * sisi
        keliling = 4 * sisi

    elif pilihan == "2":
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        luas = panjang * lebar
        keliling = 2 * (panjang + lebar)

    elif pilihan == "3":
        alas = float(input("Masukkan alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        sisi = float(input("Masukkan sisi miring: "))
        luas = 0.5 * alas * tinggi
        keliling = alas + tinggi + sisi

    elif pilihan == "4":
        r = float(input("Masukkan jari-jari: "))
        luas = math.pi * r * r
        keliling = 2 * math.pi * r

    else:
        print("Pilihan tidak valid!")
        continue

    print("\nHasil Perhitungan:")
    print("Luas     :", luas)
    print("Keliling :", keliling)

    # ===== PERULANGAN KONFIRMASI =====
    ulang = input("\nHitung lagi? (Y/T): ")
    if ulang.lower() != "Y":
        print("\nTerima kasih telah menggunakan aplikasi ini 🙏")
        break

print("=== Program Selesai ===")
