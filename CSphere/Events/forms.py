from django import forms
from .models import EventApplication


class EventApplicationForm(forms.ModelForm):
    class Meta:
        model = EventApplication
        fields = [
            'first_name',
            'last_name',
            'department',
            'grade',
            'is_club_member',
            'club_name',
            'event_purpose',
            'event_scope',
            'event_date',
            'event_duration',
        ]
