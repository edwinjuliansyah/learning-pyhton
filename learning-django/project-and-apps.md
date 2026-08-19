# Konsep Arsitektur Dasar Django

* **WEB FRAMEWORK PARADIGM**
  Logika arsitektur di mana infrastruktur dasar web dinamis (seperti penanganan protokol HTTP, *development server*, dan koneksi database untuk mengatasi sifat web yang *stateless*) diabstraksi secara otomatis. Mengapa digunakan: Membebaskan *engineer* dari tugas konfigurasi berulang, sehingga fokus komputasi dan waktu dialihkan murni untuk membangun logika bisnis (*fitur*) yang unik.

* **DJANGO CORE**
 Django adalah framework Python berskala tinggi yang mengusung filosofi "batteries-included" (fitur bawaan lengkap). Karena Django sudah mengemas fitur krusial secara bawaan seperti sistem autentikasi, panel admin, dan *middleware* keamanan penangkal serangan siber, *engineer* dapat langsung fokus menulis logika bisnis aplikasi yang unik tanpa harus merakit infrastruktur keamanan dari nol.

* **MVT**
 MVT adalah singkatan dari Model-View-Tamplate. Ini adalah pola arsitektur django untuk memisahkan bagian data, logic, dan tampilan.

* **DJANGO PROJECT**
  Entitas level tertinggi (*top-level*) yang merepresentasikan **keseluruhan** aplikasi web (contoh: platform jejaring sosial secara utuh). Secara teknis, *Project* adalah wadah manajemen (kerangka kerja) yang menyimpan direktori utama dan seluruh konfigurasi/pengaturan global yang mengatur jalannya sistem.

* **DJANGO APP**
  Sub-modul atau komponen independen di dalam sebuah *Project* yang dirancang secara khusus untuk menjalankan **satu fungsionalitas spesifik** (contoh: fitur daftar teman, sistem komentar, atau *news feed*). Prinsip desain utamanya adalah *self-contained* (mandiri dan terisolasi).

* **PROJECT VS APP**
  Perbedaan arsitektural inti: *Project* adalah keseluruhan sistem web, sedangkan *App* adalah fitur-fitur modular penyusunnya (Relasi: 1 *Project* menampung Banyak *App*). Karena *App* bersifat mandiri, sebuah *App* dapat dicabut dan digunakan kembali (*reusable*) di *Project* lain yang berbeda. Ini adalah implementasi langsung dari prinsip DRY (*Don't Repeat Yourself*).

* **APPLICATION REGISTRY (INSTALLED_APPS)**
  Sistem pendataan internal Django (berisi *metadata*). Logika *edge-case*: Meskipun Anda sudah men-generate folder *App* baru di dalam *Project*, Django akan **mengabaikannya** sepenuhnya sampai Anda mendaftarkan *App* tersebut ke dalam daftar `INSTALLED_APPS` di file pengaturan *Project*. Tanpa registrasi ini, komponen *App* (seperti *models*, *views*, dan *URLs*) tidak akan bisa berinteraksi dengan ekosistem *framework*.

* **THREE-TIER ARCHITECTURE**
 Pendekatan arsitektur modular yang memecah sistem perangkat lunak menjadi tiga lapisan logis yang terisolasi: *Presentation Tier* (UI/Front-End), *Application Tier* (Logika Back-End), dan *Data Tier* (Database). *Tujuan:* Menciptakan pemisahan tanggung jawab (*Separation of Concerns*). Jika ingin mengganti database tidak perlu merombak kode UI, begitu pula sebaliknya.

  ---

# Arsitektur & Inisialisasi Django Project

* **ISOLASI LINGKUNGAN (Virtual Environment)**
Praktik fundamental arsitektur Python di mana proyek dibungkus dalam environment yang terisolasi (menggunakan `venv`). *Mengapa digunakan:* Mencegah konflik versi *library* antar-proyek di mesin yang sama, sehingga *dependencies* Django untuk satu proyek tidak mencemari sistem operasi global atau proyek lainnya.

* **DJANGO-ADMIN vs MANAGE.PY**
 Keduanya adalah utilitas *Command-Line Interface* (CLI) untuk mengeksekusi perintah administratif (seperti *runserver* atau *startapp*). *Perbedaan arsitektur:* `django-admin` bersifat global, sedangkan `manage.py` adalah *wrapper* lokal yang ada di dalam root folder proyek. Secara logika, `manage.py` jauh lebih praktis digunakan karena secara otomatis sudah tertaut dengan konfigurasi `settings.py` proyek.

* **SINKRONISASI ORM (makemigrations vs migrate)**
Alur kerja dua tahap (*two-step mechanism*) yang menjembatani kode Python dengan tabel database. *Sebab-akibat:* Perintah `makemigrations` bertugas memindai kode model dan membuat "cetak biru" riwayat perubahan (file migrasi). Setelah itu, perintah `migrate` membaca cetak biru tersebut dan mengeksekusinya menjadi tabel fisik di dalam sistem database (seperti SQLite atau MySQL).

* **ANOMALI KEAMANAN (DEBUG & ALLOWED_HOSTS)**
Konfigurasi krusial di dalam `settings.py`. *Penanganan Edge-case:* `DEBUG = True` sangat membantu saat *development* karena memunculkan *error log* detail dan *hot-reloading*. Namun, ini **wajib** diubah ke `False` di *production* agar arsitektur server Anda tidak terekspos ke publik. Selain itu, `ALLOWED_HOSTS` bertindak sebagai *whitelist* keamanan; server akan menolak semua koneksi yang nama domain/IP-nya tidak terdaftar di daftar ini.

* **STANDAR KOMUNIKASI SERVER (WSGI vs ASGI)**
Protokol jembatan antara web server (seperti Nginx/Apache) dengan aplikasi Python. *Perbedaan Teknologi:* `wsgi.py` (Web Server Gateway Interface) adalah arsitektur klasik untuk menangani antrean *request* secara sinkronus (berurutan/satu per satu). Sedangkan `asgi.py` (Asynchronous Server Gateway Interface) adalah standar modern yang dirancang untuk menangani trafik web asinkronus (berbarengan/skala tinggi).

---

# Struktur App

Command `python3 manage.py startapp demoapp` menghasilkan struktur file berikut: 

```
C:demoproject 
│   db.sqlite3 
│   manage.py 
│ 
├───demoapp 
│   │   admin.py 
│   │   apps.py 
│   │   models.py 
│   │   tests.py 
│   │   views.py 
│   │   __init__.py 
│   │ 
│   └───migrations 
│           __init__.py 
│ 
└───demoproject 
    │   asgi.py 
    │   settings.py 
    │   urls.py 
    │   wsgi.py 
    │   __init__.py
```    
    
* **views.py**: berfungsi sebagai logika backend di server side, berkas ini berisikan fungsi fungsi app yang menerima request dan memberikan response (tampilan) kepengguna.

* **urls.py**: berfungsi sebagai dispacher url sesuai dengan urlpatterns yang sudah didefinisikan didalamnya. urls.py harus di buat manual, django tidak membuatnya secara otomatis karna tidak semua app harus memiliki urls.py

* **model.py**: berfungsi sebagai blueprint dari struktur basis data. mendefinisikan class sebagai tabel, variable sebagai kolom, dan isi variable sebagai tipe data.

* **test.py**: berfungsi sebagai pengujian kode di file lain secara otomatis.
