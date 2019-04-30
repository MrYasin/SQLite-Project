"""

EP-13 --- 97

"""

from library import *


print("""


KÜTÜPHANE PROJESİ

1 - Kitapları göster
2 - Kitap sorgulama
3 - Kitap Ekle
4 - Kitap Sil
5 - Baskı Yükselt

Q - ÇIKIŞ


""")


library = Kutuphane()


while True:

    islem = input("\nYapacağınız işlem:\n")

    if islem.isalpha():
        print("\nProgram sonlandırılıyor...\n")
        break

    elif islem == 1:
        library.kitaplari_goster()

    elif islem == 2:
        isim = input("Hangi kitabı istiyorsunuz?")
        library.kitap_sorgula(isim)

    elif islem == 3:
        kitap_isim = input("İsim:\n")
        yazar_isim = input("Yazar:\n")
        yayinevi = input("Yayinevi:\n")
        tur = input("Tür:\n")
        baski = int(input("Baskı:\n"))

        yeni_kitap = Kitap(kitap_isim, yazar_isim, yayinevi, tur, baski)

        print("Kitap Ekleniyor...\n")
        time.sleep(1)

        library.kitap_ekle(yeni_kitap)
        print("Kitap Eklendi...")

    elif islem == 4:
        delete = input("Hangi kitabı silmek istiyorsunuz?\n")
        print("Kitap siliniyor...\n")
        time.sleep(1)

        library.kitap_sil(delete)
        print("Kitap silindi...\n")

    elif islem == 5:
        upgrade = input("Hangi kitabın baskısını yükseltmek istiyorsunuz?\n")
        print("Baskı yükseltiliyor...\n")

        time.sleep(1)
        library.baski_yukselt(upgrade)

    else:
        print("Geçersiz işlem...\n")




































