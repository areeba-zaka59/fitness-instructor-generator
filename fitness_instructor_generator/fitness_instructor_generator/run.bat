@echo off
REM Advanced Fitness Instructor Generator - Startup Script

echo.
echo ============================================
echo   Advanced Fitness Instructor Generator
echo ============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.10+ from https://www.python.org
    pause
    exit /b 1
)

REM Check if Streamlit is installed
python -c "import streamlit" >nul 2>&1
if errorlevel 1 (
    echo Installing required packages...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install requirements
        pause
        exit /b 1
    )
)

REM Download spaCy model if not present
python -c "import spacy; spacy.load('en_core_web_sm')" >nul 2>&1
if errorlevel 1 (
    echo Downloading spaCy language model...
    python -m spacy download en_core_web_sm
)

REM Download NLTK data
python -c "import nltk; nltk.data.find('corpora/stopwords'); nltk.data.find('corpora/wordnet')" >nul 2>&1
if errorlevel 1 (
    echo Downloading NLTK data...
    python -c "import nltk; nltk.download('stopwords'); nltk.download('wordnet')"
)

echo.
echo ✓ All dependencies are ready!
echo.
echo Starting application...
echo The app will open in your browser at http://localhost:8501
echo.
echo To stop the app, press Ctrl+C
echo.

REM Start Streamlit
streamlit run app.py

pause
