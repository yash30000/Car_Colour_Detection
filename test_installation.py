"""
Test script to verify installation and basic functionality
Run this before using the main application
"""

import sys

def check_imports():
    """Check if all required packages are installed"""
    print("Checking required packages...")
    
    packages = {
        'cv2': 'opencv-python',
        'numpy': 'numpy',
        'PIL': 'Pillow',
        'sklearn': 'scikit-learn',
        'webcolors': 'webcolors',
        'ultralytics': 'ultralytics',
        'tkinter': 'tkinter (built-in)'
    }
    
    missing = []
    
    for module, package in packages.items():
        try:
            __import__(module)
            print(f"✓ {package}")
        except ImportError:
            print(f"✗ {package} - MISSING")
            missing.append(package)
    
    return missing


def check_yolo_model():
    """Check if YOLO model can be loaded"""
    print("\nChecking YOLO model...")
    try:
        from ultralytics import YOLO
        model = YOLO('yolov8n.pt')
        print("✓ YOLOv8 model loaded successfully")
        return True
    except Exception as e:
        print(f"✗ YOLO model error: {e}")
        return False


def check_opencv():
    """Test OpenCV functionality"""
    print("\nChecking OpenCV...")
    try:
        import cv2
        import numpy as np
        
        # Create a test image
        img = np.zeros((100, 100, 3), dtype=np.uint8)
        cv2.rectangle(img, (10, 10), (90, 90), (255, 0, 0), 2)
        
        print(f"✓ OpenCV version: {cv2.__version__}")
        return True
    except Exception as e:
        print(f"✗ OpenCV error: {e}")
        return False


def check_python_version():
    """Check Python version"""
    print("Checking Python version...")
    version = sys.version_info
    
    if version.major >= 3 and version.minor >= 8:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"✗ Python {version.major}.{version.minor}.{version.micro} (3.8+ required)")
        return False


def main():
    """Run all checks"""
    print("="*60)
    print("Car Color Detection - Installation Test")
    print("="*60)
    print()
    
    # Check Python version
    python_ok = check_python_version()
    print()
    
    # Check imports
    missing = check_imports()
    print()
    
    # Check OpenCV
    opencv_ok = check_opencv()
    print()
    
    # Check YOLO model
    yolo_ok = check_yolo_model()
    print()
    
    # Summary
    print("="*60)
    print("SUMMARY")
    print("="*60)
    
    if python_ok and not missing and opencv_ok and yolo_ok:
        print("✓ All checks passed! You're ready to use the application.")
        print("\nRun the application with:")
        print("  python main.py")
    else:
        print("✗ Some checks failed.")
        
        if missing:
            print("\nTo install missing packages:")
            print("  pip install -r requirements.txt")
        
        if not python_ok:
            print("\nPlease upgrade to Python 3.8 or higher")
        
        if not yolo_ok:
            print("\nYOLO model will be downloaded on first run (requires internet)")
    
    print()


if __name__ == "__main__":
    main()
    

