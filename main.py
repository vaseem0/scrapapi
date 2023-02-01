from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/get')
def notifications():
    url = 'http://akgsma.com'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        updates = soup.find_all('div', {'class': 'col-sm-6'})
        return jsonify([update.text for update in updates])
    else:
        return jsonify({'error': f'Request to {url} failed with status code {response.status_code}'})

if __name__ == '__main__':
    app.run(debug=True)
