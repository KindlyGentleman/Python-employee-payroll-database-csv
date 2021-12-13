#import
import pandas as pd
import csv
from tabulate import tabulate
from datetime import datetime

#data judul
judul1 = "Selamat Datang dalam Sistem Data dan Gaji Karyawan"
judul2 = 'Universitas Teknologi Perang Blitzkrieg'
print()
print('='*112)
print(judul1.center(111))
print(judul2.center(111))
print('='*112)

#data menu
pilihan_menu = {
    1: 'Menambahkan Data Karyawan',
    2: 'Menampilkan Seluruh Data Karyawan Terdaftar',
    3: 'Mencari Data Karyawan Terdaftar',
    4: 'Menghapus Data karyawan Terdaftar',
    5: 'Menampilkan Rincian Gaji dan Slip Gaji Karyawan',
    6: 'Exit'
}
pilihan_golongan = {
    1: 'Golongan IIIa',
    2: 'Golongan IIIb',
    3: 'Golongan IIIc',
    4: 'Golongan IIId',
    5: 'Golongan IVa',
    6: 'Golongan IVb',
    7: 'Golongan IVc',
    8: 'Golongan IVd'
}
pilihan_status = {
    1: 'Sudah menikah',
    2: 'Tidak/belum menikah'
}

pilihan_menu_cari = {
    1: 'Nama',
    2: 'NIP',
    3: 'Golongan',
    4: 'Jabatan'
}
#data
judul = ['Nama', 'NIP', 'Golongan', 'Jabatan', 'Status Pernikahan', 'Gaji Pokok', 'Tunjangan',
              'Gaji Total']
namafile = 'data_pekerja.csv'
pd.set_option('display.max_columns', None)
pd.set_option('display.max_row', None)
pd.set_option('display.max_colwidth', None)

#Definisi Fungsi
def printMenu():
    print()
    for i in pilihan_menu.keys():
        print (i, '-', pilihan_menu[i] )

def pilihan1():
    print('\nSilakan memasukan data Karyawan terbaru dibawah ini!')
    while (True):
        namaPekerja = input("Nama : ")
        try:
            nipPekerja = int(input("NIP : "))
        except:
            print('Tolong masukan data berupa angka, terima kasih.')
            print('Silakan memasukan ulang kembali data Karyawan terbaru dibawah ini!')
            continue
        if len(str(nipPekerja)) != 18:
            print('NIP yang Anda masukan harus memiliki panjang 18 karakter, silahkan coba lagi.')
            continue
        print('\nKeterangan Golongan dengan indeksnya:')
        for i in pilihan_golongan.keys():
            print(i, '-', pilihan_golongan[i])
        try:
            golongan_gaji = int(input("Golongan : "))
        except:
            print('Tolong masukan angka yang tertera untuk memasukan data, terima kasih.')
            print('Silakan memasukan ulang kembali data Karyawan terbaru dibawah ini!')
            continue
        jabatan_pekerja = input("Jabatan : ")
        for i in pilihan_status.keys():
            print(i, '-', pilihan_status[i])
        try:
            status_pernikahan = int(input("Masukan status penikahan Anda : "))
        except:
            print('Tolong masukan angka yang tertera untuk memasukan data, terima kasih.')
            print('Silakan memasukan ulang kembali data Karyawan terbaru dibawah ini!')
            continue
        if status_pernikahan == 1:
            jumlah_anak = int(input("Masukkan jumlah anak tanggungan (dibawah 18 tahun) : "))
            status_pernikahanhuruf = "Sudah Menikah"
        else:
            jumlah_anak = 0
            status_pernikahanhuruf = "Belum/Tidak Menikah"

        def gaji_pokok(golongan):
            conditions = {
                1: 2200000,
                2: 2500000,
                3: 2800000,
                4: 3100000,
                5: 3400000,
                6: 3700000,
                7: 4000000,
                8: 4300000
            }
            gaji_pokok = 0
            if golongan in conditions.keys():
                gaji_pokok = conditions[golongan]
            return gaji_pokok

        def golongan_gajihuruf(golongan):
            conditions = {
                1: 'Golongan IIIa',
                2: 'Golongan IIIb',
                3: 'Golongan IIIc',
                4: 'Golongan IIId',
                5: 'Golongan IVa',
                6: 'Golongan IVb',
                7: 'Golongan IVc',
                8: 'Golongan IVd'
            }
            golongan_gaji = 0
            if golongan in conditions.keys():
                golongan_gaji = conditions[golongan]
            return golongan_gaji

        def tunjangan(pernikahan, anak):
            if pernikahan == 1:
                tunjangan = 300000
                if anak == 1:
                    tunjangan += 150000
                elif anak == 2:
                    tunjangan += 300000
                elif anak <= 3:
                    tunjangan += 350000
            else:
                tunjangan = 0
            return tunjangan

        def writing_workers_data(nama, nip, golongan, jabatan, pernikahan, gajiPokok, tunjangan):
            gaji_total = gajiPokok + tunjangan
            name_dict = {
                'Nama': [nama],
                'NIP': [nip],
                'Golongan':[golongan],
                'Jabatan': [jabatan],
                'Status Pernikahan':[pernikahan],
                'Gaji Pokok':[gajiPokok],
                'Tunjangan':[tunjangan],
                'Gaji Total':[gaji_total]
            }
            df = pd.DataFrame(name_dict)
            dfnodup = (df.drop_duplicates(['NIP'],keep="first"))
            dfnodup.to_csv(namafile,mode='a', index = False,header=False)

        #    with open(namafile, mode='a') as csv_file:
        #        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',')
        #        csv_writer.writerow(
        #            {"Nama": nama, "NIP": nip, "Golongan": golongan, "Jabatan": jabatan, "Status Pernikahan": pernikahan,
        #             "Gaji Pokok": gajiPokok, "Tunjangan": tunjangan, "Gaji Total": gaji_total})

        writing_workers_data(nama=namaPekerja, nip=nipPekerja, golongan=golongan_gajihuruf(golongan_gaji), jabatan=jabatan_pekerja,
                             pernikahan=status_pernikahanhuruf, gajiPokok=gaji_pokok(golongan=golongan_gaji),
                             tunjangan=tunjangan(status_pernikahan, jumlah_anak))

        status = str(input('Apakah Anda ingin memasukan data lagi? (y/n): '))
        if (status != 'y'):
            return False
        else:
            continue

