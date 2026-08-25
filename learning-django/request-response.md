# Dasar-Dasar HTTP & HTTPS

* **SIKLUS KLIEN-SERVER (HTTP REQUEST-RESPONSE)**

 HTTP adalah protokol fundamental web yang bekerja dengan sistem sebab-akibat. Browser (Klien) selalu menjadi pihak yang memulai komunikasi dengan mengirimkan *Request* untuk meminta/mengubah *resource*, dan Server wajib menjawab dengan *Response* (berisi status keberhasilan dan data yang diminta).

* **ANATOMI HTTP REQUEST**

 Sebuah *request* tidak sekadar menembak URL, melainkan membawa konteks yang terdiri dari: *Method* (niat/jenis aksi), *Path* (lokasi spesifik resource di server), *Version* (versi HTTP), dan *Headers* (metadata tambahan seperti jenis konten/autentikasi). Untuk aksi yang mengirim data, *request* juga akan membawa *Body* (muatan data).

* **SEMANTIK HTTP METHOD (GET vs POST vs PUT vs DELETE)**

 Digunakan agar server mengerti operasi pasti yang diinginkan klien. **GET** untuk mengambil data (membaca), **POST** untuk mengirim data baru ke server (membuat), **PUT** untuk menimpa/memperbarui data yang sudah ada di server secara keseluruhan, dan **DELETE** untuk menghapus resource.

* **LOGIKA KATEGORI STATUS CODE (1xx - 5xx)**

 Cara standar server mengomunikasikan nasib sebuah *request* melalui 3 digit angka agar klien/sistem bisa langsung bereaksi tanpa membaca isi konten: **1xx** (Informasional/sementara), **2xx** (Sukses), **3xx** (Redirection/dialihkan), **4xx** (Client Error/salah klien), dan **5xx** (Server Error/salah server).

* **KEAMANAN TRANSMISI (HTTP vs HTTPS)**

 HTTP mengirim data dalam teks polos (rentan disadap/dicuri). HTTPS menyelesaikan masalah ini dengan menambahkan lapisan **Enkripsi**. Sebelum data (seperti password atau kartu kredit) dikirim melalui jaringan, data diacak menjadi kode rahasia. Hanya komputer tujuan yang memiliki kunci untuk menerjemahkannya kembali.

---

# Siklus Request-Response dalam Django

* **ARSITEKTUR REQUEST-RESPONSE DJANGO**

 Dalam Django, protokol HTTP mentah diabstraksi menjadi objek berorientasi objek (OOP). Server otomatis membungkus *request* klien menjadi objek `HttpRequest` dan mengopernya ke fungsi *View*. Tugas *View* (logika backend) adalah memprosesnya dan wajib melahirkan/mengembalikan objek `HttpResponse` kepada klien.

* **ROUTING LOGIKA VIA `request.method`**

 Atribut esensial untuk membedakan niat klien (berbasis REST). Alih-alih membuat fungsi terpisah, *Engineer* menggunakan kondisional (misal: `if request.method == 'POST'`) untuk memisahkan logika pembacaan data (GET) dari logika manipulasi data (POST/PUT/DELETE) di dalam satu ruang *View* yang sama.

* **KAPSULASI PAYLOAD (`GET`, `POST`, `FILES`, `COOKIES`)**

 Cara Django memecah data klien menjadi format kamus (*dictionary-like*) yang mudah diakses. `GET` dan `POST` menangani parameter input form/URL, `FILES` khusus untuk menangani *stream* data berkas unggahan (*multipart*), dan `COOKIES` menangkap rekam jejak interaksi klien sebelumnya.

* **OTENTIKASI & EDGE-CASE HANDLING (`request.user`)**

 Properti bawaan untuk memvalidasi identitas sesi saat ini. Secara otomatis akan mengembalikan objek `User` jika klien telah login, atau objek `AnonymousUser` jika berstatus tamu. Ini adalah gerbang logika utama untuk mencegah *unauthorized access* pada data sensitif.

* **INSTANSIASI HTTP RESPONSE**

 Perbedaan mendasar: `HttpRequest` *diberikan/disuntikkan* oleh sistem ke dalam *View*, sedangkan `HttpResponse` harus *diciptakan/diinstansiasi* secara manual oleh *Engineer* di dalam *View*. Respons ini bisa berupa teks statis, namun secara arsitektur *best-practice*, objek ini digunakan bersama *Template Engine* untuk merender halaman HTML dinamis.

* **KONTROL MUTLAK HTTP RESPONSE**
 
 Objek `HttpResponse` bukan sekadar wadah untuk *body text* (`content`). Objek ini memberi *Back-End Engineer* kontrol penuh untuk memanipulasi *metadata* sebelum dikembalikan ke klien, seperti menyisipkan/mengubah Header HTTP, menyematkan *cookie* baru, atau menimpa `status_code` sesuai kondisi keberhasilan operasi di *server*.

---