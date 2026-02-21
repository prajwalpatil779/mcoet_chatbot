# MCOET Chatbot - Setup Instructions

## Problem
Your Gemini API quota has been exceeded.

## Solution: Use FREE Local AI (Ollama)

### Step 1: Download and Install Ollama
1. Go to https://ollama.ai/download
2. Click "Download for Windows"
3. Run the installer and follow the steps
4. Ollama will start automatically

### Step 2: Download the AI Model
Once Ollama is installed and running, it will create a system tray icon.

Open PowerShell and run:
```powershell
ollama pull llama2
```

This downloads the model (2-3 GB, takes 5-10 minutes first time).

### Step 3: Start the Chatbot
Once the model is downloaded, run:
```
streamlit run chatbot.py
```

The chatbot will now use the FREE local AI model with unlimited usage!

---

## Alternative: Use Gemini API with Billing

If you prefer cloud AI:
1. Go to https://console.cloud.google.com/billing
2. Add a payment method
3. Your API key quota will be restored
4. Update `GEMINI_API_KEY` in chatbot.py

Then run: `streamlit run chatbot.py`

---

## Current Setup
✅ Chatbot configured to use Ollama (LOCAL FREE AI)
✅ Knowledge base ready with 201 college document chunks
✅ Just need to install Ollama and pull the model
