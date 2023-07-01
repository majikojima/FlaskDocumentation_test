from flask import Flask, request, jsonify

app = Flask(__name__)

TARGET_WORD = 'zarigani'  # This is the word we want to transform
TRANSFORMED_WORD = 'zari ganigani'  # This is what we will transform it into

@app.route('/transform', methods=['POST'])
def transform_text():
    data = request.json
    text = data.get('text', '')
    # Perform the text transformation
    transformed_text = text.replace(TARGET_WORD, TRANSFORMED_WORD)
    return jsonify({'transformed_text': transformed_text})

if __name__ == '__main__':
    app.run(debug=True)