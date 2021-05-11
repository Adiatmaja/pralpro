def cek_huruf(a, check):
    for i in a:
        if i not in check:
            return 'Kalimat tidak memiliki semua huruf'
    return 'Kalimat memiliki semua huruf'
def vokal_konsonan(a):
    vokal, konsonan = 0, 0
    for i in a:
        if i in check:
            vokal += 1
        else:
            konsonan += 1
    print('Huruf Vokal =', vokal)
    print('Huruf Konsonan =', konsonan)

l = list()
b = ''
s = set()
while True:
    print("Selamat datang di program pencari keunikan kata. Berikut merupakan menu yang tersedia =\n1. Cek huruf a sampai z\n2. Jumlah kata yang memiliki huruf vokal dan konsonan\n3. Jumlah variasi huruf\n4. Input/Ganti data\n5. Lihat Data\n6. Exit")
    a = str(input("Silakan pilih fitur yang tersedia = "))
    if a == '1':
        if b == '':
            print("Silakan input data terlebih dahulu")
        else:
            check = []
            for i in range(97,123):
                check.append(chr(i))
            print(cek_huruf(b, check))
    elif a == '2':
        if b == '':
            print("silakan input data terlebih dahulu")
        else:
            check = ['a', 'i', 'u', 'e', 'o']
            print(vokal_konsonan(b))
    elif a == '3':
        for i in l:
            s.add(i)
        print("Jumlah variasi huruf =", len(s))
    elif a == '4':
        b = str(input("Silakan masukkan kata yang anda ingin tes = "))
        b = b.lower()
        b = b.split(' ')
        for i in b:
            for j in i:
                l.append(j)
    elif a == '5':
        print(l)
    elif a == '6':
        print("Terimakasih sudah menggunakan program kami")
    else:
        print('Invalid Input')
