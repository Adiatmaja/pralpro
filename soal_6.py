''' Strings
Anda diminta untuk membuat sebuah program yang dapat mendata nama dan tanggal lahir dalam 1 inputan
sebelum input data, buatlah ebuah menu yang berisi:
1. Input data
2. Tunjukkan data
3. Exit
Jika user memilih 2 tetapi belum emnginputkan data maka keluarkan output "Anda belum menginputkan data"
Input memiliki Format:
<nama>/<tanggal>-<bulan>-<tahun> atau <tanggal>-<bulan>-<tahun>/<nama>
Setelah berhasil menginputkan data, tunjukannlah data yang diinputkan dengan format:
Nama = <nama>
Tanggal Lahir:
Tanggal = <tanggal>
Bulan = <bulan>
Tahun = <tahun>
'''

data = 0

while True:
    print ("Menu\n1. Input data\n2. Tunjukkan data\n3. Exit")
    menu = str(input("Masukkan pilihan = "))
    if menu == "1":
        data = str(input("Masukkan nama dan tanggal lahir = "))
        data = data.split("/")

        for i in (data):
            if i[0].isdigit():
                i = i.split("-")
                tanggal = i[0]
                bulan = i[1]
                tahun = i[2]
            else:
                nama = i
    elif menu == "2":
        if data == 0:
            print ("Anda belum menginputkan data")
        else:
            print ("Nama =", nama, "\nTanggal Lahir:", "\nTanggal =", tanggal, "\nBulan =", bulan, "\nTahun =", tahun)
    elif menu == "3":
        break
    else:
        print ("Invalid Input")
