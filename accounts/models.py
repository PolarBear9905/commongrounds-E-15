from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=63)
    email_address = models.EmailField()
    ROLES = [
           ("A", "Anonymous"),
           ("MS", "Market Seller"),
           ("EO", "Event Organizer"),
           ("BC", "Book Contributor"),
           ("PC", "Project Creator"),
           ("CM", "Commission Maker"),
    ]
    role = models.CharField(max_length=20, choices=ROLES, default="A")
    
    def __str__(self):
        return self.display_name
