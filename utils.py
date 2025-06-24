"""
Utility functions for Streamlit application
"""

import streamlit as st
import os
import markdown
import numpy as np
from PIL import Image
import io
from languages import get_text

def apply_dark_mode():
    """Apply dark mode styling to the Streamlit app"""
    dark_theme = """
    <style>
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    
    .stSelectbox > div > div {
        background-color: #262730;
        color: #FAFAFA;
    }
    
    .stSlider > div > div > div {
        background-color: #262730;
    }
    
    .stButton > button {
        background-color: #FF4B4B;
        color: white;
        border: none;
        border-radius: 4px;
        font-weight: 500;
    }
    
    .stButton > button:hover {
        background-color: #FF6B6B;
        color: white;
    }
    
    .stFileUploader > div {
        background-color: #262730;
        border: 2px dashed #4F4F4F;
        border-radius: 10px;
    }
    
    .stInfo {
        background-color: #1E3A5F;
        color: #FAFAFA;
    }
    
    .stSuccess {
        background-color: #1E5F3A;
        color: #FAFAFA;
    }
    
    .stWarning {
        background-color: #5F4E1E;
        color: #FAFAFA;
    }
    
    .stError {
        background-color: #5F1E1E;
        color: #FAFAFA;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #262730;
    }
    
    /* Header styling */
    h1, h2, h3, h4, h5, h6 {
        color: #FAFAFA !important;
    }
    
    /* Text styling */
    p, div, span {
        color: #FAFAFA;
    }
    
    /* Metric styling */
    .metric-container {
        background-color: #262730;
        padding: 10px;
        border-radius: 5px;
        margin: 5px 0;
    }
    
    /* Code block styling */
    .stCode {
        background-color: #1E1E1E;
        color: #F8F8F2;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background-color: #262730;
        color: #FAFAFA;
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #262730;
    }
    
    .stTabs [data-baseweb="tab"] {
        color: #FAFAFA;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #FF4B4B;
        color: white;
    }
    </style>
    """
    st.markdown(dark_theme, unsafe_allow_html=True)

def load_markdown_content(file_path):
    """Load and convert markdown content to HTML"""
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                html_content = markdown.markdown(content)
                return html_content
        return "Content not found."
    except Exception as e:
        return f"Error loading content: {str(e)}"

def format_file_size(size_bytes):
    """Dosya boyutunu formatla"""
    if size_bytes == 0:
        return "0B"
    
    size_names = ["B", "KB", "MB", "GB"]
    import math
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_names[i]}"

def create_download_link(data, filename, text="Download"):
    """Create a download link for processed images"""
    import base64
    b64 = base64.b64encode(data).decode()
    href = f'<a href="data:file/octet-stream;base64,{b64}" download="{filename}" style="text-decoration: none; background-color: #FF4B4B; color: white; padding: 8px 16px; border-radius: 4px; font-weight: 500;">{text}</a>'
    return href

def get_filter_info(filter_name, language='en'):
    """Get filter information from markdown files"""
    info_dir = os.path.join(os.path.dirname(__file__), 'info')
    
    # Map filter names to markdown files
    filter_files = {
        'gaussian_blur': 'gaussian_blur.md',
        'edge_detection': 'edge_detection.md',
        'threshold': 'threshold.md',
        'transforms': 'transform.md',
        'frequency': 'frequency.md',
        'restoration': 'restore.md',
        'color': 'color.md',
        'wavelets': 'wavelet.md',
        'compression': 'compression.md',
        'morphological': 'morphological.md',
        'segmentation': 'segmentation.md',
        'features': 'features.md',
        'fundamentals': 'fundamentals.md'
    }
    
    if filter_name in filter_files:
        file_path = os.path.join(info_dir, filter_files[filter_name])
        return load_markdown_content(file_path)
    
    return "Information not available for this filter."

