from django.urls import path
from.views import view, view2


urlpatterns = [
    path('',view),
    path('show',view2),
    path('voleyball',view2),
    path('match',view2),
    path('cinema',view2),


]