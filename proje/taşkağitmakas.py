print("              Taş-kağit-makas oyununa hoşgeldiniz.              ")
print("============================Kurallar============================")
print("    Siz taş, kağit ve makas arasinda bir seçim yaparsiniz.      ")
print("              Karşidaki oyuncu da bir seçim yapar.              ")
print(" Taş, makasi yener; makas, kağidi yener; kağit ise makasi yener.")
print("  Seçimlere göre bu şekilde oyun oynanir ve 2 olan kazanir.")
print("=============================DİPNOT=============================")
print("Oyundan çikmak istediğiniz anda terminale exit yazabilirsiniz")
print("================================================================")

import random,re

def sonuç(siz,rakip):
    if siz == "Taş" and rakip =="Makas" or siz == "Kağit" and rakip =="Taş" or siz == "Makas" and rakip == "Kağit": return "Galibiyet"
    elif siz == rakip: return "Beraberlik"
    else: return "Mağlubiyet"

def toplamsonuç(kişi,bilgisayar):
    if kişi == bilgisayar: return "Beraberlik"
    elif kişi > bilgisayar: return "Galibiyet"
    else: return "Mağlubiyet"

oyunsayisi = 0
kişiskor = 0
bilgisayarskor = 0
def taş_kağit_makas_ADINIZ_SOYADINIZ():
    global oyunsayisi,bilgisayarskor,kişiskor
    tursayisi = 0
    kişiturskor = 0
    bilgisayarturskor = 0
    oyunsayisi +=1

    while True:
        seçiminiz = str((input("Lütfen taş, kağit ve makastan birini seçiniz.")).lower()).capitalize().strip()
        while re.match((r"Taş|Kağit|Makas"),seçiminiz,re.IGNORECASE) is None:
            seçiminiz = str(input("Yanliş bir veri girdiniz. Lütfen taş, kağit ve makastan birini seçiniz.")).lower().capitalize().strip()
        rakipseçim = random.choice(["Taş","Kağit","Makas"])
        netice = sonuç(seçiminiz,rakipseçim)
        tursayisi +=1
        if netice == "Beraberlik":
            pass
        elif netice == "Mağlubiyet":
            bilgisayarturskor +=1
        else:
            kişiturskor +=1

        print("================TUR DURUM================")
        print("Seçiminiz:", seçiminiz)
        print("Rakibinizin seçimi:", rakipseçim)
        print("Tur sonucu:", netice)
        print("=========================================")

        
        print("===============ANLIK DURUM===============")
        print("Oyun sayisi:",oyunsayisi)
        print("Tur sayisi:",tursayisi)
        print("Skorunuz:",kişiturskor)
        print("Rakibin skoru:", bilgisayarturskor)
        print("=========================================")

        
        if kişiturskor == 2 or bilgisayarturskor == 2:
            if kişiturskor == 2:
                kişiskor +=1
            elif bilgisayarturskor == 2:
                bilgisayarskor +=1 
            print("===========GENEL SONUÇ============")
            print(f"Oyun sayisi {oyunsayisi}")
            print("Bilgisayarin kazandiği oyunlar:", bilgisayarskor)
            print("Sizin kazandiğiniz oyunlar:", kişiskor)
            print("Genel sonuç:", toplamsonuç(kişiskor,bilgisayarskor))
            print("==================================")
            tursayisi = 0
            kişiturskor = 0
            bilgisayarturskor = 0
            break

taş_kağit_makas_ADINIZ_SOYADINIZ()            

while True:
    print("Tekrar oynamak ister misiniz?")
    yanitiniz = str(input()).lower().capitalize().strip()
    if re.match(r"evet|hayir|HAYIR", yanitiniz, re.IGNORECASE):
        if yanitiniz == "Evet": taş_kağit_makas_ADINIZ_SOYADINIZ()    
        elif yanitiniz == "Hayir" or "HAYIR": break
        else: yanitiniz = str(input("Lütfen evet veya hayir yaziniz.")).lower().capitalize().strip()


            










    
        



    