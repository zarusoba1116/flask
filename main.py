from flask import Flask, render_template, request, redirect
import os
import json

app = Flask(__name__,)


@app.route('/')
def index():
    print("test1")
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save_data():
    data = request.form.to_dict()  # フォームから送信されたデータを取得
    with open('data.json', 'w') as file:
        json.dump(data, file)  # データをJSONファイルに保存
    return redirect('https://www.instagram.com')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
