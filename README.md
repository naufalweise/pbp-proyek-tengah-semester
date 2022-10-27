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
Registrasi & login customer. Laman setting (nama dan alamat). Model yang dibuat: Customer.
- Pharmacy<br>
Registrasi apotek & edit profil apotek (untuk admin aplikasi). Model yang dibuat: Pharmacy.
- Market<br>
Laman untuk list obat yang dapat dibeli (untuk customer). Fitur search obat.
- Medicine<br>
CRUD obat (untuk admin aplikasi). Model yang dibuat: Medicine.
- Order<br>
Laman membuat order baru (untuk customer). Laman melihat order (untuk admin). Model yang dibuat: Order.

## Role
Role atau peran pengguna beserta deskripsinya:

### Admin Aplikasi
Dapat melakukan:
- Registrasi apotek
- Input Obat, lihat list obat
- Lihat daftar orderan obat
<br>

### Customer
Dapat melakukan:
- Lihat List Obat yang dapat dibeli
- Pesan obat
