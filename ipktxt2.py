while True:
    print("\n=== INPUT DATA MAHASISWA ===")
    print("Ketik 'stop' pada NIM untuk berhenti.\n")

    nim = input("Masukkan NIM: ")
    if nim.lower() == "stop":
        print("\nProgram dihentikan.")
        break

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

    
    output_text = f"NIM : {nim}\nNama : {nama}\n\nNilai per Mata Kuliah:\n"
    for mk, sks, nilai in nilai_mk:
        output_text += f"-- {mk} ({sks} SKS): {nilai:.2f}\n"
    output_text += f"\nIP : {ip:.2f}\n"

    
    print("\n==============================")
    print(output_text)
    print("==============================")

    
    nama_file = f"hasil_{nim}.txt"

    
    with open(nama_file, "w") as file:
        file.write(output_text)

    print(f"Hasil berhasil disimpan ke file: {nama_file}\n")