def display_image_stats(image, title="Görüntü Bilgileri"):
    """Görüntü istatistiklerini göster"""
    st.subheader(title)
    
    img_array = np.array(image)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Genişlik", f"{image.width} px")
    
    with col2:
        st.metric("Yükseklik", f"{image.height} px")
    
    with col3:
        st.metric("Kanal Sayısı", len(img_array.shape) if len(img_array.shape) == 2 else img_array.shape[2])
    
    with col4:
        total_pixels = image.width * image.height
        st.metric("Toplam Piksel", f"{total_pixels:,}")
    
    # Histogram göster
    if st.checkbox("Histogram Göster"):
        import matplotlib.pyplot as plt
        
        fig, ax = plt.subplots(figsize=(10, 4))
        
        if len(img_array.shape) == 3:
            # Renkli görüntü
            colors = ['red', 'green', 'blue']
            for i, color in enumerate(colors):
                hist = np.histogram(img_array[:, :, i].flatten(), bins=50)[0]
                ax.plot(hist, color=color, alpha=0.7, label=f'{color.title()} Kanal')
            ax.legend()
        else:
            # Gri tonlamalı görüntü
            hist = np.histogram(img_array.flatten(), bins=50)[0]
            ax.plot(hist, color='gray', label='Gri Ton')
            ax.legend()
        
        ax.set_title("Piksel Değer Dağılımı")
        ax.set_xlabel("Piksel Değeri")
        ax.set_ylabel("Frekans")
        st.pyplot(fig)

def create_info_expander(filter_name, translations):
    """Create an expandable info section for filters"""
    with st.expander(f"{translations['show_info']}"):
        info_content = get_filter_info(filter_name)
        st.markdown(info_content, unsafe_allow_html=True)

def validate_image_format(uploaded_file):
    """Validate uploaded image format"""
    allowed_formats = ['png', 'jpg', 'jpeg', 'bmp', 'tiff', 'gif']
    if uploaded_file is not None:
        file_extension = uploaded_file.name.split('.')[-1].lower()
        return file_extension in allowed_formats
    return False

def get_processing_history():
    """Get processing history from session state"""
    if 'processing_history' not in st.session_state:
        st.session_state.processing_history = []
    return st.session_state.processing_history

def add_to_history(operation, parameters):
    """Add operation to processing history"""
    import datetime
    history = get_processing_history()
    history.append({
        'operation': operation,
        'parameters': parameters,
        'timestamp': str(datetime.datetime.now())
    })
    st.session_state.processing_history = history[-10:]  # Keep last 10 operations

def display_processing_history(translations):
    """Display processing history"""
    history = get_processing_history()
    if history:
        st.subheader("Processing History")
        for i, entry in enumerate(reversed(history)):
            with st.expander(f"{i+1}. {entry['operation']}"):
                st.write(f"**Parameters:** {entry['parameters']}")
                st.write(f"**Time:** {entry['timestamp']}")

def create_comparison_view(original, processed, translations):
    """Create a side-by-side comparison view"""
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(translations['original_image'])
        st.image(original, use_column_width=True)
        if st.button("Original Stats", key="orig_stats"):
            display_image_stats(original)
    
    with col2:
        st.subheader(translations['processed_image'])
        st.image(processed, use_column_width=True)
        if st.button("Processed Stats", key="proc_stats"):
            display_image_stats(processed)

