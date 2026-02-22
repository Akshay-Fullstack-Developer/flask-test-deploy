from flask import Flask, jsonify

app = Flask(__name__)

# Route 1: Health check — confirms the API is alive
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "message": "API is running"})

# Route 2: Get all users — a sample data endpoint
@app.route('/users', methods=['GET'])
def get_users():
    users = [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob",   "email": "bob@example.com"},
    ]
    return jsonify({"users": users})

# Route 3: Get a single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id == 1:
        return jsonify({"id": 1, "name": "Alice", "email": "alice@example.com"})
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)