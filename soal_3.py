'''
Hori mendapatkan komisi membuat program untuk suatu perusaahan bank. Perusahaan tersebut meminta agar program tersebut dapat menghitung penarikan dan deposito.
Maksimal pengambilan saldo adalah 5 juta per harinya. Setelah menginputkan penarikan, tunjukkan berapa saldo yang tersisa.
Minimal deposito adalah Rp. 10000000 Bunga deposito pertahunnya adalah 3% dan tunjukkan perkiraan bunga yang didapatkan setelah 5 tahun.
Sebagai percobaan program, saldo awal yang dimiliki pengguna adalah Rp. 2500000. 
'''

def penarikan(b):
    a = 2500000
    if 0 < b <= a:
        a = a - b
        print ("Saldo yang dimiliki sekarang adalah Rp.", a)
    else:
        print ("Penarikan saldo tidak bisa kurang dari 0 atau lebih dari saldo yang dimiliki")
    return a

def deposito(b):
    a = 2500000
    if b >= 10000000:
        a = a + b
        for i in range(5):
            a = (a * 1.03)
            print ("Saldo tahun ke -", i + 1, "adalah Rp. %.0f"%(a))
    else:
        print ("Jumlah deposit tidak bisa kurang dari Rp. 10000000")

print ("Selamat datang, layanan yang tersedia :\n1. Penarikan\n2. Deposito")
n = int(input("Silakan pilih layanan yang anda inginkan = "))

if n == 1:
    b = int(input("Berapa jumlah saldo yang ingin anda tarik? = "))
    penarikan(b)
elif n == 2:
    b = int(input("Berapa jumlah saldo yang ingin ada deposit? (Minimal Rp. 10000000) = "))
    deposito(b)
else:
    print ("Input user tidak benar")