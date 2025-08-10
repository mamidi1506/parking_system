# 📚 Phase 3 API Documentation

Complete API reference for the authentication system with all Phase 3 features.

## 🔗 Base URL
- **Development**: `http://localhost:8000/api`
- **Production**: `https://your-backend-url.onrender.com/api`

---

## 🔐 Authentication

All protected endpoints require a valid JWT token in the Authorization header:
```
Authorization: Bearer <your_access_token>
```

---

## 📋 Endpoints Overview

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/auth/register/` | Register new user | ❌ |
| POST | `/auth/login/` | Login user | ❌ |
| POST | `/auth/logout/` | Logout user | ✅ |
| GET | `/auth/profile/` | Get user profile | ✅ |
| PUT | `/auth/update-profile/` | Update user profile | ✅ |
| POST | `/auth/change-password/` | Change password | ✅ |
| POST | `/auth/delete-account/` | Delete account | ✅ |

---

## 🆕 Phase 1 & 2 Endpoints

### 1. User Registration

**Endpoint**: `POST /auth/register/`

**Description**: Register a new user account

**Request Body**:
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "mobile": "1234567890",
  "password": "securepassword123",
  "confirm_password": "securepassword123"
}
```

**Response** (201 Created):
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

**Validation Errors** (400 Bad Request):
```json
{
  "name": ["This field is required."],
  "email": ["Enter a valid email address."],
  "password": ["This password is too short. It must contain at least 8 characters."],
  "confirm_password": ["Passwords don't match."]
}
```

---

### 2. User Login

**Endpoint**: `POST /auth/login/`

**Description**: Authenticate user and return JWT tokens

**Request Body**:
```json
{
  "email": "john.doe@example.com",
  "password": "securepassword123"
}
```

**Response** (200 OK):
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

**Error Response** (400 Bad Request):
```json
{
  "non_field_errors": ["Invalid credentials."]
}
```

---

### 3. User Logout

**Endpoint**: `POST /auth/logout/`

**Description**: Logout user by blacklisting refresh token

**Headers**:
```
Authorization: Bearer <access_token>
```

**Request Body**:
```json
{
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

**Response** (200 OK):
```json
{
  "message": "Logout successful"
}
```

---

### 4. Get User Profile

**Endpoint**: `GET /auth/profile/`

**Description**: Get current user's profile information

**Headers**:
```
Authorization: Bearer <access_token>
```

**Response** (200 OK):
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

---

## 🆕 Phase 3 New Endpoints

### 5. Update User Profile

**Endpoint**: `PUT /auth/update-profile/`

**Description**: Update user profile information

**Headers**:
```
Authorization: Bearer <access_token>
```

**Request Body** (all fields optional):
```json
{
  "name": "John Smith",
  "email": "johnsmith@example.com",
  "mobile": "9876543210"
}
```

**Response** (200 OK):
```json
{
  "message": "Profile updated successfully",
  "user": {
    "id": 1,
    "name": "John Smith",
    "email": "johnsmith@example.com",
    "mobile": "9876543210",
    "date_joined": "2025-01-09T12:00:00Z"
  }
}
```

**Validation Errors** (400 Bad Request):
```json
{
  "email": ["This email is already in use."],
  "name": ["This field is required."]
}
```

---

### 6. Change Password

**Endpoint**: `POST /auth/change-password/`

**Description**: Change user password with current password validation

**Headers**:
```
Authorization: Bearer <access_token>
```

**Request Body**:
```json
{
  "current_password": "oldpassword123",
  "new_password": "newpassword456",
  "confirm_new_password": "newpassword456"
}
```

**Response** (200 OK):
```json
{
  "message": "Password changed successfully",
  "tokens": {
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
  }
}
```

**Validation Errors** (400 Bad Request):
```json
{
  "current_password": ["Current password is incorrect."],
  "new_password": ["This password is too short. It must contain at least 8 characters."],
  "confirm_new_password": ["New passwords don't match."]
}
```

**Note**: New JWT tokens are returned after password change for security.

---

### 7. Delete Account

**Endpoint**: `POST /auth/delete-account/`

**Description**: Permanently delete user account with confirmation

**Headers**:
```
Authorization: Bearer <access_token>
```

**Request Body**:
```json
{
  "password": "userpassword123",
  "confirmation": "DELETE"
}
```

**Response** (200 OK):
```json
{
  "message": "Account deleted successfully"
}
```

**Validation Errors** (400 Bad Request):
```json
{
  "password": ["Password is incorrect."],
  "confirmation": ["Please type 'DELETE' to confirm account deletion."]
}
```

**Warning**: This action is permanent and cannot be undone.

---

## 🔒 Authentication Error Responses

### 401 Unauthorized
When token is missing, invalid, or expired:
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

### 403 Forbidden
When user doesn't have permission:
```json
{
  "detail": "You do not have permission to perform this action."
}
```

---

## 🧪 Testing Examples

### Using cURL

#### 1. Register a new user
```bash
curl -X POST https://your-backend-url.onrender.com/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test User",
    "email": "test@example.com",
    "mobile": "1234567890",
    "password": "testpass123",
    "confirm_password": "testpass123"
  }'