def pilihan2():
    while(True):
        df = pd.read_csv(namafile, usecols=['Nama', 'NIP', 'Golongan', 'Jabatan'], index_col=0)
        dfnodup = (df.drop_duplicates(['NIP'],keep="first"))
        print(tabulate(dfnodup.sort_values(['Nama', 'Golongan', 'NIP']), headers=judul, tablefmt='github'))
        print()
        status1 = str(input('Apakah Anda ingin kembali ke menu? (y/n): '))
        if (status1 == 'y'):
            return False
        else:
            continue

def pilihan3():
    while (True):
        for i in pilihan_menu_cari.keys():
            print(i, '-', pilihan_menu_cari[i])
        menu = int(input('Masukan parameter yang digunakan untuk mencari: '))
        if menu in pilihan_menu_cari.keys():
            menuparameter = pilihan_menu_cari[menu]
            parameter = str(input('Masukan parameter karyawan yang ingin dicari sesuai dengan pilihan: '))
            df = pd.read_csv(namafile, usecols=['Nama', 'NIP', 'Golongan', 'Jabatan'])
            dfcari = (df[df[menuparameter].astype(str).str.contains(str(parameter))])
            print(tabulate(dfcari, headers=['indeks', 'Nama', 'NIP', 'Golongan', 'Jabatan'], tablefmt='github'))
            status1 = str(input('Apakah Anda ingin kembali ke menu? (y/n): '))
            if (status1 == 'y'):
                return False

