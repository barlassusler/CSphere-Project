from django.urls import path
from.views import view, view2, event_application, success_page


urlpatterns = [
    path('',view),
    path('show',view2),
    path('voleyball',view2),
    path('match',view2),
    path('cinema',view2),
    path('event_application', event_application, name='event_application'),
    path('success_page/', success_page, name='success_page'),
]