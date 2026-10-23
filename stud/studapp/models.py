from django.db import models

# Create your models here.
class StudentDb(models.Model):
    name = models.CharField(max_length=100)

    COURSE_CHOICES = (
        ('python', 'Python'),
        ('django', 'Django'),
        ('java', 'Java'),
    )

    course = models.CharField(
        max_length=100,
        choices=COURSE_CHOICES
    )

    age = models.IntegerField()

    email = models.EmailField()

    joined_date = models.DateTimeField(
        auto_now_add=True
    )

    is_active = models.BooleanField(default=True)