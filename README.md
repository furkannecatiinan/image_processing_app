# Digital Image Processing Application

A comprehensive Streamlit application for digital image processing with real-time preview and multi-language support.

## 🌍 Multi-Language Support

The application now supports both **Turkish** and **English** languages with complete localization:

### ✅ Completed Features

1. **Complete UI Translation**
   - All user interface elements are translated
   - Filter names and categories
   - Parameter labels and descriptions
   - Button texts and messages
   - Tips and help text

2. **State Preservation**
   - Language switching doesn't reset the application state
   - Uploaded images are preserved
   - Selected filters and parameters are maintained
   - Processed images are kept in memory

3. **Dynamic Content**
   - Filter categories update based on selected language
   - All tooltips and help messages are localized
   - Error messages and notifications are translated

### 🔧 Language System Architecture

#### Core Files:
- `languages.py` - Contains all translations and language utilities
- `utils.py` - State management and language switching utilities
- `app.py` - Main application with integrated language support

#### Key Functions:
- `get_text(key, language)` - Get localized text for any UI element
- `get_localized_filter_categories(language)` - Get filter categories in selected language
- `change_language(new_language)` - Switch language while preserving state
- `initialize_session_state()` - Initialize all session state variables

### 📝 Translation Coverage

#### UI Elements:
- ✅ Application title and headers
- ✅ Upload interface
- ✅ Filter selection menus
- ✅ Parameter sliders and inputs
- ✅ Button labels
- ✅ Tips and help messages
- ✅ Error messages
- ✅ Image captions and labels

#### Filter Categories:
- ✅ Basic Filters (Temel Filtreler)
- ✅ Advanced Filters (Gelişmiş Filtreler)
- ✅ Morphological Operations (Morfolojik İşlemler)
- ✅ Segmentation (Segmentasyon)

#### Filter Names:
- ✅ Gaussian Blur (Gaussian Bulanıklaştırma)
- ✅ Edge Detection (Kenar Belirleme)
- ✅ Thresholding (Eşikleme)
- ✅ Intensity Transform (Yoğunluk Dönüşümü)
- ✅ Frequency Filter (Frekans Filtresi)
- ✅ Noise Reduction (Gürültü Azaltma)
- ✅ Morphological Operations (Morfolojik İşlemler)
- ✅ Watershed Segmentation (Watershed Segmentasyonu)
- ✅ K-Means Clustering (K-Ortalama Kümeleme)

#### Parameters:
- ✅ Kernel Size (Çekirdek Boyutu)
- ✅ Sigma (Sigma)
- ✅ Method (Yöntem)
- ✅ Threshold Value (Eşik Değeri)
- ✅ Transform Type (Dönüşüm Türü)
- ✅ Filter Type (Filtre Türü)
- ✅ Operation (İşlem)
- ✅ And many more...

### 🚀 How to Use

1. **Language Selection**: Use the language buttons in the top-right corner
2. **State Preservation**: Your current work (uploaded image, selected filters, etc.) will be preserved when switching languages
3. **Dynamic Updates**: All UI elements update immediately when language is changed

### 🛠️ Technical Implementation

#### State Management:
```python
# Initialize session state
initialize_session_state()

# Change language without losing state
change_language('en')  # or 'tr'

# Restore state after language change
restore_state()
```

#### Translation Usage:
```python
# Get localized text
title = get_text('title', st.session_state.language)

# Get localized filter categories
categories = get_localized_filter_categories(st.session_state.language)
```

### 📚 Content Files

The application includes localized content files in the `info/` directory:
- `fundamentals.md` / `fundamentals_tr.md` - Basic concepts
- `gaussian_blur.md` / `gaussian_blur_tr.md` - Gaussian blur information
- `edge_detection.md` / `edge_detection_tr.md` - Edge detection details
- `threshold.md` / `threshold_tr.md` - Thresholding information
- And more...

### 🎯 Benefits

1. **User Experience**: Users can work in their preferred language
2. **State Preservation**: No loss of work when switching languages
3. **Complete Coverage**: All UI elements are properly translated
4. **Maintainable**: Centralized translation system for easy updates
5. **Extensible**: Easy to add new languages in the future

## 🚀 Running the Application

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py

# Or use the provided script
./run.sh
```

The application will be available at `http://localhost:8501` with full Turkish-English language support.

## 🔄 Language Switching

- Click the 🇹🇷 **Türkçe** button for Turkish
- Click the 🇺🇸 **English** button for English
- Your current work (uploaded image, selected filters, parameters) will be preserved

## 📝 Adding New Translations

To add new translations:

1. Add new keys to the `TRANSLATIONS` dictionary in `languages.py`
2. Provide both English and Turkish translations
3. Use the `get_text()` function in your code

Example:
```python
# In languages.py
'transforms': 'Intensity Transforms',
'transforms': 'Yoğunluk Dönüşümleri',

# In your code
text = get_text('transforms', st.session_state.language)
```

The language system is now complete and provides a seamless bilingual experience for users!

## Özellikler

### Çok Dilli Destek
- **Türkçe** - Tam Türkçe arayüz ve açıklamalar
- **İngilizce** - Complete English interface and descriptions

### Tema Desteği
- **Light Mode** - Klasik beyaz tema
- **Dark Mode** - Modern koyu tema

### Görüntü İşleme Kategorileri

1. **Temel Kavramlar (Fundamentals)**
   - Gaussian Bulanıklaştırma
   - Kenar Belirleme (Sobel, Canny)
   - Eşikleme (Binary, Otsu, Adaptive)

