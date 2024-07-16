import pickle
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
import requests
nltk.download('stopwords')
nltk.download('punkt')

ps = PorterStemmer()

# Load CountVectorizer (cv) and classifier (clf2) from saved files
with open('cv.pkl', 'rb') as f:
    cv = pickle.load(f)

with open('clf2.pkl', 'rb') as f:
    clf2 = pickle.load(f)

# Function to preprocess text
def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in text.split() if word not in stop_words]
    return ' '.join(filtered_words)

def stem(text):
    return ' '.join([ps.stem(word.lower()) for word in text.split()])

def evaluate_sentiment(text):
    text = remove_stopwords(text)
    text = stem(text)
    a = cv.transform([text])  # Transform text into vector using CountVectorizer
    y_pred = clf2.predict(a)  # Predict sentiment using the classifier
    return 'positive' if y_pred[0] == 1 else 'negative'

