daftarMahasiswa = {}

def tambahMahasiswa():
    print("\n--- Tambah Mahasiswa Baru ---")
    
    while True:
        nim = input("NIM: ")
        if len(nim) != 15:
            print("NIM harus 15 karakter")
        elif nim in daftarMahasiswa:
            print("NIM sudah ada")
        else:
            break

    nama = input("Nama: ")

    while True:
        try:
            ipk = float(input("IPK: "))
            if 0.0 <= ipk <= 4.0:
                break
            else:
                print("IPK tidak valid")
        except ValueError:
            print("IPK harus berupa angka")

    detailMahasiswa = {
        "nama": nama,
        "ipk": ipk
    }
    daftarMahasiswa[nim] = detailMahasiswa
    print(f"Mahasiswa '{nama}' berhasil ditambahkan.")

def tampilkanSemuaMahasiswa():
    if len(daftarMahasiswa) == 0:
        print("Tidak ada data mahasiswa.")
    else:
        for nim, detail in daftarMahasiswa.items():
            print(f"NIM: {nim}")
            print(f"Nama: {detail['nama']}")
            print(f"IPK: {detail['ipk']}")

def cariMahasiswa():
    nim = input("Masukkan NIM mahasiswa yang dicari: ")
    if nim in daftarMahasiswa:
        detail = daftarMahasiswa[nim]
        print(f"NIM: {nim}")
        print(f"Nama: {detail['nama']}")
        print(f"IPK: {detail['ipk']}")
    else:
        print("Mahasiswa tidak ditemukan.")

def hapusMahasiswa():
    nim = input("Masukkan NIM mahasiswa yang akan dihapus: ")
    if nim in daftarMahasiswa:
        del daftarMahasiswa[nim]
        print("Mahasiswa berhasil dihapus.")
    else:
        print("Mahasiswa tidak ditemukan.")

while True:
    print("------------------------------")
    print("Selamat Datang di SIAM!!")
    print("Menu:")
    print("1. Tambah Mahasiswa")
    print("2. Tampilkan Semua Mahasiswa")
    print("3. Cari Mahasiswa Berdasarkan NIM")
    print("4. Hapus Mahasiswa Berdasarkan NIM")
    print("5. Keluar")
    
    pilihan = input("Pilih: ")
    print("------------------------------")
    
    if pilihan == '1':
        tambahMahasiswa()
    elif pilihan == '2':
        tampilkanSemuaMahasiswa()
    elif pilihan == '3':
        cariMahasiswa()
    elif pilihan == '4':
        hapusMahasiswa()
    elif pilihan == '5':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")