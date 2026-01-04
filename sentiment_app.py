t55ggggggfgggg35ftftimport requests
from textblob import TextBlob

def get_sentiment(coin):
    # Free News API (Example purpose - replace with your key from newsapi.org)
    API_KEY = 'YOUR_NEWS_API_KEY' 
    url = f'https://newsapi.org/v2/everything?q={coin}&language=en&apiKey={API_KEY}'
    
    print(f"Analyzing market sentiment for: {coin}...")
    response = requests.get(url).json()
    articles = response.get('articles', [])[:5] # Top 5 news

    if not articles:f
        print("No news found!")
        return
    for i, article in enumerate(articles, 1):
        title = article['title']
        analysis = TextBlob(title)
        
        # Sentiment score (-1 to 1)
        score = analysis.sentiment.polarity
        mood = "Positive 🚀" if score > 0 else "Negative 📉" if score < 0 else "Neutral 😐"
        
        print(f"{i}. {title}")
        print(f"   Mood: {mood} (Score: {score})\n")

if __name__ == "__main__":
    coin_name = input("Enter Crypto Name (e.g. Bitcoin): ")
    get_sentiment(coin_name)
