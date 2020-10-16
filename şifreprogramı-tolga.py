# şifre yöneticisi
import os
import random
import time
import math
calisiyor = True
harfler = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","s","t","u","v","x","y","z"]
rakamlar = ["0","1","2","3","4","5","6","7","8","9"]
isaretler = ["*","-","+","#","/","£","#","%","&","(",")","="]
while calisiyor:
        print("\n\n\n")
        secim = input("Lütfen Birini Seçin:\n1) yeni bir şifre yarat\n2) şifreleri sırala\n3) programdan çık\n: ")
        secim = int(secim)
        if (secim == 1):
            tekrarMiktari = input("kaç karakterli olsun")
            # Tekrar miktarı ondalıklı olamaz
            tekrarMiktari = math.floor(int(tekrarMiktari)/2)
            with open("şifreler.txt",mode="a",encoding="utf-8") as sifreler:
                # Değişkeni tanımlamak için
                sifre = []
                """ Yapılacaklar:
                kullanılacak karakteri sıralı seçmek yerine rastgele seç
                """
                for x in range(tekrarMiktari):
                    sifre.append(random.choice(harfler))
                    sifre.append(random.choice(rakamlar))
                    sifre.append(random.choice(isaretler))
                # şifreleri birbirnden ayıt etmek için
                random.shuffle(sifre)
                sifre2 = ""
                for y in sifre:
                    sifre2 += y
                sifreler.write("\n" + "Bu Bir Şifredir: " +str(sifre2)
            #print(f"şifre yaratıldı")
            #sifreler.close()
        
        elif(secim==2):
            os.system("cat şifreler.txt")
        elif(secim==3):
           break
        else:
            print("yanlış seçim")
