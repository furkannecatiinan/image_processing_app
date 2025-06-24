#!/bin/bash

# Digital Image Processing - Streamlit Application
# Çalıştırma scripti

echo "Digital Image Processing Application - Streamlit Version"
echo "=================================================="

# Bağımlılıkları kontrol et
echo "Checking dependencies..."
if ! command -v streamlit &> /dev/null; then
    echo "Streamlit is not installed. Installing..."
    pip install -r requirements.txt
else
    echo "Streamlit is already installed"
fi

# Port kontrolü
PORT=8501
if lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null ; then
    echo "Port $PORT is already in use"
    echo "Trying to find an alternative port..."
    PORT=$((PORT + 1))
fi

echo "Starting Streamlit application on port $PORT..."
echo "Application will be available at: http://localhost:$PORT"
echo ""
echo "Features:"
echo "   - Multi-language support (Turkish/English)"
echo "   - Dark/Light mode toggle"
echo "   - 10 image processing categories"
echo "   - Real-time image preview"
echo ""
echo "Press Ctrl+C to stop the application"
echo "=================================================="

# Streamlit uygulamasını başlat
streamlit run app.py --server.port=$PORT 