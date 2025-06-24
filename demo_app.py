"""
Digital Image Processing Lab - Demo Application
Modern Streamlit-based interface for image processing filters
"""

import streamlit as st
import sys
import os

# Add the parent directory to the Python path to import filters
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.dirname(__file__))

# Import main app
from app import main

# Page configuration
st.set_page_config(
    page_title="Digital Image Processing Lab",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://github.com/your-repo/help',
        'Report a bug': 'https://github.com/your-repo/issues',
        'About': """
        # Digital Image Processing Lab 🔬
        
        Modern, interactive image processing application built with:
        - **Streamlit** for the web interface
        - **OpenCV** for image processing
        - **PIL/Pillow** for image handling
        - **NumPy** for numerical operations
        
        ### Features:
        - 🌫️ **Fundamentals**: Gaussian blur, edge detection, thresholding
        - 🎭 **Transforms**: Linear, logarithmic, power-law, histogram equalization
        - 🌊 **Frequency**: Low-pass, high-pass, band-pass filters
        - 🔧 **Restoration**: Noise addition/reduction, denoising
        - 🎨 **Color**: Pseudocolor, color balance, color space conversion
        - 📡 **Wavelets**: Wavelet transforms and reconstruction
        - 📦 **Compression**: JPEG, wavelet, RLE, Huffman coding
        - 🔷 **Morphological**: Erosion, dilation, opening, closing
        - ✂️ **Segmentation**: Watershed, GrabCut, K-means
        - 🔬 **Features**: Statistical analysis, texture features
        
        ### Languages:
        - 🇹🇷 **Türkçe** (Turkish)
        - 🇺🇸 **English**
        
        Created with ❤️ for learning digital image processing.
        """
    }
)

if __name__ == "__main__":
    # Add some initial instructions
    if 'first_visit' not in st.session_state:
        st.session_state.first_visit = True
        
        # Welcome message
        st.balloons()
        st.markdown("""
        ## 🎉 Digital Image Processing Lab'a Hoş Geldiniz!
        
        Bu uygulama ile dijital görüntü işleme tekniklerini interaktif olarak öğrenebilir ve deneyebilirsiniz.
        
        ### 🚀 Nasıl Başlarım?
        1. **Görüntü Yükleyin**: Kendi görüntünüzü yükleyin veya örnek görüntülerden birini seçin
        2. **Filtre Seçin**: Ana sayfadaki kartlardan ilginizi çeken filtreyi seçin
        3. **Parametrelerle Oynayın**: Gerçek zamanlı önizleme ile sonuçları görün
        4. **Öğrenin**: Her filtre için detaylı açıklamalar ve teori bilgisi
        5. **Karşılaştırın**: Orijinal ve işlenmiş görüntüleri yan yana görün
        
        ---
        """)
        
        # Clear first visit flag after showing welcome
        if st.button("▶️ Uygulamayı Başlat", use_container_width=True):
            st.session_state.first_visit = False
            st.rerun()
    else:
        # Run main application
        main() 