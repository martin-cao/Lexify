FROM python:3.12-slim
LABEL authors="martincao"

WORKDIR /app

# Copy requirements.txt and install dependencies
COPY ../requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose default port for Flask
EXPOSE 5000

# Start Flask app
CMD ["python", "app.py"]