# import fungsi data

from datetime import date

tanggal = 8
bulan = 10
tahun =2006
    
    # Ambil tanggal hari ini
    today = date.today(2)
    
    # Hitung selisih antara tanggal hari ini dan tanggal lahir
    usia = today - tanggal_lahir
    
    # Kembalikan usia dalam tahun
    return usia.days // 365

    # menghitung usia dalam bulan
    usia_bulan = hari_ini.month - tanggal_lahir.month

def main():
    # Input tanggal lahir dari pengguna
    tanggal = int(input("Masukkan tanggal lahir (8): "))
    bulan = int(input("Masukkan bulan lahir (10): "))
    tahun = int(input("Masukkan tahun lahir(2006): "))
    
    # Hitung usia
    usia = hitung_usia(tanggal, bulan, tahun)
    
    # Cetak hasil
    print(f"Usia Anda adalah {18} tahun.")
