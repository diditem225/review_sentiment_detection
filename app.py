from flask import Flask, render_template, request, jsonify
from groq import Groq
from datetime import datetime
import time
import os

app = Flask(__name__)

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY", "YOUR_GROQ_API_KEY_HERE"))

def analyze_sentiment(review_text: str) -> dict:
    """
    Analyzes customer review sentiment using Groq API
    """
    if not review_text or review_text.strip() == "":
        return {
            "sentiment": "Neutral",
            "reason": "Empty review",
            "timestamp": datetime.now().isoformat(),
            "review_length": 0,
            "status": "success"
        }

    try:
        prompt = f"""
        Analyze the sentiment of this customer review.
        Respond with only one word: Positive, Negative, or Neutral.
        Do not provide any explanation.

        Review: "{review_text}"
        """

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0,
            max_tokens=10
        )

        sentiment = response.choices[0].message.content.strip()

        return {
            "sentiment": sentiment,
            "timestamp": datetime.now().isoformat(),
            "review_length": len(review_text),
            "status": "success"
        }

    except Exception as e:
        error_message = str(e)
        if "Invalid API Key" in error_message:
            error_message = "Invalid Groq API Key. Please update your API key in app.py"
        elif "401" in error_message:
            error_message = "Authentication failed. Please check your Groq API key"
        
        return {
            "sentiment": "Error",
            "error": error_message,
            "timestamp": datetime.now().isoformat(),
            "status": "failed"
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    reviews = data.get('reviews', [])
    
    if not reviews:
        return jsonify({"error": "No reviews provided"}), 400
    
    results = []
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    
    for i, review in enumerate(reviews, 1):
        if review.strip():  # Only process non-empty reviews
            result = analyze_sentiment(review)
            result['review_number'] = i
            result['review_text'] = review
            
            # Ensure review_length is always set
            if 'review_length' not in result:
                result['review_length'] = len(review)
                
            results.append(result)
            
            if result["status"] == "success":
                sentiment = result["sentiment"]
                # Clean up sentiment response (remove periods, extra text)
                sentiment = sentiment.split('.')[0].strip()
                result["sentiment"] = sentiment
                
                if sentiment in sentiment_counts:
                    sentiment_counts[sentiment] += 1
            
            # Small delay to avoid rate limiting
            time.sleep(0.5)
    
    return jsonify({
        "results": results,
        "summary": sentiment_counts,
        "total_reviews": len(results),
        "timestamp": datetime.now().isoformat()
    })

@app.route('/analyze_single', methods=['POST'])
def analyze_single():
    data = request.get_json()
    review = data.get('review', '')
    
    if not review.strip():
        return jsonify({"error": "No review text provided"}), 400
    
    result = analyze_sentiment(review)
    result['review_text'] = review
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)