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