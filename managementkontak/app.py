#!/usr/bin/env python

# Untuk import function dari file function.py
from function import show   # Fungsi menampilkan daftar kontak
from function import add    # Fungsi menambah kontak
from function import delete # Fungsi menghapus kontak berdasarkan nama
from function import get    # Fungsi mencari kontak berdasarkan nama

# Deklarasi list kosong untuk menyimpan data kontak
daftar_kontak = []

# Loop utama program (berjalan terus-menerus sampai pengguna keluar)
while True:
    # Menampilkan menu utama ke pengguna
    print('\n')
    print('||===== MENU =====||')
    print('||1. Daftar Kontak||')
    print('||2. Tambah Kontak||')
    print('||3. Hapus Kontak ||')
    print('||4. Cari Kontak  ||')
    print('||0. Keluar       ||')
    print('||=====><><><=====||')

    # Meminta input dari pengguna
    usr = input('\nPilih: ')

    # Menangani pilihan pengguna berdasarkan input
    if usr == '0':
        print('\nKeluar dari Program')
        break
    elif usr in ['1', '2', '3', '4']:
        print('\nKetik \'exit\' untuk kembali ke menu')

        # Memanggil fungsi sesuai pilihan
        if usr == '1':
            show(daftar_kontak)
            continue
        elif usr == '2':
            add(daftar_kontak)
            continue
        elif usr == '3':
            delete(daftar_kontak)
            continue
        elif usr == '4':
            get(daftar_kontak)
            continue
    else:
        print('\nPerintah tidak tersedia!\n')
        continue
