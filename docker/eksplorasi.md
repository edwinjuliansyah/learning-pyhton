# Teori dan Fondasi Arsitektur Backend

## 1. Pergeseran Paradigma: Docker vs Virtual Machine (VM)
* **VM:** Memvirtualisasi *hardware*. Menjalankan OS utuh (Guest OS) di dalam OS utama. Berat, butuh RAM besar, dan harus *booting*.
* **Docker:** Memvirtualisasi pada level OS (*OS-level virtualization*). Tidak ada proses *booting* OS baru. Docker meminjam Kernel Linux dari sistem utama (host). 
* **Teknologi Kunci:** Isolasi di Docker bisa terjadi karena dua fitur Kernel Linux: **Namespaces** (mengisolasi proses/jaringan agar container merasa sendirian) dan **cgroups** (membatasi pemakaian maksimal CPU/RAM).

## 2. Standar Industri dan Lingkungan Native
Menjalankan Docker murni di atas partisi eksternal Ubuntu adalah lingkungan yang sangat ideal.
* Di Linux, Docker berjalan 100% *native* tanpa *overhead* terjemahan.
* Jika dijalankan di Windows atau macOS, Docker terpaksa membuat VM Linux super ringan di balik layar karena OS tersebut tidak memiliki Kernel Linux asli, sehingga sedikit mengorbankan performa (walaupun masih jauh lebih ringan dari VM tradisional).
* Menggunakan Docker membuat aplikasi **Agnostik Terhadap Cloud**; layaknya peti kemas, aplikasi ini bisa dijalankan di server AWS, GCP, atau laptop lokal dengan hasil yang 100% identik.

## 3. Microservices vs Modular Monolith
* **Modular Monolith:** Kodenya dipisah rapi berdasarkan fungsi, tapi tetap dijalankan di dalam 1 container/server. Jika satu fungsi *crash*, seluruh aplikasi mati.
* **Microservices:** Setiap fungsi aplikasi (misal: login, pembayaran) dijalankan di container yang berbeda-beda. Mereka saling mengobrol melalui jaringan (REST API) berkat fitur Port Mapping Docker.

## 4. Anatomi Container dan Manajemen Data
Ini adalah cara agar data *database* tidak menguap:
* **Sifat Ephemeral:** Container pada dasarnya fana. Data baru yang ditulis (seperti tabel *database*) hanya disimpan di lapisan *Writable Layer* menggunakan mekanisme *Copy-on-Write*. Saat container dihapus, *Writable Layer* ini ikut dihancurkan selamanya.
* **Volumes:** Untuk menyelamatkan data, ini adalah "jembatan" antara direktori di dalam container menuju *hard drive* fisik Ubuntu.
    * **Named Volumes:** Docker mengurus semuanya dan menyembunyikannya di `/var/lib/docker/volumes/`.
    * **Bind Mounts:** Saya yang menentukan sendiri letak *path* fisiknya (misal di folder *Home* saya).
* **Path Absolut:** Lokasi folder di dalam container (seperti `/var/lib/postgresql/data`) sudah *hardcoded* dari pembuat *image*-nya. Jika saya salah mengetik *path* ini, data tidak akan masuk ke Volume.

## 5. Eksplorasi Tingkat Sistem Operasi (Root)
Saya membuktikan teori dengan menembus keamanan Linux menggunakan `sudo su -` untuk melihat jantung Docker di `/var/lib/docker/`:
* **Ilusi OS:** Di dalam `/var/lib/docker/`, Docker diam-diam menyusun file-file sehingga membentuk direktori Linux yang utuh (`/bin`, `/etc`, `/root`). Aplikasi di dalam container tidak sadar bahwa ia hanya menumpang di folder Ubuntu saya.
* **Konsep Meta:** Saya mempelajari etimologi kata "Meta" yang berarti "Tentang". Sama seperti tag `<meta>` di HTML, file `metadata.db` di sistem Docker berfungsi sebagai buku catatan (Data tentang Data) yang mencatat inventaris Volume tanpa menyimpan data aktual *database* itu sendiri.
* **Rule of Silence:** Saya juga belajar bahwa di Linux, perintah yang dieksekusi dengan sukses sering kali tidak mengembalikan laporan teks apa pun, sehingga tidak perlu panik jika terminal tiba-tiba terdiam.