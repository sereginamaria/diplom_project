from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)

# enable CORS
CORS(app)

@app.route('/users', methods=['POST'])
def hello_world():
    return jsonify('Првиет!')

if __name__ == "__main__":
    app.run()