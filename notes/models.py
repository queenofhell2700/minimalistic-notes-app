from django.db import models

# Create your models here

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Note(models.Model):
    text = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="notes")
    
    # --- NEW FIELDS START HERE ---
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    is_done = models.BooleanField(default=False)
    # --- NEW FIELDS END HERE ---

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[:30]