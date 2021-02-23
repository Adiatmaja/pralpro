''' Struktur Kontrol Percabangan
Miwa ingin membuat sebuah program untuk toko kopi nya. Namun, ia perlu menerapkan sistem login agar dapat mengetahui siapa yang
sedang bertugas sebagai pelayan di order tersebut. Saat ini yang bekerja di Miwa Coffee adalah Akira dan Iwaki.
Dengan Username = 'Nama Staff' dan Password = Miwa Coffee.
Menu nya terbagi menjadi 2 yaitu Espresso dan Blended Coffee.
Pada menu espresso terdapat Caffe Latte dan Cappuccino dengan harga Rp. 26000 dan Rp. 22000 secara berurutan.
Sedangkan pada menu Blended Coffee terdapat Coffee Frappuccino dan Hazelnut Frappuccino dengan harga
Rp. 32000 dan Rp. 35000 secara berurutan.
Miwa juga perlu menerapkan pajak sebanyak 10% karena ia menyewa tempat di sebuah mall

Input :
a = Username
b = Password
c = Pemilihan menu
d = pemeilihan menu espresso atau blended coffee

Proses & Output :
if a == "Iwaki" atau "Akira" dan b == "Miwa Coffee:
    Memilih espresso atau blended coffee
    if c == 1:
        if d == 1:
            Caffe Latte
        elif d == 2:
            Cappuccino
        else:
            Pilihan user tidak benar
    elif c == 2:
        if d == 1:
            Coffee Frappuccino
        elif d == 2:
            Hazelnut Frappuccino
        else:
            Pilihan user tidak benar
    else:
        Pilihan User tidak benar
else:
    Username atau password salah
'''

# Espresso
x = 26000   # Caffee Latte
y = 22000   # Cappuccino
# Blended Coffee
x1 = 32000  # Coffee Frappuccino
y1 = 35000  # Hazelnut Frappuccino

a = str(input("Masukkan Username = "))
b = str(input("Masukkan Password = "))

if a == "Akira" or a == "Iwaki":
    if b == "Miwa Coffee":
        print ("Selamat datang, ", a, "Silakan pilih menu : \n1. Espresso\n2. Blended Coffee")
        c = int(input("Pilih menu (1 / 2)"))
        if c == 1:
            print("Silakan pilih menu Espresso : \n1. Caffe Latte\n2. Cappuccino")
            d = int(input("Pilih menu Espresso (1 / 2) "))
            if d == 1:
                p = x * 0.10
                t = x + p
                print ("Total Pajak = Rp.", p, "Total Harga = Rp.", t)
            elif d == 2:
                p = y * 0.10
                t = y + p
                print ("Total Pajak = Rp.", p, "Total Harga = Rp.", t)
            else:
                print ("Input user tidak benar (1/2)")
        elif c == 2:
            print ("Silakan pilih menu Blended Coffee : \n1. Coffee Frappuccino\n2. Hazelnut Frappuccino")
            d = int(input("Pilih menu Blended Coffee (1 / 2) "))
            if d == 1:
                p = x1 * 0.10
                t = x1 + p
                print ("Total Pajak = Rp.", p, "Total Harga = Rp.", t)
            elif d == 2:
                p = y1 * 0.10
                t = y1 + p
                print ("Total Pajak = Rp.", p , "Total Harga = Rp.", t)
            else:
                print ("Input user tidak benar")
        else:
            print ("Input user tidak benar")
    else:
        print ("Username atau password salah")
else:
    print ("Username atau password salah")