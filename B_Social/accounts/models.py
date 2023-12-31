from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50,null=False)
    last_name = models.CharField(max_length=50,null=False)
    school_number = models.IntegerField(max_length=9,null=False,unique=True)
    department = models.CharField(max_length=50,null=False)
    class_level = models.CharField(max_length=10,null=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20,null=False,unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



