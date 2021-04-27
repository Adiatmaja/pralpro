gtx1650 = {
    'nama' : 'GTX 1650',
    'tipe' : 'VGA',
    'tahun rilis' : 2019,
    'produksi' : 'Indonesia',
    'harga' : 2350000
}
i9 = {
    'nama' : 'Intel Core i9-10900K',
    'tipe' : 'Processor',
    'tahun rilis' : 2018,
    'produksi' : 'Swedia',
    'harga' : 7100000
}
vg249q = {
    'nama' : 'ASUS TUF Gaming VG249Q',
    'tipe' : 'Monitor',
    'tahun rilis' : '2019',
    'produksi' : 'Indonesia',
    'harga' : 3000000
}

while True:
    print("Selamat datang di katalog kami\n1. Info Produk\n2. Lihat Harga\n3. Exit")
    a = str(input("Silahkan pilih menu = "))
    if a == '1':
        print("Produk =\n1. GTX 1650\n2. Intel Core i9-10900K\n3. ASUS TUF Gaming VG249Q")
        b = str(input("Silahkan pilih barang yang akan anda cari"))
        if b == '1':
            for i in gtx1650:
                c = gtx1650.get(i)
                print(i, '= ',c)
        elif b == '2':
            for i in i9:
                c = i9.get(i)
                print(i, '= ',c)
        elif b == '3':
            for i in vg249q:
                c = vg249q.get(i)
                print(i, '= ',c)
        else:
            print("Invalid Input")
    elif a == '2':
        print("Produk =\n1. GTX 1650\n2. Intel Core i9-10900K\n3. ASUS TUF Gaming VG249Q")
        b = str(input("Silahkan pilih barang yang akan dibeli = "))
        if b == '1':
            bt = 0
            n = gtx1650.get('nama')
            p = gtx1650.get('harga')
            pr = gtx1650.get('produksi')
            tax = p * 0.10
            if pr != 'Indonesia':
                bt = 100000
            gv = p + bt + tax
            print("Harga dari", n," adalah :\nHarga produk = ",p,"\nBiaya produksi = ",bt,"\nBiaya Pajak = ",tax,"\nHarga Total = ",gv)
        elif b == '2':
            bt = 0
            n = i9.get('nama')
            p = i9.get('harga')
            pr = i9.get('produksi')
            tax = p * 0.10
            if pr != 'Indonesia':
                bt = 100000
            gv = p + bt + tax
            print("Harga dari", n," adalah :\nHarga produk = ",p,"\nBiaya produksi = ",bt,"\nBiaya Pajak = ",tax,"\nHarga Total = ",gv)
        elif b == '3':
            bt = 0
            n = vg249q.get('nama')
            p = vg249q.get('harga')
            pr = vg249q.get('produksi')
            tax = p * 0.10
            if pr != 'Indonesia':
                bt = 100000
            gv = p + bt + tax
            print("Harga dari", n," adalah :\nHarga produk = ",p,"\nBiaya produksi = ",bt,"\nBiaya Pajak = ",tax,"\nHarga Total = ",gv)
        else:
            print("Invalid Input")
    elif a == '3':
        break
    else:
        print("Invalid Input")
