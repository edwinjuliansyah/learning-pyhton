# Anatomi dan Struktur Data dalam Database

## Abstraksi Wadah Data: Tabel vs Entitas vs Objek
Ketiga istilah ini merujuk pada konsep penyimpanan yang sama namun dari paradigma yang berbeda. Disebut **Tabel** dalam konteks fisik/relasional, **Entitas** dalam pemodelan konseptual/logikal, dan **Objek** dalam Object-Oriented Database (OODB).

## Anatomi Data: Kolom (Field) vs Baris (Record)
Kolom mendefinisikan atribut spesifik dari data (seperti nama, ID), sedangkan baris adalah instansiasi dari atribut-atribut tersebut yang digabungkan menjadi satu entri/rekam jejak data tunggal yang utuh (misal: profil satu karyawan).

## Degree (Derajat) vs Cardinality (Kardinalitas)
**Degree** adalah jumlah total kolom atau atribut yang ada di dalam sebuah tabel. Sedangkan **Cardinality** jumlah total baris (record) yang ada di dalam sebuah tabel.

## Kontrak Tipe Data (Data Types)
Berfungsi bukan sekadar untuk membedakan angka dan huruf, tetapi sebagai pedoman (guideline) instruksional bagi engine SQL tentang bagaimana data harus disimpan secara fisik dan bagaimana kueri berinteraksi dengannya. Edge-case penting: Implementasi spesifik tipe data tidak universal dan bisa berbeda antar sistem (misal: MySQL vs SQL Server), sehingga engineer harus selalu merujuk pada dokumentasi sistem yang dipakai.

## Domain Data (Validasi Nilai)
Konsep lapisan keamanan untuk memastikan integritas data. Domain mendefinisikan batasan nilai "sah" (legal values) yang diizinkan masuk ke dalam suatu atribut/kolom, termasuk aturan panjang data dan fungsi lainnya, agar database tidak kemasukan junk data.

## Identitas Unik (Primary Key)
Digunakan secara absolut untuk mengidentifikasi setiap record secara spesifik, karena atribut biasa sangat rentan terhadap duplikasi (misal: dua karyawan bernama sama). Jika satu kolom tidak cukup unik untuk membedakan baris, sistem mengizinkan penggabungan beberapa kolom sekaligus untuk membentuk satu Primary Key (biasa disebut **Composite Key** di level engineering).

---

# Konsep Dasar Database Relasional

## Abstraksi Arsitektur: Relasi, Tuple, dan Skema

Dalam terminologi sistem relasional, **'Tabel'** diartikan sebagai **Relasi**, dan **'Baris'** (Record) disebut **Tuple**. Sebelum entri data terjadi, sistem mewajibkan adanya **'Skema'** (blueprint struktural) yang secara kaku mendefinisikan nama tabel, kolom pembentuknya, dan tipe datanya.

## Penanganan Data Masif: CLOB vs BLOB

Untuk menangani edge-cases payload data yang sangat besar melebihi kapasitas tipe string/binary standar. **CLOB** (Character Large Object) dialokasikan khusus untuk menyimpan blok teks raksasa (bergantung pada encoding teks), sedangkan **BLOB** (Binary Large Object) digunakan untuk menyimpan aliran data biner mentah seperti gambar, audio, atau dokumen compiled.

## Resolusi Identitas Mutlak: Primary Key & Composite Key

Aturan **Key Constraint** memaksa setiap tuple memiliki identitas unik untuk ditarik (query), dan tidak boleh `NULL`. Edge-case: Jika satu atribut tunggal gagal menjamin keunikan (misal: ID Pegawai tidak unik di tabel lintas-departemen), arsitektur mengizinkan penggabungan 2 kolom atau lebih menjadi satu entitas pengenal tunggal yang disebut **Composite Primary Key**.

## Jembatan Antar-Entitas: Foreign Key

