"""
Vigenere Cipher (cipher substitusi abjad-majemuk)
Setiap huruf plainteks digeser sejauh huruf kunci yang berkoresponden.
Enkripsi: c_i = (p_i + k_i) mod 26
Dekripsi: p_i = (c_i - k_i) mod 26
Kunci diulang; hanya huruf alfabet yang diproses dan menghabiskan huruf kunci.
"""


def _proses(teks, kunci, arah):
    kunci = [ord(c) - ord('a') for c in kunci.lower() if c.isascii() and c.isalpha()]
    if not kunci:
        raise ValueError("Kunci harus berisi minimal satu huruf.")
    hasil, j = [], 0
    for ch in teks:
        if ch.isascii() and ch.isalpha():
            awal = ord('A') if ch.isupper() else ord('a')
            geser = arah * kunci[j % len(kunci)]
            hasil.append(chr((ord(ch) - awal + geser) % 26 + awal))
            j += 1
        else:
            hasil.append(ch)
    return "".join(hasil)


def enkripsi(plainteks, kunci):
    return _proses(plainteks, kunci, +1)


def dekripsi(cipherteks, kunci):
    return _proses(cipherteks, kunci, -1)


def main():
    while True:
        print("\n=== VIGENERE CIPHER ===")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Keluar")
        pilih = input("Pilih menu: ").strip()
        if pilih == "1":
            teks = input("Plainteks: ")
            kunci = input("Kunci (huruf): ")
            print("Cipherteks:", enkripsi(teks, kunci).upper())
        elif pilih == "2":
            teks = input("Cipherteks: ")
            kunci = input("Kunci (huruf): ")
            print("Plainteks:", dekripsi(teks, kunci).lower())
        elif pilih == "3":
            break
        else:
            print("Menu tidak valid.")


if __name__ == "__main__":
    main()
