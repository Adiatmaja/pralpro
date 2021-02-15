'''
Eren telah memulai usaha sauna pada tahun 2019. Pada awal dibukanya usaha, usaha Eren berjalan dengan lancar.
pendapatan per bulannya ialah Rp. 25000000
Sedangkan Biaya air, listrik, perawatan dan gaji karyawan ialah Rp. 10000000 per bulannya
Namun, pada tahun 2020 dan setelahnya, pendapatan usaha Eren berkurang dikarenakan adanya pandemi yang mengakibatkan berkurang nya pelanggan.
Kerugian yang dialami usaha Eren berkurang hingga 25%, Hitunglah total pendapatan usaha Eren 2 tahun setelah dibukanya usaha Eren!
'''
# Input User
a = 25000000                                                          # Pendapatan
b = 10000000                                                          # Maintenance Cost
c = 2                                                                 # Tahun
d = c * 12                                                            # Jumlah Bulan

b1 = b * d                                                            # Total maintenance cost

a1 = 0                                                                # Sebagai tempat untuk menampung nilai pendapatan
for i in range (d):                                                   # For akan berjalan sebanyak jumlah tahun dikali 12
    if i < 12:
        a1 = a1 + a                                                   # Apabila masih di bulan 1 - 12, nilai akan ditambahkan ke tampungan
    else:
        a1 = a1 + (a * 0.75)                                          # Apabila sudah di bulan 12+, nilai yang akan ditambahkan ke tampungan sebelumnya dikurangi 25% terlebih dahulu

total = a1 - b1

print ("Total pendapatan selama", c, "Tahun adalah = Rp.", total)
