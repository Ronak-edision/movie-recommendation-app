import nltk

def setup_nltk_data():
    nltk.data.path.append('./nltk_data')  # Adjust path as necessary

if __name__ == "__main__":
    setup_nltk_data()
