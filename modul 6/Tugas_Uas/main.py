# Input data pegawai
nama_pegawai = input("Masukkan Nama Pegawai: ")
status_pegawai = input("Status Pegawai (Tetap/Tidak Tetap): ").lower()
gaji_pokok = float(input("Masukkan Gaji Pokok: "))
durasi_lembur = int(input("Masukkan Durasi Lembur (jam): "))

# Perhitungan
if status_pegawai == "tetap":
    tunjangan = 0.7 * gaji_pokok
    uang_lembur = durasi_lembur * (0.1 * gaji_pokok)
    gaji_bersih = gaji_pokok + tunjangan + uang_lembur
else:  # Tidak tetap
    tunjangan = 0
    uang_lembur = durasi_lembur * (0.05 * gaji_pokok)
    gaji_bersih = gaji_pokok + uang_lembur

# Output hasil
print("\n===== Rincian Gaji Pegawai =====")
print(f"Nama Pegawai       : {nama_pegawai}")
print(f"Status Pegawai     : {'Tetap' if status_pegawai == 'tetap' else 'Tidak Tetap'}")
print(f"Gaji Pokok         : Rp {gaji_pokok:,.2f}")
print(f"Tunjangan          : Rp {tunjangan:,.2f}")
print(f"Durasi Lembur      : {durasi_lembur} jam")
print(f"Uang Lembur        : Rp {uang_lembur:,.2f}")
print(f"Gaji Bersih        : Rp {gaji_bersih:,.2f}")