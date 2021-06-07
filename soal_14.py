''' Regex
Buatlah program yang dapat mengganti sebuah karakter menjadi sebuah angka
a = 4, i = 1, s = 5, o = 0
Sedangkan angka menjadi '#' dan spasi menjadi '-'
Apabila semua inputan merupakan angka maka akan mengeluarkan output '***'
Buatlah program dalam sebuah menu

Input :
a = input data kata

Proses & Output :
deklarasi variabel list1
membuat menu
apabila input = 1 maka akan input list
apabila input = 2 maka akan menghapus list
apabila input = 3 maka akan melihat data yang sudah diinput
apabila input = 4 maka akan membuat password
apabila input = 5 maka akan keluar dari program
selain itu akan mengeluarkan output 'Invalid Input'

membuat fungsi changer
deklarasi list2
membuat perulangan sebanyak jumlah data list1
menggunakan regex, mengecek apakah data berisi angka semua atau tidak
mengganti tiap kata menjadi kata yang sudah ditentukan
memasukkan data yang sudah diganti ke list2
print l2 menggunakan perulangan
'''

import re

def changer(a):
    l2 = []
    for i in a:
        z = re.findall('[A-Za-z]', i)
        if z == []:
            l2.append('***')
        else:
            b = re.sub('[0-9]', '#', i)
            c = re.sub('[ ]', '-', b)
            d = re.sub('[Aa]', '4', c)
            e = re.sub('[Ii]', '1', d)
            f = re.sub('[Ss]', '5', e)
            g = re.sub('[Oo]', '0', f)
            l2.append(g)
    for i in range (len(a)):
        print(a[i], '=>', l2[i])

l1 = []

print('Selamat datang di program pembuat password sederhana')
while True:
    print('Menu = \n1. Input List\n2. Hapus List\n3. Lihat Data\n4. Buat Password\n5. Exit')
    a = int(input('Silakan pilih menu yang anda inginkan = '))
    if a == 1:
        b = int(input("Berapa data yang akan dimasukkan? "))
        for i in range (b):
            c = str(input('Silakan input kata = '))
            l1.append(c)
    elif a == 2:
        l1 = []
        print('Data berhasil dihapus')
    elif a == 3:
        print('Data yang diinputkan = ', l1)
    elif a == 4:
        changer(l1)
    elif a == 5:
        print('Terimakasih sudah menggunakan program kami')
        break
    else:
        print('Invalid Output')
