data = []
item = set()

while True:
    try:
        print("Selamat Datang di program peringkas data penjualan\n1. Tambah Data\n2. Tampilkan Data\n3. Hapus Data\n4. Exit")
        a = int(input("Masukkan pilihan anda = "))
    except:
        print("Invalid Input")
    if a == 1:
        print("Silakan masukkan nama barang")
        while True:
            b = str(input())
            b = b.lower()
            b = b.capitalize()
            if b == "Stop":
                break
            data.append(b)
        for i in data:
            item.add(i)
    elif a == 2:
        print("Hasil Penjualan hari ini adalah:")
        for i in item:
            quantity = 0
            for j in data:
                if i == j:
                    quantity += 1
            print(quantity, i)
    elif a == 3:
        data = []
        item = set()
        print("Data berhasil dihapus")
    elif a == 4:
        break
