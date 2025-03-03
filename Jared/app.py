from flask import Flask, jsonify
import random

app = Flask(__name__)

def load_quotes():
    with open('quotes.txt', 'r') as file:
        # Read all lines and filter out empty lines
        quotes = [line.strip() for line in file.readlines() if line.strip()]
    return quotes

QUOTES = load_quotes()

@app.route('/', methods=['GET'])
def get_random_quote():
    if not QUOTES:
        return jsonify({"error": "No quotes available"}), 404
    
    random_quote = random.choice(QUOTES)
    return jsonify({
        "quote": random_quote
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 