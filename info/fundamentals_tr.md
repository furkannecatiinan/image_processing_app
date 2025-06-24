# Temel Görüntü İşleme Kavramları

## Dijital Görüntü Temelleri

Dijital görüntü, her pikselin görüntüdeki bir noktayı temsil ettiği ve renk veya yoğunluk bilgisi içerdiği iki boyutlu bir piksel dizisidir.

### Görüntü Çözünürlüğü
- **Uzaysal Çözünürlük**: Birim alandaki piksel sayısı
- **Yoğunluk Çözünürlüğü**: Olası yoğunluk seviyelerinin sayısı (bit derinliği)
- **Yaygın Çözünürlükler**: 640×480, 1920×1080, 3840×2160 (4K)

### Renk Modelleri
1. **RGB (Kırmızı, Yeşil, Mavi)**
   - Işığın ana renkleri
   - Her kanal: 0-255 yoğunluk değerleri
   - 24-bit renk derinliği (kanal başına 8 bit)

2. **Gri Tonlama**
   - Tek kanal: 0-255 yoğunluk değerleri
   - 8-bit derinlik
   - Parlaklık bilgisini temsil eder

## Temel Görüntü İşlemleri

### Yoğunluk Dönüşümleri

#### Linear Dönüşüm
- **Fonksiyon**: s = αr + β
- **Parametreler**:
  - α (alfa): Kontrast kontrolü
  - β (beta): Parlaklık kontrolü
- **Uygulamalar**: Kontrast artırma, parlaklık ayarlama

#### Logaritmik Dönüşüm
- **Fonksiyon**: s = c log(1 + r)
- **Kullanım Alanları**: Dinamik aralık sıkıştırma
- **Uygulamalar**: Spektrum gösterimleri, tıbbi görüntüleme

#### Güç Yasası (Gama) Dönüşümü
- **Fonksiyon**: s = c r^γ
- **Uygulamalar**:
  - CRT ekran düzeltmesi
  - Görüntü iyileştirme
  - Özellik çıkarma

### Histogram İşleme

#### Histogram Eşitleme
- Görüntü kontrastını artırır
- Yoğunluk seviyelerini yayar
- Histograma dayalı otomatik ayarlama

#### Histogram Eşleme
- Görüntüyü hedef histograma uyacak şekilde değiştirir
- Görüntü görünümünü standartlaştırmada yararlı
- Tıbbi görüntülemede yaygın

## Görüntü İyileştirme Teknikleri

### Uzaysal Domain Yöntemler
1. **Komşuluk İşlemleri**
   - Piksel değeri çevresindeki piksellere dayanır
   - Çekirdek/maske tabanlı işlemler
   - Yerel iyileştirme

2. **Nokta İşlemleri**
   - Piksel-piksel dönüşümler
   - Komşu piksellerden bağımsız
   - Genel iyileştirme

### Frekans Domain Yöntemler
1. **Fourier Dönüşümü**
   - Görüntüyü frekans bileşenlerine ayırır
   - Frekans tabanlı filtrelemeyi mümkün kılar
   - Genel görüntü analizi

2. **Filtreleme**
   - Alçak geçiren: Yumuşatma
   - Yüksek geçiren: Kenar iyileştirme
   - Bant geçiren: Seçici frekans koruma

## Matematiksel Temel

### Temel Kavramlar
1. **Konvolüsyon**
   - Görüntü işlemede temel işlem
   - Filtreleme işlemlerinin temeli
   - Matematiksel formül: f(x,y) * h(x,y)

2. **Korelasyon**
   - Konvolüsyona benzer
   - Şablon eşleme
   - Desen tanıma

### İstatistiksel Ölçüler
1. **Ortalama**
   - Genel parlaklık
   - Merkezi eğilim

2. **Standart Sapma**
   - Kontrast ölçüsü
   - Yoğunluk yayılımı

3. **Histogram**
   - Yoğunluk dağılımı
   - Görüntü istatistikleri

## Uygulamalar

### Tıbbi Görüntüleme
- X-ray iyileştirme
- MRI işleme
- BT tarama analizi

### Endüstriyel Denetim
- Kalite kontrol
- Hata tespiti
- Ölçüm

### Uzaktan Algılama
- Uydu görüntü işleme
- Çevresel izleme
- Coğrafi bilgi sistemleri

## En İyi Uygulamalar

1. **Ön İşleme**
   - Gürültü azaltma
   - Normalleştirme
   - Format dönüştürme

2. **Parametre Seçimi**
   - Bağlama bağımlı
   - Tekrarlı iyileştirme
   - Kalite metrikleri

3. **Kalite Değerlendirme**
   - Objektif ölçüler
   - Subjektif değerlendirme
   - Uygulamaya özel kriterler 