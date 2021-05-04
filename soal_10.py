def LihatData():
    if t == ():
            print('Anda belum menambahkan data')
    else:
        for i in range (len(t)):
            b = ' '
            search = ' '
            if search in n[i]:
                d, b = n[i].split(' ')
            else:
                d = n[i]
            day, month, year = t[i].split(' ')
            if b == ' ':
                print("\nNama =", d,"\nTanggal Lahir : \nTanggal =", day,"\nBulan =", month, "\nTahun =", year)
            else:
                print("\nNama depan =", d,"\nNama belakang =", b,"\nTanggal Lahir : \nTanggal =", day,"\nBulan =", month, "\nTahun =", year)
def TambahData(b):
    for i in range(b):
        n_temp = str(input("Silakan masukkan nama siswa = "))
        t_temp = str(input("Silakan masukkan tanggal lahir siswa = "))
        n.append(n_temp)
        t.append(t_temp)
def HapusData(b):
    if b == 'y':
        n, t = list(), list()
        print("Data berhasil dihapus")
    else:
        print("\nAnda akan kembali ke menu\n")

n, t = list(), list()
while True:
    print("Selamat datang di program penghitung nilai siswa. Berikut merupakan menu yang tersedia.\n1. Lihat Data dan Hasilnya\n2. Tambah Data\n3. Hapus Data\n4. Exit")
    a = str(input("Silakan pilih menu yang anda inginkan = "))
    if a == '1':
        LihatData()
    elif a == '2':
        b = int(input('Berapa data yang akan ditambahkan? '))
        TambahData(b)
    elif a == '3':
        b = str(input("Apakah anda yakin untuk menghapus semua data? (y/n)"))
        HapusData(b)
    elif a == '4':
        print('Terimakasih sudah menggunakan program kami')
        break
    else:
        print("Input salah")
