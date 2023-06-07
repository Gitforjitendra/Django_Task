from django.contrib.auth.models import AbstractUser, Permission
from django.contrib.auth.models import Group as AuthGroup
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('superadmin', 'Super Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name="users"
    )
    groups = models.ManyToManyField(
        AuthGroup,
        blank=True,
        related_name="users"
    )

    class Meta:
        permissions = [("can_view_users", "Can view users")]

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    
