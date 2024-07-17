# post_install.py
import nltk

def download_nltk_data():
    nltk.download('stopwords')

if __name__ == "__main__":
    nltk.download('punkt')  # Ensure necessary NLTK data is downloaded
    download_nltk_data()
