# Fungsi menampilkan seluruh kontak dalam daftar
def show(block):
    if len(block) == 0:
        print('\nKontak Masih Kosong\n')
        return

    print('\nDaftar Kontak')
    for i, micro in enumerate(block):
        print('\n==========')
        print(f'Kontak {i+1}')
        for key, value in  micro.items():
            print(f'{key}: {value}')
        print('==========')

    print('\n')
    return

def add(block):
    while True:
        nama = input('\nNama: ')

        if nama == 'exit':
            print('\nKeluar')
            return
        elif not nama or nama.isspace():
            print('\nNama tidak boleh kosong!')
            continue
        
    
        no = input('Nomor: ')

        if no == 'exit':
            print('\nKeluar')
            return
        elif not no or no.isspace():
            print('\nNomor tidak boleh kosong!')
            continue
        elif no.isdigit() == False:
            print('\nNomor harus berupa angka!')
            continue

        desc = input('Deskripsi: ')

        data = {}

        if desc == 'exit':
            print('\nKeluar')
            return
    
        data['Nama'] = nama
        data['No'] = no
        data['Desc'] = desc

        block.append(data)

        print(f'\n{data['Nama']} telah di tambahkan...')
        return

def delete(block):
    while True:

        print('\nHapus Kontak')

        usr = input('Nama: ')
        found = False

        if usr == 'exit':
            print('\nKeluar')
            return
        elif not usr:
            print('\nNama tidak boleh kosong!')
            continue
        elif usr.isspace() == True:
            print('\nNama tidak boleh kosong')
            continue

        for kontak in block:
            if kontak['Nama'] == usr:
                print('\nKontak di temukan')

                found = True
                
                confirm = input('Konfirmasi penghapusan kontak. Ketik "Hapus" untuk konfimasi penghapusan!\n')

                if confirm == 'Hapus':
                    block.remove(kontak)
                    print(f'\n{kontak['Nama']} Telah di hapus')
                    break
                else:
                    print('Membatalkan penghapusan')
                    return
                
        if found == False: 
            print('\nKontak tidak di temukan!')


def get(block):
    while True:
        print('\nCari Kontak')

        usr = input('Nama: ')
        found = False

        if usr == 'exit':
            print('\nKeluar')
            return
        elif not usr or usr.isspace():
            print('\nNama tidak boleh kosong')
            continue
        
        for kontak in block:
            if kontak['Nama'] == usr:
                print('\nKontak ditemukan')
                print('==========')
                for key, value in kontak.items():
                    print(f'{key}: {value}')
                print('==========')

                found = True

        if found == False:
            print(f'\n{usr} Tidak di temukan')