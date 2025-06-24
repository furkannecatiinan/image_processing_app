# Digital Image Processing Application

A comprehensive Streamlit-based digital image processing application inspired by the classic textbook **"Digital Image Processing" by Gonzalez & Woods**. This application brings theoretical concepts to life through an interactive, user-friendly interface.

## Inspiration

This project is inspired by **"Digital Image Processing" (4th Edition) by Rafael C. Gonzalez and Richard E. Woods**, the standard in digital image processing education. The application implements fundamental concepts from this textbook:

- Spatial Domain Processing (Chapter 3)
- Frequency Domain Processing (Chapter 4)
- Image Restoration (Chapter 5)
- Color Image Processing (Chapter 6)
- Morphological Processing (Chapter 9)
- Image Segmentation (Chapter 10)

## Features

### Core Operations
- **Spatial Filters**: Gaussian, Median, Bilateral filtering
- **Edge Detection**: Sobel, Canny, Laplacian operators
- **Thresholding**: Binary, Otsu, Adaptive methods
- **Morphological Operations**: Erosion, Dilation, Opening, Closing
- **Frequency Domain**: Low-pass, High-pass, Band-pass filters
- **Color Processing**: RGB transformations, Color space conversions
- **Image Restoration**: Noise reduction and enhancement
- **Segmentation**: Watershed, K-means clustering

### User Experience
- Real-time preview of filter effects
- Interactive parameter controls
- Multi-language support (English/Turkish)
- State preservation when switching languages
- Responsive design for desktop and mobile

## Quick Start

```bash
# Clone the repository
git clone https://github.com/furkannecatiinan/image_processing_app.git
cd image_processing_app

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

## Academic Applications

Perfect for:
- Computer Vision courses
- Digital Image Processing classes
- Research projects
- Self-study and algorithm testing

## Technical Stack

- **Frontend**: Streamlit
- **Image Processing**: OpenCV, NumPy, PIL
- **Visualization**: Matplotlib
- **Language Support**: Custom localization system

## Dependencies

```
streamlit>=1.28.0
opencv-python>=4.8.0
numpy>=1.24.0
Pillow>=10.0.0
matplotlib>=3.7.0
```

## Contributing

We welcome contributions! Please feel free to:
- Report bugs and issues
- Suggest new features
- Add new image processing algorithms
- Improve documentation

## License

This project is open source and available under the MIT License.

## Acknowledgments

- **Gonzalez & Woods**: For the foundational textbook
- **OpenCV Community**: For the excellent computer vision library
- **Streamlit Team**: For the amazing web framework

---

# Dijital Görüntü İşleme Uygulaması

**Gonzalez & Woods**'un klasik ders kitabından esinlenilerek geliştirilmiş kapsamlı bir Streamlit tabanlı dijital görüntü işleme uygulaması. Bu uygulama, teorik kavramları etkileşimli ve kullanıcı dostu bir arayüz aracılığıyla hayata geçirir.

## İlham Kaynağı

Bu proje, dijital görüntü işleme eğitiminde standart olan **Rafael C. Gonzalez ve Richard E. Woods**'un **"Digital Image Processing" (4. Baskı)** ders kitabından esinlenilmiştir. Uygulama, bu ders kitabındaki temel kavramları uygular:

- Uzamsal Alan İşleme (Bölüm 3)
- Frekans Alanı İşleme (Bölüm 4)
- Görüntü Restorasyonu (Bölüm 5)
- Renkli Görüntü İşleme (Bölüm 6)
- Morfolojik İşleme (Bölüm 9)
- Görüntü Bölütleme (Bölüm 10)

## Özellikler

### Temel İşlemler
- **Uzamsal Filtreler**: Gaussian, Median, Bilateral filtreleme
- **Kenar Belirleme**: Sobel, Canny, Laplacian operatörleri
- **Eşikleme**: Binary, Otsu, Adaptive yöntemler
- **Morfolojik İşlemler**: Aşındırma, Genişletme, Açma, Kapama
- **Frekans Alanı**: Alçak geçiren, Yüksek geçiren, Bant geçiren filtreler
- **Renk İşleme**: RGB dönüşümleri, Renk uzayı dönüşümleri
- **Görüntü Restorasyonu**: Gürültü azaltma ve iyileştirme
- **Bölütleme**: Watershed, K-means kümeleme

### Kullanıcı Deneyimi
- Filtre etkilerinin gerçek zamanlı önizlemesi
- Etkileşimli parametre kontrolleri
- Çok dilli destek (İngilizce/Türkçe)
- Dil değiştirirken durum korunması
- Masaüstü ve mobil için duyarlı tasarım

## Hızlı Başlangıç

```bash
# Repository'yi klonlayın
git clone https://github.com/furkannecatiinan/image_processing_app.git
cd image_processing_app

# Bağımlılıkları yükleyin
pip install -r requirements.txt

# Uygulamayı çalıştırın
streamlit run app.py
```

## Akademik Uygulamalar

Şunlar için mükemmel:
- Bilgisayarlı Görü dersleri
- Dijital Görüntü İşleme sınıfları
- Araştırma projeleri
- Kendi kendine öğrenme ve algoritma testi

## Teknik Altyapı

- **Ön Yüz**: Streamlit
- **Görüntü İşleme**: OpenCV, NumPy, PIL
- **Görselleştirme**: Matplotlib
- **Dil Desteği**: Özel yerelleştirme sistemi

## Bağımlılıklar

```
streamlit>=1.28.0
opencv-python>=4.8.0
numpy>=1.24.0
Pillow>=10.0.0
matplotlib>=3.7.0
```

## Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen:
- Hata ve sorunları bildirin
- Yeni özellikler önerin
- Yeni görüntü işleme algoritmaları ekleyin
- Dokümantasyonu iyileştirin

## Lisans

Bu proje açık kaynak kodludur ve MIT Lisansı altında kullanılabilir.

## Teşekkürler

- **Gonzalez & Woods**: Temel ders kitabı için
- **OpenCV Topluluğu**: Mükemmel bilgisayarlı görü kütüphanesi için
- **Streamlit Ekibi**: Harika web framework'ü için

---
