# Complete User Authentication System Setup Guide

This guide will help you set up a complete user authentication system with Django REST Framework backend and React frontend.

## Project Structure
```
parking/
├── parking_backend/          # Django backend
│   ├── parking_backend/      # Main Django project
│   ├── users/               # Users app for authentication
│   ├── requirements.txt     # Python dependencies
│   ├── .env                # Environment variables
│   └── manage.py           # Django management script
└── frontend/               # React frontend
    ├── public/
    ├── src/
    │   ├── components/     # React components
    │   ├── pages/         # Page components
    │   ├── services/      # API services
    │   └── utils/         # Utility functions
    ├── package.json       # Node.js dependencies
    └── ...
```

## Prerequisites

Before starting, make sure you have the following installed:

1. **Python 3.8+** - [Download from python.org](https://www.python.org/downloads/)
2. **Node.js 16+** - [Download from nodejs.org](https://nodejs.org/)
3. **MongoDB** - [Download MongoDB Community Edition](https://www.mongodb.com/try/download/community)

## Step 1: Install MongoDB

### Windows:
1. Download MongoDB Community Edition from the official website
2. Run the installer and follow the setup wizard
3. Make sure to install MongoDB as a Windows Service
4. MongoDB will automatically start and run on `mongodb://localhost:27017`

### Verify MongoDB Installation:
Open Command Prompt and run:
```cmd
mongosh
```
If it connects successfully, MongoDB is running correctly.

## Step 2: Set Up Python Virtual Environment

1. Open Command Prompt or PowerShell
2. Navigate to your project directory:
   ```cmd
   cd C:\Users\{YourUsername}\parking
   ```

3. Create a virtual environment:
   ```cmd
   python -m venv venv
   ```

4. Activate the virtual environment:
   ```cmd
   venv\Scripts\activate
   ```

## Step 3: Install Backend Dependencies

1. Navigate to the backend directory:
   ```cmd
   cd parking_backend
   ```

2. Install Python packages:
   ```cmd
   pip install -r requirements.txt
   ```

## Step 4: Configure Environment Variables

The `.env` file in the `parking_backend` directory contains:
```
MONGODB_URI=mongodb://localhost:27017/parking_db
SECRET_KEY=your-secret-key-here-change-in-production
DEBUG=True
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

**Important**: For production, change the `SECRET_KEY` to a secure random string.

## Step 5: Set Up Django Database

1. Make sure you're in the `parking_backend` directory with virtual environment activated

2. Create database migrations:
   ```cmd
   python manage.py makemigrations
   ```

3. Apply migrations:
   ```cmd
   python manage.py migrate
   ```

4. Create a superuser (optional, for Django admin):
   ```cmd
   python manage.py createsuperuser
   ```

## Step 6: Install Frontend Dependencies

1. Open a new Command Prompt/PowerShell window
2. Navigate to the frontend directory:
   ```cmd
   cd C:\Users\{YourUsername}\parking\frontend
   ```

3. Install Node.js packages:
   ```cmd
   npm install
   ```

## Step 7: Run the Application

You'll need to run both backend and frontend simultaneously.

### Terminal 1 - Backend (Django):
```cmd
cd C:\Users\{YourUsername}\parking\parking_backend
venv\Scripts\activate
python manage.py runserver
```

The backend will run on: `http://localhost:8000`

### Terminal 2 - Frontend (React):
```cmd
cd C:\Users\{YourUsername}\parking\frontend
npm start
```

The frontend will run on: `http://localhost:3000`

## Step 8: Test the Application

1. Open your browser and go to `http://localhost:3000`
2. You should see a login page
3. Click "Create Account" to register a new user
4. Fill in the registration form and submit
5. You'll be redirected to the dashboard
6. Test the logout functionality

## API Endpoints

The backend provides these API endpoints:

- `POST /api/auth/register/` - User registration
- `POST /api/auth/login/` - User login
- `GET /api/auth/profile/` - Get user profile (protected)
- `POST /api/auth/logout/` - User logout

## Features Implemented

### Backend (Django REST Framework):
- ✅ Custom User model with email authentication
- ✅ JWT token authentication
- ✅ Password hashing and validation
- ✅ MongoDB integration using Djongo
- ✅ CORS configuration for React frontend
- ✅ User registration and login endpoints
- ✅ Protected user profile endpoint

### Frontend (React):
- ✅ User Registration page with form validation
- ✅ User Login page
- ✅ Protected Dashboard showing user details
- ✅ JWT token management (localStorage)
- ✅ Automatic token validation and refresh
- ✅ Protected routes (redirect to login if not authenticated)
- ✅ Logout functionality
- ✅ Modern, responsive UI design

## Troubleshooting

### Common Issues:

1. **MongoDB Connection Error**:
   - Make sure MongoDB is running
   - Check if the connection string in `.env` is correct

2. **CORS Errors**:
   - Ensure backend is running on port 8000
   - Check CORS_ALLOWED_ORIGINS in settings.py

3. **Module Not Found Errors**:
   - Make sure virtual environment is activated
   - Reinstall packages: `pip install -r requirements.txt`

4. **Frontend Won't Start**:
   - Delete `node_modules` and run `npm install` again
   - Check if Node.js version is 16+

5. **Authentication Issues**:
   - Clear browser localStorage
   - Check if backend endpoints are accessible

### Testing Backend Only:

You can test the backend API using tools like Postman or curl:

```bash
# Register a user
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com", 
    "password": "securepassword123",
    "confirm_password": "securepassword123"
  }'

# Login
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "securepassword123"
  }'
```

## Security Notes

1. Change the `SECRET_KEY` in production
2. Set `DEBUG=False` in production
3. Configure proper CORS origins for production
4. Use HTTPS in production
5. Consider implementing refresh token rotation
6. Add rate limiting for authentication endpoints

## Next Steps

This authentication system provides a solid foundation. You can extend it by adding:

- Password reset functionality
- Email verification
- User profile updates
- Role-based permissions
- Two-factor authentication
- Social media login integration

The system is now ready for development and can be easily deployed to cloud platforms like Heroku, AWS, or DigitalOcean.
