from django.db import models

# Create your models here.
class QuestionsDb(models.Model):

    title = models.CharField(max_length=200)

    LANGUAGE_CHOICES = (
        ('Python', 'Python'),
        ('java', 'Java'),
        ('cpp', 'C++'),
    )

    language = models.CharField(
        max_length=100,
        choices=LANGUAGE_CHOICES
    )

    DIFFICULTY_CHOICES = (
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    )

    difficulty_level = models.CharField(
        max_length=100,
        choices=DIFFICULTY_CHOICES
    )

    score = models.IntegerField()

    topic = models.CharField(max_length=100)

    notes = models.TextField()

    published_date = models.DateTimeField(auto_now_add=True)

    sample_input = models.TextField()

    sample_output = models.TextField()

    is_active = models.BooleanField(default=True)