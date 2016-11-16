## Latar Belakang Masalah :
1. Shapefile Geospasial
2. Beberapa Perintah Shapefile Pada Python

## Shapefile Geospasial
Shapefile sendiri adalah suatu format data geospasial yang biasa digunakan pada software Sistem Informasi Geografis. 

## Beberapa Perintah Shapefile Pada Python
Menambahkan data geospasial :
* Import Shapefile a = shapefile.writer()

SHP file Geometri
* a.point(x,y) a.poly([x,y],[x,y])

DBF file Table
* a.field(‘namafolder’,’C’,’4’) a.record(‘BDG’)

Disimpan dengan Method
* a.save(‘file.shp’)

Menambahkan data :
1. Poin = a.poly([a,b], [c,d])

2. Polygon = a.field(‘kota’,’C’,’4’)

Membuat Attribute :
* a.field(‘Kota’,’C’,’4’) a.record(‘Bandung’)

Menyimpan Shapefile :
* a.save(‘namafile’)

Parameter Writer :
1. Shapefile Poin = a.point(‘10’,’12’)

2. Shapefile Polygon = a.poly(ports = ([3.5], [5,5] , [5,7] ))

3. Shapefile Polyline = a.ports([3.5], [5,5] , [3,5], shapetype.shapefile.polyline)

## Kesimpulan
Jadi, kesimpulan pada pertemuan hari ini kita membahas bagaimana cara memanipulasi data pada geospasial dan mengetahui lebih detail tentang shapefile data dan beberapa perintah shapefile pada python.

## Saran
Mudah-mudahan buat pertemuan selanjutnya materi dan praktikumnya dijelaskan lebih mendetail lagi.

* Nama : Bayu Rahmad Azhari
* NPM : 1144125
* Kelas : 3C
* Prodi : D4 Teknik Informatika
* Kampus : Politeknik Pos Indonesia

Link Matakuliah : http://kampus.awangga.net/assignments/sisteminformasigeografis2016

Referensi : https://id.wikipedia.org/wiki/Shapefile 

Scan Plagiarisme :
* https://drive.google.com/open?id=0B5FSMUsdCMU4c1c5ODRSNjlrVEU
* https://drive.google.com/open?id=0B5FSMUsdCMU4ODgxVHc4blNmaUE