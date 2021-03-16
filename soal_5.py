''' Struktur Kontrol Kompleks
Anda diminta untuk membuat program kalkulator yang dapat menghitung semua angka di dalam 1 inputan user.
Saat program berjalan, program langsung menampilkan menu kepada user.
Di dalam menu terdapat Imput angka, penjumlahan, perkalian dan exit.
'''

lst = []

while True:
    print ("Menu = \n1. Input Angka\n2. Penjumlahan\n3. Perkalian\n4. Exit")
    z = int(input("Masukkan Pilihan = "))
    if z == 1:
        lst = []

        a = str(input("Angka: "))

        length = len(a)

        n = 0
        for i in range (length):
            b = a[n]
            lst.append(b)
            n += 1
    elif z == 2:
        if lst == []:
            print ("Anda belum memasukkan angka")
        else:
            total = 0
            c = 0
            for i in lst:
                c = int(i)
                total += c
            print ("Total penjumlahannya adalah =", total)
    elif z == 3:
        if lst == []:
            print ("Anda Belum memasukkan angka")
        else:
            total = 1
            c = 0
            for i in lst:
                c = int(i)
                total *= c
            print ("Total perkaliannya adalah =", total)
    elif z == 4:
        break
    else:
        print ("Invalid Input")
