from django.urls import path, include
from users.views import Register, UserChange, ProfileView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('user-change/', UserChange.as_view(), name='user-change'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile')
]
