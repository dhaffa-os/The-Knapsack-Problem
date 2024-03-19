def knapsack(berat, nilai, kapasitas, jumlah):
    # kondisi dasar
    if jumlah == 0 or kapasitas == 0:
        return 0
    if t[jumlah][kapasitas] != -1:
        return t[jumlah][kapasitas]

    # kode diagram pilihan
    if berat[jumlah-1] <= kapasitas:
        t[jumlah][kapasitas] = max(
            nilai[jumlah-1] + knapsack(
                berat, nilai, kapasitas-berat[jumlah-1], jumlah-1),
            knapsack(berat, nilai, kapasitas, jumlah-1))
        return t[jumlah][kapasitas]
    elif berat[jumlah-1] > kapasitas:
        t[jumlah][kapasitas] = knapsack(berat, nilai, kapasitas, jumlah-1)
        return t[jumlah][kapasitas]

# Kode Driver
if __name__ == '__main__':
    keuntungan = [60, 100, 120]
    berat = [10, 20, 30]
    kapasitas = 50
    jumlah = len(keuntungan)
    
    # Kita menginisialisasi matriks dengan -1 pada awalnya.
    t = [[-1 for i in range(kapasitas + 1)] for j in range(jumlah + 1)]
    print('\nHasil Output = ', knapsack(berat, keuntungan, kapasitas, jumlah))
    print('\n')