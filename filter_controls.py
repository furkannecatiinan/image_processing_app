"""
Detailed filter controls for individual filter pages
"""

import streamlit as st
import sys
import os

# Add parent directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from filters import (
    apply_gaussian_blur, apply_edge_detection, apply_threshold,
    apply_intensity_transform, apply_frequency_filter, 
    apply_noise_reduction, apply_noise,
    apply_pseudocolor, apply_color_balance, apply_color_smoothing,
    convert_color_space, apply_wavelet_transform,
    compress_jpeg, compress_wavelet, compress_rle, compress_huffman,
    apply_morphological_operation, apply_morphological_gradient, apply_skeleton,
    apply_watershed_segmentation, apply_grabcut_segmentation,
    apply_kmeans_segmentation, extract_features
)

def render_fundamentals_filter(filter_name, image, translations):
    """Render fundamental filter controls"""
    if filter_name == "gaussian_blur":
        st.markdown("#### 🌫️ Gaussian Blur Parametreleri")
        
        col1, col2 = st.columns(2)
        with col1:
            kernel_size = st.slider(
                "🔧 Kernel Boyutu", 
                min_value=3, max_value=21, value=5, step=2,
                help="Daha büyük değerler daha fazla bulanıklaştırma sağlar"
            )
        with col2:
            sigma = st.slider(
                "📊 Sigma (σ)", 
                min_value=0.1, max_value=5.0, value=1.0, step=0.1,
                help="Gaussian çekirdeğinin standart sapması"
            )
        
        # Real-time preview
        if st.checkbox("🔄 Gerçek Zamanlı Önizleme", value=True):
            return apply_gaussian_blur(image, kernel_size, sigma)
        
        if st.button("✨ Filtreyi Uygula", use_container_width=True):
            return apply_gaussian_blur(image, kernel_size, sigma)
    
    elif filter_name == "edge_detection":
        st.markdown("#### 🔍 Edge Detection Parametreleri")
        
        col1, col2 = st.columns(2)
        with col1:
            method = st.selectbox(
                "🛠️ Yöntem", 
                options=["sobel", "canny"],
                format_func=lambda x: "Sobel Operatörü" if x == "sobel" else "Canny Kenar Algılayıcı"
            )
        with col2:
            threshold = st.slider(
                "🎯 Eşik Değeri", 
                min_value=10, max_value=300, value=100,
                help="Kenar tespiti için eşik değeri"
            )
        
        if method == "canny":
            blur_size = st.slider(
                "🌫️ Ön Bulanıklaştırma", 
                min_value=3, max_value=15, value=5, step=2,
                help="Gürültüyü azaltmak için ön bulanıklaştırma"
            )
        else:
            blur_size = 5
        
        if st.checkbox("🔄 Gerçek Zamanlı Önizleme", value=True):
            return apply_edge_detection(image, method, threshold, blur_size)
        
        if st.button("✨ Filtreyi Uygula", use_container_width=True):
            return apply_edge_detection(image, method, threshold, blur_size)
    
    elif filter_name == "threshold":
        st.markdown("#### ⚫ Thresholding Parametreleri")
        
        col1, col2 = st.columns(2)
        with col1:
            method = st.selectbox(
                "🛠️ Yöntem", 
                options=["binary", "otsu", "adaptive"],
                format_func=lambda x: {
                    "binary": "Binary Threshold",
                    "otsu": "Otsu's Method",
                    "adaptive": "Adaptive Threshold"
                }[x]
            )
        
        with col2:
            max_value = st.slider(
                "📈 Maksimum Değer", 
                min_value=100, max_value=255, value=255
            )
        
        if method == "binary":
            threshold_val = st.slider(
                "🎯 Eşik Değeri", 
                min_value=0, max_value=255, value=127
            )
        else:
            threshold_val = 127
        
        if st.checkbox("🔄 Gerçek Zamanlı Önizleme", value=True):
            return apply_threshold(image, threshold_val, method, max_value)
        
        if st.button("✨ Filtreyi Uygula", use_container_width=True):
            return apply_threshold(image, threshold_val, method, max_value)
    
    return None

