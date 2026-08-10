# Konsep Arsitektur Dasar Django

* **WEB FRAMEWORK PARADIGM**
  Logika arsitektur di mana infrastruktur dasar web dinamis (seperti penanganan protokol HTTP, *development server*, dan koneksi database untuk mengatasi sifat web yang *stateless*) diabstraksi secara otomatis. Mengapa digunakan: Membebaskan *engineer* dari tugas konfigurasi berulang, sehingga fokus komputasi dan waktu dialihkan murni untuk membangun logika bisnis (*fitur*) yang unik.

* **DJANGO PROJECT**
  Entitas level tertinggi (*top-level*) yang merepresentasikan **keseluruhan** aplikasi web (contoh: platform jejaring sosial secara utuh). Secara teknis, *Project* adalah wadah manajemen (kerangka kerja) yang menyimpan direktori utama dan seluruh konfigurasi/pengaturan global yang mengatur jalannya sistem.

* **DJANGO APP**
  Sub-modul atau komponen independen di dalam sebuah *Project* yang dirancang secara khusus untuk menjalankan **satu fungsionalitas spesifik** (contoh: fitur daftar teman, sistem komentar, atau *news feed*). Prinsip desain utamanya adalah *self-contained* (mandiri dan terisolasi).

* **PROJECT VS APP**
  Perbedaan arsitektural inti: *Project* adalah keseluruhan sistem web, sedangkan *App* adalah fitur-fitur modular penyusunnya (Relasi: 1 *Project* menampung Banyak *App*). Karena *App* bersifat mandiri, sebuah *App* dapat dicabut dan digunakan kembali (*reusable*) di *Project* lain yang berbeda. Ini adalah implementasi langsung dari prinsip DRY (*Don't Repeat Yourself*).

* **APPLICATION REGISTRY (INSTALLED_APPS)**
  Sistem pendataan internal Django (berisi *metadata*). Logika *edge-case*: Meskipun Anda sudah men-generate folder *App* baru di dalam *Project*, Django akan **mengabaikannya** sepenuhnya sampai Anda mendaftarkan *App* tersebut ke dalam daftar `INSTALLED_APPS` di file pengaturan *Project*. Tanpa registrasi ini, komponen *App* (seperti *models*, *views*, dan *URLs*) tidak akan bisa berinteraksi dengan ekosistem *framework*.