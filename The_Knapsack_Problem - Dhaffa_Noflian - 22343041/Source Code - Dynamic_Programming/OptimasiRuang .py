def knapSack(kapasitas, berat, nilai, jumlah):
     
    # Membuat array dp
    dp = [0 for i in range(kapasitas+1)]
 
    # Mengambil i elemen pertama
    for i in range(1, jumlah+1):
         
        # Mulai dari belakang,
        # sehingga kita juga memiliki data
        # dari komputasi sebelumnya saat mengambil i-1 item
        for w in range(kapasitas, 0, -1):
            if berat[i-1] <= w:
                 
                # Menemukan nilai maksimum
                dp[w] = max(dp[w], dp[w-berat[i-1]]+nilai[i-1])
     
    # Mengembalikan nilai maksimum dari knapsack
    return dp[kapasitas]

# Kode Driver
if __name__ == '__main__':
    keuntungan = [60, 100, 120]
    berat = [10, 20, 30]
    kapasitas = 50
    jumlah = len(keuntungan)
    print('\nHasil Output = ', knapSack(kapasitas, berat, keuntungan, jumlah))
    print('\n')