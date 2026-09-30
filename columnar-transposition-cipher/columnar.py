"""
Columnar Transposition Cipher (cipher transposisi)
Enkripsi: plainteks ditulis per baris dalam matriks selebar panjang kata kunci,
lalu dibaca per kolom sesuai urutan alfabet huruf kata kunci.
Jika baris terakhir kurang, diisi huruf dummy 'X'.
"""


def urutan_kolom(kunci):
    """Indeks kolom yang dibaca berurutan (huruf kembar: yang kiri lebih dulu)."""
    return sorted(range(len(kunci)), key=lambda i: (kunci[i], i))


def bersihkan(teks):
    return "".join(c for c in teks.upper() if c.isascii() and c.isalpha())


def enkripsi(plainteks, kunci, dummy="X"):
    kunci = bersihkan(kunci)
    p = bersihkan(plainteks)
    n = len(kunci)
    if n == 0:
        raise ValueError("Kata kunci tidak boleh kosong.")
    while len(p) % n != 0:
        p += dummy
    baris = [p[i:i + n] for i in range(0, len(p), n)]
    return "".join("".join(b[k] for b in baris) for k in urutan_kolom(kunci))


def dekripsi(cipherteks, kunci):
    kunci = bersihkan(kunci)
    c = bersihkan(cipherteks)
    n = len(kunci)
    if n == 0 or len(c) % n != 0:
        raise ValueError("Panjang cipherteks harus kelipatan panjang kunci.")
    tinggi = len(c) // n
    kolom = [None] * n
    for pos, k in enumerate(urutan_kolom(kunci)):
        kolom[k] = c[pos * tinggi:(pos + 1) * tinggi]
    return "".join(kolom[k][r] for r in range(tinggi) for k in range(n))


def main():
    while True:
        print("\n=== COLUMNAR TRANSPOSITION CIPHER ===")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Keluar")
        pilih = input("Pilih menu: ").strip()
        if pilih == "1":
            teks = input("Plainteks: ")
            kunci = input("Kata kunci: ")
            print("Cipherteks:", enkripsi(teks, kunci))
        elif pilih == "2":
            teks = input("Cipherteks: ")
            kunci = input("Kata kunci: ")
            print("Plainteks:", dekripsi(teks, kunci).lower())
        elif pilih == "3":
            break
        else:
            print("Menu tidak valid.")


if __name__ == "__main__":
    main()
