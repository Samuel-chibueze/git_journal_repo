from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import AuthorListCreateAPIView, AuthorDetailAPIView, JournalListCreateAPIView, JournalDetailAPIView, UserCreateAPIView, UserLoginAPIView

urlpatterns = [
    path('authors/', AuthorListCreateAPIView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorDetailAPIView.as_view(), name='author-detail'),
    path('journals/', JournalListCreateAPIView.as_view(), name='journal-list-create'),
    path('journals/<int:pk>/', JournalDetailAPIView.as_view(), name='journal-detail'),
    path('users/', UserCreateAPIView.as_view(), name='user-create'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

"""
URL patterns:

1. `authors/` (GET, POST)
   - GET: Retrieve a list of all authors (requires authentication).
   - POST: Create a new author (requires authentication).
   - Example: 
     - GET: curl -X GET -H "Authorization: Bearer <access_token>" http://localhost:8000/authors/
     - POST: curl -X POST -d "user=1&bio=Author bio&phone_number=1234567890" -H "Authorization: Bearer <access_token>" http://localhost:8000/authors/

2. `authors/<int:pk>/` (GET, PUT, DELETE)
   - GET: Retrieve details of a specific author (requires authentication).
   - PUT: Update a specific author (requires authentication).
   - DELETE: Delete a specific author (requires authentication).
   - Example:
     - GET: curl -X GET -H "Authorization: Bearer <access_token>" http://localhost:8000/authors/1/
     - PUT: curl -X PUT -d "bio=Updated bio" -H "Authorization: Bearer <access_token>" http://localhost:8000/authors/1/
     - DELETE: curl -X DELETE -H "Authorization: Bearer <access_token>" http://localhost:8000/authors/1/

3. `journals/` (GET, POST)
   - GET: Retrieve a list of all journal entries (requires authentication).
   - POST: Create a new journal entry (requires authentication).
   - Example:
     - GET: curl -X GET -H "Authorization: Bearer <access_token>" http://localhost:8000/journals/
     - POST: curl -X POST -d "title=Journal title&description=Journal description" -H "Authorization: Bearer <access_token>" http://localhost:8000/journals/

4. `journals/<int:pk>/` (GET, PUT, DELETE)
   - GET: Retrieve details of a specific journal entry (requires authentication).
   - PUT: Update a specific journal entry (requires authentication).
   - DELETE: Delete a specific journal entry (requires authentication).
   - Example:
     - GET: curl -X GET -H "Authorization: Bearer <access_token>" http://localhost:8000/journals/1/
     - PUT: curl -X PUT -d "title=Updated title" -H "Authorization: Bearer <access_token>" http://localhost:8000/journals/1/
     - DELETE: curl -X DELETE -H "Authorization: Bearer <access_token>" http://localhost:8000/journals/1/

5. `users/` (POST)
   - POST: Create a new user.
   - Example:
     - POST: curl -X POST -d "username=newuser&password=password&email=newuser@example.com" http://localhost:8000/users/

6. `login/` (POST)
   - POST: Login a user and retrieve JWT tokens.
   - Example:
     - POST: curl -X POST -d "username=user&password=password" http://localhost:8000/login/

7. `api/token/` (POST)
   - POST: Obtain a new pair of access and refresh tokens.
   - Example:
     - POST: curl -X POST -d "username=user&password=password" http://localhost:8000/api/token/

8. `api/token/refresh/` (POST)
   - POST: Refresh an existing access token using a refresh token.
   - Example:
     - POST: curl -X POST -d "refresh=<refresh_token>" http://localhost:8000/api/token/refresh/
"""
