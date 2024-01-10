from django.urls import path
from.views import view
from.views import view1
urlpatterns = [
    path('',view),
    path('study', view1),
    path('camping', view1),
    path('horse-riding', view1),
    path('skiing', view1),
    path('music', view1),
    path('bungeejumping', view1),
    path('run', view1),
    path('hiking', view1),
]