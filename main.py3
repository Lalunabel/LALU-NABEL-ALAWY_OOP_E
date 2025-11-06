 # Kelas Induk
class Dosen:
    def __init__(self, nama, nim, usia, mata_kuliah):
        self.nama ="edy"
        self.nim = "123456"
        self.usia ="17"
        self.mata_kuliah ="pemrograman berorientasi objek"

    def tampilkan_data(self):
        print("=== Data Dosen ===")
        print(f"Nama         : {self.nama}")
        print(f"NIM          : {self.nim}")
        print(f"Usia         : {self.usia}")
        print(f"Mata Kuliah  : {self.mata_kuliah}")

# Kelas Anak (Mahasiswa) mewarisi dari Dosen
class Mahasiswa(Dosen):
    def __init__(self, nama, nim, usia, jurusan):
        # Gunakan init sendiri (tidak perlu atribut dosen seperti mata_kuliah)
        self.nama = "lalu nabel alawy"
        self.nim = "24241160"
        self.usia = "21"
        self.jurusan="pendidikan teknologi imformas"
    def tampilkan_data(self):
        print("=== Data Mahasiswa ===")
        print(f"Nama     : {self.nama}")
        print(f"NIM      : {self.nim}")
        print(f"Usia     : {self.usia}")
        print(f"Jurusan  : {self.jurusan}")


# Membuat objek dari kelas Dosen
dosen1 = Dosen("edy", "D001", 17, "Pemrograman Python")

# Membuat objek dari kelas Mahasiswa
mhs1 = Mahasiswa("Lalu Nabel", "M24311167", 21, "Teknik Informatika")

# Menampilkan data
dosen1.tampilkan_data()
print()  # baris kosong
mhs1.tampilkan_data()
