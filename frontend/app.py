from flask import Flask, render_template, request
from backend_ready import find_word

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_word = request.form['search_word']
    results = find_word(search_word)
    return render_template('search_results.html', search_word=search_word, results=results)

if __name__ == '__main__':
    app.run(debug=True)
