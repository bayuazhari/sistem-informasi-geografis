## Latar Belakang Masalah :
1. Open Geospatial Consortium (OGC)
2. Arsitektur Open Geospatial Consortium (OGC)
3. Geospatial Web Services (GWS)
4. Tipe Geospatial Web Services (GWS)
5. Penggunaan Open Layer Dengan MapProxy

## Open Geospatial Consortium (OGC)
Open Geospatial Consortium (OGC) adalah sebuah konsorsium industri internasional yang didirikan pada tahun 1994 yang terdiri dari hampir 500 perusahaan, instansi pemerintahan, organisasi penelitian, LSM, dan universitas diseluruh dunia yang berkolaborasi dalam proses konsensus pengembangan dan penerapan standar untuk konten geospasial, Internet of Things, pengolahan data GIS dan data sharing.

## Arsitektur Open Geospatial Consortium (OGC)
Hubungan antara klien/server dan protokol OGC.
<p align ="center">
<img src="../../img/arsitektur-ogc.png" width="600px">
</p>

## Geospatial Web Services (GWS)
Geospatial Web Services (GWS) menjadi teknologi yang paling banyak digunakan untuk data sharing dan pertukaran data diantara para stakeholder geospasial. GWS membantu pengguna menemukan, mengakses, dan kadang-kadang memanipulasi data lokasi di web dinamis dari jaringan terdistribusi. GWS dirancang untuk mengumpulkan data sekaligus dan memperbarui atau mengedit data secara real time.

## Tipe Geospatial Web Services (GWS)
* Web Map Service (WMS)<br>
Web Map Service (WMS) memberikan pengguna sarana untuk melayani peta georeferensi yang disediakan database GIS menggunakan jaringan internet. WMS menghasilkan peta dalam format gambar seperti : PNG, JPEG atau GIS dan dapat ditampilkan pada browser.
* Web Map Tile Service (WMS)<br>
Web Map Tile Service (WMTS) hampir sama dengan Web Map Service (WMS), perbedaannya WMTS mengirimkan tiles (kebanyakan ukurannya 256x256 pixel), sementara WMS mengirimkan satu gambar per permintaan. Keuntungan utama dari tiles adalah bahwa tiles dapat pre-render pada sisi server, dan cache di sisi klien Hal ini akan mengurangi waktu menunggu data dan bandwidth.
* Web Feature Service (WFS)<br>
Web Feature Service (WFS) adalah antarmuka yang memungkinkan pengguna untuk mengakses dan memanipulasi informasi fitur geospasial dari sumber jaringan terdistribusi. operasi dasarnya termasuk GetCapabilities, DescribeFeatureType dan GetFeature.
* Web Coverage Service (WCS)<br>
Web Coverage Service (WCS) merupakan raster standar pelayanan OGC yang mengambil informasi geospasial yang berkaitan dengan fenomena multidimensi pada titik-titik dalam ruang yang berbeda-beda di wilayah geografis. Setiap WCS menyediakan akses ke informasi melalui tiga operasi: GetCapabilities, DescribeCoverage, dan GetCoverage.


## Penggunaan Open Layer Dengan MapProxy
Contoh penggunaan open layer mapproxy bisa di lihat di https://openlayers.org/en/latest/examples/xyz.html, edit untuk menampilkan peta Indonesia dengan merubah source dan viewnya:<br>
Source : https://map.vas.web.id/wmts/agm/webmercator/{z}/{x}/{y}.png<br>
View : ol.proj.transform([118.015776, -2.6000285], 'EPSG:4326', 'EPSG:3857')<br>
Contoh lengkapnya :
~~~
<!DOCTYPE html>
<html>
  <head>
    <title>XYZ</title>
    <link rel="stylesheet" href="https://openlayers.org/en/v3.20.1/css/ol.css" type="text/css">
    <!-- The line below is only needed for old environments like Internet Explorer and Android 4.x -->
    <script src="https://cdn.polyfill.io/v2/polyfill.min.js?features=requestAnimationFrame,Element.prototype.classList,URL"></script>
    <script src="https://openlayers.org/en/v3.20.1/build/ol.js"></script>
  </head>
  <body>
    <div id="map" class="map"></div>
    <script>
      var map = new ol.Map({
        target: 'map',
        layers: [
          new ol.layer.Tile({
            source: new ol.source.XYZ({
              url: 'https://map.vas.web.id/wmts/agm/webmercator/{z}/{x}/{y}.png'
            })
          })
        ],
        view: new ol.View({
          center: ol.proj.transform([118.015776, -2.6000285], 'EPSG:4326', 'EPSG:3857'),
          zoom: 5
        })
      });
    </script>
  </body>
</html>
~~~

## Kesimpulan
Jadi, Open Geospatial Consortium (OGC) merupakan organisasi internasional yang mengatur standar format penggunaan data geospasial, dan Geospatial Web Services (GWS) merupakan bagian dari OGC untuk kebutuhan penggunaan data geospasial di pemrograman berbasis GIS terdapat juga beberapa tipe GWS yaitu : Web Map Service (WMS), Web Map Tile Service (WMTS), Web Feature Service (WFS), dan Web Coverage Service (WCS).

## Saran
Diharapkan memahami materi secara mendetail dan perhatikan setiap perbedaan dari tipe Geospatial Web Services (GWS) dengan benar.
<br>
* Nama : Bayu Rahmad Azhari
* NPM : 1144125
* Kelas : 3C
* Prodi : D4 Teknik Informatika
* Kampus : Politeknik Pos Indonesia

Link Matakuliah : http://kampus.awangga.net/assignments/sisteminformasigeografis2016

Referensi : 
* https://live.osgeo.org/en/standards/standards.html
* http://www.istl.org/10-spring/internet2.html

Scan Plagiarisme :
* https://drive.google.com/open?id=0B5FSMUsdCMU4ZWVDNjNuS0dpMEk
* https://drive.google.com/open?id=0B5FSMUsdCMU4MlBNZzdHYVhmdVU 
