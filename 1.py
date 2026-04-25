from groq import Groq
from datetime import datetime
import sys
import time
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY", "YOUR_GROQ_API_KEY_HERE"))

def analyze_sentiment(review_text: str) -> dict:
    """
    Analyzes customer review sentiment using Groq API

    Args:
        review_text (str): The customer review to analyze

    Returns:
        dict: Contains sentiment, timestamp, review_length, and status
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

        # Extract text from Groq response
        sentiment = response.choices[0].message.content.strip()

        return {
            "sentiment": sentiment,
            "timestamp": datetime.now().isoformat(),
            "review_length": len(review_text),
            "status": "success"
        }

    except Exception as e:
        return {
            "sentiment": "Error",
            "error": str(e),
            "timestamp": datetime.now().isoformat(),
            "status": "failed"
        }

def generate_business_report(reviews: list) -> None:
    """
    Generates a formatted business report for multiple reviews
    """
    print("=" * 60)
    print("AUTOMATED SENTIMENT ANALYSIS REPORT")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}

    for i, review in enumerate(reviews, 1):
        result = analyze_sentiment(review)
        
        # Add delay to avoid rate limiting (Groq has generous limits but still good practice)
        time.sleep(1)

        if result["status"] == "success":
            sentiment = result["sentiment"]
            sentiment_counts[sentiment] = sentiment_counts.get(sentiment, 0) + 1

            print(f"\nReview #{i}:")
            print(f"Text: {review[:80]}..." if len(review) > 80 else f"Text: {review}")
            print(f"Sentiment: {sentiment}")
            print(f"Processed: {result['timestamp']}")
        else:
            print(f"\nReview #{i}: ERROR - {result['error']}")

    print("\n" + "=" * 60)
    print("SUMMARY:")
    print(f"Positive: {sentiment_counts['Positive']}")
    print(f"Negative: {sentiment_counts['Negative']}")
    print(f"Neutral: {sentiment_counts['Neutral']}")
    print("=" * 60)
    print("\nBusiness Impact: Saves 15+ hours/month of manual review analysis")

if __name__ == "__main__":

    reviews = [
        "The delivery was super fast and the product quality is excellent!",
        "Terrible customer service. My package arrived damaged and no one responds to emails.",
        "Product is okay for the price. Nothing special but it works."
    ]

    print("\n")
    generate_business_report(reviews)