Karena tabel dalam sistem relasional tidak boleh berdiri sendiri (siloed), **Foreign Key** digunakan sebagai pointer (penunjuk). Ini adalah kolom pada satu tabel yang merujuk secara langsung pada **Primary Key** di tabel lain, memungkinkan pemisahan entitas data tanpa kehilangan relasi logisnya.

## Filter Anomali Level Kolom: Domain Constraint

Ini adalah logika validasi gerbang depan. **Domain constraint** mencegah masuknya data sampah (garbage in) dengan memaksa setiap cell mematuhi aturan spesifik kolomnya (contoh: secara semantik, kolom nomor kontak memblokir input huruf, atau membatasi length maksimal 10 digit).

## Konsistensi Relasi Lintas-Tabel: Referential Integrity

Aturan sebab-akibat tertinggi antar tabel untuk mencegah anomali orphan records (data yatim piatu). Logikanya: Jika Tabel A memiliki **Foreign Key** yang menunjuk ke Tabel B, maka nilai data tersebut wajib eksis terlebih dahulu secara fisik di Tabel B. (Sistem akan melempar error jika kita memasukkan ID Siswa di tabel Nilai, namun ID tersebut belum terdaftar di tabel master Siswa).

---

# Konsep Key dalam Desain Basis Data Relasional

## Atribut Multi-Value

Konsep dasar di mana setiap kolom (attribute) dalam baris data harus memegang nilai tunggal (**simple attribute**). Atribut multi-nilai (contoh: satu kolom berisi list beberapa mata pelajaran) harus dihindari dalam desain relasional karena akan merusak integritas struktur data dan menyulitkan kueri.

## Candidate Key

Kolom apa pun dalam tabel yang memiliki data unik di setiap barisnya (tidak ada duplikasi) sehingga secara teknis berpotensi/kandidat untuk dijadikan pengidentifikasi baris tersebut. Satu tabel bisa memiliki beberapa **Candidate Key**.

## Primary Key vs Alternate Key

**Primary Key** adalah satu Candidate Key yang secara resmi dipilih oleh engineer sebagai identitas utama tabel tersebut. Sisa Candidate Key lain yang tidak terpilih secara otomatis statusnya menjadi **Alternate Key** (atau Secondary Key).

## Composite Key

Gabungan dua kolom atau lebih yang disatukan untuk membentuk sebuah identifier yang unik. Secara logika, teknik ini digunakan sebagai solusi fallback ketika sebuah tabel tidak memiliki satu pun kolom tunggal yang nilainya bisa dijamin 100% unik (misalnya: menggabungkan `Nama Staf` + `Jabatan`).

## Foreign Key

Kolom dalam sebuah tabel yang berisi referensi langsung ke Primary Key milik tabel lain. Secara arsitektural, ini adalah 'jembatan' fundamental yang mengeksekusi sifat "relasional" dari database—mengubah tabel-tabel yang terisolasi menjadi satu sistem yang saling terhubung.

---

# Jenis-Jenis Relasi Antartabel

Model relasional menghubungkan data antartabel menggunakan tiga jenis hubungan yang sering digambarkan melalui **ER-Diagram (Entity-Relationship Diagram)**:

| Jenis Relasi | Penjelasan | Contoh |
|---|---|---|
| **One-to-One (1:1)** | Satu data di Tabel A berhubungan dengan tepat satu data di Tabel B. | 1 Negara memiliki 1 Ibukota; 1 Kepala Departemen memimpin 1 Departemen. |
| **One-to-Many (1:N)** | Satu data di Tabel A berhubungan dengan banyak data di Tabel B. | 1 Pelanggan dapat membuat banyak Pesanan; 1 Mahasiswa mendaftar di banyak Kelas. |
| **Many-to-Many (N:N)** | Banyak data di Tabel A berhubungan dengan banyak data di Tabel B. | Banyak Mahasiswa dibimbing oleh banyak Staf; Pelanggan membeli banyak Produk. |

> *Relasi* Many-to-Many *biasanya tidak dibiarkan begitu saja, melainkan dipecah menjadi dua relasi* One-to-Many *dengan menambahkan sebuah tabel perantara (sering disebut `junction table`).*