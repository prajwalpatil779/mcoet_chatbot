# OLLAMA SETUP - STEP BY STEP

## Current Status
✅ Ollama installer downloaded to: C:\Users\a2z\AppData\Local\Temp\OllamaSetup.exe

## MANUAL STEPS TO COMPLETE:

### Step 1: Run the Installer
1. Open Windows Explorer
2. Navigate to: `C:\Users\a2z\AppData\Local\Temp\`
3. Double-click: `OllamaSetup.exe`
4. Click "Install" and wait for completion (2-5 minutes)
5. Ollama will start automatically and show a system tray icon

### Step 2: Download the AI Model
Once Ollama is installed and running:
1. Open PowerShell
2. Run this command:
   ```powershell
   ollama pull llama2
   ```
3. Wait for download to complete (2-3 GB, takes 5-10 minutes)

### Step 3: Test Ollama is Running
In PowerShell, run:
```powershell
ollama list
```
You should see `llama2` in the list.

### Step 4: Start the Chatbot
In PowerShell, from the chatbot folder:
```powershell
cd c:\Users\a2z\Desktop\mcoet_chatbot
streamlit run chatbot.py
```

Then open: http://localhost:8501

## AUTOMATED SCRIPT (Run if above doesn't work)

**Option A: Python Auto-Download**
```python
import subprocess
import time

# Wait a bit for any previous process to finish
time.sleep(5)

# Run installer
subprocess.run([r"C:\Users\a2z\AppData\Local\Temp\OllamaSetup.exe"], check=False)

# Wait for installation
time.sleep(60)

# Pull model
subprocess.run(["ollama", "pull", "llama2"], check=False)
```

---

## TROUBLESHOOTING

**"ollama command not found"?**
- Close PowerShell completely
- Open a NEW PowerShell window
- Try the command again (installer needs to update PATH)

**Stuck on pulling model?**
- This is normal - models are 2-3 GB
- Let it run in background
- Check progress: `ollama list`

**Still having issues?**
- Restart your computer
- Run installer again
- Check if Ollama appears in system tray (bottom right)

---

## ESTIMATED TIME
- Installer: 2-5 minutes
- Model download: 5-15 minutes (depends on internet)
- **Total: 10-20 minutes**

Once complete, the chatbot will work **FOREVER for FREE with UNLIMITED usage!**
