import sys
import os

class Mahasiswa:
    def _init_(self, nim=0, nama=""):
        self.nim = nim
        self.nama = nama

dataSiswa = []

def menu():
    os.system('cls')
    print("Menu Aplikasi Data Siswa LinkedList python")
    print("")
    print("1. Input Data Siswa")
    print("2. Tampilkan Data Siswa")
    print("3. Update Data Siswa")
    print("4. Hapus Data Siswa")
    print("5. Author")
    print("6. Keluar Aplikasi")
    try:
        pilih = int(input("Masukkan pilihan anda : "))
    except ValueError:
        print("Input tidak valid, masukkan angka antara 1-6")
        input("Tekan Enter untuk kembali...")
        return menu()

    if pilih == 1:
        pilihl()
    elif pilih == 2:
        tampil()
        input("kembali menu utama")
        menu()
    elif pilih == 3:
        update_data()
    elif pilih == 4:
        hapus_data()
    elif pilih == 5:
        author()
        input("\n\n kembali menu utama")
        menu()
    elif pilih == 6:
        sys.exit()
    else:
        print("Pilihan tidak tersedia")
        input("Tekan Enter untuk kembali...")
        menu()

def tampil():
    os.system('cls')
    print("DATA MAHASISWA")
    if not dataSiswa:
        print("Belum ada data mahasiswa.")
        return
    for data in dataSiswa:
        print("Nim : " + str(data.nim))
        print("Nama : " + data.nama)
        print("---------------")

def author():
    os.system('cls')
    print("alvin meko | 672010193")
    print("uksw 2015")

def pilihl():
    ulang = 'Y'
    while ulang in ('y', 'Y'):
        os.system('cls')
        siswaBaru = Mahasiswa()
        print("INPUT DATA MAHASISWA ")
        try:
            siswaBaru.nim = int(input("masukkan nim : "))
        except ValueError:
            print("NIM harus berupa angka")
            input("Tekan Enter untuk ulang input...")
            continue
        siswaBaru.nama = input("masukkan nama siswa : ")
        dataSiswa.append(siswaBaru)
        ulang = input("Apakah Anda Ingin Mengulang (Y/ T) ? ")
    menu()

def update_data():
    index_update = -1
    tampil()
    if not dataSiswa:
        input("kembali menu utama")
        menu()
        return
    try:
        id_edit = int(input("Input Nim yang akan di update : "))
    except ValueError:
        print("NIM harus berupa angka")
        input("kembali menu utama")
        menu()
        return
    for a in range(0, len(dataSiswa)):
        if id_edit == dataSiswa[a].nim:
            index_update = a
            break
    if index_update > -1:
        print("INPUT DATA YANG DI UPDATE ")
        siswa = Mahasiswa()
        try:
            siswa.nim = int(input("masukkan nim : "))
        except ValueError:
            print("NIM harus berupa angka")
            input("kembali menu utama")
            menu()
            return
        siswa.nama = input("masukkan nama siswa : ")
        dataSiswa[index_update] = siswa
        print("berhasil update data siswa")
    else:
        print("nim tidak ditemukan")
    input("kembali menu utama")
    menu()

def hapus_data():
    index_delete = -1
    tampil()
    if not dataSiswa:
        input("kembali menu utama")
        menu()
        return
    try:
        id_hapus = int(input("Input Nim yang akan di hapus : "))
    except ValueError:
        print("NIM harus berupa angka")
        input("kembali menu utama")
        menu()
        return
    for a in range(0, len(dataSiswa)):
        if id_hapus == dataSiswa[a].nim:
            index_delete = a
            break
    if index_delete > -1:
        del dataSiswa[index_delete]
        print("Data Telah di hapus")
    else:
        print("nim tidak ditemukan")
    input("kembali menu utama")
    menu()

if __name__ == "__main__":
    menu()