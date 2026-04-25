# Review Sentiment Detection

A beautiful, modern web application for analyzing customer review sentiment using AI.

## 🚀 Quick Start

1. **Get a Groq API Key:**
   - Go to https://console.groq.com/
   - Sign up or log in
   - Create a new API key
   - Copy the key

2. **Set up Environment Variable (Recommended):**
   
   **Option A: Using .env file**
   ```bash
   # Copy the example file
   cp .env.example .env
   
   # Edit .env and add your API key
   GROQ_API_KEY=your_actual_api_key_here
   ```
   
   **Option B: Set environment variable directly**
   ```bash
   # Windows (PowerShell)
   $env:GROQ_API_KEY="your_actual_api_key_here"
   
   # Windows (CMD)
   set GROQ_API_KEY=your_actual_api_key_here
   
   # Linux/Mac
   export GROQ_API_KEY="your_actual_api_key_here"
   ```
   
   **Option C: Hardcode in app.py (Not recommended for public repos)**
   - Open `app.py`
   - Replace `"YOUR_GROQ_API_KEY_HERE"` with your actual API key

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the App:**
   ```bash
   python app.py
   ```

5. **Open in Browser:**
   - Go to http://127.0.0.1:5000
   - Start analyzing reviews!

## ✨ Features

- **Modern Dark UI** with sophisticated design
- **Batch Review Analysis** - analyze multiple reviews at once
- **Real-time AI Processing** using Groq's fast Llama 3.1 model
- **Visual Results Dashboard** with sentiment statistics
- **Sample Reviews** included for quick testing
- **Mobile Responsive** design

## 🎨 What You'll See

- **Positive Reviews** 😊 - Green styling
- **Negative Reviews** 😞 - Red styling  
- **Neutral Reviews** 😐 - Yellow styling
- **Summary Statistics** - Total counts for each sentiment

## 🔧 Files

- `app.py` - Flask web server
- `templates/index.html` - Modern dark-themed web interface
- `1.py` - Original command-line version
- `requirements.txt` - Python dependencies

## 📊 Sample Reviews Included

- "The delivery was super fast and the product quality is excellent!"
- "Terrible customer service. My package arrived damaged and no one responds to emails."
- "Product is okay for the price. Nothing special but it works."

## 🛠️ Troubleshooting

If you see "Invalid API Key" errors:
1. Make sure you have a valid Groq API key
2. Update the key in `app.py`
3. Restart the Flask app

## 🎯 Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **AI Model:** Llama 3.1 8B via Groq API
- **Styling:** Modern dark theme with glassmorphism

Enjoy analyzing customer sentiment with AI! 🎉