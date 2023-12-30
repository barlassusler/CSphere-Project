from django.contrib.auth.models import User

user = User.objects.get(username='admin_username')
user.is_staff = True
user.is_superuser = True
user.save()





