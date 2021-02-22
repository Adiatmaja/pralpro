'''
Miwa ingin membuat sebuah program untuk toko kopi nya. Namun, ia perlu menerapkan sistem login agar dapat mengetahui siapa yang
sedang bertugas sebagai pelayan di order tersebut. Saat ini yang bekerja di Miwa Coffee adalah Akira dan Iwaki.
Dengan Username = 'Nama Staff' dan Password = Miwa Coffee.
Menu nya terbagi menjadi 2 yaitu Espresso dan Blended Coffee.
Pada menu espresso terdapat Caffe Latte dan Cappuccino dengan harga Rp. 26000 dan Rp. 22000 secara berurutan.
Sedangkan pada menu Blended Coffee terdapat Coffee Frappuccino dan Hazelnut Frappuccino dengan harga
Rp. 32000 dan Rp. 35000 secara berurutan.
Terdapat opsi penyajian panas atau dingin, apabila dingin maka akan menambah biaya Rp. 2000
Kemudian Miwa juga perlu untuk menerapkan pajak sebesar 10% karena ia menyewa tempat di sebuah mall.
'''

# Espresso
x = 26000
y = 22000
# Blended Coffee
x1 = 32000
y1 = 35000

a = str(input("Username = "))
b = str(input("Password = "))

if a == "Akira" or a == "Iwaki":
    if b == "Miwa Coffee":
        print ("Halo,", a, "\nSilakan pilih jenis kopi\n1. Espresso\n2. Blended Coffee")
        c = int(input("Pilih jenis kopi (1/2) "))
        if c == 1:
            print ("Silakan pilih kopi Espresso = \n1. Caffe Latte\n2. Cappuccino")
            d = int(input("Pilih kopi Espresso (1 / 2) "))
            if d == 1:
                e = str(input("(Panas / Dingin)"))
                e = e.lower()
                if e == "panas":
                    p = x * 0.10
                    t = x + p
                    print ("Pajak = Rp.", p,"\nTotal Harga = Rp.", t)
                elif e == "dingin":
                    p = (x + 2000) * 0.10
                    t = x + p
                    print ("Pajak = Rp.", p,"\nTotal Harga = Rp.", t)
                else:
                    print ("Input tidak sesuai (Panas / Dingin)")
            elif d == 2:
                e = str(input("(Panas / Dingin) "))
                e = e.lower()
                if e == "panas":
                    p = y * 0.10
                    t = y + p
                    print ("Pajak = Rp.", p, "\nTotal Harga = Rp.", t)
                elif e == "dingin":
                    p = (y + 2000) * 0.10
                    t = y + p
                    print ("Pajak = Rp.", p, "\nTotal Harga = Rp.", t)
                else:
                    print ("Input tidak sesuai (Panas / Dingin) ")
            else:
                print ("Pilihan tidak sesuai (1 / 2) ")
        elif c == 2:
            print ("Silakan pilih Blended Coffee = \n1. Coffee Frappuccino\n2. Hazelnut Frappuccino")
            d = int(input("Pilih Blended Coffee (1 / 2) "))
            if d == 1:
                e = str(input("(Panas / Dingin) "))
                e = e.lower()
                if e == "panas":
                    p = x1 * 0.10
                    t = x1 + p
                    print ("Pajak = Rp.", p, "\nTotal Harga = Rp.", t)
                elif e == "dingin":
                    p = (x1 + 2000) * 0.10
                    t = x1 + p
                    print ("Pajak = Rp.", p, "\nTotal Harga = Rp.", t)
                else:
                    print ("Input tidak sesuai (Panas / Dingin) ")
            elif d == 2:
                e = str(input("(Panas / Dingin) "))
                e = e.lower()
                if e == "panas":
                    p = y1 * 0.10
                    t = y1 + p
                    print ("Pajak = Rp.", p, "\nTotal Harga = Rp.", t)
                elif e == "dingin":
                    p = (y1 + 2000) * 0.10
                    t = y1 + p
                    print ("Pajak = Rp.", p, "\nTotal Harga Rp.", t)
                else:
                    print ("Input tidak sesuai (Panas / Dingin) ")
            else:
                print ("Pilihan tidak sesuai (1 / 2) ")
    else:
        print ("Username atau Password salah")
else:
    print ("Username atau Password salah")