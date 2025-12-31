from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Hardcoded list of blog posts
POSTS = [
    {"id": 1, "title": "First Post", "content": "This is the first post."},
    {"id": 2, "title": "Second Post", "content": "This is the second post."},
]

# LIST ENDPOINT (Step 1)
@app.route('/api/posts', methods=['GET'])
def list_posts():
    return jsonify(POSTS), 200

# ADD ENDPOINT (Step 2)
@app.route('/api/posts', methods=['POST'])
def add_post():
    data = request.get_json()

    missing_fields = []
    if not data or "title" not in data:
        missing_fields.append("title")
    if not data or "content" not in data:
        missing_fields.append("content")

    if missing_fields:
        return jsonify({
            "error": "Missing required fields",
            "missing": missing_fields
        }), 400

    new_id = max(post["id"] for post in POSTS) + 1 if POSTS else 1

    new_post = {
        "id": new_id,
        "title": data["title"],
        "content": data["content"]
    }

    POSTS.append(new_post)
    return jsonify(new_post), 201

# DELETE ENDPOINT (Step 3)
@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    # Find post by ID
    post = next((p for p in POSTS if p["id"] == post_id), None)

    if not post:
        return jsonify({
            "error": f"Post with id {post_id} not found."
        }), 404

    # Remove post
    POSTS.remove(post)

    return jsonify({
        "message": f"Post with id {post_id} has been deleted successfully."
    }), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
