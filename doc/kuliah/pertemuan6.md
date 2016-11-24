## Latar Belakang Masalah :
1. Create Shapefile
2. Edit Shapefile
3. Delete Shapefile

## Create Shapefile
Cara create shapefile pada program python adalah sebagai berikut :
* import shapefile
* sf = shapefile.Writer(shapeType = 1)
* sf.shapeType
* sf.field(‘NAMA’, ‘C’, ‘40’)
* sf.field(‘PEMILIK’, ‘C’, ‘40’)
* sf.record(‘Warteg’, ‘Reza Fahlevi’)
* sf.point(10,10,0,0)
* sf.save(‘warteg.shp’) 

## Edit Shapefile
Cara edit shapefile pada program python adalah sebagai berikut :
* import shapefile
* sf = shapefile.Editor(shapefile = ‘warteg.shp’)
* sf.point(19,19,0,0)
* sf.record(‘Warung Padang’, ‘Riki Karnovi’)
* sf.save(‘warteg’)

## Delete Shapefile
Cara delete shapefile pada program python adalah sebagai berikut :
* import shapefile
* sf = shapefile.Reader(‘warteg.shp’)
* sf.record(0)
* sf.record(1)
* sf.shapes()[0].points
* sf.shapes()[1].points
* e = shapefile.Editor(‘warteg.shp’)
* e.shape(1)
* e.delete(1)
* e.save(‘warteg’)

## Kesimpulan
Jadi, kesimpulannya shapefile juga bisa menambah, mengubah dan menghapus data dengan mudah mengunakan python.

## Saran
Mudah-mudahan buat pertemuan selanjutnya materi dan praktikumnya dijelaskan lebih mendetail lagi.
<br>

* Nama : Bayu Rahmad Azhari
* NPM : 1144125
* Kelas : 3C
* Prodi : D4 Teknik Informatika
* Kampus : Politeknik Pos Indonesia

Link Matakuliah : http://kampus.awangga.net/assignments/sisteminformasigeografis2016

Referensi : https://pypi.python.org/pypi/pyshp 

Scan Plagiarisme :
* https://drive.google.com/open?id=0B5FSMUsdCMU4OGh6a2hpNkFiOEU
* https://drive.google.com/open?id=0B5FSMUsdCMU4d29xZnh0TGhLSk0 