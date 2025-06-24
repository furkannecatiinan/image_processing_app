"""
Filter UI components for Streamlit application
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

from utils import create_info_expander

def render_filter_controls(category, image, translations):
    """Render filter controls based on category"""
    
    if category == "fundamentals":
        return render_fundamentals_controls(image, translations)
    elif category == "transforms":
        return render_transforms_controls(image, translations)
    elif category == "frequency":
        return render_frequency_controls(image, translations)
    elif category == "restoration":
        return render_restoration_controls(image, translations)
    elif category == "color":
        return render_color_controls(image, translations)
    elif category == "wavelets":
        return render_wavelets_controls(image, translations)
    elif category == "compression":
        return render_compression_controls(image, translations)
    elif category == "morphological":
        return render_morphological_controls(image, translations)
    elif category == "segmentation":
        return render_segmentation_controls(image, translations)
    elif category == "features":
        return render_features_controls(image, translations)
    
    return None

def render_fundamentals_controls(image, translations):
    """Render fundamental operations controls"""
    st.subheader(translations['fundamentals'])
    
    # Info button
    create_info_expander('fundamentals', translations)
    
    filter_type = st.selectbox(
        translations['method'],
        [translations['gaussian_blur'], translations['edge_detection'], translations['threshold']]
    )
    
    if filter_type == translations['gaussian_blur']:
        col1, col2 = st.columns(2)
        with col1:
            kernel_size = st.slider(translations['kernel_size'], 3, 15, 5, step=2)
        with col2:
            sigma = st.slider(translations['sigma'], 0.1, 3.0, 1.0, step=0.1)
        
        if st.button(translations['apply_filter'], key="fundamental_apply"):
            return apply_gaussian_blur(image, kernel_size, sigma)
    
    elif filter_type == translations['edge_detection']:
        col1, col2 = st.columns(2)
        with col1:
            method = st.selectbox(translations['method'], [translations['sobel'], translations['canny']])
        with col2:
            threshold = st.slider(translations['threshold_value'], 50, 200, 100)
        
        if st.button(translations['apply_filter'], key="edge_apply"):
            method_key = 'sobel' if method == translations['sobel'] else 'canny'
            return apply_edge_detection(image, method_key, threshold)
    
    elif filter_type == translations['threshold']:
        col1, col2, col3 = st.columns(3)
        with col1:
            threshold_val = st.slider(translations['threshold_value'], 0, 255, 127)
        with col2:
            method = st.selectbox(translations['method'], 
                                [translations['binary'], translations['otsu'], translations['adaptive']])
        with col3:
            max_val = st.slider(translations['max_value'], 0, 255, 255)
        
        if st.button(translations['apply_filter'], key="threshold_apply"):
            method_key = {'binary': 'binary', 'otsu': 'otsu', 'adaptive': 'adaptive'}[
                {translations['binary']: 'binary', translations['otsu']: 'otsu', 
                 translations['adaptive']: 'adaptive'}[method]
            ]
            return apply_threshold(image, threshold_val, method_key, max_val)
    
    return None

def render_transforms_controls(image, translations):
    """Render intensity transform controls"""
    st.subheader(translations['transforms'])
    
    transform_type = st.selectbox(
        translations['transform_type'],
        [translations['linear'], translations['logarithmic'], 
         translations['power_law'], translations['histogram_eq']]
    )
    
    params = {}
    
    if transform_type == translations['linear']:
        col1, col2 = st.columns(2)
        with col1:
            params['alpha'] = st.slider(translations['alpha'], 0.1, 3.0, 1.0, step=0.1)
        with col2:
            params['beta'] = st.slider(translations['beta'], -100, 100, 0, step=5)
        transform_key = 'linear'
    
    elif transform_type == translations['logarithmic']:
        params['c'] = st.slider('C', 0.1, 2.0, 1.0, step=0.1)
        transform_key = 'logarithmic'
    
    elif transform_type == translations['power_law']:
        params['gamma'] = st.slider(translations['gamma'], 0.1, 3.0, 1.0, step=0.1)
        transform_key = 'power-law'
    
    else:  # histogram equalization
        transform_key = 'histogram'
    
    if st.button(translations['apply_filter'], key="transform_apply"):
        return apply_intensity_transform(image, transform_key, params)
    
    return None

def render_frequency_controls(image, translations):
    """Render frequency domain controls"""
    st.subheader(translations['frequency'])
    
    filter_type = st.selectbox(
        translations['filter_type'],
        [translations['lowpass'], translations['highpass'], translations['bandpass']]
    )
    
    cutoff = st.slider(translations['cutoff'], 0.1, 1.0, 0.5, step=0.1)
    
    if st.button(translations['apply_filter'], key="frequency_apply"):
        filter_key = {
            translations['lowpass']: 'lowpass',
            translations['highpass']: 'highpass',
            translations['bandpass']: 'bandpass'
        }[filter_type]
        return apply_frequency_filter(image, filter_key, cutoff)
    
    return None

def render_restoration_controls(image, translations):
    """Render image restoration controls"""
    st.subheader(translations['restoration'])
    
    operation = st.selectbox(
        translations['operation'],
        [translations['add_noise'], translations['noise_reduction']]
    )
    
    if operation == translations['add_noise']:
        col1, col2 = st.columns(2)
        with col1:
            noise_type = st.selectbox(translations['noise_type'], 
                                    [translations['gaussian'], translations['salt_pepper'], translations['speckle']])
        with col2:
            intensity = st.slider(translations['intensity'], 0.01, 0.5, 0.1, step=0.01)
        
        if st.button(translations['apply_filter'], key="noise_apply"):
            noise_key = {
                translations['gaussian']: 'gaussian',
                translations['salt_pepper']: 'salt_pepper',
                translations['speckle']: 'speckle'
            }[noise_type]
            return apply_noise(image, noise_key, intensity)
    
    else:  # noise reduction
        col1, col2 = st.columns(2)
        with col1:
            method = st.selectbox(translations['method'], 
                                [translations['gaussian'], translations['median'], translations['bilateral']])
        with col2:
            kernel_size = st.slider(translations['kernel_size'], 3, 15, 5, step=2)
        
        params = {'kernel_size': kernel_size}
        if method == translations['bilateral']:
            params['d'] = 9
            params['sigma_color'] = 75
            params['sigma_space'] = 75
        elif method == translations['gaussian']:
            params['sigma'] = 1.0
        
        if st.button(translations['apply_filter'], key="denoise_apply"):
            method_key = {
                translations['gaussian']: 'gaussian',
                translations['median']: 'median',
                translations['bilateral']: 'bilateral'
            }[method]
            return apply_noise_reduction(image, method_key, params)
    
    return None

def render_color_controls(image, translations):
    """Render color processing controls"""
    st.subheader(translations['color'])
    
    operation = st.selectbox(
        translations['operation'],
        [translations['color_balance'], translations['color_smoothing'], 
         translations['color_space'], translations['pseudocolor']]
    )
    
    if operation == translations['color_balance']:
        col1, col2, col3 = st.columns(3)
        with col1:
            r_scale = st.slider(translations['r_scale'], 0.1, 2.0, 1.0, step=0.1)
        with col2:
            g_scale = st.slider(translations['g_scale'], 0.1, 2.0, 1.0, step=0.1)
        with col3:
            b_scale = st.slider(translations['b_scale'], 0.1, 2.0, 1.0, step=0.1)
        
        if st.button(translations['apply_filter'], key="color_balance_apply"):
            return apply_color_balance(image, r_scale, g_scale, b_scale)
    
    elif operation == translations['color_smoothing']:
        kernel_size = st.slider(translations['kernel_size'], 3, 15, 5, step=2)
        
        if st.button(translations['apply_filter'], key="color_smooth_apply"):
            return apply_color_smoothing(image, kernel_size)
    
    elif operation == translations['color_space']:
        target_space = st.selectbox(translations['target_space'], 
                                  [translations['hsv'], translations['lab'], 
                                   translations['yuv'], translations['gray']])
        
        if st.button(translations['apply_filter'], key="color_space_apply"):
            space_key = {
                translations['hsv']: 'hsv',
                translations['lab']: 'lab',
                translations['yuv']: 'yuv',
                translations['gray']: 'gray'
            }[target_space]
            return convert_color_space(image, space_key)
    
    else:  # pseudocolor
        if st.button(translations['apply_filter'], key="pseudocolor_apply"):
            return apply_pseudocolor(image)
    
    return None

def render_wavelets_controls(image, translations):
    """Render wavelet transform controls"""
    st.subheader(translations['wavelets'])
    
    col1, col2 = st.columns(2)
    with col1:
        wavelet_type = st.selectbox(translations['wavelet_type'], 
                                  [translations['haar'], translations['db4'], translations['bior2.2']])
    with col2:
        level = st.slider(translations['level'], 1, 4, 1)
    
    if st.button(translations['apply_filter'], key="wavelet_apply"):
        wavelet_key = {
            translations['haar']: 'haar',
            translations['db4']: 'db4',
            translations['bior2.2']: 'bior2.2'
        }[wavelet_type]
        return apply_wavelet_transform(image, wavelet_key, level)
    
    return None

def render_compression_controls(image, translations):
    """Render compression controls"""
    st.subheader(translations['compression'])
    
    col1, col2 = st.columns(2)
    with col1:
        compression_type = st.selectbox(translations['compression_type'], 
                                      [translations['jpeg'], translations['wavelet'], 
                                       translations['rle'], translations['huffman']])
    with col2:
        quality = st.slider(translations['quality'], 10, 100, 80)
    
    if st.button(translations['apply_filter'], key="compression_apply"):
        if compression_type == translations['jpeg']:
            compressed_data = compress_jpeg(image, quality)
            return decompress_jpeg(compressed_data)
        elif compression_type == translations['wavelet']:
            compressed_data = compress_wavelet(image, quality)
            return decompress_wavelet(compressed_data)
        elif compression_type == translations['rle']:
            compressed_data = compress_rle(image, quality)
            return decompress_rle(compressed_data)
        else:  # huffman
            compressed_data = compress_huffman(image, quality)
            return decompress_huffman(compressed_data)
    
    return None

def render_morphological_controls(image, translations):
    """Render morphological operations controls"""
    st.subheader(translations['morphological'])
    
    col1, col2, col3 = st.columns(3)
    with col1:
        operation = st.selectbox(translations['operation'], 
                               [translations['erosion'], translations['dilation'], 
                                translations['opening'], translations['closing']])
    with col2:
        kernel_shape = st.selectbox(translations['kernel_shape'], 
                                  [translations['rect'], translations['ellipse'], translations['cross']])
    with col3:
        kernel_size = st.slider(translations['kernel_size'], 3, 15, 3, step=2)
    
    iterations = st.slider(translations['iterations'], 1, 5, 1)
    
    if st.button(translations['apply_filter'], key="morphological_apply"):
        operation_key = {
            translations['erosion']: 'erosion',
            translations['dilation']: 'dilation',
            translations['opening']: 'opening',
            translations['closing']: 'closing'
        }[operation]
        
        shape_key = {
            translations['rect']: 'rect',
            translations['ellipse']: 'ellipse',
            translations['cross']: 'cross'
        }[kernel_shape]
        
        return apply_morphological_operation(image, operation_key, shape_key, kernel_size, iterations)
    
    return None

def render_segmentation_controls(image, translations):
    """Render segmentation controls"""
    st.subheader(translations['segmentation'])
    
    method = st.selectbox(translations['method'], 
                         [translations['watershed'], translations['grabcut'], translations['kmeans']])
    
    if method == translations['kmeans']:
        k = st.slider(translations['k_clusters'], 2, 8, 3)
        
        if st.button(translations['apply_filter'], key="kmeans_apply"):
            return apply_kmeans_segmentation(image, k)
    
    elif method == translations['watershed']:
        if st.button(translations['apply_filter'], key="watershed_apply"):
            return apply_watershed_segmentation(image)
    
    else:  # grabcut
        if st.button(translations['apply_filter'], key="grabcut_apply"):
            return apply_grabcut_segmentation(image)
    
    return None

def render_features_controls(image, translations):
    """Render feature extraction controls"""
    st.subheader(translations['features'])
    
    feature_type = st.selectbox(translations['feature_type'], 
                              [translations['basic'], translations['texture'], translations['color_hist']])
    
    if st.button(translations['apply_filter'], key="features_apply"):
        feature_key = {
            translations['basic']: 'basic',
            translations['texture']: 'texture',
            translations['color_hist']: 'color_hist'
        }[feature_type]
        
        features = extract_features(image, feature_key)
        
        # Display features in a nice format
        st.write("### Extracted Features:")
        if isinstance(features, dict):
            for key, value in features.items():
                st.write(f"**{key}**: {value}")
        else:
            st.write(features)
        
        # Return original image since feature extraction doesn't modify it
        return image
    
    return None 