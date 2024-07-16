mkdir -p~/.streamlit/
echo"\
[server]\n\
port=$PORT\n\
enableCORS= false\n\
headless= true\n\
\n\
">~/.streamlit/config.toml

# Create a directory for NLTK data
mkdir -p ~/.nltk_data

# Download NLTK stopwords to the created directory
python -c "import nltk; nltk.download('stopwords', download_dir='/home/adminuser/.nltk_data')"
