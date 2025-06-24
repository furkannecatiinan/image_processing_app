# Gaussian Bulanıklaştırma Filtresi

Gaussian Bulanıklaştırma filtresi, bir görüntüdeki gürültüyü ve detayları azaltmak için yaygın olarak kullanılan bir görüntü yumuşatma tekniğidir.

## Nasıl Çalışır
Filtre, görüntüyü bulanıklaştırmak için kullanılan bir çekirdek oluşturmak amacıyla Gaussian fonksiyonunu uygular. Her pikselin yeni değeri, komşu piksellerin Gaussian dağılımı tarafından belirlenen ağırlıklarla hesaplanan ağırlıklı ortalamasıdır.

## Parametreler
- **Çekirdek Boyutu**: Bulanıklaştırma etkisinin boyutunu kontrol eder (tek sayı olmalı)
- **Sigma**: Gaussian dağılımının yayılımını kontrol eder

## Kullanım Alanları
- Gürültü azaltma
- Kenar tespiti için ön işleme
- Yumuşak odaklama efektleri oluşturma
- Görüntü detayını azaltma

## Matematiksel Temel
Gaussian fonksiyonu: G(x,y) = (1/2πσ²) × e^(-(x²+y²)/2σ²)

## Avantajları
- Kenarları koruyarak yumuşatma
- Doğal görünümlü sonuçlar
- Ayarlanabilir yoğunluk
- Hızlı hesaplama

## Tipik Kullanım Senaryoları
- **Fotoğraf düzenleme**: Cilt yumuşatma, arka plan bulanıklaştırma
- **Bilimsel görüntüleme**: Gürültü azaltma, ön işleme
- **Computer Vision**: Özellik tespiti öncesi hazırlık
- **Web tasarım**: Görsel efektler 