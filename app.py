import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io
import os
import sys

# Add the parent directory to the Python path to import filters
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from filters import (
    apply_gaussian_blur, apply_edge_detection, apply_threshold,
    apply_intensity_transform, apply_frequency_filter, 
    apply_noise_reduction, apply_morphological_operation,
    apply_watershed_segmentation, apply_kmeans_segmentation
)

# Import language support and utilities
from languages import get_text
from utils import initialize_session_state, change_language, restore_state, get_localized_filter_categories

# Configure Streamlit page
st.set_page_config(
    page_title="Görüntü İşleme",
    page_icon="📷",
    layout="wide"
)

# Initialize session state
initialize_session_state()

# Restore state if needed (after language change)
restore_state()

# Simple and clean CSS
st.markdown("""
<style>
    .main-title {
        text-align: center;
        color: #2c3e50;
        font-size: 2.5rem;
        margin-bottom: 2rem;
        padding: 1rem;
        border-bottom: 3px solid #3498db;
    }
    
    .filter-section {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
        border-left: 4px solid #3498db;
    }
    
    .info-section {
        background-color: #e8f4fd;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        border-left: 4px solid #17a2b8;
    }
    
    .markdown-content {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
        border-left: 4px solid #28a745;
    }
    
    .image-container {
        padding: 1rem;
        border: 1px solid #ddd;
        border-radius: 8px;
        background-color: white;
        margin: 1rem 0;
    }
    
    .metric-box {
        background-color: #ecf0f1;
        padding: 1rem;
        border-radius: 5px;
        text-align: center;
        margin: 0.5rem;
    }
    
    .tip-box {
        background-color: #fff3cd;
        border: 1px solid #ffeaa7;
        border-radius: 5px;
        padding: 0.75rem;
        margin: 0.5rem 0;
    }
    
    .language-selector {
        position: fixed;
        top: 10px;
        right: 10px;
        z-index: 999;
        background: white;
        padding: 0.5rem;
        border-radius: 5px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

def load_markdown_content(filename, language='tr'):
    """Markdown dosyasını yükle"""
    try:
        # Dil uzantısı ekle
        if language == 'tr':
            filename_with_lang = filename.replace('.md', '_tr.md')
        else:
            filename_with_lang = filename
        
        filepath = os.path.join('info', filename_with_lang)
        
        # Türkçe dosya yoksa İngilizce'yi dene
        if not os.path.exists(filepath) and language == 'tr':
            filepath = os.path.join('info', filename)
        
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        else:
            return f"**{get_text('file_not_found', language)}:** {filename}"
    except Exception as e:
        return f"**{get_text('file_read_error', language)}:** {str(e)}"

def show_language_selector():
    """Dil seçici göster - state'i koruyarak"""
    st.markdown('<div class="language-selector">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button("🇹🇷 Türkçe", use_container_width=True, 
                    type="primary" if st.session_state.language == 'tr' else "secondary"):
            change_language('tr')
            st.rerun()
    
    with col2:
        if st.button("🇺🇸 English", use_container_width=True,
                    type="primary" if st.session_state.language == 'en' else "secondary"):
            change_language('en')
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

def load_image(uploaded_file):
    """Görüntü yükleme fonksiyonu"""
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        # RGBA görüntüleri RGB'ye çevir
        if image.mode == 'RGBA':
            image = image.convert('RGB')
        return image
    return None

def show_image_stats(image):
    """Görüntü istatistiklerini göster"""
    if image is None:
        return
    
    # Görüntü bilgileri
    width, height = image.size
    mode = image.mode
    
    # İstatistikler
    img_array = np.array(image)
    
    if len(img_array.shape) == 3:  # Renkli görüntü
        mean_r = np.mean(img_array[:, :, 0])
        mean_g = np.mean(img_array[:, :, 1])
        mean_b = np.mean(img_array[:, :, 2])
        std_r = np.std(img_array[:, :, 0])
        std_g = np.std(img_array[:, :, 1])
        std_b = np.std(img_array[:, :, 2])
        
        st.markdown('<div class="metric-box">', unsafe_allow_html=True)
        st.write(f"**Boyut:** {width} × {height}")
        st.write(f"**Mod:** {mode}")
        st.write(f"**Ortalama RGB:** ({mean_r:.1f}, {mean_g:.1f}, {mean_b:.1f})")
        st.write(f"**Standart Sapma:** ({std_r:.1f}, {std_g:.1f}, {std_b:.1f})")
        st.markdown('</div>', unsafe_allow_html=True)
    else:  # Gri tonlama
        mean_val = np.mean(img_array)
        std_val = np.std(img_array)
        
        st.markdown('<div class="metric-box">', unsafe_allow_html=True)
        st.write(f"**Boyut:** {width} × {height}")
        st.write(f"**Mod:** {mode}")
        st.write(f"**Ortalama:** {mean_val:.1f}")
        st.write(f"**Standart Sapma:** {std_val:.1f}")
        st.markdown('</div>', unsafe_allow_html=True)

def show_filter_info_with_markdown(filter_type, language='tr'):
    """Filtre bilgilerini markdown ile göster"""
    st.markdown('<div class="markdown-content">', unsafe_allow_html=True)
    
    # Filtre tipine göre bilgi dosyası seç
    info_files = {
        'gaussian_blur': 'gaussian_blur.md',
        'edge_detection': 'edge_detection.md',
        'threshold': 'threshold.md',
        'intensity_transform': 'fundamentals.md',
        'frequency_filter': 'frequency.md',
        'noise_reduction': 'restore.md',
        'morphological': 'morphological.md',
        'watershed': 'segmentation.md',
        'kmeans': 'segmentation.md'
    }
    
    filename = info_files.get(filter_type, 'fundamentals.md')
    content = load_markdown_content(filename, language)
    
    st.markdown(f"**{get_text(filter_type, language)}**")
    st.markdown(content)
    st.markdown('</div>', unsafe_allow_html=True)

def compare_images(original, processed):
    """Orijinal ve işlenmiş görüntüleri karşılaştır"""
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.image(original, caption=get_text('original_image', st.session_state.language), use_column_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.image(processed, caption=get_text('processed_image', st.session_state.language), use_column_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

def main():
    # Dil seçici
    show_language_selector()
    
    # Başlık
    st.markdown(f'<h1 class="main-title">{get_text("title", st.session_state.language)}</h1>', unsafe_allow_html=True)
    
    # Görüntü yükleme
    st.sidebar.header(get_text("upload_header", st.session_state.language))
    uploaded_file = st.sidebar.file_uploader(
        get_text("upload_text", st.session_state.language),
        type=['png', 'jpg', 'jpeg', 'bmp', 'tiff'],
        key="file_uploader"
    )
    
    # Store uploaded file in session state
    if uploaded_file is not None:
        st.session_state.uploaded_file = uploaded_file
    
    # Use stored file if available
    current_file = uploaded_file if uploaded_file is not None else st.session_state.uploaded_file
    
    if current_file is None:
        st.info(get_text("upload_info", st.session_state.language))
        
        # Uygulama hakkında bilgi
        about_content = load_markdown_content('fundamentals.md', st.session_state.language)
        
        st.markdown('<div class="info-section">', unsafe_allow_html=True)
        st.markdown(f"**{get_text('about_app', st.session_state.language)}**")
        st.markdown(about_content)
        st.markdown('</div>', unsafe_allow_html=True)
        return
    
    # Görüntüyü yükle
    image = load_image(current_file)
    if image is None:
        st.error(get_text("image_load_error", st.session_state.language))
        return
    
    # Orijinal görüntüyü göster
    st.subheader(get_text("uploaded_image", st.session_state.language))
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.image(image, caption=get_text("original_image", st.session_state.language), use_column_width=True)
    
    with col2:
        show_image_stats(image)
    
    # Filtre seçimi
    st.sidebar.header(get_text("filter_selection", st.session_state.language))
    
    filter_categories = get_localized_filter_categories(st.session_state.language)
    
    selected_category = st.sidebar.selectbox(
        get_text("category_select", st.session_state.language),
        list(filter_categories.keys()),
        key="category_selectbox"
    )
    
    # Store selected category
    st.session_state.selected_category = selected_category
    
    selected_filter_name = st.sidebar.selectbox(
        get_text("filter_select", st.session_state.language), 
        list(filter_categories[selected_category].keys()),
        key="filter_selectbox"
    )
    
    selected_filter = filter_categories[selected_category][selected_filter_name]
    
    # Store selected filter
    st.session_state.selected_filter = selected_filter
    
    # Filtre bilgilerini göster
    show_filter_info_with_markdown(selected_filter, st.session_state.language)
    
    # Filtre parametrelerini ayarla ve uygula
    st.markdown(f'<div class="filter-section">', unsafe_allow_html=True)
    st.subheader(f"🔧 {selected_filter_name} {get_text('filter_settings', st.session_state.language)}")
    
    processed_image = None
    
    if selected_filter == "gaussian_blur":
        col1, col2 = st.columns(2)
        with col1:
            kernel_size = st.slider(get_text("kernel_size", st.session_state.language), 3, 31, 5, step=2)
        with col2:
            sigma = st.slider(get_text("sigma", st.session_state.language), 0.1, 10.0, 1.0, step=0.1)
        
        blur_intensity = get_text("light_blur", st.session_state.language) if kernel_size <= 7 else get_text("medium_blur", st.session_state.language) if kernel_size <= 15 else get_text("strong_blur", st.session_state.language)
        
        st.markdown(f"""
        <div class="tip-box">
            <strong>{get_text('tip', st.session_state.language)}:</strong> {get_text("kernel_size", st.session_state.language)} {kernel_size}, {get_text("sigma", st.session_state.language)} {sigma:.1f} → {blur_intensity} {get_text("gaussian_blur", st.session_state.language).lower()}
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(get_text("apply_filter", st.session_state.language), use_container_width=True):
            processed_image = apply_gaussian_blur(image, kernel_size, sigma)
    
    elif selected_filter == "edge_detection":
        method = st.selectbox(get_text("method", st.session_state.language), [get_text("sobel", st.session_state.language), get_text("canny", st.session_state.language)])
        
        if method == get_text("canny", st.session_state.language):
            col1, col2 = st.columns(2)
            with col1:
                threshold1 = st.slider(get_text("lower_threshold", st.session_state.language), 0, 255, 50)
            with col2:
                threshold2 = st.slider(get_text("upper_threshold", st.session_state.language), 0, 255, 150)
            
            detection_type = get_text("sensitive_detection", st.session_state.language) if threshold1 < 30 else get_text("medium_detection", st.session_state.language) if threshold1 < 80 else get_text("selective_detection", st.session_state.language)
            
            st.markdown(f"""
            <div class="tip-box">
                <strong>{get_text('tip', st.session_state.language)}:</strong> {get_text("lower_threshold", st.session_state.language)} {threshold1}, {get_text("upper_threshold", st.session_state.language)} {threshold2} → {detection_type} {get_text("edge_detection", st.session_state.language).lower()}
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(get_text("apply_filter", st.session_state.language), use_container_width=True):
                processed_image = apply_edge_detection(image, "canny", threshold1, threshold2)
        else:
            st.markdown(f"""
            <div class="tip-box">
                <strong>{get_text('tip', st.session_state.language)}:</strong> {get_text("sobel_tip", st.session_state.language)}
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(get_text("apply_filter", st.session_state.language), use_container_width=True):
                processed_image = apply_edge_detection(image, "sobel")
    
    elif selected_filter == "threshold":
        col1, col2 = st.columns(2)
        with col1:
            method = st.selectbox(get_text("method", st.session_state.language), [get_text("binary", st.session_state.language), get_text("otsu", st.session_state.language), get_text("adaptive", st.session_state.language)])
        with col2:
            threshold_value = st.slider(get_text("threshold_value", st.session_state.language), 0, 255, 127, 
                                      disabled=(method != get_text("binary", st.session_state.language)))
        
        threshold_effect = get_text("fixed_threshold", st.session_state.language) if method == get_text("binary", st.session_state.language) else get_text("auto_threshold", st.session_state.language) if method == get_text("otsu", st.session_state.language) else get_text("local_threshold", st.session_state.language)
        
        st.markdown(f"""
        <div class="tip-box">
            <strong>{get_text('tip', st.session_state.language)}:</strong> {method} {get_text("method", st.session_state.language).lower()} → {threshold_effect}
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(get_text("apply_filter", st.session_state.language), use_container_width=True):
            method_key = "binary" if method == get_text("binary", st.session_state.language) else "otsu" if method == get_text("otsu", st.session_state.language) else "adaptive"
            processed_image = apply_threshold(image, method_key, threshold_value)
    
    elif selected_filter == "intensity_transform":
        transform_type = st.selectbox(get_text("transform_type", st.session_state.language), ["log", "gamma", "linear"])
        
        if transform_type == "gamma":
            gamma = st.slider(get_text("gamma", st.session_state.language), 0.1, 3.0, 1.0, step=0.1)
            
            gamma_effect = get_text("brightens", st.session_state.language) if gamma < 1.0 else get_text("no_change", st.session_state.language) if gamma == 1.0 else get_text("darkens", st.session_state.language)
            
            st.markdown(f"""
            <div class="tip-box">
                <strong>{get_text('tip', st.session_state.language)}:</strong> {get_text("gamma", st.session_state.language)} {gamma:.1f} → {gamma_effect}
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(get_text("apply_filter", st.session_state.language), use_container_width=True):
                processed_image = apply_intensity_transform(image, transform_type, gamma=gamma)
        else:
            effect = get_text("illuminates_dark", st.session_state.language) if transform_type == "log" else get_text("simple_contrast", st.session_state.language)
            st.markdown(f"""
            <div class="tip-box">
                <strong>{get_text('tip', st.session_state.language)}:</strong> {transform_type.title()} {get_text("transform_type", st.session_state.language).lower()} → {effect}
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(get_text("apply_filter", st.session_state.language), use_container_width=True):
                processed_image = apply_intensity_transform(image, transform_type)
    
    elif selected_filter == "frequency_filter":
        col1, col2 = st.columns(2)
        with col1:
            filter_type = st.selectbox(get_text("filter_type", st.session_state.language), ["lowpass", "highpass", "bandpass"])
        with col2:
            cutoff = st.slider(get_text("cutoff", st.session_state.language), 1, 100, 30)
        
        effect = {
            "lowpass": get_text("smoothing_noise", st.session_state.language),
            "highpass": get_text("sharpening_detail", st.session_state.language), 
            "bandpass": get_text("selective_filtering", st.session_state.language)
        }
        
        st.markdown(f"""
        <div class="tip-box">
            <strong>{get_text('tip', st.session_state.language)}:</strong> {filter_type.title()} {get_text("filter_type", st.session_state.language).lower()}, {get_text("cutoff", st.session_state.language)} {cutoff} → {effect[filter_type]}
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(get_text("apply_filter", st.session_state.language), use_container_width=True):
            processed_image = apply_frequency_filter(image, filter_type, cutoff)
    
    elif selected_filter == "noise_reduction":
        method = st.selectbox(get_text("method", st.session_state.language), [get_text("bilateral", st.session_state.language), get_text("median", st.session_state.language), get_text("gaussian", st.session_state.language)])
        
        if method == get_text("bilateral", st.session_state.language):
            col1, col2, col3 = st.columns(3)
            with col1:
                d = st.slider(get_text("neighborhood_diameter", st.session_state.language), 5, 15, 9)
            with col2:
                sigma_color = st.slider(get_text("color_sigma", st.session_state.language), 10, 150, 75)
            with col3:
                sigma_space = st.slider(get_text("space_sigma", st.session_state.language), 10, 150, 75)
            
            st.markdown(f"""
            <div class="tip-box">
                <strong>{get_text('tip', st.session_state.language)}:</strong> {get_text("bilateral_tip", st.session_state.language)}
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(get_text("apply_filter", st.session_state.language), use_container_width=True):
                processed_image = apply_noise_reduction(image, "bilateral", d=d, 
                                                     sigma_color=sigma_color, sigma_space=sigma_space)
        else:
            kernel_size = st.slider(get_text("kernel_size", st.session_state.language), 3, 15, 5, step=2)
            
            effect = get_text("salt_pepper_ideal", st.session_state.language) if method == get_text("median", st.session_state.language) else get_text("general_noise", st.session_state.language)
            st.markdown(f"""
            <div class="tip-box">
                <strong>{get_text('tip', st.session_state.language)}:</strong> {method.title()} {get_text("filter_type", st.session_state.language).lower()} → {effect}
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(get_text("apply_filter", st.session_state.language), use_container_width=True):
                method_key = "median" if method == get_text("median", st.session_state.language) else "gaussian"
                processed_image = apply_noise_reduction(image, method_key, kernel_size=kernel_size)
    
    elif selected_filter == "morphological":
        col1, col2 = st.columns(2)
        with col1:
            operation = st.selectbox(get_text("operation", st.session_state.language), [get_text("opening", st.session_state.language), get_text("closing", st.session_state.language), get_text("erosion", st.session_state.language), get_text("dilation", st.session_state.language)])
        with col2:
            kernel_size = st.slider(get_text("kernel_size", st.session_state.language), 3, 15, 5, step=2)
        
        effects = {
            get_text("opening", st.session_state.language): get_text("noise_cleaning", st.session_state.language),
            get_text("closing", st.session_state.language): get_text("gap_filling", st.session_state.language),
            get_text("erosion", st.session_state.language): get_text("object_shrinking", st.session_state.language),
            get_text("dilation", st.session_state.language): get_text("object_expansion", st.session_state.language)
        }
        
        st.markdown(f"""
        <div class="tip-box">
            <strong>{get_text('tip', st.session_state.language)}:</strong> {operation} {get_text("operation", st.session_state.language).lower()} → {effects[operation]}
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(get_text("apply_filter", st.session_state.language), use_container_width=True):
            operation_key = "opening" if operation == get_text("opening", st.session_state.language) else "closing" if operation == get_text("closing", st.session_state.language) else "erosion" if operation == get_text("erosion", st.session_state.language) else "dilation"
            processed_image = apply_morphological_operation(image, operation_key, kernel_size)
    
    elif selected_filter == "watershed":
        st.markdown(f"""
        <div class="tip-box">
            <strong>{get_text('tip', st.session_state.language)}:</strong> {get_text("watershed_tip", st.session_state.language)}
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(get_text("apply_filter", st.session_state.language), use_container_width=True):
            processed_image = apply_watershed_segmentation(image)
    
    elif selected_filter == "kmeans":
        k = st.slider(get_text("k_clusters", st.session_state.language), 2, 10, 3)
        
        segmentation_type = get_text("simple_segmentation", st.session_state.language) if k <= 3 else get_text("detailed_segmentation", st.session_state.language) if k <= 6 else get_text("very_detailed_segmentation", st.session_state.language)
        
        st.markdown(f"""
        <div class="tip-box">
            <strong>{get_text('tip', st.session_state.language)}:</strong> K={k} → {segmentation_type}
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(get_text("apply_filter", st.session_state.language), use_container_width=True):
            processed_image = apply_kmeans_segmentation(image, k)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # İşlenmiş görüntüyü göster
    if processed_image is not None:
        st.session_state.processed_image = processed_image
        st.subheader(get_text("result", st.session_state.language))
        compare_images(image, processed_image)
        
        # İndirme bağlantısı
        st.subheader(get_text("download", st.session_state.language))
        buffer = io.BytesIO()
        processed_image.save(buffer, format='PNG')
        st.download_button(
            label=get_text("download_button", st.session_state.language),
            data=buffer.getvalue(),
            file_name=f"processed_{current_file.name}",
            mime="image/png",
            use_container_width=True
        )

if __name__ == "__main__":
    main() 