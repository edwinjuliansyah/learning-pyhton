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

  ---

  # Konsep Second Normal Form (2NF)

* **FUNCTIONAL DEPENDENCY**
  Logika relasi di mana nilai sebuah kolom (biasanya *non-primary key*) secara mutlak ditentukan oleh kolom lain yang unik (*primary key*). Secara intuitif, karena nilai seperti nama bisa ganda (misal: dua mahasiswa bernama "Tony"), sistem tidak bisa menggunakannya untuk pencarian spesifik; sistem harus menggunakan ID unik karena data personal tersebut bergantung secara fungsional pada entitas ID utamanya.

* **PARTIAL DEPENDENCY**
  Cacat desain atau *edge-case* yang terjadi secara khusus pada tabel berskema *Composite Primary Key*, di mana sebuah atribut non-kunci hanya bergantung pada *sebagian* dari kunci utama gabungan tersebut. Secara logika, ini memicu duplikasi data yang tidak perlu; contohnya, untuk mengetahui 'Nama Vaksin', sistem sebenarnya hanya butuh 'Vaccine ID', sehingga mengikatnya dengan 'Patient ID' merupakan sebuah redundansi struktural.

* **SECOND NORMAL FORM (2NF)**
  Standar arsitektur tabel progresif (berlaku setelah struktur lulus 1NF) yang menetapkan aturan mutlak: seluruh kolom non-kunci harus bergantung pada keseluruhan komponen *Primary Key*. Tabel yang masih menoleransi *Partial Dependency* dinyatakan gagal memenuhi standar 2NF dan akan tetap rentan terhadap anomali redundansi data.

* **2NF DECOMPOSITION**
  Solusi teknis untuk mencapai standar 2NF dengan memecah (*decompose*) satu tabel monolitik menjadi beberapa tabel terpisah berdasarkan entitas aslinya (misal: tabel Pasien, Vaksin, dan Status Vaksinasi). Melalui pemisahan ini, atribut non-kunci dialokasikan ke tabelnya masing-masing dan dijamin bergantung sepenuhnya 100% pada *Primary Key* tunggal di tabel barunya.

  ---

  # Konsep Third Normal Form (3NF)

* **HIERARKI NORMALISASI PROGRESIF**
  Logika dasar bahwa normalisasi adalah proses yang progresif. Sebuah database mutlak harus sudah divalidasi dan lolos aturan 1NF dan 2NF sebelum bisa dievaluasi untuk 3NF. Mengabaikan prasyarat fondasi ini akan membuat arsitektur 3NF menjadi cacat dan tidak valid.

* **TRANSITIVE DEPENDENCY**
  Cacat arsitektur di mana sebuah kolom non-kunci (*non-primary key*) diam-diam bergantung secara fungsional pada kolom non-kunci lainnya. Secara matematis direpresentasikan sebagai: Jika A menentukan B, dan B menentukan C, maka A menentukan C melalui B. Ini melanggar prinsip independensi data dalam satu tabel.

* **IDENTIFIKASI GEJALA TRANSITIF**
  Cara intuitif mendeteksi anomali ini adalah ketika Anda bisa menebak nilai suatu kolom hanya dengan melihat kolom lain yang bukan *Primary Key*. Contohnya: Jika Anda tahu nilainya 'Prancis' (Negara), Anda otomatis tahu bahasanya 'Prancis' (Bahasa). Karena keduanya bukan identitas utama (ID), keterikatan antar-mereka menciptakan duplikasi data yang tidak perlu di setiap baris.

* **THIRD NORMAL FORM (3NF)**
  Standar arsitektur tingkat tiga yang memiliki satu aturan mutlak: setiap atribut non-kunci harus bergantung sepenuhnya dan HANYA pada *Primary Key*, bukan pada atribut non-kunci lainnya. Jika diucapkan dalam kredo database: *"All attributes must depend on the key, the whole key, and nothing but the key."*

* **3NF DECOMPOSITION & FOREIGN KEY**
  Solusi teknis untuk membasmi *Transitive Dependency* dengan memecah atribut yang saling bergantung (seperti Negara dan Bahasa) menjadi tabel baru tersendiri (Tabel Negara). Di tabel utama yang lama, disisakan salah satu atribut (misal: Negara) untuk bertindak sebagai *Foreign Key* (Kunci Tamu) yang menautkan kembali kedua tabel tersebut. Pemecahan ini memastikan redundansi hilang, dan setiap nilai di tabel baru murni 100% patuh pada *Primary Key*-nya sendiri.