from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Complaint(models.Model):
    STATUS_CHOICES = [
        ('Initiated', 'Initiated'),
        ('Processed', 'Processed'),
        ('Reject', 'Reject'),
        ('Success', 'Success'),
    ]

    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    violation_date = models.DateField()
    place =models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    uploaded_file = models.FileField(upload_to='complaint_videos/')
    comment=models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Initiated')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Complaint #{self.id}: {self.violation_date} - {self.place} ({self.status})'
