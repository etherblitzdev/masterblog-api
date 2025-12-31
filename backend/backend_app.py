from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Hardcoded list of blog posts
POSTS = [
    {"id": 1, "title": "First Post", "content": "This is the first post."},
    {"id": 2, "title": "Second Post", "content": "This is the second post."},
]

# LIST POSTS (Step 1)
@app.route('/api/posts', methods=['GET'])
def list_posts():
    return jsonify(POSTS), 200

# ADD POST (Step 2)
@app.route('/api/posts', methods=['POST'])
def add_post():
    data = request.get_json()

    missing = []
    if not data or "title" not in data:
        missing.append("title")
    if not data or "content" not in data:
        missing.append("content")

    if missing:
        return jsonify({"error": "Missing required fields", "missing": missing}), 400

    new_id = max(post["id"] for post in POSTS) + 1 if POSTS else 1
    new_post = {"id": new_id, "title": data["title"], "content": data["content"]}
    POSTS.append(new_post)
    return jsonify(new_post), 201

# DELETE POST (Step 3)
@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = next((p for p in POSTS if p["id"] == post_id), None)
    if not post:
        return jsonify({"error": f"Post with id {post_id} not found."}), 404

    POSTS.remove(post)
    return jsonify({"message": f"Post with id {post_id} has been deleted successfully."}), 200

# UPDATE POST (Step 4)
@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = next((p for p in POSTS if p["id"] == post_id), None)
    if not post:
        return jsonify({"error": f"Post with id {post_id} not found."}), 404

    data = request.get_json() or {}

    # Optional fields: keep old values if missing
    new_title = data.get("title", post["title"])
    new_content = data.get("content", post["content"])

    post["title"] = new_title
    post["content"] = new_content

    return jsonify(post), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