def display_filter_theory(category, filter_name, language='tr'):
    """Display detailed theory and explanation for filters"""
    
    # Theory content in both Turkish and English
    theory_content = {
        'gaussian_blur': {
            'tr': {
                'title': '🌫️ Gaussian Blur (Gaussian Bulanıklaştırma)',
                'theory': '''
                **Gaussian Blur**, görüntüleri yumuşatmak ve gürültüyü azaltmak için kullanılan temel bir filtredir.
                
                **Matematiksel Temel:**
                - Gaussian fonksiyonu kullanarak konvolüsyon işlemi yapılır
                - 2D Gaussian kernel ile görüntü çarpılır
                - Formula: G(x,y) = (1/2πσ²) * e^(-(x²+y²)/2σ²)
                
                **Parametreler:**
                - **Kernel Boyutu**: Filtrenin etki alanı (3x3, 5x5, 7x7, vb.)
                - **Sigma (σ)**: Gaussian dağılımının standart sapması
                
                **Kullanım Alanları:**
                - Gürültü azaltma
                - Görüntü yumuşatma
                - Ön işleme adımı
                - Kenar tespiti öncesi hazırlık
                ''',
                'applications': [
                    'Fotoğraf düzenleme',
                    'Medikal görüntüleme',
                    'Bilgisayarlı görü',
                    'Video işleme'
                ]
            },
            'en': {
                'title': '🌫️ Gaussian Blur',
                'theory': '''
                **Gaussian Blur** is a fundamental filter used to smooth images and reduce noise.
                
                **Mathematical Foundation:**
                - Convolution operation using Gaussian function
                - Image is multiplied with 2D Gaussian kernel
                - Formula: G(x,y) = (1/2πσ²) * e^(-(x²+y²)/2σ²)
                
                **Parameters:**
                - **Kernel Size**: Filter's area of effect (3x3, 5x5, 7x7, etc.)
                - **Sigma (σ)**: Standard deviation of Gaussian distribution
                
                **Use Cases:**
                - Noise reduction
                - Image smoothing
                - Preprocessing step
                - Preparation before edge detection
                ''',
                'applications': [
                    'Photo editing',
                    'Medical imaging',
                    'Computer vision',
                    'Video processing'
                ]
            }
        },
        'edge_detection': {
            'tr': {
                'title': '🔍 Kenar Tespiti (Edge Detection)',
                'theory': '''
                **Kenar Tespiti**, görüntülerdeki yoğunluk değişimlerini tespit etmek için kullanılır.
                
                **Sobel Operatörü:**
                - 3x3 konvolüsyon kernelleri kullanır
                - X ve Y yönlerinde gradyanları hesaplar
                - Hızlı ve etkili kenar tespiti sağlar
                
                **Canny Kenar Algılayıcı:**
                - Çok aşamalı algoritma
                - Gaussian yumuşatma → Gradyan hesaplama → Non-maximum suppression → Hysteresis
                - Daha hassas ve temiz kenarlar
                
                **Kullanım Alanları:**
                - Nesne tanıma
                - Şekil analizi
                - Görüntü segmentasyonu
                ''',
                'applications': [
                    'Otonom araçlar',
                    'Endüstriyel kalite kontrol',
                    'Tıbbi tanı',
                    'Robotik görü'
                ]
            },
            'en': {
                'title': '🔍 Edge Detection',
                'theory': '''
                **Edge Detection** is used to detect intensity changes in images.
                
                **Sobel Operator:**
                - Uses 3x3 convolution kernels
                - Calculates gradients in X and Y directions
                - Provides fast and effective edge detection
                
                **Canny Edge Detector:**
                - Multi-stage algorithm
                - Gaussian smoothing → Gradient calculation → Non-maximum suppression → Hysteresis
                - More precise and clean edges
                
                **Use Cases:**
                - Object recognition
                - Shape analysis
                - Image segmentation
                ''',
                'applications': [
                    'Autonomous vehicles',
                    'Industrial quality control',
                    'Medical diagnosis',
                    'Robotic vision'
                ]
            }
        },
        'threshold': {
            'tr': {
                'title': '⚫ Eşikleme (Thresholding)',
                'theory': '''
                **Eşikleme**, gri tonlamalı görüntüleri ikili (binary) görüntülere dönüştürür.
                
                **Binary Threshold:**
                - Sabit bir eşik değeri kullanır
                - Piksel değeri > eşik → 255 (beyaz)
                - Piksel değeri ≤ eşik → 0 (siyah)
                
                **Otsu's Method:**
                - Otomatik eşik değeri hesaplama
                - Sınıf içi varyansı minimize eder
                - Histogram tabanlı yaklaşım
                
                **Adaptive Threshold:**
                - Yerel komşuluk tabanlı eşikleme
                - Değişken aydınlatma koşulları için ideal
                ''',
                'applications': [
                    'Belge tarama',
                    'Nesne segmentasyonu',
                    'Optik karakter tanıma',
                    'Barkod okuma'
                ]
            }
        }
    }
    
    content = theory_content.get(filter_name, {}).get(language, {})
    if content:
        st.markdown(f"### {content['title']}")
        st.markdown(content['theory'])
        
        st.markdown("**🎯 Uygulama Alanları:**" if language == 'tr' else "**🎯 Applications:**")
        for app in content['applications']:
            st.markdown(f"- {app}")
    else:
        st.info("Bu filtre için detaylı bilgi henüz eklenmemiş." if language == 'tr' else "Detailed information not yet available for this filter.")

