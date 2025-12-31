from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Expanded Data Model (Step 8)
POSTS = [
    {
        "id": 1,
        "title": "First Post",
        "content": "This is the first post.",
        "categories": ["general"],
        "tags": ["intro"],
        "comments": []
    },
    {
        "id": 2,
        "title": "Second Post",
        "content": "This is the second post.",
        "categories": ["updates"],
        "tags": ["news"],
        "comments": []
    },
]

# STEP 1 + STEP 6 + STEP 7: LIST POSTS with sorting + pagination
@app.route('/api/posts', methods=['GET'])
def list_posts():
    sort_field = request.args.get("sort")
    direction = request.args.get("direction", "asc")
    page = request.args.get("page", type=int)
    limit = request.args.get("limit", type=int)

    # Validate sorting
    if sort_field and sort_field not in ["title", "content"]:
        return jsonify({"error": "Invalid sort field. Must be 'title' or 'content'."}), 400

    if direction not in ["asc", "desc"]:
        return jsonify({"error": "Invalid direction. Must be 'asc' or 'desc'."}), 400

    sorted_posts = POSTS.copy()

    # Apply sorting
    if sort_field:
        reverse = (direction == "desc")
        sorted_posts.sort(key=lambda p: p[sort_field].lower(), reverse=reverse)

    # Apply pagination
    if page is not None and limit is not None:
        start = (page - 1) * limit
        end = start + limit
        paginated = sorted_posts[start:end]
        return jsonify({
            "page": page,
            "limit": limit,
            "total": len(sorted_posts),
            "results": paginated
        }), 200

    return jsonify(sorted_posts), 200

# STEP 2: ADD POST
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

    new_post = {
        "id": new_id,
        "title": data["title"],
        "content": data["content"],
        "categories": data.get("categories", []),
        "tags": data.get("tags", []),
        "comments": []
    }

    POSTS.append(new_post)
    return jsonify(new_post), 201

# STEP 3: DELETE POST
@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = next((p for p in POSTS if p["id"] == post_id), None)
    if not post:
        return jsonify({"error": f"Post with id {post_id} not found."}), 404

    POSTS.remove(post)
    return jsonify({"message": f"Post with id {post_id} has been deleted successfully."}), 200

# STEP 4: UPDATE POST
@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = next((p for p in POSTS if p["id"] == post_id), None)
    if not post:
        return jsonify({"error": f"Post with id {post_id} not found."}), 404

    data = request.get_json() or {}

    post["title"] = data.get("title", post["title"])
    post["content"] = data.get("content", post["content"])
    post["categories"] = data.get("categories", post["categories"])
    post["tags"] = data.get("tags", post["tags"])

    return jsonify(post), 200

# STEP 5: SEARCH POSTS
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

# STEP 8: ADD COMMENT
@app.route('/api/posts/<int:post_id>/comments', methods=['POST'])
def add_comment(post_id):
    post = next((p for p in POSTS if p["id"] == post_id), None)
    if not post:
        return jsonify({"error": f"Post with id {post_id} not found."}), 404

    data = request.get_json() or {}
    comment = data.get("comment")

    if not comment:
        return jsonify({"error": "Missing 'comment' field"}), 400

    post["comments"].append(comment)
    return jsonify(post), 201


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
