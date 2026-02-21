@echo off
REM Quick start script for Ollama and Chatbot

echo ============================================================
echo MCOET Chatbot - Quick Start
echo ============================================================
echo.

echo Checking Ollama installation...
if not exist "C:\Users\%USERNAME%\AppData\Local\Programs\Ollama\ollama.exe" (
    echo.
    echo ERROR: Ollama not found!
    echo.
    echo Please download and install Ollama first:
    echo 1. Go to: https://ollama.ai/download
    echo 2. Click "Download for Windows"
    echo 3. Run the installer
    echo 4. Wait for completion
    echo 5. Run this script again
    echo.
    echo Installation link: https://ollama.ai/download
    echo.
    pause
    exit /b 1
)

echo ✓ Ollama found!
echo.

echo Checking if Ollama service is running...
sc query Ollama | find "RUNNING" >nul
if %errorlevel% neq 0 (
    echo Starting Ollama service...
    net start Ollama 2>nul
    if %errorlevel% neq 0 (
        echo Running Ollama in background...
        cd /d "C:\Users\%USERNAME%\AppData\Local\Programs\Ollama"
        start "" ollama.exe serve
        timeout /t 5
    )
) else (
    echo ✓ Ollama service is running
)

echo.
echo Checking if llama2 model is available...
cd /d "C:\Users\%USERNAME%\AppData\Local\Programs\Ollama"
ollama list | find "llama2" >nul

if %errorlevel% neq 0 (
    echo.
    echo llama2 model not found. Downloading (takes 10-15 minutes)...
    echo.
    ollama pull llama2
) else (
    echo ✓ llama2 model is ready!
)

echo.
echo ============================================================
echo Starting MCOET Chatbot...
echo ============================================================
echo.

cd /d "C:\Users\%USERNAME%\Desktop\mcoet_chatbot"

echo Opening chatbot at http://localhost:8501
echo.

timeout /t 2

streamlit run chatbot.py
