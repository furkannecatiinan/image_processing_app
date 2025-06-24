# Kenar Tespiti

Kenar tespiti, bir görüntü içindeki nesnelerin sınırlarını tanımlayan temel bir görüntü işleme tekniğidir.

## Nasıl Çalışır
Filtre, görüntüde parlaklığın hızla değiştiği alanları tespit ederek çalışır. Bu değişiklikleri tanımlamak ve kenar olarak işaretlemek için çeşitli operatörler (Sobel veya Canny gibi) kullanır.

## Parametreler
- **Yöntem**: Kenar tespit algoritması seçimi (Sobel, Canny)
- **Eşik**: Kenar tespitinin hassasiyetini belirler
- **Bulanıklaştırma**: Gürültüyü azaltmak için ön işleme bulanıklaştırma miktarı

## Kullanım Alanları
- Nesne sınır tespiti
- Özellik çıkarımı
- Görüntü segmentasyonu
- Desen tanıma
- Bilgisayarlı görü uygulamaları

## Algoritma Türleri

### Sobel Operatörü
- **Avantajları**: Hızlı, basit, etkili
- **Kullanım**: Genel amaçlı kenar tespiti
- **Özellikler**: X ve Y yönlerinde gradyan hesaplama

### Canny Kenar Algılayıcı
- **Avantajları**: Yüksek hassasiyet, temiz kenarlar
- **Kullanım**: Hassas kenar tespiti gerekli uygulamalar
- **Özellikler**: Çok aşamalı algoritma, gürültü direnci

## Pratik İpuçları
- **Düşük eşik**: Daha fazla kenar, daha fazla gürültü
- **Yüksek eşik**: Daha az kenar, daha temiz sonuç
- **Ön bulanıklaştırma**: Gürültülü görüntüler için önerilir

## Uygulama Alanları
- **Otonom araçlar**: Yol ve trafik işaret tespiti
- **Güvenlik sistemleri**: Hareket ve nesne tespiti
- **Tıbbi görüntüleme**: Organ ve doku sınır analizi
- **Kalite kontrol**: Üretim hatalarının tespiti 