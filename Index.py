import subprocess
import sys

try:
    import nltk
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "nltk"])
    import nltk


nltk.download('punkt')
nltk.download('punkt_tab')   # <-- added to fix LookupError
nltk.download('wordnet')
nltk.download('stopwords')

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

news_data = [
    "India launches new space mission to study the sun.",
    "Global markets fall amid economic slowdown fears.",
    "AI technology is revolutionizing healthcare in rural areas.",
    "Election commission announces new voter ID rules.",
    "Scientists discover new species in the Amazon rainforest.",
    "Heavy rainfall causes flooding in multiple cities.",
    "Tech companies face new regulations on user privacy.",
    "Education ministry releases new school curriculum.",
    "Wildfires continue to spread across California forests.",
    "Medical researchers make progress in cancer vaccine development."
]

def preprocess(text):
    tokens = word_tokenize(text.lower())
    return [lemmatizer.lemmatize(token) for token in tokens if token.isalnum() and token not in stop_words]

news_tokens = [preprocess(news) for news in news_data]

def chatbot():
    print("NewsBot: Hello! Ask me about recent news topics (type 'exit' to quit).")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("NewsBot: Goodbye!")
            break

        user_tokens = preprocess(user_input)
        scores = [len(set(user_tokens).intersection(set(news))) for news in news_tokens]

        max_score = max(scores)
        if max_score == 0:
            print("NewsBot: Sorry, I couldn't find anything related.")
        else:
            best_match_index = scores.index(max_score)
            print("NewsBot:", news_data[best_match_index])

if __name__ == "__main__":
    chatbot()
