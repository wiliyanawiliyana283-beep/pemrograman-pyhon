# PROGRAM PENENTUAN NILAI DAN TEMPAT BILANGAN
# menggunakan fungsi try_except untuk menangani kesalahan (error), jika user input selain angka
print("/nAPLIKASI PENENTUAN NILAI DAN TEMPAT BILANGAN")
# meminta input bilangan dari user
try:
    angka = int(input("\nMasukkan bilangan (maksimal 7 digit): "))

    # penentuan nilai tempat
    # membatasi jumlah angka yang di masukkan
    # jumlah angka ga boleh lebih dari dari 7 digit
    if 0 <= angka <= 9999999:

        # ambil nilai jutaan 
        jutaan = angka // 1000000
        # hitung sisa setelah di ambil jutaan 
        sisajutaan = angka % 1000000

        # ambil nilai ratus ribuan 
        ratusribuan = sisajutaan // 100000
        # hitung sisa setelah diambil ratus ribuannya 
        sisaratusribuan = sisajutaan % 100000

        # ambil nilai puluh ribuan 
        puluhribuan = sisaratusribuan // 10000
        # hitung sisa setelah diambil puluh ribuannya
        sisapuluhribuan = sisaratusribuan % 10000
        
          # ambil nilai ribuan 
        ribuan = sisapuluhribuan // 1000
        # hitung sisa setelah diambil ribuannya
        sisaribuan = sisapuluhribuan % 1000

        # ambil nilai ratusan dari sisaribuan
        ratusan = sisaribuan // 100
        # hitung sisa setelah diambil ratusannya
        sisaratusan = sisaribuan % 100

        # ambil nilai puluhan  dari sisaratusan 
        puluhan = sisaratusan // 10
        # sisa terakhir adalah satuan 
        satuan = sisaratusan % 10

        # menampilkan hasil sesuai dengan nilai tempat 
        print(f"\nAnda memasukkan bilangan {angka} dimana:")
        print(f"{jutaan} merupakan jutaan")
        print(f"{ratusribuan} merupakan ratusribuan")
        print(f"{puluhribuan} merupakan puluhribuan")
        print(f"{ribuan} merupakan ribuan")
        print(f"{ratusan} merupakan ratusan")
        print(f"{puluhan} merupakan puluhan")
        print(f"{satuan} merupakan satuan")

    else:
        print("Harap masukkan bilangan antara 0-999999.")

except ValueError:
    print("input tidak validi Harap masukkan angka.")
    