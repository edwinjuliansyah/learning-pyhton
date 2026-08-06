# Konsep Normalisasi Database

* **DATABASE NORMALIZATION**
  Proses restrukturisasi arsitektur skema database untuk meminimalkan duplikasi data, mencegah anomali modifikasi, dan menyederhanakan query SQL dengan menerapkan prinsip bahwa setiap tabel hanya boleh merepresentasikan satu tujuan (single-purpose entity).

* **MULTI-PURPOSE TABLE ANTI-PATTERN**
  Akar penyebab terjadinya kesalahan struktur database adalah ketika satu tabel dipaksa menampung beberapa entitas sekaligus (misal: data mahasiswa, kursus, dan departemen digabung dalam satu tabel), yang menciptakan ketergantungan prosedural antar-entitas yang sebenarnya tidak berkaitan.

* **INSERT ANOMALY**
  Kegagalan sistem saat mencoba memasukkan data entitas baru karena adanya keterikatan dengan entitas lain. Secara logika, ini terjadi karena Primary Key constraint (tidak boleh NULL); contohnya, sistem tidak bisa menyimpan data "kursus baru" jika belum ada data "mahasiswa" yang mendaftar ke kursus tersebut.

* **UPDATE ANOMALY**
  Risiko inkonsistensi data (data inconsistency) dan inefisiensi komputasi akibat duplikasi atribut. Ketika satu fakta di dunia nyata berubah (misal: pergantian kepala departemen), sistem terpaksa melakukan operasi update pada puluhan atau ribuan baris yang berulang; gagal memperbarui satu baris saja akan merusak integritas seluruh database.

* **DELETION ANOMALY**
  Hilangnya data krusial secara permanen dan tidak disengaja (unintended data loss) akibat operasi penghapusan pada entitas lain. Ini terjadi karena data entitas A (misal: info departemen) menumpang pada baris data entitas B (misal: mahasiswa); saat mahasiswa terakhir di departemen tersebut dihapus dari tabel, seluruh referensi mengenai departemen itu ikut lenyap.

* **SINGLE-PURPOSE DECOMPOSITION**
  Solusi arsitektural dari normalisasi yaitu memecah (decompose) satu tabel monolitik menjadi beberapa tabel relasional yang independen (tabel Student, Course, dan Department terpisah), sehingga setiap operasi CRUD terisolasi dan hanya memengaruhi satu entitas domain secara spesifik.

  ---

  # Konsep First Normal Form (1NF)

* **FIRST NORMAL FORM (1NF)**
  Tahap fondasi normalisasi yang bertujuan menetapkan struktur dasar tabel dengan menegakkan dua aturan mutlak: memastikan *data atomicity* dan mengeliminasi kelompok data yang berulang (*repeating groups*).

* **DATA ATOMICITY**
  Prinsip di mana setiap sel (*field*) dalam tabel hanya boleh menampung satu nilai tunggal (*single instance value*). Menggabungkan beberapa nilai sekaligus (seperti dua nomor telepon dalam satu baris kontak) melanggar aturan ini dan menyulitkan sistem untuk mencari atau mengurutkan data.

* **ROW-SPLITTING ANTI-PATTERN**
  Cara keliru untuk mengatasi masalah *atomicity* dengan menduplikasi baris (membuat baris baru untuk setiap data yang ganda). Secara logika arsitektur ini gagal total karena merusak integritas tabel; *Primary Key* yang seharusnya menjadi identitas unik justru menjadi duplikat.

* **COLUMN-SPLITTING ANTI-PATTERN**
  Pendekatan salah lainnya yaitu memecah nilai ganda menjadi beberapa kolom terpisah (misal: telepon_1, telepon_2). Ini memicu masalah baru berupa *repeating groups*, di mana data entitas direkam berulang kali. Jika ada perubahan data pada entitas tersebut, teknisi harus melakukan pembaruan di banyak tempat sekaligus, yang sangat rawan menyebabkan *data inconsistency*.

* **1NF DECOMPOSITION & FOREIGN KEY**
  Solusi arsitektural yang sah untuk mencapai 1NF. Logikanya adalah mengidentifikasi entitas yang berbeda (misal: entitas "Kursus" dan "Tutor"), memecahnya menjadi tabel independen yang memiliki *Primary Key* masing-masing, lalu menautkan kembali kedua tabel tersebut secara relasional menggunakan *Foreign Key*.