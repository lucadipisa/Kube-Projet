from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint GET
@app.route('/get', methods=['GET'])
def get_data():
    data = {"message": "GET request successful -  POuLZT"}
    return jsonify(data), 200

# Endpoint POST
@app.route('/post', methods=['POST'])
def post_data():
    request_data = request.json
    if 'name' in request_data:
        message = f"Hello, {request_data['name']}! POST request successful"
    else:
        message = "Hello! POST request successful"
    return jsonify({"message": message}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)