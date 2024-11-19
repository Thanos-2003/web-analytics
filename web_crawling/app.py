from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for crawling the data
@app.route('/crawl', methods=['POST'])
def crawl():
    url = request.form['url']  # Get URL from the form input

    try:
        # Fetch the content of the URL
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)})

    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Example: Extract all the titles in <h1> tags
    titles = [h1.get_text() for h1 in soup.find_all('h1')]
 

    return jsonify({'titles': titles})

if __name__ == '__main__':
    app.run(debug=True)
