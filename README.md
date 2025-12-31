# 📘 MasterBlog API — Full Documentation (Steps 1–8)

A complete educational backend + frontend project built with **Flask**, implementing a fully functional blog API with CRUD operations, search, sorting, pagination, and an expanded data model (categories, tags, comments).  
The project supports **local macOS development** and **Codio deployment** using a unified Flask application.

---

# 📌 Project Overview

MasterBlog API is a step‑by‑step learning project that evolves from a simple “list posts” endpoint into a fully featured blog backend with:

- CRUD operations  
- Search  
- Sorting  
- Pagination  
- Categories & tags  
- Comments  
- Frontend served from Flask  
- Codio‑safe deployment (single‑port architecture)  

Each step builds on the previous one, resulting in a clean, extensible API suitable for teaching, testing, and further development.

---

# 📁 Folder Structure

```
masterblog-api/
├── backend/                 # Legacy backend (used for local development)
│   └── backend_app.py
├── frontend/                # Frontend templates + static files
│   ├── frontend_app.py      # Legacy frontend (used for local development)
│   ├── static/
│   │   ├── main.js
│   │   └── style.css
│   └── templates/
│       └── index.html
├── combined_app.py          # Codio-safe unified frontend + backend server
└── postman/                 # All Postman collections for Steps 1–8
```

---

# 🚀 Running the Project

## 🖥️ Local macOS Development (Two‑App Model)

Run backend:

```bash
python3 backend/backend_app.py
```

Run frontend:

```bash
python3 frontend/frontend_app.py
```

Open the frontend:

```
http://127.0.0.1:5001
```

All features work locally because both apps run on `localhost`.

---

## 🟦 Codio Deployment (Unified Single‑Port Model)

Codio **blocks cross‑port fetch()**, so frontend + backend must run on the **same Flask app**.

Run:

```bash
python3 combined_app.py
```

Codio URL:

```
https://<project>-5002.codio.io/
```

This serves:

- `/` → frontend  
- `/static/...` → JS/CSS  
- `/api/...` → backend  

All from the same origin → **fetch() works**.

---

# 🧩 API Documentation (Steps 1–8)

Below is the complete reference for all implemented features.

---

# 🟦 Step 1 — List Posts

### **GET /api/posts**

Returns all posts.

#### Optional Query Parameters (added in later steps)

| Parameter   | Description |
|-------------|-------------|
| `sort`      | Sort by `title` or `content` |
| `direction` | `asc` or `desc` |
| `page`      | Page number |
| `limit`     | Items per page |

---

# 🟩 Step 2 — Add Post

### **POST /api/posts**

#### Body (JSON)

```json
{
  "title": "My Title",
  "content": "My Content",
  "categories": ["optional"],
  "tags": ["optional"]
}
```

Returns the created post with `201 Created`.

---

# 🟥 Step 3 — Delete Post

### **DELETE /api/posts/<id>**

Deletes a post by ID.

- `200 OK` → deleted  
- `404 Not Found` → invalid ID  

---

# 🟧 Step 4 — Update Post

### **PUT /api/posts/<id>**

#### Body (JSON)

```json
{
  "title": "New Title",
  "content": "New Content",
  "categories": ["dev"],
  "tags": ["python"]
}
```

Only provided fields are updated.

---

# 🟨 Step 5 — Search Posts

### **GET /api/posts/search**

#### Query Parameters

| Parameter | Description |
|-----------|-------------|
| `title`   | Search in title |
| `content` | Search in content |

Returns all matching posts.

---

# 🟪 Step 6 — Sorting

Sorting is integrated into **GET /api/posts**.

### Example:

```
/api/posts?sort=title&direction=desc
```

---

# 🟫 Step 7 — Pagination

Pagination is integrated into **GET /api/posts**.

### Example:

```
/api/posts?page=2&limit=5
```

Returns:

```json
{
  "page": 2,
  "limit": 5,
  "total": 17,
  "results": [ ... ]
}
```

---

# 🟩 Step 8 — Expanded Data Model

Posts now include:

```json
{
  "id": 1,
  "title": "...",
  "content": "...",
  "categories": [...],
  "tags": [...],
  "comments": [...]
}
```

### Add Comment

**POST /api/posts/<id>/comments**

#### Body:

```json
{ "comment": "Nice post!" }
```

---

# 📦 Postman Collections

All collections are located in:

```
postman/
```

Includes:

- Step1_List_Endpoint  
- Step2_Add_Endpoint  
- Step3_Delete_Endpoint  
- Step4_Update_Endpoint  
- Step5_Search_Endpoint  
- Step6_Sorting_Endpoint  
- Step7_Pagination_Endpoint  
- Step8_Expanded_Model_Endpoint  
- Step1–8_Complete_API  

---

# 🧠 Features Summary

The MasterBlog API now supports:

### ✔ CRUD Operations
- Create posts  
- Read posts  
- Update posts  
- Delete posts  

### ✔ Query Features
- Search  
- Sorting  
- Pagination  

### ✔ Expanded Data Model
- Categories  
- Tags  
- Comments  

### ✔ Frontend Integration
- Served from Flask  
- Works locally  
- Works in Codio (single‑port mode)  

---

# 🚀 Next Steps (Future Enhancements)

### **1. Authentication (JWT)**
Add:

- User registration  
- Login  
- Token‑based authentication  
- Role‑based permissions  

### **2. Rate Limiting**
Prevent abuse with:

- Per‑IP limits  
- Per‑user limits  
- Burst control  

### **3. API Versioning**
Introduce:

```
/api/v1/posts
```

to support future changes.

### **4. More Data Model Features**
Add:

- Post authors  
- Comment authors  
- Categories CRUD  
- Tag filtering  

### **5. Database Integration**
Replace in‑memory storage with:

- SQLite  
- PostgreSQL  
- SQLAlchemy ORM  

---

# 🎉 Final Notes

This project now represents a complete, extensible, production‑style educational API with a fully integrated frontend and backend.  
It is ready for further expansion, deployment, or use as a teaching reference.

