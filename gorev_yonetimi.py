"""
Basit Görev Yönetim Uygulamasi (To-Do List)
"""

# Görev listesi - Programın başında boş bir liste
gorevler = []

# Dosya adı
dosya_adi = "gorevler.txt"


# Dosyadan görevleri okuma fonksiyonu
def gorevleri_oku():
    """Kaydedilmiş görevleri dosyadan okur"""
    try:
        dosya = open(dosya_adi, "r", encoding="utf-8")
        okunan_gorevler = []
        
        for satir in dosya:
            gorev = satir.strip()  # Baştaki ve sondaki boşlukları temizle
            if gorev != "":  # Boş satırları atlama
                okunan_gorevler.append(gorev)
        
        dosya.close()
        return okunan_gorevler
        
    except:
        # Dosya yoksa veya hata varsa boş liste döndür
        return []


# Dosyaya görevleri kaydetme fonksiyonu
def gorevleri_kaydet():
    """Görevleri dosyaya kaydeder"""
    try:
        dosya = open(dosya_adi, "w", encoding="utf-8")
        
        for gorev in gorevler:
            dosya.write(gorev + "\n")
        
        dosya.close()
        
    except:
        print("Hata: Dosyaya kaydedilemedi!")


# Görevleri listeleme fonksiyonu
def gorevleri_listele():
    """Tüm görevleri ekrana yazdırır"""
    print("\n--- GÖREV LİSTESİ ---")
    
    if len(gorevler) == 0:
        print("Henüz hiç görev yok.")
    else:
        for i in range(len(gorevler)):
            print(str(i + 1) + ". " + gorevler[i])
    
    print("---------------------\n")


# Yeni görev ekleme fonksiyonu
def gorev_ekle():
    """Yeni bir görev ekler"""
    yeni_gorev = input("Yeni görev: ")
    
    if yeni_gorev == "":
        print("Hata: Boş görev eklenemez!")
    else:
        gorevler.append(yeni_gorev)
        gorevleri_kaydet()
        print("Görev eklendi!")


# Görev silme fonksiyonu
def gorev_sil():
    """Bir görevi siler"""
    if len(gorevler) == 0:
        print("Silinecek görev yok!")
        return
    
    gorevleri_listele()
    
    try:
        numara = input("Silmek istediğiniz görevin numarası: ")
        numara = int(numara)
        
        if numara < 1 or numara > len(gorevler):
            print("Hata: Geçersiz numara!")
        else:
            silinen = gorevler[numara - 1]
            gorevler.remove(silinen)
            gorevleri_kaydet()
            print("Görev silindi!")
            
    except:
        print("Hata: Lütfen sayı girin!")


# Görev düzenleme fonksiyonu
def gorev_duzenle():
    """Bir görevi düzenler"""
    if len(gorevler) == 0:
        print("Düzenlenecek görev yok!")
        return
    
    gorevleri_listele()
    
    try:
        numara = input("Düzenlemek istediğiniz görevin numarası: ")
        numara = int(numara)
        
        if numara < 1 or numara > len(gorevler):
            print("Hata: Geçersiz numara!")
        else:
            print("Eski görev: " + gorevler[numara - 1])
            yeni_gorev = input("Yeni görev: ")
            
            if yeni_gorev == "":
                print("Hata: Boş görev eklenemez!")
            else:
                gorevler[numara - 1] = yeni_gorev
                gorevleri_kaydet()
                print("Görev güncellendi!")
                
    except:
        print("Hata: Lütfen sayı girin!")


# Ana menüyü gösterme fonksiyonu
def menu_goster():
    """Ana menüyü ekrana yazdırır"""
    print("\n===== GÖREV YÖNETİMİ =====")
    print("1. Görevleri Listele")
    print("2. Yeni Görev Ekle")
    print("3. Görev Düzenle")
    print("4. Görev Sil")
    print("5. Çıkış")
    print("==========================")


# PROGRAM BAŞLANGIÇ
print("Görev Yönetim Programına Hoş Geldiniz!")

# Başlangıçta kaydedilmiş görevleri yükle
gorevler = gorevleri_oku()

if len(gorevler) > 0:
    print(str(len(gorevler)) + " görev yüklendi.")


# Ana döngü
while True:
    menu_goster()
    secim = input("Seçiminiz (1-5): ")
    
    if secim == "1":
        gorevleri_listele()
        
    elif secim == "2":
        gorev_ekle()
        
    elif secim == "3":
        gorev_duzenle()
        
    elif secim == "4":
        gorev_sil()
        
    elif secim == "5":
        print("Programdan çıkılıyor. Görüşmek üzere!")
        break
        
    else:
        print("Hata: Geçersiz seçim! Lütfen 1-5 arası seçim yapın.")