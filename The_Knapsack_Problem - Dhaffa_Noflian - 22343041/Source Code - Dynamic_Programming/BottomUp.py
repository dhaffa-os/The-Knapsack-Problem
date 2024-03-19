def knapSack(kapasitas, berat, nilai, jumlah):
    K = [[0 for x in range(kapasitas + 1)] for x in range(jumlah + 1)]

    # Membangun tabel K[][] dalam cara bottom-up
    for i in range(jumlah + 1):
        for w in range(kapasitas + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif berat[i-1] <= w:
                K[i][w] = max(nilai[i-1]
                              + K[i-1][w-berat[i-1]],
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[jumlah][kapasitas]

# Kode Driver
if __name__ == '__main__':
    keuntungan = [60, 100, 120]
    berat = [10, 20, 30]
    kapasitas = 50
    jumlah = len(keuntungan)
    print('\nHasil Output = ', knapSack(kapasitas, berat, keuntungan, jumlah))
    print('\n')