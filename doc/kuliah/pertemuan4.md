## Latar Belakang Masalah :
1. Retrieve Data Geospasial
2. Shapefile Geospasial
3. Format .shp
4. Format .dbf

## Retrieve Data Geospasial
Retrieve data adalah salah satu cara untuk memanipulasi data yang digunakan untuk melihat isi data pada geospasial dengan format file .shp.

## Shapefile Geospasial
Shapefile sendiri adalah suatu format data geospasial yang biasa digunakan pada software Sistem Informasi Geografis. Format shapefile dibagi menjadi beberapa, dan disini kita membahas dua format yaitu format .shp dan .dbs.Shapefile sendiri adalah suatu format data geospasial yang biasa digunakan pada software Sistem Informasi Geografis. Format shapefile dibagi menjadi beberapa, dan disini kita membahas dua format yaitu format .shp dan .dbs.

## Format .shp
Format .shp merupakan salah satu bentuk file yang berada didalam shapefile yang menyimpan data dari geometri. Didalam file shp terdapat beberapa data seperti :
1. Bbox merupakan boundary box yaitu koordinat 4 titik atau koordinat batas view pada peta yang berbetuk persegi panjang di peta.
2. Shape Type ada beberapa jenis, diantaranya adalah :
• Point : koordinat titik bernomorkan standar 1 dari ESRI.
• PolyLine : koordinat titik-titik yang membentuk garis tapi tidak membentuk area bernomorkan standar 3 dari ESRI.
• Polygon : koordinat membentuk area bernomorkan standar 5 dari ESRI.
Membaca jumlah data geometri pada phython :
- import shapefile
- sf = shapefile.Reader(“negara.shp”)
- sf.shapes
- x = sf.shapes()
- print len(x)

## Format .dbf
Format .dbf merupakan sebuah format file yang dapat menyimpan file tabular dan menyimpan data atribut.
Membaca data dbf pada phython :
- import shapefile
- sf.records()
- sf.records(n)

## Kesimpulan
Jadi, kesimpulan pada pertemuan hari ini kita membahas bagaimana cara memanipulasi data pada geospasial dan mengetahui lebih detail tentang shapefile data geospasial.Jadi, kesimpulan pada pertemuan hari ini kita membahas bagaimana cara memanipulasi data pada geospasial dan mengetahui lebih detail tentang shapefile data geospasial.

## Saran
Buat praktikum mudah-mudahan buat pertemuan selanjutnya materi dan praktikumnya dijelaskan lebih mendetail lagi.

* Nama : Bayu Rahmad Azhari
* NPM : 1144125
* Kelas : 3C
* Prodi : D4 Teknik Informatika
* Kampus : Politeknik Pos Indonesia

Link Matakuliah : http://kampus.awangga.net/assignments/sisteminformasigeografis2016

Referensi : https://en.wikipedia.org/wiki/Data_retrieval 

Scan Plagiarisme :
* https://drive.google.com/open?id=0B5FSMUsdCMU4SnR5RjdNdGhpV00
* https://drive.google.com/open?id=0B5FSMUsdCMU4dXVnQ1AtRDd5UTQ

