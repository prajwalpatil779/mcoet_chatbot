@echo off
REM MCOET Chatbot - Simple Ollama Installer

echo ============================================================
echo MCOET Chatbot - Ollama Installation
echo ============================================================
echo.

echo Waiting for any locked files to release...
timeout /t 3 /nobreak

echo.
echo Closing any running Ollama processes...
taskkill /F /IM ollama.exe 2>nul
taskkill /F /IM OllamaSetup.exe 2>nul
timeout /t 2 /nobreak

echo.
echo Removing old installer...
del /F /Q "%TEMP%\OllamaSetup.exe" 2>nul

echo.
echo Downloading Ollama installer (1.2 GB - this may take 5-10 minutes)...
echo Please wait...

REM Download using PowerShell
powershell -Command "try { (New-Object System.Net.WebClient).DownloadFile('https://ollama.ai/download/OllamaSetup.exe', '%TEMP%\OllamaSetup.exe'); Write-Host 'Download complete!'; exit 0 } catch { Write-Host 'Download failed!'; exit 1 }"

if %errorlevel% neq 0 (
    echo.
    echo ERROR: Could not download Ollama
    echo Please download manually from: https://ollama.ai/download
    pause
    exit /b 1
)

echo.
echo Starting Ollama installer...
echo.
start "" "%TEMP%\OllamaSetup.exe"

echo.
echo The installer window should open. Please follow the installation steps.
echo After installation completes, Ollama will start automatically.
echo.
echo Waiting 2 minutes for installation to complete...
timeout /t 120 /nobreak

echo.
echo Checking if Ollama was installed...
if exist "C:\Users\%USERNAME%\AppData\Local\Programs\Ollama\ollama.exe" (
    echo ✓ Ollama found! 
    echo.
    echo Now downloading the AI model (llama2)...
    echo This will take 5-15 minutes depending on your internet speed.
    echo.
    cd /d "C:\Users\%USERNAME%\AppData\Local\Programs\Ollama"
    ollama pull llama2
    
    echo.
    echo ============================================================
    echo SUCCESS! Ollama and llama2 are ready!
    echo ============================================================
    echo.
    echo You can now run the chatbot:
    echo   cd c:\Users\%USERNAME%\Desktop\mcoet_chatbot
    echo   streamlit run chatbot.py
    echo.
    echo Then open: http://localhost:8501
    echo.
) else (
    echo.
    echo WARNING: Ollama not found in expected location.
    echo It may still be installing. Please wait a few more minutes.
    echo.
    echo You can try running manually:
    echo   Start Menu ^> Search "Ollama" ^> Click to start
    echo.
    echo Then from PowerShell:
    echo   ollama pull llama2
    echo.
)

pause
