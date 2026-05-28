#!/usr/bin/env python3
"""
Comprehensive test script for the Advanced Fitness Instructor Generator.
Validates all modules and components before running the app.
"""

import sys
import importlib
from pathlib import Path

def test_import(module_name, display_name=None):
    """Test if a module can be imported."""
    display_name = display_name or module_name
    try:
        importlib.import_module(module_name)
        print(f"OK: {display_name} module")
        return True
    except ImportError as e:
        print(f"FAIL: {display_name} module - {str(e)}")
        return False

def test_local_module(module_path, display_name):
    """Test local project modules."""
    try:
        spec = importlib.util.spec_from_file_location(display_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        print(f"OK: {display_name}")
        return True
    except Exception as e:
        print(f"FAIL: {display_name} - {str(e)}")
        return False

def main():
    """Run all tests."""
    print("\n" + "="*60)
    print("  Advanced Fitness Instructor Generator - Test Suite")
    print("="*60 + "\n")
    
    # Test external packages
    print("Testing External Dependencies:")
    print("-" * 40)
    
    external_packages = [
        ("streamlit", "Streamlit (Web UI)"),
        ("numpy", "NumPy (Numerical Computing)"),
        ("spacy", "spaCy (NLP)"),
        ("mediapipe", "MediaPipe (Pose Detection)"),
        ("cv2", "OpenCV (Computer Vision)"),
        ("matplotlib", "Matplotlib (Visualization)"),
        ("PIL", "Pillow (Image Processing)"),
        ("nltk", "NLTK (Text Processing)"),
        ("pyttsx3", "pyttsx3 (Text-to-Speech)"),
        ("sklearn", "scikit-learn (Machine Learning)"),
    ]
    
    external_results = []
    for package, display in external_packages:
        external_results.append(test_import(package, display))
    
    print("\nTesting Local Modules:")
    print("-" * 40)
    
    # Test local modules
    base_path = Path(__file__).parent
    local_modules = [
        (base_path / "nlp" / "preprocess.py", "NLP Preprocessing"),
        (base_path / "nlp" / "entity_extractor.py", "Entity Extractor"),
        (base_path / "nlp" / "intent_classifier.py", "Intent Classifier"),
        (base_path / "nlp" / "advanced_nlp.py", "Advanced NLP"),
        (base_path / "workout_engine" / "generator.py", "Workout Generator"),
        (base_path / "workout_engine" / "pose_visualizer.py", "Pose Visualizer"),
        (base_path / "workout_engine" / "animator.py", "Exercise Animator"),
        (base_path / "audio" / "tts.py", "Text-to-Speech"),
    ]
    
    local_results = []
    for module_path, display in local_modules:
        if module_path.exists():
            local_results.append(test_local_module(str(module_path), display))
        else:
            print(f"✗ {display} - File not found at {module_path}")
            local_results.append(False)
    
    # Summary
    print("\n" + "="*60)
    all_tests = external_results + local_results
    passed = sum(all_tests)
    total = len(all_tests)
    
    if passed == total:
        print(f"ALL PASSED: {total} tests")
        print("="*60)
        print("\nReady to run the application\n")
        print("To start the Fitness Instructor Generator, run:")
        print("  streamlit run app.py\n")
        return 0
    else:
        print(f"{total - passed} out of {total} tests FAILED")
        print("="*60)
        print("\nPlease install missing dependencies using:")
        print("  pip install -r requirements.txt\n")
        print("Then download the spaCy model:")
        print("  python -m spacy download en_core_web_sm\n")
        return 1

if __name__ == "__main__":
    sys.exit(main())
