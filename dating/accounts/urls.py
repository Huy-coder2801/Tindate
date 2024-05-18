from django.urls import path
from .views import profile, find_user_by_name

urlpatterns = [
    path('', find_user_by_name, name="search_user"),
    path('profile/', profile, name='users-profile'),
]