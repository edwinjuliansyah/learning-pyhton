## DATA TYPES

**Mekanisme fundamental** untuk mendikte Database Management System (DBMS) tentang bagaimana menginterpretasi tipe data, bertindak sebagai **filter utama** yang memastikan setiap kolom hanya menerima format yang telah disepakati demi menjaga integritas sistem.

## INTEGER vs DECIMAL

Logika **presisi angka**; `INTEGER` hanya memproses bilangan bulat dan akan otomatis membulatkan (render up/down) data pecahan yang masuk, sedangkan `DECIMAL` dirancang untuk menyimpan presisi nilai fraksional secara absolut. Memaksa tipe data numerik agar hanya menerima angka positif (**unsigned**) akan melipatgandakan batas maksimum nilai yang bisa disimpannya.

## CHAR vs VARCHAR

**Arsitektur alokasi memori string**; `CHAR` mengalokasikan ruang memori secara statis di awal dan tidak bisa diubah (ideal untuk panjang data yang terprediksi/pasti), sedangkan `VARCHAR` mengalokasikan memori secara dinamis hanya sebesar jumlah karakter aktual yang diinputkan (efisien untuk data bervariasi agar memori tidak terbuang).

## TEXT TYPES

**Skalabilitas penyimpanan teks**; saat karakter melebihi batas kewajaran string biasa, logika database beralih ke tipe data spesifik berdasarkan besaran dokumen: `TINYTEXT` (paragraf pendek <255), `TEXT` (artikel <65.000), `MEDIUMTEXT` (buku <16,7 juta), hingga `LONGTEXT` (skala data masif hingga 4GB).

## DATABASE CONSTRAINTS

**Lapis pertahanan validasi** pada level kolom atau tabel. Secara logika, ini adalah fungsi **gatekeeper**—jika sebuah operasi (seperti insert/update) melanggar aturan yang ditetapkan, DBMS tidak akan berkompromi dan akan langsung menggugurkan (abort) eksekusi tersebut untuk mencegah korupsi data.

## NOT NULL vs DEFAULT

Strategi penanganan data kosong (null/empty); `NOT NULL` merupakan penanganan ketat yang akan menggagalkan perekaman jika kolom krusial dibiarkan kosong, sementara `DEFAULT` merupakan penanganan reaktif yang menyelamatkan perekaman dengan cara menyuntikkan nilai fallback secara otomatis saat tidak ada input dari pengguna.

---

# Peran Data Types

## Menentukan Aturan Operator (Komunikasi Sistem)

Tipe data adalah cara database mengidentifikasi dan membatasi operasi apa yang sah digunakan pada sebuah kolom. Misalnya, operasi aritmatika murni hanya berlaku untuk tipe data numerik, sementara pencarian pola (`LIKE`) didesain khusus untuk tipe data teks.

## Manajemen Alokasi Memori

Tipe data bertindak sebagai cetak biru bagi server untuk memesan kapasitas ruang penyimpanan yang presisi dan efisien di dalam hard drive maupun RAM (sebagai contoh, `TINYINT` memesan 1 byte, sedangkan `INT` memesan 4 byte).

## Penjaga Gerbang Integritas (Kontrak Data)

Tipe data berfungsi sebagai pertahanan pertama sistem yang secara otomatis menolak masukan data yang menyalahi format atau tidak logis (seperti menolak teks biasa yang dimasukkan ke dalam kolom `DATE`), sehingga memastikan data selalu bersih dan terprediksi.

## Optimasi Kecepatan Pencarian (Indeks)

Database mengurutkan indeks berdasarkan tipe datanya. Angka diurutkan secara matematis, sedangkan teks diurutkan secara leksikografis (seperti kamus). Definisi tipe data yang tepat membuat mesin database mampu menemukan data dalam jumlah masif dengan sangat cepat.

## Mencegah Konversi Siluman (Implicit Conversion)

Tipe data memaksa instruksi dieksekusi secara eksplisit. Hal ini mencegah sistem database mencoba "menebak-nebak" dan mengubah format data secara diam-diam di belakang layar, yang mana sering menjadi akar penyebab error atau anomali komputasi.

## Syarat Mutlak Relasi Antartabel (Primary & Foreign Key)

Dalam menghubungkan dua tabel yang berbeda, tipe data pada **Primary Key** (tabel referensi) dan **Foreign Key** (tabel anak) harus 100% identik. Kontrak kaku ini menjamin database tidak salah mencocokkan identitas dan memastikan proses penggabungan tabel (`JOIN`) berjalan sangat cepat tanpa beban memori yang tidak perlu.