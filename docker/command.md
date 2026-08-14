# Command Docker & Linux untuk Backend

## 1. Instalasi Docker Engine (Native Ubuntu)

* `sudo apt-get remove docker docker-engine docker.io containerd runc` : Membersihkan sisa paket Docker tidak resmi bawaan Ubuntu.
* `sudo apt-get update` : Memperbarui buku indeks repositori Ubuntu.
* `sudo apt-get install ca-certificates curl gnupg` : Menginstal alat untuk mengunduh jalur aman (HTTPS).
* `sudo install -m 0755 -d /etc/apt/keyrings` : Membuat folder rahasia untuk GPG key dengan hak akses ketat.
* `curl -fsSL <url-kunci> | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg` : Mengunduh kunci keamanan secara diam-diam (`-s`) dan mengubah formatnya dari teks ke data rahasia.
* `sudo chmod a+r /etc/apt/keyrings/docker.gpg` : Memberikan izin agar semua pengguna (`a`) bisa membaca (`+r`) kunci tersebut.
* `echo <url-repo-otomatis> | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null` : Mendaftarkan repo Docker resmi. `> /dev/null` membuang teks laporan ke "lubang hitam" agar terminal tetap bersih (Rule of Silence).
* `sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin` : Menginstal paket utamanya.
* `sudo usermod -aG docker $USER` : Memasukkan user saya ke grup Docker agar bisa menjalankan perintah `docker` tanpa perlu mengetik `sudo` terus-menerus (wajib *restart* terminal setelahnya).

## 2. Eksplorasi Image & Named Volumes
Sebelum menyalakan container, saya bisa mengatur dan mengunduh komponennya secara manual.

* `docker pull postgres:16.4` : Mengunduh cetakan image secara *offline* agar nanti bisa dijalankan tanpa koneksi internet. Menggunakan tag `:16.4` (bukan `:latest`) agar versi software terkunci.
* `docker volume create data_pg_lokal` : Memerintahkan Docker membuat "brankas" data kosong lebih awal. Hasil data akan disimpan dalam `/var/lib/docker/volumes/` membutuhkan akses dewa/super root untuk masuk kedalamnya, gunakan command `sudo su -` untuk akses super root lalu `exit` untuk kembali ke akses normal
* `docker volume inspect data_pg_lokal` : Untuk melihat di letak fisik mana (Mountpoint) brankas itu berada di hard drive Ubuntu.

## 3. Running Server Database (PostgreSQL)
Menghidupkan server database lengkap dengan isolasi, pemetaan, dan penyimpanan permanen.

    docker run --name server-pg-lokal \
      -e POSTGRES_PASSWORD=rahasia \
      -p 5432:5432 \
      -v data_pg_lokal:/var/lib/postgresql/data \
      -d postgres:16.4

**Bedah Argumen:**
* `\` : Line continuation. Hanya untuk menyambung baris agar perintah panjang mudah dibaca, bukan untuk logika atau indentasi.
* `--name` : Memberi nama container agar saya tidak perlu repot menghafal ID acak.
* `-e` : Environment Variable. Menyuntikkan nilai sandi tepat saat OS container diciptakan.
* `-p` : Port Mapping. Membuat "lorong" dari port 5432 laptop Ubuntu saya, ditembuskan ke port 5432 milik dimensi container PostgreSQL.
* `-v` : Volumes. Menghubungkan brankas `data_pg_lokal` (Kiri) ke path mutlak `/var/lib/postgresql/data` (Kanan). **Ingat:** Path kanan tidak boleh salah ketik karena sudah *hardcoded* dari pabriknya.
* `-d` : Detached mode. Menjalankan server senyap di latar belakang agar saya tetap bisa memakai terminal.

## 4. Akses Database via CLI (Cara Puris)
Menyusup masuk ke dalam container untuk menggunakan alat klien bawaannya.

* `docker exec -it server-pg-lokal psql -U postgres`
  * `exec -it` : Membuka Interactive Terminal, menambatkan terminal host saya langsung ke dalam terminal shell container.
  * `psql` : Nama program klien resmi postgres.
  * `-U postgres` : Login menggunakan user default `postgres`.