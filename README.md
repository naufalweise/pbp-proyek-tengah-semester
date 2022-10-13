# Proyek Tengah Semester

## Daftar Anggota
Kelompok B01:
- Elang Permana
- Nadhira Shahnaz Zain
- Naufal Weise Widyatama
- Rafa Maritza
- Taqiya Zayin Hanafie

## Tautan Aplikasi Heroku
https://pbp-b01-proyek-tengah-semester.herokuapp.com/

## Deskripsi Aplikasi
Salah satu prioritas G20 adalah Global Health. Saat ini, banyak negara yang mengalami krisis kesehatan, lebih spesifiknya berkaitan dengan Anti-Microbial Resistance. OECD menargetkan untuk menyelesaikan isu ini dengan mempermudah akses antibiotik dan obat-obatan lainnya. Oleh karena itu, kami mengajukan aplikasi online pharmacy yang bertujuan untuk mempermudah akses obat-obatan ke masyarakat.

Aplikasi online pharmacy adalah aplikasi berbasis web yang menyediakan layanan pembelian obat secara online. Aplikasi ini menghubungkan pembeli dengan apotek dalam jual beli obat-obatan.

## Daftar Modul
Daftar modul yang akan diimplementasi:
- Customer<br>
Registrasi & login customer. Laman setting (nama, alamat, dll.)
- Admin aplikasi<br>
Registrasi apotek. Buat akun admin apotek.
- Market<br>
Laman utk list obat yg dpt dibeli (utk customer). Fitur search obat.
- Admin Apotek<br>
CRUD Obat apotek miliknya.
- Order<br>
Laman membuat order baru (utk customer). Laman melihat order (utk admin apotek).

## Role
Role atau peran pengguna beserta deskripsinya:

### Admin Aplikasi
Dapat melakukan:
- Registrasi Apotek
- Membuat akun admin apotek
### Admin Apotek
Dapat melakukan:
- Input Obat, lihat List obat
- Lihat daftar orderan obat
<br>
Hanya bisa mengakses data apotek miliknya.

### Customer
Dapat melakukan:
- lihat List Obat yang dpt dibeli
- Pesan obat
