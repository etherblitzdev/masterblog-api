from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Hardcoded list of blog posts (Step 1 requirement)
POSTS = [
    {"id": 1, "title": "First Post", "content": "This is the first post."},
    {"id": 2, "title": "Second Post", "content": "This is the second post."},
]

# LIST ENDPOINT (Step 1)
@app.route('/api/posts', methods=['GET'])
def list_posts():
    return jsonify(POSTS), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
