"""
Demo page for Image Processing Application
"""

import streamlit as st
import os
from PIL import Image
import sys

# Add parent directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def main():
    st.set_page_config(
        page_title="Demo - Image Processing",
        page_icon="⚙️",
        layout="wide"
    )
    
    st.title("Demo - Digital Image Processing Application")
    st.markdown("---")
    
    # Introduction
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ## Streamlit Versiyona Hoş Geldiniz!
        
        Bu demo sayfası, Image Processing uygulamasının Streamlit versiyonunun temel özelliklerini gösterir.
        
        ### Ana Özellikler:
        
        - **Çok Dilli Destek**: Türkçe ve İngilizce
        - **Dark/Light Mode**: Modern tema desteği
        - **Gerçek Zamanlı Önizleme**: Anlık görüntü işleme
        - **10 Farklı Kategori**: Kapsamlı filtre seçenekleri
        - **Responsive Tasarım**: Her cihazda mükemmel görünüm
        """)
    
    with col2:
        st.info("""
        **İpucu**
        
        Sol kenar çubuğından bir görüntü yükleyerek 
        uygulamayı test edebilirsiniz!
        """)
    
    # Feature showcase
    st.markdown("## Özellik Vitrini")
    
    tabs = st.tabs(["Filtreler", "Dil Desteği", "Tema", "İstatistikler"])
    
    with tabs[0]:
        st.markdown("""
        ### Mevcut Filtre Kategorileri
        
        1. **Temel Kavramlar** - Gaussian blur, edge detection, thresholding
        2. **Yoğunluk Dönüşümleri** - Linear, logarithmic, power-law transforms
        3. **Frekans Alanı** - Low-pass, high-pass, band-pass filters
        4. **Görüntü Restorasyon** - Noise addition/reduction
        5. **Renk İşleme** - Color balance, smoothing, space conversion
        6. **Wavelet Dönüşümü** - Haar, Daubechies, Biorthogonal
        7. **Görüntü Sıkıştırma** - JPEG, Wavelet, RLE, Huffman
        8. **Morfolojik İşlemler** - Erosion, dilation, opening, closing
        9. **Görüntü Bölütleme** - Watershed, GrabCut, K-means
        10. **Özellik Çıkarımı** - Basic, texture, color histogram features
        """)
    
    with tabs[1]:
        st.markdown("""
        ### Çok Dilli Destek
        
        Uygulama tam olarak iki dilde çalışır:
        
        - **Türkçe**: Tüm arayüz elemanları ve açıklamalar
        - **İngilizce**: Complete interface and descriptions
        
        Dil değiştirmek için sağ üst köşedeki "Language" seçeneğini kullanın.
        """)
    
    with tabs[2]:
        st.markdown("""
        ### Tema Desteği
        
        **Light Mode (Varsayılan)**
        - Klasik beyaz arka plan
        - Koyu metin
        - Minimal tasarım
        
        **Dark Mode**
        - Modern koyu tema
        - Göz dostu renkler
        - Gece kullanımı için ideal
        
        Temayı değiştirmek için "Dark Mode" checkbox'ını kullanın.
        """)
    
    with tabs[3]:
        st.markdown("""
        ### Teknik Özellikler
        
        - **Framework**: Streamlit 1.28+
        - **Image Processing**: OpenCV, PIL
        - **Mathematical Operations**: NumPy, PyWavelets
        - **UI Components**: Native Streamlit widgets
        - **File Support**: PNG, JPG, JPEG, BMP, TIFF
        - **Max File Size**: 200MB
        - **Response Time**: < 1 second for most operations
        """)
    
    # Comparison
    st.markdown("---")
    st.markdown("## Tkinter vs Streamlit Karşılaştırması")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Orijinal Tkinter Versiyonu
        - Desktop uygulaması
        - Hızlı başlatma
        - Platform bağımlı
        - Paylaşım zorluğu
        - Eski arayüz
        """)
    
    with col2:
        st.markdown("""
        ### Yeni Streamlit Versiyonu
        - Web tabanlı
        - Modern arayüz
        - Responsive tasarım
        - Kolay paylaşım
        - Gerçek zamanlı güncellemeler
        """)
    
    # Call to action
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("Ana Uygulamayı Başlat", use_container_width=True):
            st.switch_page("app.py")

if __name__ == "__main__":
    main() 