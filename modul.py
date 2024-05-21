def tambah_data_barang(barang_list):
    nama = input("Masukkan nama barang: ")
    jumlah = int(input("Masukkan jumlah barang: "))
    barang_list.append({'nama': nama, 'jumlah': jumlah})
    print("Data barang berhasil ditambahkan.")

def edit_data(barang_list):
    nama = input("Masukkan nama barang yang akan diedit: ")
    for barang in barang_list:
        if barang['nama'] == nama:
            barang['jumlah'] = int(input(f"Masukkan jumlah baru untuk {nama}: "))
            print("Data barang berhasil diedit.")
            return
    print("Barang tidak ditemukan.")

def hapus_data_barang(barang_list):
    nama = input("Masukkan nama barang yang akan dihapus: ")
    for barang in barang_list:
        if barang['nama'] == nama:
            barang_list.remove(barang)
            print("Data barang berhasil dihapus.")
            return
    print("Barang tidak ditemukan.")

def cari_data(barang_list):
    nama = input("Cari Nama Barang: ")
    hasil_pencarian = [barang for barang in barang_list if nama.lower() in barang['nama'].lower()]
    
    if hasil_pencarian:
        print("===== Hasil Pencarian =====")
        for barang in hasil_pencarian:
            print(f"{barang['nama']}, Stok: {barang['jumlah']}")
    else:
        print("Barang tidak ditemukan.")

def tampilkan_data_barang(barang_list):
    if not barang_list:
        print("Tidak ada data barang.")
    else:
        for barang in barang_list:
            print(f"Nama: {barang['nama']}, Jumlah: {barang['jumlah']}")

def tampilkan_jumlah_data(barang_list):
    print(f"Jumlah data barang: {len(barang_list)}")