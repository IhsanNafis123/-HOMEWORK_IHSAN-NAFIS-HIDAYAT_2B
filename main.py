import modul as md

def main():
    md.barang_list = []
    while True:
        print("\nSelamat datang di program Manajemen Stok Barang!")
        print("Pilihan:")
        print("1. Tambah Data Barang")
        print("2. Edit Data")
        print("3. Hapus Data Barang")
        print("4. Cari Data")
        print("5. Tampilkan Data Barang")
        print("6. Tampilkan Jumlah Data")
        print("7. Keluar")
        
        pilihan = input("Masukkan pilihan Anda: ")
        
        if pilihan == '1':
           md.tambah_data_barang(md.barang_list)
        elif pilihan == '2':
            md.edit_data(md.barang_list)
        elif pilihan == '3':
            md.hapus_data_barang(md.barang_list)
        elif pilihan == '4':
            md.cari_data(md.barang_list)
        elif pilihan == '5':
            md.tampilkan_data_barang(md.barang_list)
        elif pilihan == '6':
            md.tampilkan_jumlah_data(md.barang_list)
        elif pilihan == '7':
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()