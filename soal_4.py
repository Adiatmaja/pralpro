''' Struktur Kontrol Perulangan
Buatlah sebuah program yang dapat menginputkan angka secara terus menerus apabila user menginputkan 0 maka proses input berhenti,
menuju ke menu dan meminta user apakah user ingin menambahkan nilai lagi, menampilkan rata - rata dari semua input,
jumlah bilangan genap berdasarkan input atau jumlah bilangan ganjil berdasarkan input, kemudian ada pilihan exit.

Input :
b = Pemilihan menu
a = Memasukkan nilai ke data

Proses dan Output :
Membuat variabel n sebagai list
Menampilkan menu
Jika b = 1 maka user diminta menambahkan nilai ke data
    input a dengan perulangan
Jika b = 2 maka akan menampilkan rata rata dari data
    d = jumlah nilai / jumlah data
    print (d)
Jika b = 3 maka akan menampilkan jumlah bilangan genap
    jika data % 2 = 0
        e += 1
        print (e)
Jika b = 4 maka akan menampilkan jumlah bilangan ganjil
    jika data % 2 = 1
        f += 1
        print (f)
Jika b = 5 maka program akan berhenti
'''

n = []
e = 0
f = 0

while True:
    print ("MENU : \n1. Input Nilai\n 2. Rata - rata\n3. Bilangan genap\n4. Bilangan ganjil\n5. Exit")
    b = int(input("Masukkan pilihan = "))
    if b == 1:
        while True:
            a = int(input("Masukkan nilai = "))
            if a == 0:
                break
            n.append(a)
    elif b == 2:
        for i in (n):
            c += n
        d = c / len(n)
        print ("Rata rata nya adalah", d)
    elif b == 3:
        for i in (n):
            if n % 2 == 0:
                e += 1
        print ("Bilangan genap ada = ", e)
        e = 0
    elif b == 4:
        for i in (n):
            if n % 2 == 1:
                f += 1
        print ("Bilangan ganjil ada = ", f)
        f = 0
    elif b == 5:
        break
    else:
        print ("Input tidak benar")