```

#### 2. Login
```bash
curl -X POST https://your-backend-url.onrender.com/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "testpass123"
  }'
```

#### 3. Get profile (use token from login)
```bash
curl -X GET https://your-backend-url.onrender.com/api/auth/profile/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

#### 4. Update profile
```bash
curl -X PUT https://your-backend-url.onrender.com/api/auth/update-profile/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{
    "name": "Updated Name",
    "mobile": "9876543210"
  }'
```

#### 5. Change password
```bash
curl -X POST https://your-backend-url.onrender.com/api/auth/change-password/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{
    "current_password": "testpass123",
    "new_password": "newpass456",
    "confirm_new_password": "newpass456"
  }'
```

#### 6. Delete account
```bash
curl -X POST https://your-backend-url.onrender.com/api/auth/delete-account/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{
    "password": "newpass456",
    "confirmation": "DELETE"
  }'
```

---

## 📱 Postman Collection

### Setting up Postman

1. **Create new collection**: "Authentication API"
2. **Set up environment variables**:
   - `base_url`: `https://your-backend-url.onrender.com/api`
   - `access_token`: (will be set automatically)
   - `refresh_token`: (will be set automatically)

3. **Pre-request scripts** for authenticated endpoints:
```javascript
// Add this to authenticated requests
pm.request.headers.add({
  key: 'Authorization',
  value: 'Bearer ' + pm.environment.get('access_token')
});
```

4. **Test scripts** for login/register:
```javascript
// Add this to login/register requests
if (pm.response.code === 200 || pm.response.code === 201) {
    var jsonData = pm.response.json();
    if (jsonData.tokens) {
        pm.environment.set("access_token", jsonData.tokens.access);
        pm.environment.set("refresh_token", jsonData.tokens.refresh);
    }
}
```

### Collection Structure
```
Authentication API
├── 📁 Auth
│   ├── Register User
│   ├── Login User
│   └── Logout User
├── 📁 Profile
│   ├── Get Profile
│   ├── Update Profile
│   ├── Change Password
│   └── Delete Account
```

---

## 🔧 Rate Limiting (Future Enhancement)

For production, consider implementing rate limiting:

```python
# In Django settings.py
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/hour',
        'user': '1000/hour'
    }
}
```

---

## 📊 Response Codes Summary

| Code | Description | When |
|------|-------------|------|
| 200 | OK | Successful GET, PUT, POST (non-creation) |
| 201 | Created | Successful registration |
| 400 | Bad Request | Validation errors, invalid data |
| 401 | Unauthorized | Missing/invalid token |
| 403 | Forbidden | Permission denied |
| 404 | Not Found | Endpoint doesn't exist |
| 500 | Server Error | Internal server error |

---

## 🛡️ Security Considerations

### Token Management
- **Access tokens** expire in 1 hour
- **Refresh tokens** expire in 7 days
- **Tokens are blacklisted** on logout
- **New tokens generated** after password change

### Password Security
- **Minimum 8 characters** required
- **Django's PBKDF2** hashing used
- **Current password required** for changes
- **Confirmation required** for account deletion

### API Security
- **CORS properly configured**
- **HTTPS enforced** in production
- **Input validation** on all endpoints
- **SQL injection protected** by Django ORM

---

This completes the API documentation for Phase 3. All endpoints are thoroughly tested and production-ready! 🚀