def show_before_after_comparison(original, processed, titles=None):
    """Show before/after comparison with enhanced UI"""
    if titles is None:
        titles = ["Orijinal", "İşlenmiş"]
    
    # Create tabs for different view modes
    tab1, tab2, tab3 = st.tabs(["🖼️ Yan Yana", "🔄 Geçiş", "📊 İstatistikler"])
    
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"**{titles[0]}**")
            st.image(original, use_column_width=True)
        with col2:
            st.markdown(f"**{titles[1]}**")
            st.image(processed, use_column_width=True)
    
    with tab2:
        # Slider-based comparison
        comparison_ratio = st.slider("Karşılaştırma", 0.0, 1.0, 0.5, step=0.01)
        if comparison_ratio < 0.5:
            st.image(original, caption=f"{titles[0]} ({(1-comparison_ratio)*100:.0f}%)", use_column_width=True)
        else:
            st.image(processed, caption=f"{titles[1]} ({comparison_ratio*100:.0f}%)", use_column_width=True)
    
    with tab3:
        display_comparison_stats(original, processed)

def display_comparison_stats(original, processed):
    """Display enhanced comparison statistics"""
    import numpy as np
    
    orig_array = np.array(original)
    proc_array = np.array(processed)
    
    st.markdown("#### 📈 Görüntü İstatistikleri Karşılaştırması")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        orig_mean = np.mean(orig_array)
        proc_mean = np.mean(proc_array)
        delta_mean = proc_mean - orig_mean
        st.metric("Ortalama Değer", f"{proc_mean:.1f}", f"{delta_mean:+.1f}")
    
    with col2:
        orig_std = np.std(orig_array)
        proc_std = np.std(proc_array)
        delta_std = proc_std - orig_std
        st.metric("Standart Sapma", f"{proc_std:.1f}", f"{delta_std:+.1f}")
    
    with col3:
        mse = np.mean((orig_array - proc_array) ** 2)
        st.metric("MSE", f"{mse:.2f}")
    
    with col4:
        # PSNR calculation
        if mse > 0:
            psnr = 20 * np.log10(255.0 / np.sqrt(mse))
            st.metric("PSNR (dB)", f"{psnr:.1f}")
        else:
            st.metric("PSNR (dB)", "∞")
    
    # Histogram comparison
    if st.checkbox("📊 Histogram Karşılaştırması"):
        import matplotlib.pyplot as plt
        import plotly.graph_objects as go
        from plotly.subplots import make_subplots
        
        fig = make_subplots(rows=1, cols=2, subplot_titles=('Orijinal', 'İşlenmiş'))
        
        # Original histogram
        hist_orig, bins = np.histogram(orig_array.flatten(), bins=50)
        fig.add_trace(go.Scatter(x=bins[:-1], y=hist_orig, name='Orijinal', line=dict(color='blue')), row=1, col=1)
        
        # Processed histogram  
        hist_proc, bins = np.histogram(proc_array.flatten(), bins=50)
        fig.add_trace(go.Scatter(x=bins[:-1], y=hist_proc, name='İşlenmiş', line=dict(color='red')), row=1, col=2)
        
        fig.update_layout(height=400, showlegend=True, title_text="Histogram Karşılaştırması")
        st.plotly_chart(fig, use_container_width=True)

