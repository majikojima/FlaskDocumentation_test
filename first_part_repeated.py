from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/transform', methods=['POST'])
def transform_text():
    data = request.get_json()
    text = data.get('text')

    # Split the string into two parts
    first_part = text[:2]
    last_part = text[2:]

    repeated_first_part = first_part * 2

    transformed_text = repeated_first_part + ' ' + last_part

    return jsonify({'transformed_text': transformed_text})

if __name__ == '__main__':
    app.run(debug=True)
