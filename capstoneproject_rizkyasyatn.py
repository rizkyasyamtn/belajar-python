# Inisialisasi list untuk menyimpan data pasien
patients = []

# Fungsi untuk menampilkan semua data pasien
def read_patients():
    if len(patients) == 0:
        print("Tidak ada data pasien.")
    else:
        print("\nData Pasien Rumah Sakit:")
        for idx, patient in enumerate(patients):
            print(f"{idx+1}. ID: {patient['id']}, Nama: {patient['nama']}, Usia: {patient['usia']}, Diagnosa: {patient['diagnosa']}")

# Fungsi untuk menambahkan data pasien baru
def create_patient():
    id_pasien = input("Masukkan ID Pasien: ")
    nama = input("Masukkan Nama Pasien: ")
    usia = input("Masukkan Usia Pasien: ")
    diagnosa = input("Masukkan Diagnosa Pasien: ")
    
    # Tambahkan ke list patients
    patient = {
        'id': id_pasien,
        'nama': nama,
        'usia': usia,
        'diagnosa': diagnosa
    }
    
    patients.append(patient)
    print("Data pasien berhasil ditambahkan.")

# Fungsi untuk memperbarui data pasien
def update_patient():
    read_patients()
    if len(patients) == 0:
        return
    
    patient_id = input("Masukkan ID Pasien yang ingin diupdate: ")
    for patient in patients:
        if patient['id'] == patient_id:
            print("Data lama:")
            print(f"ID: {patient['id']}, Nama: {patient['nama']}, Usia: {patient['usia']}, Diagnosa: {patient['diagnosa']}")
            patient['nama'] = input("Masukkan Nama Baru: ")
            patient['usia'] = input("Masukkan Usia Baru: ")
            patient['diagnosa'] = input("Masukkan Diagnosa Baru: ")
            print("Data pasien berhasil diperbarui.")
            return
    print("Pasien dengan ID tersebut tidak ditemukan.")

# Fungsi untuk menghapus data pasien
def delete_patient():
    read_patients()
    if len(patients) == 0:
        return

    patient_id = input("Masukkan ID Pasien yang ingin dihapus: ")
    for patient in patients:
        if patient['id'] == patient_id:
            patients.remove(patient)
            print("Data pasien berhasil dihapus.")
            return
    print("Pasien dengan ID tersebut tidak ditemukan.")

# Fungsi utama untuk menjalankan sistem
def main():
    while True:
        print("\n--- Sistem Manajemen Data Pasien Rumah Sakit ---")
        print("1. Tambah Data Pasien")
        print("2. Lihat Data Pasien")
        print("3. Update Data Pasien")
        print("4. Hapus Data Pasien")
        print("5. Keluar")
        choice = input("Pilih opsi: ")
        
        if choice == '1':
            create_patient()
        elif choice == '2':
            read_patients()
        elif choice == '3':
            update_patient()
        elif choice == '4':
            delete_patient()
        elif choice == '5':
            print("Sistem keluar.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# Menjalankan program utama
if __name__ == "__main__":
    main()
