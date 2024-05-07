def hitung_total_harga(jumlah_barang):
    total = 0
    for i in range(jumlah_barang):
        harga_barang = float(input("Masukkan harga barang ke-{}: ".format(i + 1)))
        total += harga_barang
    return total

def main():
    jumlah_barang = int(input("Masukkan jumlah barang: "))
    total_harga = hitung_total_harga(jumlah_barang)
    print("Total harga belanjaan adalah:", total_harga)

if __name__ == "__main__":
    main()
