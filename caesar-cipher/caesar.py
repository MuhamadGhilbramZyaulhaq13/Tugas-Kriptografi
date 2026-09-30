"""
Caesar Cipher (cipher substitusi abjad-tunggal)
Enkripsi: c = (p + k) mod 26
Dekripsi: p = (c - k) mod 26
Hanya huruf alfabet yang diproses; karakter lain dibiarkan.
"""


def geser(teks, k):
    hasil = []
    for ch in teks:
        if ch.isascii() and ch.isalpha():
            awal = ord('A') if ch.isupper() else ord('a')
            hasil.append(chr((ord(ch) - awal + k) % 26 + awal))
        else:
            hasil.append(ch)
    return "".join(hasil)


def enkripsi(plainteks, k):
    return geser(plainteks, k)


def dekripsi(cipherteks, k):
    return geser(cipherteks, -k)


def brute_force(cipherteks):
    """Kriptanalisis exhaustive key search: coba semua 26 kunci."""
    for k in range(26):
        print(f"k = {k:2d} -> {dekripsi(cipherteks, k)}")


def main():
    while True:
        print("\n=== CAESAR CIPHER ===")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Brute force (kriptanalisis)")
        print("4. Keluar")
        pilih = input("Pilih menu: ").strip()
        if pilih == "1":
            teks = input("Plainteks: ")
            k = int(input("Kunci (0-25): "))
            print("Cipherteks:", enkripsi(teks, k))
        elif pilih == "2":
            teks = input("Cipherteks: ")
            k = int(input("Kunci (0-25): "))
            print("Plainteks:", dekripsi(teks, k))
        elif pilih == "3":
            brute_force(input("Cipherteks: "))
        elif pilih == "4":
            break
        else:
            print("Menu tidak valid.")


if __name__ == "__main__":
    main()
