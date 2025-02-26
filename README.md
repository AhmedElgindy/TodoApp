# 📝 Django To-Do App with JWT Authentication

A simple To-Do app built with Django REST Framework (DRF) using JWT authentication. The app is containerized with Docker and supports CRUD operations on To-Do items.

---

## 🚀 Features

✅ User authentication using JWT  
✅ Create, read, update, and delete To-Do items  
✅ Each user can only access their own To-Do list  
✅ Dockerized setup for easy deployment  
✅ Includes a Postman collection for testing APIs  

---

## 📌 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/AhmedElgindy/TodoApp.git

```

### 2️⃣ Set Up a Virtual Environment
```bash
pipenv install
pipenv shell

```

### 4️⃣ Apply Migrations
```bash
python manage.py migrate
```

### 5️⃣ Create a Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6️⃣ Run the Development Server
```bash
python manage.py runserver
```

The API will be available at:  
🔗 `http://127.0.0.1:8000/api/`

---

## 🐳 Docker Setup

### 1️⃣ Build and Run the Container
```bash
docker compose up --build
```

The app will be running at:  
🔗 `http://localhost:8000/`

---

## 🛠 API Endpoints

### 🟢 Authentication

| Method | Endpoint           | Description       |
|--------|--------------------|------------------|
| `POST` | `/api/token/`      | Get Access Token |
| `POST` | `/api/token/refresh/` | Refresh Token |

#### Example: Login Request
```json
{
    "username": "ahmed",
    "password": "yourpassword"
}
```

#### Response
```json
{
    "refresh": "your_refresh_token",
    "access": "your_access_token"
}
```

Use the `access` token in the request headers:
```
Authorization: Bearer your_access_token
```

---

### 🟡 To-Do Endpoints

| Method   | Endpoint        | Description              |
|----------|----------------|--------------------------|
| `GET`    | `/api/todos/`   | List all To-Dos (Auth)  |
| `POST`   | `/api/todos/`   | Create a new To-Do (Auth) |
| `GET`    | `/api/todos/{id}/` | Retrieve a specific To-Do (Auth) |
| `PUT`    | `/api/todos/{id}/` | Update a To-Do (Auth) |
| `DELETE` | `/api/todos/{id}/` | Delete a To-Do (Auth) |

#### Example: Create a To-Do

Request (with `Authorization: Bearer <token>` in the header):
```json
{
    "title": "Workout",
    "completed": false
}
```

Response:
```json
{
    "id": 1,
    "title": "Workout",
    "completed": false,
    "created_at": "2025-02-26T12:34:56Z",
    "user": "ahmed"
}
```

---


## 📝 How Authentication Works

1. **User signs up** using `/signup/`
2. **User logs in** using `/login/`
3. The API returns **access** and **refresh** tokens.
4. The user includes `Authorization: Bearer <access_token>` in headers for authentication.
5. If the token expires, the user can refresh it using `/api/token/refresh/`.

---
📂 Postman Collection: [Download Here](TODOAPI.postman_collection.json)




## 📌 Notes

- The app uses **JWT authentication**, so you need to include the `Authorization: Bearer <token>` header in requests.  
- Each user sees **only their own To-Dos**.  

---

## 📜 License

This project is open-source and available under the **MIT License**.

---
