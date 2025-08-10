# API Testing Examples

This document provides sample requests for testing the authentication API endpoints using curl and Postman.

## Base URL
```
http://localhost:8000/api/auth/
```

## 1. User Registration

### curl Example:
```bash
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "mobile": "1234567890",
    "password": "securepassword123",
    "confirm_password": "securepassword123"
  }'
```

### Expected Response:
```json
{
  "message": "User registered successfully",
  "user": {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "mobile": "1234567890",
    "date_joined": "2025-01-09T12:00:00Z"
  },
  "tokens": {
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
  }
}
```

### Postman Setup:
- **Method**: POST
- **URL**: `http://localhost:8000/api/auth/register/`
- **Headers**: 
  - `Content-Type: application/json`
- **Body** (raw JSON):
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "mobile": "1234567890",
  "password": "securepassword123",
  "confirm_password": "securepassword123"
}
```

---

## 2. User Login

### curl Example:
```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john.doe@example.com",
    "password": "securepassword123"
  }'
```

### Expected Response:
```json
{
  "message": "Login successful",
  "user": {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "mobile": "1234567890",
    "date_joined": "2025-01-09T12:00:00Z"
  },
  "tokens": {
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
  }
}
```

### Postman Setup:
- **Method**: POST
- **URL**: `http://localhost:8000/api/auth/login/`
- **Headers**: 
  - `Content-Type: application/json`
- **Body** (raw JSON):
```json
{
  "email": "john.doe@example.com",
  "password": "securepassword123"
}
```

---

## 3. Get User Profile (Protected Endpoint)

### curl Example:
```bash
curl -X GET http://localhost:8000/api/auth/profile/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN_HERE"
```

### Expected Response:
```json
{
  "user": {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "mobile": "1234567890",
    "date_joined": "2025-01-09T12:00:00Z"
  }
}
```

### Postman Setup:
- **Method**: GET
- **URL**: `http://localhost:8000/api/auth/profile/`
- **Headers**: 
  - `Content-Type: application/json`
  - `Authorization: Bearer YOUR_ACCESS_TOKEN_HERE`

---

## 4. User Logout

### curl Example:
```bash
curl -X POST http://localhost:8000/api/auth/logout/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN_HERE" \
  -d '{
    "refresh_token": "YOUR_REFRESH_TOKEN_HERE"
  }'
```

### Expected Response:
```json
{
  "message": "Logout successful"
}
```

### Postman Setup:
- **Method**: POST
- **URL**: `http://localhost:8000/api/auth/logout/`
- **Headers**: 
  - `Content-Type: application/json`
  - `Authorization: Bearer YOUR_ACCESS_TOKEN_HERE`
- **Body** (raw JSON):
```json
{
  "refresh_token": "YOUR_REFRESH_TOKEN_HERE"
}
```

---

## Error Response Examples

### Validation Error (400):
```json
{
  "name": ["This field is required."],
  "email": ["Enter a valid email address."],
  "password": ["This password is too short. It must contain at least 8 characters."]
}
```

### Authentication Error (401):
```json
{
  "detail": "Given token not valid for any token type",
  "code": "token_not_valid",
  "messages": [
    {
      "token_class": "AccessToken",
      "token_type": "access",
      "message": "Token is invalid or expired"
    }
  ]
}
```

### Invalid Credentials (400):
```json
{
  "non_field_errors": ["Invalid credentials."]
}
```

---

## Testing Workflow

### 1. Complete Registration and Login Test:

1. **Register a new user**:
   ```bash
   curl -X POST http://localhost:8000/api/auth/register/ \
     -H "Content-Type: application/json" \
     -d '{
       "name": "Test User",
       "email": "test@example.com",
       "mobile": "9876543210",
       "password": "testpassword123",
       "confirm_password": "testpassword123"
     }'
   ```

2. **Copy the access token from the response and test profile endpoint**:
   ```bash
   curl -X GET http://localhost:8000/api/auth/profile/ \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer PASTE_ACCESS_TOKEN_HERE"
   ```

3. **Test logout with refresh token**:
   ```bash
   curl -X POST http://localhost:8000/api/auth/logout/ \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer PASTE_ACCESS_TOKEN_HERE" \
     -d '{
       "refresh_token": "PASTE_REFRESH_TOKEN_HERE"
     }'
   ```

### 2. Test Login Flow:

1. **Login with the registered user**:
   ```bash
   curl -X POST http://localhost:8000/api/auth/login/ \
     -H "Content-Type: application/json" \
     -d '{
       "email": "test@example.com",
       "password": "testpassword123"
     }'
   ```

2. **Test protected endpoint with new token**.

---

## Postman Collection

You can create a Postman collection with the following structure:

```
Authentication API Collection
├── Register User
├── Login User  
├── Get User Profile
└── Logout User
```

### Environment Variables in Postman:
- `base_url`: `http://localhost:8000/api/auth`
- `access_token`: (automatically set from login response)
- `refresh_token`: (automatically set from login response)

### Auto-extract tokens in Postman:
Add this script to the **Tests** tab of Login and Register requests:

```javascript
if (pm.response.code === 200 || pm.response.code === 201) {
    var jsonData = pm.response.json();
    if (jsonData.tokens) {
        pm.environment.set("access_token", jsonData.tokens.access);
        pm.environment.set("refresh_token", jsonData.tokens.refresh);
    }
}
```

---

## Database Verification

After testing the API, you can verify that data is stored correctly:

### SQLite Database Check:
```bash
# Navigate to backend directory
cd parking_backend

# Open Django shell
python manage.py shell

# Check users in database
from users.models import User
users = User.objects.all()
for user in users:
    print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}, Mobile: {user.mobile}")
```

### MongoDB Database Check (if using MongoDB):
```bash
# Connect to MongoDB
mongosh

# Switch to parking_db
use parking_db

# List collections
show collections

# Find all users
db.users.find().pretty()
```

This completes the API testing documentation with comprehensive examples for both curl and Postman.