2. **Yoğunluk Dönüşümleri (Intensity Transforms)**
   - Doğrusal Dönüşüm
   - Logaritmik Dönüşüm
   - Güç Yasası (Gamma)
   - Histogram Eşitleme

3. **Frekans Alanı (Frequency Domain)**
   - Alçak Geçiren Filtre
   - Yüksek Geçiren Filtre
   - Bant Geçiren Filtre

4. **Görüntü Restorasyon (Image Restoration)**
   - Gürültü Ekleme (Gaussian, Salt&Pepper, Speckle)
   - Gürültü Azaltma (Gaussian, Median, Bilateral)

5. **Renk İşleme (Color Processing)**
   - Renk Dengesi
   - Renk Yumuşatma
   - Renk Uzayı Dönüşümü (RGB, HSV, LAB, YUV)
   - Sahte Renk

6. **Wavelet Dönüşümü (Wavelet Transform)**
   - Haar Wavelets
   - Daubechies Wavelets
   - Biorthogonal Wavelets

7. **Görüntü Sıkıştırma (Image Compression)**
   - JPEG Sıkıştırma
   - Wavelet Sıkıştırma
   - Run Length Encoding
   - Huffman Kodlama

8. **Morfolojik İşlemler (Morphological Operations)**
   - Aşındırma (Erosion)
   - Genişletme (Dilation)
   - Açma (Opening)
   - Kapama (Closing)

9. **Görüntü Bölütleme (Image Segmentation)**
   - Watershed
   - GrabCut
   - K-Means Clustering

10. **Özellik Çıkarımı (Feature Extraction)**
    - Temel Özellikler
    - Doku Özellikleri
    - Renk Histogramı

## Kurulum

### 1. Gereksinimler
```bash
cd streamlit
pip install -r requirements.txt
```

### 2. Uygulamayı Çalıştırma
```bash
streamlit run app.py
```

Uygulama varsayılan olarak `http://localhost:8501` adresinde açılacaktır.

## Kullanım

### 1. Görüntü Yükleme
- Sol kenar çubuğundaki "Upload Image" butonunu kullanın
- Desteklenen formatlar: PNG, JPG, JPEG, BMP, TIFF
- Alternatif olarak örnek görüntüleri kullanabilirsiniz

### 2. Filtre Seçimi
- Sol kenar çubuğundan bir kategori seçin
- Her kategori kendi filtre seçenekleri sunar
- Parametreleri ayarlayın ve "Apply Filter" butonuna basın

### 3. Sonuç Görüntüleme
- Orijinal ve işlenmiş görüntüler yan yana görüntülenir
- İşlenmiş görüntüyü "Download Processed Image" butonu ile indirebilirsiniz

### 4. Dil ve Tema Değiştirme
- Sağ üst köşeden dil seçeneklerini değiştirebilirsiniz
- Dark Mode'u açıp kapatabilirsiniz

## Proje Yapısı

```
streamlit/
├── app.py                 # Ana Streamlit uygulaması
├── languages.py           # Çok dilli destek
├── filters_ui.py          # Filtre UI bileşenleri
├── utils.py              # Yardımcı fonksiyonlar
├── requirements.txt       # Python bağımlılıkları
├── .streamlit/
│   └── config.toml       # Streamlit konfigürasyonu
└── README.md             # Bu dosya
```

## Orijinal Tkinter Versiyonundan Farklar

### Avantajlar
- **Web Tabanlı**: Herhangi bir tarayıcıdan erişilebilir
- **Modern UI**: Daha temiz ve kullanıcı dostu arayüz
- **Responsive**: Farklı ekran boyutlarına uyum
- **Kolay Paylaşım**: URL ile kolayca paylaşılabilir
- **Otomatik Güncellemeler**: Kod değişiklikleri anında yansır

### Teknik İyileştirmeler
- **Gerçek Zamanlı Önizleme**: Parametreler değiştirildiğinde anlık görüntü
- **Otomatik Görüntü Boyutlandırma**: Ekrana göre otomatik ölçeklendirme
- **Gelişmiş Hata Yönetimi**: Daha iyi hata mesajları
- **Performans Optimizasyonu**: Streamlit'in caching özelliği

## Geliştirme

### Yeni Filtre Ekleme
1. `filters/` klasöründe yeni filtre fonksiyonunu ekleyin
2. `filters_ui.py` dosyasında UI kontrollerini tanımlayın
3. `languages.py` dosyasında çevirileri ekleyin

### Tema Özelleştirme
`utils.py` dosyasındaki `apply_dark_mode()` fonksiyonunu düzenleyin.

## Sorun Giderme

### Yaygın Sorunlar
1. **Import Hatası**: Ana dizinin Python path'inde olduğundan emin olun
2. **Görüntü Yüklenmiyor**: Dosya formatının desteklendiğini kontrol edin
3. **Filtre Çalışmıyor**: Görüntünün önce yüklendiğinden emin olun

### Destek
Sorunlar için GitHub issues açabilir veya kod geliştirmelerine katkıda bulunabilirsiniz.

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

---

**Not**: Bu Streamlit versiyonu, orijinal Tkinter uygulamasının tüm özelliklerini koruyarak modern bir web arayüzü sunar. Tüm görüntü işleme algoritmaları aynı kalmış, sadece kullanıcı arayüzü modernize edilmiştir. 