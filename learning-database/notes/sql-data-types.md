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