from django.db import models

class EventApplication(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    is_club_member = models.BooleanField(default=False)
    club_name = models.CharField(max_length=100, blank=True, null=True)
    event_purpose = models.TextField()
    event_scope = models.TextField()
    event_date = models.DateField()
    event_duration = models.TimeField()
