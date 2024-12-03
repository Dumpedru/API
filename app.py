from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    a = data.get('a', 0)
    b = data.get('b', 0)
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400
    
    kerület = 2 * (a + b)
    terület = a * b
    return jsonify({"kerület": kerület, "terület": terület})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

