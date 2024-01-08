from flask import Flask, jsonify, render_template
import os

app = Flask(__name__, static_folder='./templates/images')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
