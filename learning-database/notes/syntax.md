# DDL

Membuat Database `CREATE DATABASE nama_data;`

Menghapus Database `DROP DATABASE nama_data;`

Membuat table `CREATE TABLE nama_table (kolom1 tipe_data, kolom2 tipe_data, kolom3 tipe_data);`

Mengubah kolom table 
- Menambahkan kolom baru `ALTER TABLE nama_table ADD nama_kolom_baru tipe_data;`
- Menghapus kolom `ALTER TABLE nama_table DROP nama_kolom;`
- modifikasi tipe data `ALTER TABLE nama_table MODIFY nama_kolom tipe_data_baru;` selain tipe data bisa modifikasi untuk constraint.

# DML

Menambahkan data `INSERT INTO nama_table (kolom1, kolom2, kolom3) VALUES (data1, data2, data3);`

Menambahkan data kekolom kosong dengan referensi dari kolom ditable lain `INSERT INTO table_target (kolom1, kolom2) SELECT kolom_referensi1, kolom_referensi2 FROM nama_table_referensi;`

# DQL

Menampilkan data `SELECT kolom1, kolom2 FROM table;`, jika ingin menampilkan semua gunakan * `SELECT * FROM table;`

