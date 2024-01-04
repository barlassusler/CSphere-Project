from django.urls import path
from .views import signup, login, home_login

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('home_login/', home_login, name='home_login')
]