''' Struktur Kontrol Perulangan
Buatlah sebuah program yang dapat menginputkan angka secara terus menerus apabila user menginputkan 0 maka proses input berhenti,
menuju ke menu dan meminta user apakah user ingin menambahkan nilai lagi, menampilkan jumlah bilangan genap berdasarkan input atau
jumlah bilangan ganjil berdasarkan input, kemudian ada pilihan exit.
'''

n = []
c = 0
d = 0

while True:
    print ("Menu :\n1. Input Nilai\n2. Bilangan genap\n3. Bilangan ganjil\n4. Exit")
    a = int(input("Masukkan pilihan = "))
    if a == 1:
        while True:
            b = int(input("Masukkan nilai = "))
            if b == 0:
                break
            n.append(b)
    elif a == 2:
        for i in (n):
            if i % 2 == 0:
                c += 1
        print ("Bilangan genap ada =", c)
        c = 0
    elif a == 3:
        for i in (n):
            if i % 2 == 1:
                d += 1
        print ("Bilangan ganjil ada =", d)
        d = 0
    elif a == 4:
        break
    else:
        print ("Input tidak benar")
