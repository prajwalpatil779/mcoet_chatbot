#!/usr/bin/env python3
"""
Automated Ollama Setup Script
Installs Ollama and downloads llama2 model for MCOET Chatbot
"""

import subprocess
import time
import os
import sys
import ctypes
from pathlib import Path

def run_as_admin(cmd):
    """Run command with admin privileges"""
    try:
        subprocess.run(cmd, shell=True, check=True)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def check_ollama_installed():
    """Check if Ollama is installed"""
    paths = [
        r"C:\Users\{}\AppData\Local\Programs\Ollama\ollama.exe".format(os.getenv('USERNAME')),
        r"C:\Program Files\Ollama\ollama.exe"
    ]
    
    for path in paths:
        if Path(path).exists():
            return path
    
    return None

def main():
    print("=" * 60)
    print("MCOET Chatbot - Ollama Automated Setup")
    print("=" * 60)
    print()
    
    # Step 1: Check/Install Ollama
    print("STEP 1: Checking Ollama installation...")
    ollama_path = check_ollama_installed()
    
    if ollama_path:
        print(f"✅ Ollama found at: {ollama_path}")
    else:
        print("❌ Ollama not installed")
        print("\n⏳ Please complete these manual steps:")
        print("1. Go to: https://ollama.ai/download")
        print("2. Download and install for Windows")
        print("3. Wait for installation to complete")
        print("4. Re-run this script")
        print("\nOr double-click: C:\\Users\\{}\\AppData\\Local\\Temp\\OllamaSetup.exe".format(os.getenv('USERNAME')))
        input("\nPress Enter after installing Ollama...")
        
        # Re-check
        ollama_path = check_ollama_installed()
        if not ollama_path:
            print("❌ Ollama still not found. Please install manually.")
            sys.exit(1)
        else:
            print(f"✅ Ollama now installed at: {ollama_path}")
    
    # Step 2: Start Ollama
    print("\nSTEP 2: Starting Ollama service...")
    try:
        subprocess.run(["net", "start", "Ollama"], capture_output=True)
        print("✅ Ollama service started")
        time.sleep(3)
    except:
        print("⚠️ Could not start service via net start")
        print("Attempting to run Ollama directly...")
        try:
            subprocess.Popen([ollama_path, "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print("✅ Ollama running in background")
            time.sleep(5)
        except Exception as e:
            print(f"❌ Could not start Ollama: {e}")
            print("Please start Ollama manually from system tray or Start menu")
            input("Press Enter after starting Ollama...")
    
    # Step 3: Pull llama2 model
    print("\nSTEP 3: Downloading llama2 AI model (2-3 GB)...")
    print("⏳ This may take 5-15 minutes depending on your internet speed...")
    print("=" * 60)
    
    try:
        # Use ollama command directly
        result = subprocess.run(
            [ollama_path.replace("ollama.exe", "ollama"), "pull", "llama2"],
            capture_output=False
        )
        
        if result.returncode == 0:
            print("=" * 60)
            print("✅ llama2 model downloaded successfully!")
        else:
            print("=" * 60)
            print("⚠️ Model download may have failed")
            print("Try running manually:")
            print(f"  {ollama_path} pull llama2")
    except Exception as e:
        print(f"❌ Error downloading model: {e}")
        print("Try running manually from PowerShell:")
        print("  ollama pull llama2")
    
    # Step 4: Verify installation
    print("\nSTEP 4: Verifying installation...")
    try:
        result = subprocess.run(
            [ollama_path.replace("ollama.exe", "ollama"), "list"],
            capture_output=True,
            text=True
        )
        if "llama2" in result.stdout:
            print("✅ llama2 model is ready!")
            print("\n" + "=" * 60)
            print("🎉 SUCCESS! Ollama is fully set up!")
            print("=" * 60)
            print("\nNow run the chatbot:")
            print("  cd c:\\Users\\{}\\Desktop\\mcoet_chatbot".format(os.getenv('USERNAME')))
            print("  streamlit run chatbot.py")
            print("\nThen open: http://localhost:8501")
            return True
        else:
            print("⚠️ llama2 not found in model list")
            print("Output:", result.stdout)
    except Exception as e:
        print(f"Could not verify: {e}")
    
    return False

if __name__ == "__main__":
    try:
        success = main()
        if not success:
            print("\n❌ Setup incomplete. Please check the manual setup guide:")
            print("See: OLLAMA_MANUAL_SETUP.md")
    except KeyboardInterrupt:
        print("\n\nSetup cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
    finally:
        print("\nPress Enter to close...")
        input()