def render_transforms_filter(filter_name, image, translations):
    """Render intensity transform controls"""
    st.markdown("#### 🎭 Intensity Transform Parametreleri")
    
    params = {}
    
    if filter_name == "linear":
        col1, col2 = st.columns(2)
        with col1:
            params['alpha'] = st.slider(
                "📈 Alpha (Kontrast)", 
                min_value=0.1, max_value=3.0, value=1.0, step=0.1,
                help="Kontrast çarpanı"
            )
        with col2:
            params['beta'] = st.slider(
                "💡 Beta (Parlaklık)", 
                min_value=-100, max_value=100, value=0, step=5,
                help="Parlaklık değeri"
            )
        transform_key = 'linear'
    
    elif filter_name == "logarithmic":
        params['c'] = st.slider(
            "🔢 C Sabiti", 
            min_value=0.1, max_value=2.0, value=1.0, step=0.1,
            help="Logaritmik dönüşüm sabiti"
        )
        transform_key = 'logarithmic'
    
    elif filter_name == "power_law":
        params['gamma'] = st.slider(
            "⚡ Gamma", 
            min_value=0.1, max_value=3.0, value=1.0, step=0.1,
            help="Güç kanunu üssü (gamma)"
        )
        transform_key = 'power-law'
    
    else:  # histogram_eq
        st.info("Histogram eşitleme için parametre gerekmez")
        transform_key = 'histogram'
    
    if st.checkbox("🔄 Gerçek Zamanlı Önizleme", value=True):
        return apply_intensity_transform(image, transform_key, params)
    
    if st.button("✨ Filtreyi Uygula", use_container_width=True):
        return apply_intensity_transform(image, transform_key, params)
    
    return None

def render_frequency_filter(filter_name, image, translations):
    """Render frequency domain controls"""
    st.markdown("#### 🌊 Frequency Domain Parametreleri")
    
    cutoff = st.slider(
        "✂️ Kesim Frekansı", 
        min_value=0.1, max_value=1.0, value=0.5, step=0.1,
        help="Frekans filtresi kesim noktası"
    )
    
    filter_type_map = {
        'lowpass': 'lowpass',
        'highpass': 'highpass', 
        'bandpass': 'bandpass'
    }
    
    if st.checkbox("🔄 Gerçek Zamanlı Önizleme", value=True):
        return apply_frequency_filter(image, filter_type_map[filter_name], cutoff)
    
    if st.button("✨ Filtreyi Uygula", use_container_width=True):
        return apply_frequency_filter(image, filter_type_map[filter_name], cutoff)
    
    return None

def render_restoration_filter(filter_name, image, translations):
    """Render restoration controls"""
    if filter_name == "add_noise":
        st.markdown("#### 🎲 Gürültü Ekleme Parametreleri")
        
        col1, col2 = st.columns(2)
        with col1:
            noise_type = st.selectbox(
                "🔊 Gürültü Türü", 
                options=["gaussian", "salt_pepper", "speckle"],
                format_func=lambda x: {
                    "gaussian": "Gaussian Gürültüsü",
                    "salt_pepper": "Tuz-Biber Gürültüsü", 
                    "speckle": "Speckle Gürültüsü"
                }[x]
            )
        with col2:
            intensity = st.slider(
                "📊 Gürültü Yoğunluğu", 
                min_value=0.01, max_value=0.5, value=0.1, step=0.01,
                help="Gürültü şiddeti"
            )
        
        if st.checkbox("🔄 Gerçek Zamanlı Önizleme", value=True):
            return apply_noise(image, noise_type, intensity)
        
        if st.button("✨ Filtreyi Uygula", use_container_width=True):
            return apply_noise(image, noise_type, intensity)
    
    elif filter_name == "noise_reduction":
        st.markdown("#### 🧹 Gürültü Azaltma Parametreleri")
        
        col1, col2 = st.columns(2)
        with col1:
            method = st.selectbox(
                "🛠️ Yöntem", 
                options=["gaussian", "median", "bilateral"],
                format_func=lambda x: {
                    "gaussian": "Gaussian Filtreleme",
                    "median": "Median Filtreleme",
                    "bilateral": "Bilateral Filtreleme"
                }[x]
            )
        with col2:
            kernel_size = st.slider(
                "🔧 Kernel Boyutu", 
                min_value=3, max_value=15, value=5, step=2
            )
        
        params = {'kernel_size': kernel_size}
        if method == 'bilateral':
            params.update({
                'd': st.slider("📏 Filtre Çapı", 5, 15, 9, step=2),
                'sigma_color': st.slider("🎨 Renk Sigma", 10, 150, 75),
                'sigma_space': st.slider("📍 Uzay Sigma", 10, 150, 75)
            })
        elif method == 'gaussian':
            params['sigma'] = st.slider("📊 Sigma", 0.1, 3.0, 1.0, step=0.1)
        
        if st.checkbox("🔄 Gerçek Zamanlı Önizleme", value=True):
            return apply_noise_reduction(image, method, params)
        
        if st.button("✨ Filtreyi Uygula", use_container_width=True):
            return apply_noise_reduction(image, method, params)
    
    return None

