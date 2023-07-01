from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/transform', methods=['POST'])
def transform():
    data = request.get_json()
    text = data.get('text')
    
    # Split the string into two parts
    first_part = text[:-2]
    last_part = text[-2:]
    
    # Repeat the last part twice
    repeated_last_part = last_part * 2
    
    # Join the parts back together
    transformed_text = first_part + ' ' + repeated_last_part
    
    return jsonify({'transformed_text': transformed_text})

if __name__ == '__main__':
    app.run(debug=True)
