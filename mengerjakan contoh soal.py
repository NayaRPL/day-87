print(''' buatlah variabel yang masing-masing dapat menampung nama,alamat,tanggal lahir,jenis kelamin
      tinggi badan, berat badan dan status.kemudian berikan nilai/value setiap variabel kemudian tampilkan 
      semua variabel tersebut.''')
print(        '#'*20     )
def soal_1():
    print('''      nama : nurul inayah
          alamat : limboro Timur , kelurahan Tande
          tanggal lahir : 10 maret 2002
          jenis kelamin: perempuan
          tinggi badan : 156
          berat badan : -
          status : mahasiswa''')
soal_1() 
print('''-buatlah program yang dapat menghitung harga jual tanah jika diketahui panjang dan lebar tanah tersebut.
      lebar dan panjang tanah di dapatkan dari inputan keyboard.Harga jual tanah parameter adalah Rp. 300.000 .''')
for i in range (1):
   lebar_tanah=int(input("masukkan lebar tanah : "))
   panjang_tanah=int(input("masukkan panjang tanah : "))
   luas_tanah=lebar_tanah*panjang_tanah
   harga_tanah = 300000 * luas_tanah
   print("harga tanah :",harga_tanah)
   

for i in range (1,100):
    if i % 3 != 1 :
        i+=1
        print(i) 
   
