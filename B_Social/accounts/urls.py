from django.urls import path
from .views import add_student, user_login

urlpatterns = [
    path('signup', add_student),
    path('login', user_login),
]