import os
import subprocess
import shutil

def build_exe():
    """Build the executable using PyInstaller"""
    print("Building DSA Challenge Application...")
    print("=" * 50)
    
    # Clean previous builds
    if os.path.exists('build'):
        print("Cleaning build directory...")
        shutil.rmtree('build')
    if os.path.exists('dist'):
        print("Cleaning dist directory...")
        shutil.rmtree('dist')
    
    # Run PyInstaller
    print("\nRunning PyInstaller...")
    result = subprocess.run(['pyinstaller', 'build.spec', '--clean'], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("\n✓ Build successful!")
        print(f"\nExecutable created at: dist/DSA_Challenge.exe")
        print(f"File size: {os.path.getsize('dist/DSA_Challenge.exe') / (1024*1024):.2f} MB")
        
        # Copy data directory to dist
        if not os.path.exists('dist/data'):
            print("\nCopying data directory...")
            shutil.copytree('data', 'dist/data')
        
        print("\n" + "=" * 50)
        print("Build complete! You can now distribute the 'dist' folder.")
        print("Users can run DSA_Challenge.exe directly.")
    else:
        print("\n✗ Build failed!")
        print(result.stderr)

if __name__ == "__main__":
    build_exe()
