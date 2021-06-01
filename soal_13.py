''' Rekursif
Buatlah sebuah program yang dapat mencari angka terkecil dan angka terbesar dari sebuah list

Input:
a = pemilihan pada menu
b = input data pada list

Proses dan Output:
membuat fungsi untuk mencari minimum dan maksimum
keduanya akan mengembalikkan value
deklarasi variabel l sebagi list kosong
membuat menu
membuat if sebagai pemilihan menu
memasukkan data jika inputnya adalah '1'
menghapus data ketika inputnya adalah '2'
melihat list yang sudah di inputkan ketika inputnya '3'
mencari nilai minimum dan maksimum jika inputnya '4'
mengakhiri program jika inputnya '5'
mengeluarkan output 'Invalid Input' jika inputnya bukan 1,2,3,4 atau 5
'''

def minimum(l):
    if len(l) == 1:
        return l[0]
    else:
        minNumber = minimum(l[1:])
        min = l[0]
        if minNumber < min:
            min = minNumber
        return min
def maximum(l):
    if len(l) == 1:
        return l[0]
    else:
        maxNumber = maximum(l[1:])
        max = l[0]
        if maxNumber > max:
            max = maxNumber
        return max

l = []

print('Selamat datang di program pencari nilai minimum dan maksimum')
while True:
    print('Menu =\n1. Input List\n2. Hapus List\n3. Lihat list yang sudah di input \n4. Cari \n5. Exit program')
    a = str(input('Silakan pilih yang ada di menu = '))
    if a == '1':
        print('Silakan masukkan data, input spasi untuk berhenti input data')
        while True:
            b = str(input())
            if b == ' ':
                break
            else:
                b = int(b)
                l.append(b)
    elif a == '2':
        print("List berhasil dihapus")
        l = []
    elif a == '3':
        print ('Data yang sudah di input =', l)
    elif a == '4':
        if len(l) == 0:
            print('Anda belum menginputkan data')
        else:
            print('Angka terkecil =', minimum(l))
            print('Angka terbesar =', maximum(l))
    elif a == '5':
        print('Terimakasih sudah menggunakan program kami')
        break
    else:
        print('Invalid Input')
