from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Hardcoded list of blog posts
POSTS = [
    {"id": 1, "title": "First Post", "content": "This is the first post."},
    {"id": 2, "title": "Second Post", "content": "This is the second post."},
]

# LIST POSTS (Step 1 + Step 6 sorting)
@app.route('/api/posts', methods=['GET'])
def list_posts():
    sort_field = request.args.get("sort")
    direction = request.args.get("direction", "asc")

    # Validate sort field if provided
    if sort_field and sort_field not in ["title", "content"]:
        return jsonify({"error": "Invalid sort field. Must be 'title' or 'content'."}), 400

    # Validate direction if provided
    if direction not in ["asc", "desc"]:
        return jsonify({"error": "Invalid direction. Must be 'asc' or 'desc'."}), 400

    # Default: return original order
    sorted_posts = POSTS.copy()

    # Apply sorting only if sort field is provided
    if sort_field:
        reverse = (direction == "desc")
        sorted_posts.sort(key=lambda p: p[sort_field].lower(), reverse=reverse)

    return jsonify(sorted_posts), 200

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

    post["title"] = data.get("title", post["title"])
    post["content"] = data.get("content", post["content"])

    return jsonify(post), 200

# SEARCH POSTS (Step 5)
@app.route('/api/posts/search', methods=['GET'])
def search_posts():
    title_query = request.args.get("title", "").lower()
    content_query = request.args.get("content", "").lower()

    results = []

    for post in POSTS:
        title_match = title_query in post["title"].lower() if title_query else False
        content_match = content_query in post["content"].lower() if content_query else False

        if title_match or content_match:
            results.append(post)

    return jsonify(results), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
