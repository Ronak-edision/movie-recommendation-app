mkdir -p~/.streamlit/
echo"\
[server]\n\
port=$PORT\n\
enableCORS= false\n\
headless= true\n\
\n\
">~/.streamlit/config.toml

# Download NLTK stopwords to the default directory
python -c "import nltk; nltk.download('stopwords')"
