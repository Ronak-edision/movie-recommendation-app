# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.9-slim

# Copy local code to the container image.
ENV APP_HOME /app
ENV NLTK_DATA /app/nltk_data


WORKDIR $APP_HOME
COPY . .

# Install production dependencies.
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run the setup script to download NLTK stopwords
RUN chmod +x setup.sh && ./setup.sh

# Run the web service on container startup.
CMD ["streamlit", "run", "app.py", "--server.port", "8080", "--server.address", "0.0.0.0"]
