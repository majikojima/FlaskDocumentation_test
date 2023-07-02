from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def transform_text():
    transformed_text = ""
    if request.method == 'POST':
        text = request.form['text']

        first_part = text[:-2]
        last_part = text[-2:]

        repeated_last_part = last_part * 2

        transformed_text = first_part + ' ' + repeated_last_part

    return render_template('index.html', transformed_text=transformed_text)

if __name__ == '__main__':
    app.run()