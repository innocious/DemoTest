from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.get_json()
    # Process the data here (if needed.)
    return jsonify({"message": "Data received successfully", "data": data}), 200

if __name__ == '__main__':
    app.run(debug=True)
