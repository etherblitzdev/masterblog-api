from flask import Flask, jsonify, request
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


# ADD ENDPOINT (Step 2)
@app.route('/api/posts', methods=['POST'])
def add_post():
    # Extract JSON body
    data = request.get_json()

    # Validate required fields
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

    # Generate new unique integer ID
    new_id = max(post["id"] for post in POSTS) + 1 if POSTS else 1

    # Create new post object
    new_post = {
        "id": new_id,
        "title": data["title"],
        "content": data["content"]
    }

    # Add to list
    POSTS.append(new_post)

    # Return created post with 201 status
    return jsonify(new_post), 201


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)

