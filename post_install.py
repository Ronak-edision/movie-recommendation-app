# post_install.py
import nltk
import ssl

def download_nltk_data():
    try:
        nltk.data.find("corpora/stopwords")
    except (LookupError, ssl.SSLError):
        ssl._create_default_https_context = ssl._create_unverified_context
        nltk.download('stopwords', download_dir='nltk_data', quiet=True)

if __name__ == "__main__":
    download_nltk_data()
