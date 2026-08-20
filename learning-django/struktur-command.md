# Command

- django-admin

`django-admin startproject nama_folder`

membuat struktur tamplate awal project django

- manage.py

`python manage.py (command)`

manage.py yang berfungsi sama seperti django-admin untuk tugashanya saja scopenya lokal 

- startapp

`python manage.py startapp (name of app)`

membuat sub project atau app untuk fungsi tertentu


- makemigrations

`python manage.py makemigrations`

django mengelola operasi basisdata dengan teknik ORM. Migrasi mengacu pada pembuatan tabel basis data yang strukturnya sesuai dengan model data yang dideklarasikan dalam aplikasi

- migrate

`pyhton manage.py migrate`

ini menyinkronkan status basis data dengan model dan migrasi yang saat ini telah dideklarasikan

- runserver

`python manage.py runserver`

ini memulai server pengembangan bawaan django di mesin lokal dengan alamat ip 127.0.0.1 dan port 8000.

- shell

`python manage.py shell`

perintah ini membuka shell python interaktif di dalam proyek. ini berguna ketika perlu melakukan beberapa operasi interaktif dengan cepat. django lebih memilih Ipython dari pada shell python standar, jika Ipython telah teristall

---

# Struktur project 

perintah startproject sebelumnya akan membuat folder dengan nama yang ditentukan dan didalamnya terdapat folderlain yang memiliki nama serupa. folder bagian dalam tersebut disebut sebagai package dan harus memiliki file __init__.py agar dikenai python. selain itu template startproject juga akan menambahkan 4 file py lain didalam folder tersebut

```
C:\djenv\demoproject 
│   manage.py 
│ 
└───demoproject 
        asgi.py 
        settings.py 
        urls.py 
        wsgi.py 
        __init__.py 
```

paket python berisi konfigurasi basis data yang digunakan oleh berbagai submodul (apps) dan pengaturan khusus lainnya

- setting.py

Django mengonfigurasi parameter-parameter tertentu beserta nilai defaultnya dan menempatkannya di berkas ini. 
Utilitas django-admin dan skrip manage.py menggunakan pengaturan ini saat melakukan berbagai tugas administratif.

- urls.py

Skrip ini berisi daftar objek urlpatterns. Setiap kali browser klien meminta sebuah URL, server Django akan mencari pola yang cocok dan mengarahkan aplikasi ke tampilan yang telah dipetakan. 

Struktur default urls.py berisi tampilan yang dipetakan ke situs Admin proyek.

```
from django.contrib import admin 
from django.urls import path 

 urlpatterns = [ 
    path('admin/', admin.site.urls), 
] 
```

- asgi.py

Berkas ini digunakan oleh server aplikasi yang mengikuti standar ASGI untuk menyajikan aplikasi web asinkron.

- wsgi.py

Banyak server aplikasi web mengimplementasikan standar WSGI. Berkas ini merupakan titik masuk bagi server yang kompatibel dengan WSGI tersebut untuk menyajikan aplikasi web klasik. 

## Isi settings.py

Berkas ini mendefinisikan atribut-atribut yang memengaruhi fungsi aplikasi Django. Template ` startproject ` menetapkan beberapa nilai default untuk atribut-atribut ini. Nilai-nilai tersebut dapat dimodifikasi sesuai kebutuhan selama penggunaan aplikasi.

- INSTALLED_APPS

Ini adalah daftar string. Setiap string mewakili jalur aplikasi di dalam folder proyek induk. Template startproject menginstal beberapa aplikasi secara default. Aplikasi-aplikasi tersebut muncul dalam daftar INSTALLED_APPS.

```
INSTALLED_APPS = [ 
    'django.contrib.admin', 
    'django.contrib.auth', 
    'django.contrib.contenttypes', 
    'django.contrib.sessions', 
    'django.contrib.messages', 
    'django.contrib.staticfiles', 
    'demoapp',
] 
```

Daftar ini harus diperbarui dengan menambahkan namanya setiap kali aplikasi baru diinstal. 

Misalnya, jika kita membuat demoapp dengan perintah berikut:

python manage.py startapp demoapp

```
INSTALLED_APPS = [ 
    'django.contrib.admin', 
    'django.contrib.auth', 
    'django.contrib.contenttypes', 
    'django.contrib.sessions', 
    'django.contrib.messages', 
    'django.contrib.staticfiles', 
    'demoapp',
] 
```

- Database

Atribut ini adalah kamus yang menentukan konfigurasi satu atau lebih basis data yang akan digunakan oleh aplikasi Django saat ini. Secara default, Django menggunakan basis data SQLite. Oleh karena itu, pengaturan ini memiliki konfigurasi yang telah ditentukan sebelumnya untuknya.

```
DATABASES = {   
    'default': {   
        'ENGINE': 'django.db.backends.mysql',   
        'NAME': 'djangotest',   
        'USER': 'root',   
        'PASSWORD': 'password',   
        'HOST': '127.0.0.1',   
        'PORT': '3306',            
    }   
} 
```

MySQL umumnya menggunakan port 3306. Port 8000 yang ditampilkan sebelumnya adalah port default untuk server web pengembangan Django, dan tidak terkait dengan SQLite (SQLite berbasis file dan tidak menggunakan port jaringan).

- DEBUG = True

Secara default, server pengembangan berjalan dalam mode debug. Hal ini membantu pengembangan aplikasi karena server mendeteksi perubahan dalam kode dan hasilnya dapat diperbarui tanpa perlu memulai ulang. Namun, mode ini harus dinonaktifkan di lingkungan produksi.

- ALLOWED HOSTS

Atribut ini berupa daftar string. Secara default, daftar ini kosong. Setiap string mewakili host/domain yang memenuhi syarat penuh tempat situs Django ini dapat disajikan. Misalnya, untuk membuat situs yang berjalan di localhost dapat dilihat dari luar, dapat menambahkan 0.0.0.0:8000 ke daftar ini.

- ROOT_URLCONF

`ROOT_URLCONF = 'demoproject.urls'`

Pengaturan ini berupa string yang mengarah ke modul urls.py tempat pola URL proyek berada. Dalam hal ini, pengaturannya adalah:

- STATIC_URL

Pengaturan ini mengarah ke folder tempat berkas statis, seperti kode JavaScript, berkas CSS, dan gambar, disimpan. Biasanya, pengaturan ini ditetapkan ke 'static/' yang sesuai dengan folder dengan nama tersebut di dalam folder induk proyek.

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
    
- views.py

berfungsi sebagai logika backend di server side, berkas ini berisikan fungsi fungsi app yang menerima request dan memberikan response (tampilan) kepengguna.

- urls.py

berfungsi sebagai dispacher url sesuai dengan urlpatterns yang sudah didefinisikan didalamnya. urls.py harus di buat manual, django tidak membuatnya secara otomatis karna tidak semua app harus memiliki urls.py

- model.py

berfungsi sebagai blueprint dari struktur basis data. mendefinisikan class sebagai tabel, variable sebagai kolom, dan isi variable sebagai tipe data.

- test.py

berfungsi sebagai pengujian kode di file lain secara otomatis.