def pilihan4():
    while(True):
        try:
            parameter = int(input('Masukan NIP karyawan yang ingin dihapus: '))
        except:
            print('Data yang Anda masukan bukan berupa angka, silakan coba lagi. Terima kasih.')
            continue
        df = pd.read_csv(namafile,usecols=['Nama', 'NIP', 'Golongan', 'Jabatan','Status Pernikahan'], index_col=0)
        dfall = pd.read_csv(namafile, usecols=['Nama', 'NIP', 'Golongan', 'Jabatan','Status Pernikahan'] , index_col=0)
        dfcari = (df[df['NIP'].astype(str).str.contains(str(parameter))])
        print(tabulate(dfcari, headers=judul, tablefmt='github'))
        status = str(input('Apakah data yang Anda cari sudah benar? (y/n): '))
        if (status == 'y'):
            print(tabulate(dfcari, headers=judul, tablefmt='github'))
            status = str(input('Apakah data yang Anda akan hapus sudah benar? (y/n): '))
            if (status == 'y'):
                dfcari = (dfall[dfall['NIP'].astype(str).str.contains(str(parameter))==False])
                dfcari.to_csv(namafile, sep=',')
                print('Data yang Anda pilih sudah dihapus, kembali ke menu utama')
                return False
            else:
                status = str(input('Apakah Anda ingin kembali ke menu? (y/n): '))
                if (status == 'y'):
                    return False
                else:
                    continue
        else:
            status = str(input('Apakah Anda ingin kembali ke menu? (y/n): '))
            if (status == 'y'):
                return False
            else:
                continue

def pilihan5():
    while(True):
        try:
            parameter = int(input('Masukan NIP karyawan yang ingin ditampilkan datanya: '))
        except:
            print('Data yang Anda masukan bukan berupa angka, silakan coba lagi. Terima kasih.')
            continue
        df = pd.read_csv(namafile, usecols=['Nama', 'NIP', 'Golongan', 'Jabatan'],index_cols=0)
        dfcari = (df[df['NIP'].astype(str).str.contains(str(parameter))])
        dfall = pd.read_csv(namafile, usecols=judul)
        print(tabulate(dfcari, headers=judul, tablefmt='github'))
        status = str(input('Apakah data yang Anda inginkan sudah benar? (y/n): '))
        if (status == 'y'):
            dfcari = (dfall[dfall['NIP'].astype(str).str.contains(str(parameter))])
            print(tabulate(dfcari, headers=judul, tablefmt='github'))
            status = str(input('Apakah Anda ingin menampilkan slip gaji? (y/n): '))
            if (status == 'y'):
                now = datetime.now()
                dfcari = (dfall[dfall['NIP'].astype(str).str.contains(str(parameter))])
                judul1 = "SLIP GAJI"
                judul2 = 'Universitas Teknologi Perang Blitzkrieg'
                judul3 = 'Arcisstraße 21, 80333 München, Jerman'
                print()
                print('=' * 112)
                print(judul1.center(111))
                print(judul2.center(111))
                print(judul3.center(111))
                print('=' * 112)
                print('NIP\t\t\t\t: {}'.format(dfcari.iloc[0]['NIP']))
                print('Nama\t\t\t: {}'.format(dfcari.iloc[0]['Nama']))
                print('GOlongan\t\t: {}'.format(dfcari.iloc[0]['Golongan']))
                print('Jabatan\t\t\t: {}'.format(dfcari.iloc[0]['Jabatan']))
                print('\nPENGHASILAN\n')
                print('Gaji Pokok\t\t: {}'.format(dfcari.iloc[0]['Gaji Pokok']))
                print('Tunjangan\t\t: {}'.format(dfcari.iloc[0]['Tunjangan']))
                print('Gaji Total\t\t: {}\n'.format(dfcari.iloc[0]['Gaji Total']))
                print('Tanggal Percetakan: {}'.format(now.strftime("%d/%m/%Y %H:%M:%S")))
                print('Manajemen HRD')

        status = str(input('Apakah Anda ingin kembali ke menu? (y/n): '))
        if (status == 'y'):
            return False
        else:
            continue

if __name__=='__main__':
    while(True):
        printMenu()
        pilihan = ''
        try:
            pilihan = int(input('\nSelamat datang dalam sistem, silahkan pilih opsi menu: '))
        except:
            print('Tolong masukan data berupa angka, terima kasih.')
        if pilihan == 1:
           pilihan1()
        elif pilihan == 2:
            pilihan2()
        elif pilihan == 3:
            pilihan3()
        elif pilihan == 4:
            pilihan4()
        elif pilihan == 5:
            pilihan5()
        elif pilihan == 6:
            print('Sampai jumpa kembali')
            exit()
        else:
            print('Tolong masukan angka yang tertera untuk mengakses menu yang terlampir, terima kasih.')
