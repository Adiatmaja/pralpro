''' Files
Sebuah sekolah ingin mendata semua siswa yang mengikuti kegiatan OSIS.
Anda sebagai seseorang yang sedang mengikuti kelas programming diminta untuk membuat sebuah program yang dapat menuliskan sebuah data di file .txt.
Data yang diminta adalah nama, umur dan tanggal lahir.
Anda juga diminta agar program tersebut juga dapat menampilkan data dan pilihan untuk membersihkan data apabila salah menginput data.

Input:
a = Pemilihan menu
b = Jumlah siswa yang akan di data
nama_temp = Nama siswa
umur_temp = Umur siswa
tgl_temp = Tanggal Lahir siswa

Proses dan Output:
deklarasi variabel nama, umur dan tanggal sebagai list
membuat loop unlimited:
    output print menu dan meminta input user
    jika a = 1:
        meminta input user berapa data yang akan dimasukkan
        perulangan sebanyak input user:
            input nama, umur dan tanggal lahir
            memasukkan kedalam list
        membuka file Data OSIS.txt
        membuat perulangan sebanyak data yang dimasukkan:
            memasukkan data ke file .txt
        output print "Data berhasil dimasukkan"
    jika a = 2:
        membuka file Data OSIS.txt
        membuat perulangan dari isi .txt
            membagi data dengan ","
            output print data
    jika a = 3:
        membuka file Data OSIS.txt
        menghapus data di file Data OSIS.txt
    jika a = 4:
        output print "Berhasil Keluar"
        keluar dari program
    selain itu:
        output print "Invalid input"
'''

nama,umur,tgl = [],[],[]

while True:
    print ("Selamat Datang di program pendata siswa OSIS.\n1.Masukkan Data\n2. Lihat Data\n3. Bersihkan Data\n4. Exit")
    a = int(input("Masukkan Pilihan = "))

    if a == 1:
        b = int(input("Silahkan masukkan jumlah siswa yang akan didata = "))
        for i in range (b):
            nama_temp = str(input("Masukkan nama = "))
            umur_temp = str(input("Masukkan umur = "))
            tgl_temp = str(input("Masukkan tanggal lahir = "))
            nama.append(nama_temp)
            umur.append(umur_temp)
            tgl.append(tgl_temp)
        handle = open("Data OSIS.txt", "w")
        for j in range (len(nama)):
            handle.write(nama[j]+","+umur[j]+","+tgl[j]+"\n")
        print ("Data berhasil dimasukkan")
    elif a == 2:
        handle = open("Data OSIS.txt", "r")
        for i in handle:
            data = i.split(",")
            print("Nama =", data[0], "Umur =", data[1], "Tanggal Lahir =", data[2])
    elif a == 3:
        handle = open("Data OSIS.txt", "w").close()
        print("Data berhasil dihapus")
    elif a == 4:
        print("Berhasil Keluar")
        break
    else:
        print ("Invalid Input")
