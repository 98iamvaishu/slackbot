from django.db import models
from django.utils import timezone
# Create your models here.
class Text(models.Model):
	msg = models.CharField(max_length = 100,null = True)
	