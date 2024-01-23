from flask import Flask, render_template, request, redirect, url_for
from src.model import probe_model_5l_profit  

import json

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        data = json.load(file)
        result = probe_model_5l_profit(data['data'])
        return render_template('result.html', result=result)

    return redirect(request.url)

if __name__ == '__main__':
    app.run(debug=True)