def render_color_filter(filter_name, image, translations):
    """Render color processing controls"""
    if filter_name == "pseudocolor":
        st.markdown("#### 🌈 Pseudocolor Parametreleri")
        st.info("Gri tonlamalı görüntüye sahte renk uygulanır")
        
        if st.button("✨ Filtreyi Uygula", use_container_width=True):
            return apply_pseudocolor(image)
    
    elif filter_name == "color_balance":
        st.markdown("#### ⚖️ Renk Dengesi Parametreleri")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            r_scale = st.slider("🔴 Kırmızı", 0.1, 3.0, 1.0, step=0.1)
        with col2:
            g_scale = st.slider("🟢 Yeşil", 0.1, 3.0, 1.0, step=0.1)
        with col3:
            b_scale = st.slider("🔵 Mavi", 0.1, 3.0, 1.0, step=0.1)
        
        if st.checkbox("🔄 Gerçek Zamanlı Önizleme", value=True):
            return apply_color_balance(image, r_scale, g_scale, b_scale)
        
        if st.button("✨ Filtreyi Uygula", use_container_width=True):
            return apply_color_balance(image, r_scale, g_scale, b_scale)
    
    elif filter_name == "color_space":
        st.markdown("#### 🔄 Renk Uzayı Dönüşümü")
        
        target_space = st.selectbox(
            "🎯 Hedef Renk Uzayı",
            options=["hsv", "lab", "yuv", "gray"],
            format_func=lambda x: {
                "hsv": "HSV (Hue-Saturation-Value)",
                "lab": "LAB (L*a*b*)",
                "yuv": "YUV",
                "gray": "Gri Tonlama"
            }[x]
        )
        
        if st.button("✨ Filtreyi Uygula", use_container_width=True):
            return convert_color_space(image, target_space)
    
    return None

def render_wavelet_filter(filter_name, image, translations):
    """Render wavelet controls"""
    st.markdown("#### 🌊 Wavelet Transform Parametreleri")
    
    col1, col2 = st.columns(2)
    with col1:
        wavelet_type = st.selectbox(
            "🌊 Wavelet Türü",
            options=["haar", "db4", "bior2.2"],
            format_func=lambda x: {
                "haar": "Haar Wavelet",
                "db4": "Daubechies 4",
                "bior2.2": "Biorthogonal 2.2"
            }[x]
        )
    with col2:
        level = st.slider(
            "📊 Ayrışım Seviyesi", 
            min_value=1, max_value=4, value=2
        )
    
    if filter_name == "wavelet_transform":
        if st.button("✨ Wavelet Dönüşümü Uygula", use_container_width=True):
            return apply_wavelet_transform(image, wavelet_type, level)
    
    return None

