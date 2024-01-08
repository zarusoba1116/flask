from flask import Flask, jsonify, render_template, request
import os
import json

app = Flask(__name__,)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save_data():
    data = request.form.to_dict()  # フォームからのデータを辞書に変換
    with open('data.json', 'w') as file:
        json.dump(data, file)  # データをJSONファイルに保存
    return 'Data saved successfully!'

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
