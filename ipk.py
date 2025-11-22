
nim = input("Masukkan NIM: ")
nama = input("Masukkan Nama: ")


mata_kuliah = [
    ("Statistik", 3),
    ("Pancasila", 2),
    ("Pemrograman", 3)
]

nilai_mk = []

print("\nMasukkan nilai untuk setiap mata kuliah:")
for mk, sks in mata_kuliah:
    nilai = float(input(f"Nilai untuk {mk}: "))
    nilai_mk.append((mk, sks, nilai))


total_bobot = sum(sks * nilai for _, sks, nilai in nilai_mk)
total_sks = sum(sks for _, sks, _ in nilai_mk)
ip = total_bobot / total_sks


print("\n==============================")
print(f"NIM : {nim}")
print(f"Nama : {nama}\n")
print("Nilai per Mata Kuliah:")
for mk, sks, nilai in nilai_mk:
    print(f"-- {mk} ({sks} SKS): {nilai:.2f}")

print(f"\nIP : {ip:.2f}")
