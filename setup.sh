mkdir -p~/.streamlit/
echo"\
[server]\n\
port=$PORT\n\
enableCORS= false\n\
headless= true\n\
\n\
">~/.streamlit/config.toml

# Download NLTK stopwords to a custom directory
mkdir -p ~/.nltk_data
python -m nltk.downloader -d ~/.nltk_data stopwords

