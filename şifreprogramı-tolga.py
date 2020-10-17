# şifre yöneticisi
import os
import random
import time
import math
# while True da işe yarar çünkü break ile kapattım ana döngüyü
calisiyor = True
# senin yaptığın gibi listeler
harfler = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","s","t","u","v","x","y","z"]
rakamlar = ["0","1","2","3","4","5","6","7","8","9"]
isaretler = ["*","-","+","#","/","£","#","%","&","(",")","="]
while calisiyor:
        # arayüzü güzelleştirmek için
        print("\n\n\n")
        secim = input("Lütfen Birini Seçin:\n1) yeni bir şifre yarat\n2) şifreleri sırala\n3) programdan çık\n: ")
        secim = int(secim)
        if (secim == 1):
            # döngüde 3 fonsiyon var o yüzden 3'e bölüyoruz seçimi
            tekrarMiktari = input("kaç karakterli olsun")
            # Tekrar miktarı ondalıklı olamaz
            tekrarMiktari = math.floor(int(tekrarMiktari)/3)
            # internetten araştırdım bunu
            with open("şifreler.txt",mode="a",encoding="utf-8") as sifreler:
                # Değişkeni tanımlamak için bunu yapmayınca name is not defined diyordu döngüde de eşittir kulllanammazsın çünkü tekrar ediyor
                sifre = []
                """ Yapılacaklar:
                kullanılacak karakteri sıralı seçmek yerine rastgele seç
                """
                for x in range(tekrarMiktari):
                    sifre.append(random.choice(harfler))
                    sifre.append(random.choice(rakamlar))
                    sifre.append(random.choice(isaretler))
                random.shuffle(sifre)
                # şifre listesindeki elemanları yazmak için ayrı bir değişken
                sifre2 = ""
                # w3 schools'daki listeler kısmına bak
                for y in sifre:
                    sifre2 += y
                #dosyaya yazılan şifreleri birbirinden ayırt etmek için
                sifreler.write("\n" + "Bu Bir Şifredir: " +str(sifre2))
            print(f"şifre yaratıldı")
            sifreler.close()
        
        elif(secim==2):
            os.system("cat şifreler.txt")
        elif(secim==3):
           break
        else:
            print("yanlış seçim")