def render_compression_filter(filter_name, image, translations):
    """Render compression controls"""
    st.markdown("#### 📦 Sıkıştırma Parametreleri")
    
    quality = st.slider(
        "🎯 Kalite", 
        min_value=1, max_value=100, value=80,
        help="Sıkıştırma kalitesi (yüksek = daha iyi kalite)"
    )
    
    compression_map = {
        'jpeg': compress_jpeg,
        'wavelet_compress': compress_wavelet,
        'rle': compress_rle,
        'huffman': compress_huffman
    }
    
    if filter_name in compression_map:
        if st.button("✨ Sıkıştırmayı Uygula", use_container_width=True):
            return compression_map[filter_name](image, quality)
    
    return None

def render_morphological_filter(filter_name, image, translations):
    """Render morphological controls"""
    st.markdown("#### 🔷 Morfolojik İşlem Parametreleri")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        kernel_size = st.slider("🔧 Kernel Boyutu", 3, 15, 5, step=2)
    with col2:
        kernel_shape = st.selectbox(
            "🔷 Kernel Şekli",
            options=["rect", "ellipse", "cross"],
            format_func=lambda x: {
                "rect": "Dikdörtgen",
                "ellipse": "Elips",
                "cross": "Artı"
            }[x]
        )
    with col3:
        iterations = st.slider("🔄 Tekrarlama", 1, 5, 1)
    
    operation_map = {
        'erosion': 'erosion',
        'dilation': 'dilation', 
        'opening': 'opening',
        'closing': 'closing'
    }
    
    if filter_name in operation_map:
        if st.button("✨ İşlemi Uygula", use_container_width=True):
            return apply_morphological_operation(
                image, operation_map[filter_name], 
                kernel_shape, kernel_size, iterations
            )
    
    return None

def render_segmentation_filter(filter_name, image, translations):
    """Render segmentation controls"""
    st.markdown("#### ✂️ Bölütleme Parametreleri")
    
    if filter_name == "kmeans":
        k_clusters = st.slider(
            "🎯 Küme Sayısı (K)", 
            min_value=2, max_value=10, value=3,
            help="K-means için küme sayısı"
        )
        
        if st.button("✨ K-Means Bölütleme", use_container_width=True):
            return apply_kmeans_segmentation(image, k_clusters)
    
    elif filter_name == "watershed":
        if st.button("✨ Watershed Bölütleme", use_container_width=True):
            return apply_watershed_segmentation(image)
    
    elif filter_name == "grabcut":
        if st.button("✨ GrabCut Bölütleme", use_container_width=True):
            return apply_grabcut_segmentation(image)
    
    return None

def render_features_filter(filter_name, image, translations):
    """Render feature extraction controls"""
    st.markdown("#### 🔬 Özellik Çıkarımı")
    
    feature_map = {
        'basic_features': 'basic',
        'texture_features': 'texture',
        'color_histogram': 'color_hist'
    }
    
    if filter_name in feature_map:
        if st.button("✨ Özellikleri Çıkar", use_container_width=True):
            features = extract_features(image, feature_map[filter_name])
            st.json(features)
            return image  # Return original image since this is analysis
    
    return None

# Main function to route filter controls
def render_filter_controls_detailed(category, filter_name, image, translations):
    """Route to appropriate filter control renderer"""
    
    if category == "fundamentals":
        return render_fundamentals_filter(filter_name, image, translations)
    elif category == "transforms":
        return render_transforms_filter(filter_name, image, translations)
    elif category == "frequency":
        return render_frequency_filter(filter_name, image, translations)
    elif category == "restoration":
        return render_restoration_filter(filter_name, image, translations)
    elif category == "color":
        return render_color_filter(filter_name, image, translations)
    elif category == "wavelets":
        return render_wavelet_filter(filter_name, image, translations)
    elif category == "compression":
        return render_compression_filter(filter_name, image, translations)
    elif category == "morphological":
        return render_morphological_filter(filter_name, image, translations)
    elif category == "segmentation":
        return render_segmentation_filter(filter_name, image, translations)
    elif category == "features":
        return render_features_filter(filter_name, image, translations)
    
    return None 