# Görüntü Eşikleme

Eşikleme, görüntü segmentasyonu ve ikili görüntüler oluşturmak için basit ancak etkili bir yöntemdir.

## Nasıl Çalışır
Filtre, belirli bir eşik değerinin üzerindeki pikselleri beyaza, altındakileri siyaha ayarlayarak görüntüyü siyah-beyaza dönüştürür.

## Parametreler
- **Eşik Değeri**: Siyah ve beyaz arasındaki kesim noktası (0-255)
- **Yöntem**: Eşikleme türü (Binary, Otsu, Adaptive)
- **Maksimum Değer**: Eşiğin üzerindeki pikseller için ayarlanacak değer

## Kullanım Alanları
- Belge tarama
- Metin çıkarımı
- Nesne segmentasyonu
- Maske oluşturma
- Karmaşık görüntüleri basitleştirme

## Eşikleme Yöntemleri

### Binary (İkili) Eşikleme
- **Özellik**: Sabit eşik değeri kullanır
- **Kullanım**: Kontrollü eşikleme gerekli durumlarda
- **Avantaj**: Basit ve hızlı

### Otsu Yöntemi
- **Özellik**: Otomatik eşik değeri hesaplama
- **Kullanım**: Bimodal histogramlı görüntüler
- **Avantaj**: Parametre gerektirmez

### Adaptive (Uyarlamalı) Eşikleme
- **Özellik**: Yerel komşuluk tabanlı eşikleme
- **Kullanım**: Değişken aydınlatma koşulları
- **Avantaj**: Aydınlatma değişimlerine dayanıklı

## Pratik İpuçları
- **Otsu**: Belirgin iki seviyeli görüntüler için ideal
- **Binary**: Eşik değerini bildiğiniz durumlarda
- **Adaptive**: Gölge ve aydınlatma problemleri için

## Uygulama Örnekleri
- **Belge işleme**: Metin-arka plan ayırımı
- **QR kod okuma**: Kod-arka plan kontrastı
- **Hücre sayımı**: Biyolojik görüntülerde hücre tespiti
- **Kalite kontrol**: Üründe kusur tespiti 