# post_install.py
import nltk
from nltk.data import find
import ssl

def download_nltk_data():
    try:
        find("corpora/stopwords.zip")
    except LookupError:
        context = ssl._create_unverified_context()
        nltk.download('stopwords', download_dir='nltk_data', quiet=True, context=context)

if __name__ == "__main__":
    download_nltk_data()
