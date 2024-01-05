from django.urls import path
from.views import view, view2,event_application,success_page


urlpatterns = [
    path('',view),
    path('ai2',view2),
    path('join',view2),
    path('join',view2),
    path('join',view2),
    path('event-application', event_application, name='event_application'),
    path('success_page/', success_page, name='success_page'),


]