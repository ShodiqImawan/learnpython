# Fungsi menampilkan seluruh kontak yang ada dalam daftar_kontak
def show(block):
    # Cek apakah daftar_kontak masih kosong
    if len(block) == 0:
        print('\nKontak Masih Kosong\n')
        return

    # Tampilkan setiap kontak satu per satu
    print('\nDaftar Kontak')
    for i, micro in enumerate(block): 
        # enumerate() digunakan untuk mendapatkan indeks (i) dan data kontak(micro) sekaligus
        print('\n==========')
        print(f'Kontak {i+1}') # Tampilkan nomor urut kontak dimulai dari 1
        for key, value in  micro.items():
            print(f'{key}: {value}') # Tampilkan setiap pasangan key dan value
        print('==========')

    print('\n')
    return

# Fungsi untuk menambahkan kontak ke dalam daftar_kontak
def add(block):
    while True:
        # Input nama kontak
        nama = input('\nNama: ')

        # Jika input 'exit' keluar dari fungsi
        if nama == 'exit':
            print('\nKeluar')
            return
        # Cek apakah nama kosong/hanya spasi
        elif not nama or nama.isspace():
            print('\nNama tidak boleh kosong!')
            continue
        
        # Input nomor kontak
        no = input('Nomor: ')

        # Jika input 'exit' keluar dari fungsi
        if no == 'exit':
            print('\nKeluar')
            return
        # Cek apakah nomor kosong/hanya spasi
        elif not no or no.isspace():
            print('\nNomor tidak boleh kosong!')
            continue
        # Cek apakah nomor adalah angka
        elif no.isdigit() == False:
            print('\nNomor harus berupa angka!')
            continue

        # Input deskripsi kontak
        desc = input('Deskripsi: ')

        # Jika input 'exit' keluar dari fungsi
        if desc == 'exit':
            print('\nKeluar')
            return
        
        # Buat data dictionary berisi data kontak dari input pengguna 
        data = {
            'Nama': nama,
            'No': no,
            'Deskripsi': desc
        }

        # Tambahkan data ke daftar_kontak
        block.append(data)

        print(f'\n{data["Nama"]} telah di tambahkan...')
        return

# Fungsi untuk menghapus kontak berdasarkan nama
def delete(block):
    while True:

        print('\nHapus Kontak')

        # Minta input nama kontak yang ingin di hapus
        usr = input('Nama: ')

        # Hasil penemuan
        found = False

        # Jika input 'exit' keluar dari fungsi
        if usr == 'exit':
            print('\nKeluar')
            return
        # Cek apakah nama kosong/hanya spasi
        elif not usr or usr.isspace():
            print('\nNama tidak boleh kosong!')
            continue

        # Mencari kontak berdasarkan nama
        for kontak in block:
            if kontak['Nama'] == usr:
                print('\nKontak di temukan')

                # Berikan tanda bahwa kontak di temukan
                found = True
                
                # Minta input konfirmasi penghapusan dari pengguna
                confirm = input('Konfirmasi penghapusan kontak. Ketik "Hapus" untuk konfimasi penghapusan!\n')

                if confirm == 'Hapus':
                    # Hapus kontak
                    block.remove(kontak) 
                    print(f'\n{kontak["Nama"]} Telah di hapus')
                    break
                else:
                    print('Membatalkan penghapusan')
                    return

        # Jika kontak tidak di temukan
        if found == False: 
            print('\nKontak tidak di temukan!')

# Fungsi untuk mencari kontak berdasarkan nama
def get(block):
    while True:
        print('\nCari Kontak')

        # Minta input nama kontak yang ingin dicari
        usr = input('Nama: ')

        # Hasil penemuan
        found = False

        # Jika input 'exit' keluar dari fungsi
        if usr == 'exit':
            print('\nKeluar')
            return
        # Cek apakah nama kosong/hanya spasi
        elif not usr or usr.isspace():
            print('\nNama tidak boleh kosong')
            continue
        
        # Mencari kontak berdasarkan nama
        for kontak in block:
            if kontak['Nama'] == usr:
                # Berikan tanda bahwa kontak di temukan
                found = True

                print('\nKontak ditemukan')
                print('==========')

                # Tampilkan informasi lengkap kontak
                for key, value in kontak.items():
                    print(f'{key}: {value}')
                print('==========')

        # Jika kontak tidak di temukan
        if found == False:
            print(f'\n{usr} Tidak di temukan')