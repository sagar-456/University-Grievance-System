
# Create your models here.
from django.db import models

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from django.utils import timezone 

from django.contrib.auth.models import User 
 

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=10)
    gender = models.CharField(max_length=20)
    user_type=models.CharField(max_length=20)

class Contact(models.Model):
    email=models.EmailField()
    name=models.CharField(max_length=255)
    subject=models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

def validate_title(value):
    if any(char.isdigit() for char in value):
        raise ValidationError("Title must not contain digits.")
    
class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    title=models.CharField(max_length=50, default='Title', validators=[validate_title])
    post_content = models.TextField()

    def __str__(self):
        return self.post_content
    
class UserNotice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    notice_content = models.TextField()

    def __str__(self):
        return self.notice_content
    
class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notice = models.ForeignKey(UserNotice, on_delete=models.CASCADE)
    response = models.TextField()

    def __str__(self):
        return self.response