def load_image(uploaded_file):
    """Güvenli görüntü yükleme fonksiyonu"""
    try:
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            # RGBA görüntüleri RGB'ye çevir
            if image.mode == 'RGBA':
                image = image.convert('RGB')
            return image
        return None
    except Exception as e:
        st.error(f"Görüntü yüklenirken hata oluştu: {str(e)}")
        return None

def compare_images_detailed(original, processed):
    """Detaylı görüntü karşılaştırması"""
    st.subheader("🔍 Detaylı Karşılaştırma")
    
    orig_array = np.array(original)
    proc_array = np.array(processed)
    
    # Boyut uyumluluğunu kontrol et
    if orig_array.shape != proc_array.shape:
        st.warning("Görüntüler farklı boyutlarda! Karşılaştırma sınırlı olacak.")
        return
    
    # MSE hesaplama
    mse = np.mean((orig_array.astype(float) - proc_array.astype(float)) ** 2)
    
    # PSNR hesaplama
    if mse > 0:
        psnr = 20 * np.log10(255.0 / np.sqrt(mse))
    else:
        psnr = float('inf')
    
    # SSIM hesaplama (basit versiyon)
    def simple_ssim(img1, img2):
        mu1 = np.mean(img1)
        mu2 = np.mean(img2)
        sigma1 = np.var(img1)
        sigma2 = np.var(img2)
        sigma12 = np.mean((img1 - mu1) * (img2 - mu2))
        
        c1 = 0.01 ** 2
        c2 = 0.03 ** 2
        
        ssim = ((2 * mu1 * mu2 + c1) * (2 * sigma12 + c2)) / ((mu1**2 + mu2**2 + c1) * (sigma1 + sigma2 + c2))
        return ssim
    
    if len(orig_array.shape) == 2:
        ssim = simple_ssim(orig_array, proc_array)
    else:
        ssim = np.mean([simple_ssim(orig_array[:,:,i], proc_array[:,:,i]) for i in range(orig_array.shape[2])])
    
    # Metrikleri göster
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("MSE", f"{mse:.2f}", help="Ortalama Kare Hata (düşük daha iyi)")
    
    with col2:
        if psnr == float('inf'):
            st.metric("PSNR", "∞ dB", help="Peak Signal-to-Noise Ratio (yüksek daha iyi)")
        else:
            st.metric("PSNR", f"{psnr:.2f} dB", help="Peak Signal-to-Noise Ratio (yüksek daha iyi)")
    
    with col3:
        st.metric("SSIM", f"{ssim:.3f}", help="Structural Similarity Index (1'e yakın daha iyi)")

def create_download_button(image, filename="processed_image.png"):
    """İndirme butonu oluştur"""
    buffer = io.BytesIO()
    image.save(buffer, format='PNG')
    
    st.download_button(
        label="📥 İşlenmiş Görüntüyü İndir",
        data=buffer.getvalue(),
        file_name=filename,
        mime="image/png",
        help="İşlenmiş görüntüyü PNG formatında indir"
    )

