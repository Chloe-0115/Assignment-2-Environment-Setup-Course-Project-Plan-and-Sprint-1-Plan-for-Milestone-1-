# Quotes Microservice

A simple Flask microservice that serves a random motivational quote.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

The server will start on http://localhost:5000

## API Endpoint

Simply make a GET request to the root endpoint:
```
GET /
```

You can test it using curl:
```bash
curl http://localhost:5000
```

## Response Format

The service returns a JSON response with a random quote:
```json
{
    "quote": "Your random quote here"
}
``` 
