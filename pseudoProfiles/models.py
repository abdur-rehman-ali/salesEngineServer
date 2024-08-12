from django.db import models

class PseudoProfile(models.Model):
  VISA_STATUS_CHOICES = [
    ('citizen', 'Citizen'),
    ('permanent_resident', 'Permanent Resident'),
    ('temporary_resident', 'Temporary Resident'),
    ('student', 'Student'),
    ('work_permit', 'Work Permit'),
  ]

  name = models.CharField(max_length=255, unique=True)
  email = models.EmailField(unique=True)
  address = models.TextField()
  country = models.CharField(max_length=100)
  visa_status = models.CharField(max_length=20, choices=VISA_STATUS_CHOICES, default='citizen')
  contact_number = models.CharField(max_length=20)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name