def show_processing_info(filter_name, parameters=None):
    """İşleme bilgilerini göster"""
    with st.expander("ℹ️ İşlem Bilgileri", expanded=False):
        st.write(f"**Uygulanan Filtre:** {filter_name}")
        
        if parameters:
            st.write("**Parametreler:**")
            for key, value in parameters.items():
                st.write(f"- {key}: {value}")
        
        st.write("**Kullanım İpuçları:**")
        
        filter_tips = {
            "gaussian_blur": [
                "Küçük kernel boyutu: Az bulanıklık",
                "Büyük kernel boyutu: Fazla bulanıklık",
                "Sigma değeri bulanıklık yoğunluğunu kontrol eder"
            ],
            "edge_detection": [
                "Sobel: Hızlı ve basit kenar tespiti",
                "Canny: Daha hassas ama yavaş",
                "Düşük eşik: Daha fazla kenar",
                "Yüksek eşik: Daha az ama net kenar"
            ],
            "threshold": [
                "Binary: Sabit eşik değeri",
                "Otsu: Otomatik eşik hesaplama",
                "Adaptive: Yerel eşikleme"
            ]
        }
        
        if filter_name in filter_tips:
            for tip in filter_tips[filter_name]:
                st.write(f"• {tip}")

def validate_image(image):
    """Görüntü doğrulaması"""
    if image is None:
        return False, "Görüntü yüklenemedi"
    
    # Minimum boyut kontrolü
    if image.width < 10 or image.height < 10:
        return False, "Görüntü çok küçük (minimum 10x10 piksel)"
    
    # Maksimum boyut kontrolü
    max_pixels = 4000 * 4000  # 16 megapiksel
    if image.width * image.height > max_pixels:
        return False, f"Görüntü çok büyük (maksimum {max_pixels:,} piksel)"
    
    return True, "Görüntü geçerli"

def initialize_session_state():
    """Initialize all session state variables"""
    if 'language' not in st.session_state:
        st.session_state.language = 'tr'
    if 'uploaded_file' not in st.session_state:
        st.session_state.uploaded_file = None
    if 'selected_category' not in st.session_state:
        st.session_state.selected_category = None
    if 'selected_filter' not in st.session_state:
        st.session_state.selected_filter = None
    if 'processed_image' not in st.session_state:
        st.session_state.processed_image = None
    if 'filter_params' not in st.session_state:
        st.session_state.filter_params = {}

def change_language(new_language):
    """Change language without causing a full app rerun"""
    if st.session_state.language != new_language:
        st.session_state.language = new_language
        # Store current state to preserve it
        st.session_state.previous_state = {
            'uploaded_file': st.session_state.uploaded_file,
            'selected_category': st.session_state.selected_category,
            'selected_filter': st.session_state.selected_filter,
            'processed_image': st.session_state.processed_image,
            'filter_params': st.session_state.filter_params.copy() if st.session_state.filter_params else {}
        }

def restore_state():
    """Restore previous state after language change"""
    if hasattr(st.session_state, 'previous_state'):
        for key, value in st.session_state.previous_state.items():
            if key not in st.session_state or st.session_state[key] is None:
                st.session_state[key] = value
        # Clear the previous state
        del st.session_state.previous_state

def get_localized_filter_categories(language):
    """Get filter categories with proper localization"""
    return {
        get_text("basic_filters", language): {
            get_text("gaussian_blur", language): "gaussian_blur",
            get_text("edge_detection", language): "edge_detection",
            get_text("threshold", language): "threshold"
        },
        get_text("advanced_filters", language): {
            get_text("intensity_transform", language): "intensity_transform",
            get_text("frequency_filter", language): "frequency_filter",
            get_text("noise_reduction", language): "noise_reduction"
        },
        get_text("morphological_operations", language): {
            get_text("morphological_op", language): "morphological",
        },
        get_text("segmentation_filters", language): {
            get_text("watershed", language): "watershed",
            get_text("kmeans", language): "kmeans"
        }
    }

def get_filter_name_by_key(filter_key, language):
    """Get localized filter name by its key"""
    categories = get_localized_filter_categories(language)
    for category_name, filters in categories.items():
        for filter_name, key in filters.items():
            if key == filter_key:
                return filter_name
    return filter_key

def get_category_name_by_filter(filter_key, language):
    """Get localized category name by filter key"""
    categories = get_localized_filter_categories(language)
    for category_name, filters in categories.items():
        for filter_name, key in filters.items():
            if key == filter_key:
                return category_name
    return None 