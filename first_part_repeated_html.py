# FlaskモジュールからFlaskクラス、requestモジュール、render_template関数をインポートする
from flask import Flask, request, render_template

# Flaskアプリケーションのインスタンスを作成する
app = Flask(__name__)

# ルートURL('/')に対してGETとPOSTのメソッドを許可するルートを作成する
@app.route('/', methods=['GET', 'POST'])
def transform_text():
    # 変換されたテキストを格納する変数を初期化する
    transformed_text = ""

    # リクエストのメソッドがPOSTの場合のみ処理を実行する
    if request.method == 'POST':
        # フォームから入力されたテキストを取得する
        text = request.form['text']

        # テキストを2つの部分に分割する
        first_part = text[:2]
        last_part = text[2:]

        # 最初の部分を3回繰り返す
        repeated_first_part = first_part * 3

        # 変換されたテキストを作成する
        transformed_text = repeated_first_part + last_part

    # テンプレート('index.html')に変換されたテキストを渡して表示する
    return render_template('index.html', transformed_text=transformed_text)

# スクリプトが直接実行された場合にのみFlaskアプリケーションを起動する
if __name__ == '__main__':
    app.run(debug=True)
